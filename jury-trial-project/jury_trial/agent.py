import time
from openai import OpenAI
from .config import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, MODEL, MAX_TOKENS, TEMPERATURE, require_api_key
from .prompts import get_agent_prompts


class Agent:
    """A single jury member powered by the DeepSeek API (OpenAI-compatible).

    Each agent has a unique role (judge, prosecution, defence, forensic, psychologist)
    defined by its system prompt. The agent receives discussion context as a user
    message and returns its analysis.

    Includes automatic retry with exponential backoff for transient API errors
    (rate limiting, timeouts, server errors).
    """

    def __init__(self, agent_id: str, case_name: str, lang: str = "zh"):
        prompts = get_agent_prompts(case_name)
        if agent_id not in prompts:
            raise ValueError(f"Unknown agent_id: {agent_id}. "
                             f"Valid: {list(prompts)}")
        self.agent_id = agent_id
        self.system_prompt = prompts[agent_id]
        # Append language instruction
        lang_instruction = {
            "zh": "\n\nIMPORTANT: Please conduct ALL discussion and analysis "
                  "in Chinese (中文). Write your entire response in Chinese.",
            "en": "\n\nIMPORTANT: Please conduct ALL discussion and analysis "
                  "in English. Write your entire response in English.",
        }
        self.system_prompt += lang_instruction.get(lang, lang_instruction["zh"])
        require_api_key()
        self.client = OpenAI(
            api_key=DEEPSEEK_API_KEY,
            base_url=DEEPSEEK_BASE_URL,
        )

    def respond(self, user_message: str, max_retries: int = 3) -> str:
        """Send a message to the agent and return its response text.

        Retries on transient API errors (rate limits, timeouts, server errors)
        with exponential backoff: 2s, 4s, 8s.
        """
        last_error = None
        for attempt in range(max_retries):
            try:
                response = self.client.chat.completions.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": self.system_prompt},
                        {"role": "user", "content": user_message},
                    ],
                    max_tokens=MAX_TOKENS,
                    temperature=TEMPERATURE,
                )
                content = response.choices[0].message.content
                if content is None or content.strip() == "":
                    if attempt < max_retries - 1:
                        time.sleep(2 ** attempt)
                        continue
                    return "[WARNING: Agent returned an empty response.]"
                return content

            except Exception as e:
                last_error = e
                error_msg = str(e).lower()
                retryable = any(kw in error_msg for kw in [
                    "rate", "timeout", "connection", "server_error",
                    "overloaded", "capacity", "503", "429", "500",
                    "internal_server_error", "service_unavailable",
                ])
                if retryable and attempt < max_retries - 1:
                    wait = 2 ** (attempt + 2)  # 4s, 8s, 16s
                    print(f"\n    [Retry {attempt+1}/{max_retries} in {wait}s: {type(e).__name__}]",
                          flush=True)
                    time.sleep(wait)
                    continue
                break

        return f"[API Error after {max_retries} attempts: {type(last_error).__name__}: {last_error}]"
