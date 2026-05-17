# Jury Trial — Multi-Agent Murder Mystery Deliberation

A learning project demonstrating **multi-agent AI systems** through a structured
murder mystery discussion. Five AI agents — each with a distinct role and
personality — deliberate over four rounds of evidence to identify the murderer.

Powered by the **DeepSeek API** (OpenAI-compatible). Supports English and
Chinese discussion, interactive or automatic mode, and a pluggable case library.

## What This Project Teaches

| Concept | How It's Demonstrated |
|---|---|
| **Role Specialisation** | Each agent has a unique system prompt (Judge, Prosecution, Defence, Forensic, Psychologist) |
| **Multi-Agent Interaction** | Agents build on, challenge, and respond to each other's arguments across rounds |
| **Emergent Reasoning** | The correct conclusion emerges from discussion, not from any single agent's knowledge |
| **Context Management** | Round summaries are compressed and fed back to agents to manage token usage |
| **Prompt Engineering** | Strict "deduction game" rules prevent agents from relying on pre-trained knowledge of famous cases |
| **Orchestration** | A central orchestrator manages turn-taking, evidence release, retry logic, and bilingual output |

## Project Structure

```
jury-trial-project/
├── run.py                  # Convenience launcher
├── requirements.txt        # openai + python-dotenv
├── .env.example            # API key template
├── README.md
├── README_zh.md            # Chinese documentation
├── logs/                   # Discussion transcripts (markdown)
└── jury_trial/
    ├── __init__.py
    ├── config.py           # API configuration (DeepSeek)
    ├── prompts.py          # Agent system prompts (templated by case name)
    ├── agent.py            # Agent class (OpenAI-compatible API, with retry)
    ├── orchestrator.py     # Discussion flow, bilingual UI, markdown logging
    ├── main.py             # CLI entry point
    └── cases/              # Pluggable case library
        ├── __init__.py     # Case registry
        ├── alpine_express.py   # Adapted from Murder on the Orient Express
        ├── decagon_island.py   # Adapted from 十角館の殺人
        └── wedding_chamber.py  # Adapted from 本陣殺人事件
```

## Setup

### 1. Create virtual environment and install dependencies

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

**macOS / Linux:**
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure your API key

```bash
cp .env.example .env
# Edit .env and add your DeepSeek API key
# Get one at: https://platform.deepseek.com
```

`.env` format:
```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
DEEPSEEK_BASE_URL=https://api.deepseek.com
MODEL=deepseek-v4-flash
MAX_TOKENS=4096
TEMPERATURE=0.7
```

### 3. Run

```bash
# Interactive mode (press Enter between rounds, Chinese discussion)
python run.py

# Automatic mode (no pauses)
python run.py --auto

# English discussion
python run.py --lang en

# Select a specific case
python run.py --case decagon_island

# List available cases
python run.py --list-cases

# Dry run (see structure without API calls)
python run.py --dry-run
python run.py --case wedding_chamber --dry-run
```

## CLI Reference

| Flag | Description |
|---|---|
| `--auto` | Run without waiting for user input between rounds |
| `--dry-run` | Print case structure without making API calls |
| `--case CASE_ID` | Select case (default: `alpine_express`) |
| `--list-cases` | List all available cases and exit |
| `--lang {en,zh}`, `-l` | Discussion language (default: `zh`) |

## The Agents

| Agent | Role | Focus |
|---|---|---|
| **Presiding Judge** (主审法官) | Moderator | Introduces evidence, summarises, keeps discussion on track |
| **Prosecution Investigator** (检方探员) | Builds the case | Connects clues, identifies suspects, constructs narrative |
| **Defence Analyst** (辩护分析师) | Challenges assumptions | Points out gaps, alternative explanations, reasonable doubt |
| **Forensic Expert** (法医专家) | Physical evidence | Wound patterns, toxicology, trace evidence, timing |
| **Forensic Psychologist** (行为心理学家) | Behavioural analysis | Suspect behaviour, deception, group dynamics, profiling |

## Discussion Flow

