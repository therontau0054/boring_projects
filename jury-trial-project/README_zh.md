# 审判团 — 多 Agent 本格推理谋杀案审议系统

一个用于学习**多 Agent 系统**的实践项目。5 个 AI Agent 各司其职（法官、检方、辩护、法医、心理分析师），
围绕一桩谋杀案展开 4 轮讨论，通过结构化审议逐步推理出真凶。

基于 **DeepSeek API**（兼容 OpenAI 格式）。支持中英文讨论、交互/自动模式、可插拔案件库。

## 本项目教什么

| 概念 | 如何体现 |
|---|---|
| **角色专业化** | 每个 Agent 有独立的 system prompt（法官、检方、辩护、法医、心理分析师） |
| **多 Agent 交互** | Agent 在跨轮讨论中相互构建、质疑、回应 |
| **涌现式推理** | 正确结论来自讨论过程，而非任何单个 Agent 的已有知识 |
| **上下文管理** | 每轮总结被压缩后反馈给 Agent，合理控制 token 消耗 |
| **提示词工程** | 严格的「推理游戏」规则防止 Agent 依赖预训练知识中的已知案件 |
| **编排调度** | 中央 Orchestrator 管理发言顺序、证据释放、重试逻辑和双语输出 |

## 项目结构

```
jury-trial-project/
├── run.py                  # 便捷启动脚本
├── requirements.txt        # openai + python-dotenv
├── .env.example            # API Key 配置模板
├── README.md               # 英文文档
├── README_zh.md            # 中文文档（本文件）
├── logs/                   # 讨论记录（Markdown 格式）
└── jury_trial/
    ├── __init__.py
    ├── config.py           # API 配置（DeepSeek）
    ├── prompts.py          # Agent 系统提示词（通过案件名模板化）
    ├── agent.py            # Agent 类（OpenAI 兼容 API，含重试机制）
    ├── orchestrator.py     # 讨论编排、双语 UI、Markdown 日志
    ├── main.py             # CLI 入口
    └── cases/              # 可插拔案件库
        ├── __init__.py     # 案件注册表
        ├── alpine_express.py   # 改编自《东方快车谋杀案》
        ├── decagon_island.py   # 改编自《十角館の殺人》
        └── wedding_chamber.py  # 改编自《本陣殺人事件》
```

## 环境搭建

### 1. 创建虚拟环境并安装依赖

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

### 2. 配置 API Key

```bash
cp .env.example .env
# 编辑 .env，填入 DeepSeek API Key
# 获取地址：https://platform.deepseek.com
```

`.env` 格式：
```
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
DEEPSEEK_BASE_URL=https://api.deepseek.com
MODEL=deepseek-v4-flash
MAX_TOKENS=4096
TEMPERATURE=0.7
```

### 3. 运行

```bash
# 交互模式（每轮按 Enter 继续，中文讨论）
python run.py

# 自动模式（无需按键）
python run.py --auto

# 英文讨论
python run.py --lang en

# 选择案件
python run.py --case decagon_island

# 查看可用案件
python run.py --list-cases

# 空跑查看结构（不调用 API）
python run.py --dry-run
python run.py --case wedding_chamber --dry-run
```

## 命令行参数

| 参数 | 说明 |
|---|---|
| `--auto` | 自动运行，无需按键 |
| `--dry-run` | 仅打印案件结构，不调用 API |
| `--case CASE_ID` | 选择案件（默认：`alpine_express`） |
| `--list-cases` | 列出所有可用案件 |
| `--lang {en,zh}`, `-l` | 讨论语言（默认：`zh`） |

## Agent 角色

| Agent | 角色 | 核心职责 |
|---|---|---|
| **Presiding Judge** (主审法官) | 主持人 | 引入证据、总结讨论、维持秩序 |
| **Prosecution Investigator** (检方探员) | 构建案件 | 关联线索、识别嫌疑人、建立叙事 |
| **Defence Analyst** (辩护分析师) | 质疑假设 | 指出逻辑漏洞、提出替代解释、合理怀疑 |
| **Forensic Expert** (法医专家) | 物证分析 | 伤口模式、毒理学、微量物证、时间推断 |
| **Forensic Psychologist** (行为心理学家) | 行为分析 | 嫌疑人行为、欺骗迹象、群体动力学、心理画像 |

## 讨论流程

