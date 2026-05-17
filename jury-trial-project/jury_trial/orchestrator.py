import textwrap
import time
import types
from typing import List, Tuple

from .agent import Agent
from .prompts import AGENT_NAMES

# Discussion order: judge introduces, then analysts, then judge summarises.
ANALYST_ORDER = ["prosecution", "defense", "forensic", "psychologist"]

BANNER_WIDTH = 64
CALL_DELAY = 1.5  # seconds between API calls to avoid rate limiting
FINAL_ROUND = 99  # sentinel for the final deliberation phase


class Orchestrator:
    """Manages the multi-round jury deliberation.

    Coordinates the flow: judge introduces evidence → analysts discuss →
    judge summarises → repeat. After all evidence rounds, runs the final
    deliberation where each agent names the murderer.

    Parameters
    ----------
    case_module : module
        A case module exporting CLUES_BY_ROUND, TRUTH, CASE_NAME, CASE_DESC.
    interactive : bool
        If True, wait for user input between rounds.
    """

    def __init__(self, case_module: types.ModuleType, interactive: bool = True,
                 lang: str = "zh"):
        self.case = case_module
        self.case_name: str = case_module.CASE_NAME
        self.case_desc: str = getattr(case_module, "CASE_DESC", "")
        self.clues_by_round: dict = case_module.CLUES_BY_ROUND
        self.truth: str = case_module.TRUTH
        self.lang = lang

        self.interactive = interactive
        self.case_id: str = getattr(case_module, "CASE_ID", "unknown")
        self.agents = {
            aid: Agent(aid, case_name=self.case_name, lang=lang)
            for aid in AGENT_NAMES
        }
        self.round_summaries: List[str] = []
        self.all_rounds_transcript: List[Tuple[int, str, str]] = []
        self.full_log: List[str] = []
        self._current_round: int = 0

    # ------------------------------------------------------------------
    # Bilingual UI helpers
    # ------------------------------------------------------------------

    def _s(self, en: str, zh: str) -> str:
        """Pick the right language string."""
        return zh if self.lang == "zh" else en

    # ------------------------------------------------------------------
    # Public entry point
    # ------------------------------------------------------------------

    def run(self):
        title = self._s(
            f"JURY TRIAL — {self.case_name.upper()}",
            f"审判团 — {self.case_name.upper()}",
        )
        self._print_header(title)
        print(self.case_desc)
        print(self._s(
            f"Your jury of {len(self.agents)} AI agents will now deliberate.\n",
            f"由 {len(self.agents)} 名 AI Agent 组成的审判团现在开始审议。\n",
        ))

        for round_num in sorted(self.clues_by_round):
            self._run_evidence_round(round_num)
            if self.interactive:
                input(self._s(
                    "\nPress Enter to continue to the next round...",
                    "\n按 Enter 键继续下一轮...",
                ))

        self._run_final_deliberation()
        self._reveal_truth()
        self._save_log()

    # ------------------------------------------------------------------
    # Evidence rounds (1–4)
    # ------------------------------------------------------------------

    def _run_evidence_round(self, round_num: int):
        self._current_round = round_num
        clues = self.clues_by_round[round_num]
        title = clues["title"]
        clue_list = clues["clues"]

        self._print_round_banner(round_num, title)
        self._print_clues(clue_list)

        # 1) Judge introduces the round
        judge_msg = self._build_judge_intro_prompt(round_num, title, clue_list)
        judge_response = self._call_agent("judge", judge_msg)
        self._record_and_print("judge", judge_response)
        time.sleep(CALL_DELAY)

        # 2) Each analyst responds
        for agent_id in ANALYST_ORDER:
            msg = self._build_analyst_prompt(agent_id, round_num, title, clue_list)
            response = self._call_agent(agent_id, msg)
            self._record_and_print(agent_id, response)
            time.sleep(CALL_DELAY)

        # 3) Judge summarises
        summary_msg = self._build_judge_summary_prompt(round_num)
        summary = self._call_agent("judge", summary_msg)
        self._record_and_print("judge", summary)
        self.round_summaries.append(summary)
        self._log(f"\n=== END OF ROUND {round_num} ===\n")
        time.sleep(CALL_DELAY)

    # ------------------------------------------------------------------
    # Final deliberation
    # ------------------------------------------------------------------

    def _run_final_deliberation(self):
        self._current_round = FINAL_ROUND
        self._print_header(self._s("FINAL DELIBERATION", "最终裁决"))
        print(self._s(
            "All evidence has been presented. Each agent now gives their "
            "final theory and names the murderer.\n",
            "所有证据已呈现在此。每位 Agent 现在给出最终推理，并指认凶手。\n",
        ))

        for agent_id in ANALYST_ORDER + ["judge"]:
            msg = self._build_verdict_prompt(agent_id)
            response = self._call_agent(agent_id, msg)
            self._record_and_print(agent_id, response)
            time.sleep(CALL_DELAY)

    # ------------------------------------------------------------------
    # Prompt builders
    # ------------------------------------------------------------------

    def _build_judge_intro_prompt(self, round_num: int, title: str,
                                   clue_list: List[str]) -> str:
        clues_text = "\n".join(f"  [{i+1}] {c}" for i, c in enumerate(clue_list))
        prev = self._prev_rounds_context()
        evidence_label = self._s("New Evidence for This Round", "本轮新证据")
        task_label = self._s("Your Task (Presiding Judge)", "你的任务（主审法官）")
        task_body = self._s(
            "Introduce this new evidence to the panel. Highlight the 2-3 most "
            "significant pieces. Then invite the Prosecution Investigator to "
            "present their analysis first.",
            "向审判团介绍这些新证据。重点突出 2-3 条最重要的线索。"
            "然后邀请检方探员首先发表分析。",
        )
        return textwrap.dedent(f"""\
        ## ROUND {round_num}: {title}

        {prev}
        ### {evidence_label}:
        {clues_text}

        ### {task_label}:
        {task_body}""")

    def _build_analyst_prompt(self, agent_id: str, round_num: int,
                               title: str, clue_list: List[str]) -> str:
        clues_text = "\n".join(f"  [{i+1}] {c}" for i, c in enumerate(clue_list))
        prev = self._prev_rounds_context()
        this_round = self._this_round_context()
        evidence_label = self._s("New Evidence for This Round", "本轮新证据")
        disc_label = self._s("Discussion So Far This Round", "本轮已有讨论")
        task_label = self._s(f"Your Task ({AGENT_NAMES[agent_id]})",
                             f"你的任务（{AGENT_NAMES[agent_id]}）")
        task_body = self._s(
            "Provide your analysis of the new evidence. You MUST base every "
            "conclusion on the evidence above. Address points made by earlier "
            "speakers in this round if relevant. Focus on your area of expertise.",
            "请对新证据进行分析。你的每一个结论都必须基于以上证据。"
            "如有必要，回应本轮中其他成员的发言。专注于你的专业领域。",
        )
        return textwrap.dedent(f"""\
        ## ROUND {round_num}: {title}

        {prev}
        ### {evidence_label}:
        {clues_text}

        ### {disc_label}:
        {this_round}

        ### {task_label}:
        {task_body}""")

    def _build_judge_summary_prompt(self, round_num: int) -> str:
        this_round = self._this_round_context()
        disc_label = self._s("Full Discussion of This Round", "本轮完整讨论")
        task_label = self._s("Your Task (Presiding Judge)", "你的任务（主审法官）")
        task_body = self._s(
            "Summarise this round:\n"
            "1. Key findings and insights.\n"
            "2. Points of agreement among the panel.\n"
            "3. Open questions that need resolution.\n"
            "4. What we should focus on when more evidence arrives.",
            "总结本轮讨论：\n"
            "1. 关键发现与洞见。\n"
            "2. 审判团的共识点。\n"
            "3. 尚待解决的开放问题。\n"
            "4. 下一轮应关注的重点。",
        )
        return textwrap.dedent(f"""\
        ## ROUND {round_num} Discussion Complete

        {self._prev_rounds_context()}
        ### {disc_label}:
        {this_round}

        ### {task_label}:
        {task_body}""")

    def _build_verdict_prompt(self, agent_id: str) -> str:
        all_clues = []
        for rn in sorted(self.clues_by_round):
            for c in self.clues_by_round[rn]["clues"]:
                all_clues.append(f"  [R{rn}] {c}")

        clues_text = "\n".join(all_clues)
        summaries_text = "\n\n".join(
            f"Round {i+1} Summary: {s[:600]}..."
            for i, s in enumerate(self.round_summaries)
        )

        evidence_label = self._s("All Evidence Presented in This Case", "本案全部证据")
        summaries_label = self._s("Round-by-Round Summaries", "各轮讨论总结")
        task_label = self._s(f"Your Final Task ({AGENT_NAMES[agent_id]})",
                             f"你的最终任务（{AGENT_NAMES[agent_id]}）")
        task_body = self._s(
            "Based on ALL the evidence above, present your final conclusion:\n"
            "1. Who killed the victim? Name the murderer(s) explicitly.\n"
            "2. What was the motive?\n"
            "3. How was the crime committed (method)?\n"
            "4. What is your confidence level (High / Medium / Low)?\n\n"
            "Remember: base your conclusion ONLY on the evidence provided above.",
            "基于以上全部证据，给出你的最终结论：\n"
            "1. 谁是凶手？请明确指出凶手姓名。\n"
            "2. 作案动机是什么？\n"
            "3. 犯罪手法是什么？\n"
            "4. 你的置信度如何（高 / 中 / 低）？\n\n"
            "记住：你的结论必须仅基于以上提供的证据。",
        )
        return textwrap.dedent(f"""\
        ## FINAL VERDICT

        ### {evidence_label}:
        {clues_text}

        ### {summaries_label}:
        {summaries_text}

        ### {task_label}:
        {task_body}""")

    # ------------------------------------------------------------------
    # Context helpers
    # ------------------------------------------------------------------

    def _prev_rounds_context(self) -> str:
        if not self.round_summaries:
            return ""
        header = self._s("### Summary of Previous Rounds:", "### 前轮讨论总结：")
        lines = [header]
        for i, s in enumerate(self.round_summaries, 1):
            lines.append(f"\n--- Round {i} Summary ---\n{s[:500]}")
        return "\n".join(lines) + "\n"

    def _this_round_context(self) -> str:
        """Return the current round's discussion so far."""
        entries = [e for e in self.all_rounds_transcript
                   if e[0] == self._current_round]
        if not entries:
            return self._s("(No discussion yet this round.)",
                           "（本轮尚无讨论。）")

        lines = []
        for _, speaker_id, text in entries:
            lines.append(
                f"\n[{AGENT_NAMES.get(speaker_id, speaker_id)}]:\n{text[:500]}"
            )
        return "\n".join(lines)

    # ------------------------------------------------------------------
    # API & recording
    # ------------------------------------------------------------------

    def _call_agent(self, agent_id: str, message: str) -> str:
        thinking = self._s("is thinking ...", "正在思考 ...")
        print(f"\n  ... {AGENT_NAMES[agent_id]} {thinking}", end="", flush=True)
        response = self.agents[agent_id].respond(message)
        print("\r" + " " * 50 + "\r", end="")  # clear the "thinking" line
        return response

    def _record_and_print(self, agent_id: str, text: str):
        self.all_rounds_transcript.append((self._current_round, agent_id, text))
        self._print_agent_response(agent_id, text)

    def _log(self, text: str):
        self.full_log.append(text)

    # ------------------------------------------------------------------
    # Output formatting
    # ------------------------------------------------------------------

    def _print_header(self, title: str):
        print("\n" + "=" * BANNER_WIDTH)
        print(f"  {title}")
        print("=" * BANNER_WIDTH + "\n")

    def _print_round_banner(self, round_num: int, title: str):
        print("\n" + "-" * BANNER_WIDTH)
        print(f"  ROUND {round_num}: {title}")
        print("-" * BANNER_WIDTH)

    def _print_clues(self, clue_list: List[str]):
        print(self._s("\n  [NEW EVIDENCE]", "\n  [新证据]"))
        for i, clue in enumerate(clue_list, 1):
            wrapped = textwrap.fill(clue, width=BANNER_WIDTH - 6,
                                    initial_indent=f"    [{i}] ",
                                    subsequent_indent="        ")
            print(wrapped)
        print()

    def _print_agent_response(self, agent_id: str, text: str):
        label = AGENT_NAMES.get(agent_id, agent_id)
        print(f"\n  ── {label} ──")
        wrapped = textwrap.fill(text, width=BANNER_WIDTH - 4,
                                initial_indent="    ",
                                subsequent_indent="    ")
        print(wrapped)
        self._log(f"\n── {label} ──\n{text}")

    # ------------------------------------------------------------------
    # Truth reveal & log
    # ------------------------------------------------------------------

    def _reveal_truth(self):
        self._print_header(self._s("TRUTH REVEALED", "真相揭晓"))
        print(self.truth)
        self._log(f"\n\n{self.truth}")

    def _save_log(self):
        import os
        from datetime import datetime

        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{log_dir}/{self.case_id}_{timestamp}.md"

        with open(filename, "w", encoding="utf-8") as f:
            L = self._s  # shorthand
            # --- Header ---
            trial_label = L("Jury Trial", "审判团")
            case_id_label = L("Case ID", "案件 ID")
            date_label = L("Date", "日期")
            agents_label = L("Agents", "Agent 数量")
            f.write(f"# {trial_label}: {self.case_name}\n\n")
            f.write(f"- **{case_id_label}**: `{self.case_id}`\n")
            f.write(f"- **{date_label}**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"- **{agents_label}**: {len(self.agents)}\n\n")
            f.write(f"> {self.case_desc}\n\n")
            f.write("---\n\n")

            # --- Evidence rounds ---
            for rn in sorted(self.clues_by_round):
                clues = self.clues_by_round[rn]
                round_label = L("Round", "第")
                f.write(f"## {round_label} {rn}: {clues['title']}\n\n")

                evidence_label = L("New Evidence", "新证据")
                f.write(f"### {evidence_label}\n\n")
                for i, clue in enumerate(clues["clues"], 1):
                    f.write(f"{i}. {clue}\n")
                f.write("\n")

                disc_label = L("Discussion", "讨论记录")
                f.write(f"### {disc_label}\n\n")
                entries = [e for e in self.all_rounds_transcript if e[0] == rn]
                for _, speaker_id, text in entries:
                    label = AGENT_NAMES.get(speaker_id, speaker_id)
                    f.write(f"**{label}**\n\n{text}\n\n")

                if rn <= len(self.round_summaries):
                    summary_label = L("Judge's Round Summary", "法官本轮总结")
                    f.write(f"### {summary_label}\n\n")
                    f.write(f"{self.round_summaries[rn - 1]}\n\n")

                f.write("---\n\n")

            # --- Final deliberation ---
            final_label = L("Final Deliberation", "最终裁决")
            f.write(f"## {final_label}\n\n")
            final_entries = [e for e in self.all_rounds_transcript
                             if e[0] == FINAL_ROUND]
            for _, speaker_id, text in final_entries:
                label = AGENT_NAMES.get(speaker_id, speaker_id)
                f.write(f"**{label}**\n\n{text}\n\n")

            # --- Truth ---
            f.write("---\n\n")
            truth_label = L("Truth Revealed", "真相揭晓")
            f.write(f"## {truth_label}\n\n")
            f.write(f"{self.truth}\n")

        print(self._s(
            f"\nDiscussion log saved to: {filename}",
            f"\n讨论记录已保存至：{filename}",
        ))