```
Round 1 → Judge introduces evidence → 4 analysts respond → Judge summarises
Round 2 → Judge introduces evidence → 4 analysts respond → Judge summarises
Round 3 → Judge introduces evidence → 4 analysts respond → Judge summarises
Round 4 → Judge introduces evidence → 4 analysts respond → Judge summarises
Final Deliberation → Each agent presents their final theory → Truth revealed
```

Each agent sees the new evidence plus summaries of previous rounds, plus the
current round's discussion so far. This keeps the context window manageable
while preserving the full reasoning chain.

## Case Library

Cases are pluggable modules in `jury_trial/cases/`. Each module exports:

| Attribute | Description |
|---|---|
| `CASE_ID` | Short identifier for CLI (`--case` flag) |
| `CASE_NAME` | Display name |
| `CASE_DESC` | One-paragraph summary shown at startup |
| `CLUES_BY_ROUND` | Dict mapping round numbers to `{"title": ..., "clues": [...]}` |
| `TRUTH` | Full solution revealed after the final verdict |

### Available Cases

| ID | Title | Original Work | Core Mystery |
|---|---|---|---|
| `alpine_express` | The Alpine Express Murder | Murder on the Orient Express | 12 passengers conspire, interlocking alibis |
| `decagon_island` | The Decagon Island Mystery | 十角館の殺人 (Ayatsuji) | Faked death on an isolated island, hidden-room killer |
| `wedding_chamber` | The Wedding Chamber Murder | 本陣殺人事件 (Yokomizo) | Mechanical locked-room trick, backwards footprints |

### Adding a New Case

Create a file in `jury_trial/cases/`:

```python
# cases/my_case.py
CASE_ID = "my_case"
CASE_NAME = "My Case Name"
CASE_DESC = "Brief description shown at startup."

CLUES_BY_ROUND = {
    1: {"title": "Round 1 Title", "clues": ["clue 1", "clue 2", ...]},
    2: {"title": "Round 2 Title", "clues": ["clue 1", "clue 2", ...]},
    # as many rounds as needed
}

TRUTH = """
Full solution text revealed after the verdict.
"""
```

Then register it in `jury_trial/cases/__init__.py`:

```python
from . import my_case
CASES = {..., "my_case": my_case}
```

No other code changes needed. Agent prompts are automatically customised with
the case name. The framework loads everything else dynamically.

## Preventing "Cheating" from Pre-Trained Knowledge

LLMs are trained on Wikipedia, books, and film summaries, so they likely
"know" the solutions to famous mystery cases. This project uses multiple
defences:

1. **All names changed**: Characters, places, the setting — everything renamed.
2. **Details altered**: Clue descriptions and relationships modified from the originals.
3. **Strict system prompt rule**: Every agent is told this is a "deduction game"
   and MUST only use evidence provided during the discussion.
4. **Multi-step reasoning required**: The solutions (collective murder, faked death,
   mechanical trick) are counterintuitive — agents naturally look for simpler
   explanations and must be led by accumulating evidence.

## Language Support

The `--lang` flag controls the discussion language by appending a language
instruction to each agent's system prompt (`agent.py:26-32`). All UI labels,
task prompts, and log headers are bilingual via the `Orchestrator._s(en, zh)`
helper. The case evidence remains in its original language.

```bash
python run.py --lang zh   # Chinese discussion (default)
python run.py --lang en   # English discussion
```

## Error Handling & Retry

The agent (`agent.py`) includes automatic retry with exponential backoff for
transient API errors (rate limits, timeouts, server errors): 4s → 8s → 16s.
A 1.5-second delay between API calls avoids triggering rate limits proactively.
If all retries are exhausted, an explicit `[API Error]` message is printed
rather than failing silently.

## Output

Each run saves a structured markdown transcript to `logs/{case_id}_{timestamp}.md`
containing: case metadata, all evidence by round, full discussion transcript,
judge's summaries, final deliberation, and the revealed truth.

## Cost

DeepSeek API pricing is approximately **¥1–2 RMB** per full run with
`deepseek-v4-flash` (default).

Change the model in `.env`:
```
MODEL=deepseek-v4-pro
```