```
第一轮 → 法官引入证据 → 4 位分析师发言 → 法官总结
第二轮 → 法官引入证据 → 4 位分析师发言 → 法官总结
第三轮 → 法官引入证据 → 4 位分析师发言 → 法官总结
第四轮 → 法官引入证据 → 4 位分析师发言 → 法官总结
最终裁决 → 每位 Agent 给出最终推理 → 真相揭晓
```

每个 Agent 在发言时能看到：本轮新证据 + 前轮总结 + 本轮已有的讨论记录。
这样既能保持完整的推理链条，又不会超出上下文窗口。

## 案件库

案件以可插拔模块形式存放在 `jury_trial/cases/` 中。每个模块导出：

| 属性 | 说明 |
|---|---|
| `CASE_ID` | CLI 使用的简短标识符 |
| `CASE_NAME` | 案件显示名称 |
| `CASE_DESC` | 启动时显示的一段简介 |
| `CLUES_BY_ROUND` | 按轮次组织的线索字典 `{"title": ..., "clues": [...]}` |
| `TRUTH` | 最终真相（结案时揭示） |

### 已有案件

| ID | 标题 | 改编原作 | 核心谜题 |
|---|---|---|---|
| `alpine_express` | 阿尔卑斯快车谋杀案 | 《东方快车谋杀案》 | 12 人集体作案、互相串供 |
| `decagon_island` | 十角岛谜案 | 《十角館の殺人》（綾辻行人） | 孤岛连续杀人、伪造死亡藏于暗室 |
| `wedding_chamber` | 新婚密室杀人案 | 《本陣殺人事件》（横溝正史） | 机械密室机关、倒退脚印诡计 |

### 添加新案件

在 `jury_trial/cases/` 下新建文件：

```python
# cases/my_case.py
CASE_ID = "my_case"
CASE_NAME = "我的案件名"
CASE_DESC = "启动时的简要描述。"

CLUES_BY_ROUND = {
    1: {"title": "第一轮标题", "clues": ["线索 1", "线索 2", ...]},
    2: {"title": "第二轮标题", "clues": ["线索 1", "线索 2", ...]},
    # 需要几轮就写几轮
}

TRUTH = """
结案时揭示的完整真相文本。
"""
```

然后在 `jury_trial/cases/__init__.py` 中注册：

```python
from . import my_case
CASES = {..., "my_case": my_case}
```

无需修改任何其他代码。Agent 提示词会自动填入案件名，框架动态加载案件内容。

## 防止 Agent「作弊」的设计

LLM 的训练数据包含维基百科、书籍、电影摘要，因此它们很可能「知道」著名推理案件的答案。
本项目通过以下策略迫使 Agent 进行真正的推理：

1. **全部改名**：人物、地点、场景——全部重新命名。
2. **细节修改**：线索描述和人物关系相比原作有所改动。
3. **严格的 system prompt 规则**：每个 Agent 被告知这是「推理游戏」，必须仅使用讨论中提供的证据。
4. **需要多步推理**：案件解答（集体谋杀、伪造死亡、机械机关）都是反直觉的——
   Agent 天然会寻找单一凶手，必须通过逐轮积累的证据才能推导出正确结论。

## 语言支持

`--lang` 参数通过在 system prompt 末尾追加语言指令来控制讨论语言（`agent.py:26-32`）。
所有界面标签、任务提示词、日志标题均通过 `Orchestrator._s(en, zh)` 方法实现双语。
案件线索保留原文语言。

```bash
python run.py --lang zh   # 中文讨论（默认）
python run.py --lang en   # 英文讨论
```

## 错误处理与重试

`agent.py` 内置指数退避自动重试（4s → 8s → 16s），针对限流、超时、服务端错误等瞬时异常。
API 调用之间设置 1.5 秒间隔，主动避免触发限流。若重试耗尽，会打印明确的 `[API Error]`
信息，而非静默失败。

## 输出

每次运行会在 `logs/{case_id}_{timestamp}.md` 保存一份结构化 Markdown 记录，
包含：案件元信息、全部证据（按轮次）、完整讨论记录、法官总结、最终裁决和真相。

## 费用

使用 `deepseek-v4-flash`（默认模型），一次完整运行约 **¥1–2 元**。

在 `.env` 中更换模型：
```
MODEL=deepseek-v4-pro
```
