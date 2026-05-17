# Abstracts of Papers

## VLA
### TMRL: Diffusion Timestep-Modulated Pretraining Enables Exploration for Efficient Policy Finetuning
**Authors**: Matthew M. Hong, Jesse Zhang, Anusha Nagabandi, Abhishek Gupta

**Published Date**: 2026-05-12

**Updated Date**: 2026-05-12

**PDF Url**: [2605.12236v1](https://arxiv.org/pdf/2605.12236v1)

**Abstract**: Fine-tuning pre-trained robot policies with reinforcement learning (RL) often inherits the bottlenecks introduced by pre-training with behavioral cloning (BC), which produces narrow action distributions that lack the coverage necessary for downstream exploration. We present a unified framework that enables the exploration necessary to enable efficient robot policy finetuning by bridging BC pre-training and RL fine-tuning. Our pre-training method, Context-Smoothed Pre-training (CSP), injects forward-diffusion noise into policy inputs, creating a continuum between precise imitation and broad action coverage. We then fine-tune pre-trained policies via Timestep-Modulated Reinforcement Learning (TMRL), which trains the agent to dynamically adjust this conditioning during fine-tuning by modulating the diffusion timestep, granting explicit control over exploration. Integrating seamlessly with arbitrary policy inputs, e.g., states, 3D point clouds, or image-based VLA policies, we show that TMRL improves RL fine-tuning sample efficiency. Notably, TMRL enables successful real-world fine-tuning on complex manipulation tasks in under one hour. Videos and code available at https://weirdlabuw.github.io/tmrl/.


### Premover: Fast Vision-Language-Action Control by Acting Before Instructions Are Complete
**Authors**: Joonha Park, Jiseung Jeong, Taesik Gong

**Published Date**: 2026-05-12

**Updated Date**: 2026-05-12

**PDF Url**: [2605.12160v1](https://arxiv.org/pdf/2605.12160v1)

**Abstract**: Vision-Language-Action (VLA) policies are typically evaluated as if the user had finished typing or speaking before the robot begins acting. In real deployment, however, users take several seconds to enter a request, leaving the policy idle for a substantial fraction of the interaction. We introduce Premover, a lightweight module that converts this idle window into useful precomputation. Premover keeps the VLA backbone frozen and attaches two small projection heads, one for image patches, one for language tokens, that map an intermediate layer of the backbone into a shared space. The resulting focus map is supervised by simulator-rendered target-object segmentation masks and applied as a per-patch reweighting of the next step's image tokens. A single scalar readiness threshold, trained jointly from streaming prefixes, decides when the policy should begin acting. On the LIBERO benchmark suite, Premover reduces mean wall-clock time from 34.0 to 29.4 seconds, a 13.6% reduction, while matching the full-prompt baseline's success rate (95.1% vs. 95.0%); naive premoving, by contrast, collapses to 66.4%.


### Beyond World-Frame Action Heads: Motion-Centric Action Frames for Vision-Language-Action Models
**Authors**: Huoren Yang, Jianchao Zhao, Hu Yusong, Qiguan Ou, Yuyang Gao, Wei Ke, Yuhang He, SongLin Dong, Zhiheng Ma, Yihong Gong

**Published Date**: 2026-05-12

**Updated Date**: 2026-05-12

**PDF Url**: [2605.11809v1](https://arxiv.org/pdf/2605.11809v1)

**Abstract**: Vision-Language-Action (VLA) models have advanced rapidly with stronger backbones, broader pre-training, and larger demonstration datasets, yet their action heads remain largely homogeneous: most directly predict action commands in a fixed world coordinate frame. We propose \textbf{MCF-Proto}, a lightweight action head that equips VLA policies with a Motion-Centric Action Frame (MCF) and a prototype-based action parameterization. At each step, the policy predicts a rotation $R_t \in SO(3)$, composes actions in the transformed local frame from a set of prototypes, and maps them back to the world frame for end-to-end training, using only standard demonstrations without auxiliary supervision. This simple design induces stable emergent structure. Without explicit directional labels, the learned local frames develop a stable geometric structure whose axes are strongly compatible with demonstrated end-effector motion. Meanwhile, actions in the learned representation become substantially more compact, with variation captured by fewer dominant directions and more regularly organized by shared prototypes. These structural properties translate into improved robustness, especially under geometric perturbations. Our results suggest that adding lightweight geometric and compositional structure to the action head can materially improve how VLA policies organize and generalize robotic manipulation behavior. An anonymized code repository is provided in the supplementary material.


### DreamAvoid: Critical-Phase Test-Time Dreaming to Avoid Failures in VLA Policies
**Authors**: Xianzhe Fan, Yuxiang Lu, Shenyuan Gao, Xiaoyang Wu, Ruihua Han, Manling Li, Hengshuang Zhao

**Published Date**: 2026-05-12

**Updated Date**: 2026-05-12

**PDF Url**: [2605.11750v1](https://arxiv.org/pdf/2605.11750v1)

**Abstract**: Vision-Language-Action (VLA) models are often brittle in fine-grained manipulation, where minor action errors during the critical phases can rapidly escalate into irrecoverable failures. Since existing VLA models rely predominantly on successful demonstrations for training, they lack an explicit awareness of failure during these critical phases. To address this, we propose DreamAvoid, a critical-phase test-time dreaming framework that enables VLA models to anticipate and avoid failures. We also introduce an autonomous boundary learning paradigm to refine the system's understanding of the subtle boundary between success and failure. Specifically, we (1) utilize a Dream Trigger to determine whether the execution has entered a critical phase, (2) sample multiple candidate action chunks from the VLA via an Action Proposer, and (3) employ a Dream Evaluator, jointly trained on mixed data (success, failure, and boundary cases), to "dream" the short-horizon futures corresponding to the candidate actions, evaluate their values, and select the optimal action. We conduct extensive evaluations on real-world manipulation tasks and simulation benchmarks. The results demonstrate that DreamAvoid can effectively avoid failures, thereby improving the overall task success rate. Our code is available at https://github.com/XianzheFan/DreamAvoid.


### OOM-Free Alpamayo via CPU-GPU Memory Swapping for Vision-Language-Action Models
**Authors**: Seungwoo Roh, Huiyeong Kim, Jong-Chan Kim

**Published Date**: 2026-05-12

**Updated Date**: 2026-05-12

**PDF Url**: [2605.11678v1](https://arxiv.org/pdf/2605.11678v1)

**Abstract**: End-to-end Vision-Language-Action (VLA) models for autonomous driving unify perception, reasoning, and control in a single neural network, achieving strong driving performance but requiring 20-60GB of GPU memory-far exceeding the 12-16GB available on commodity GPUs. We present a framework, which enables memory-efficient VLA inference on VRAM-constrained GPUs through system-level optimization alone, without model modification. Our work proceeds in three stages: (1) Sequential Demand Layering reduces VRAM usage from model-level to layer-level granularity; (2) Pipelined Demand Layering hides parameter transfer time within layer execution time via transfer--compute overlap; and (3) a GPU-Resident Layer Decision Policy, informed by per-module residency benefit analysis, eliminates the residual transfer overhead that pipelining cannot hide. We further propose a performance prediction model that determines the optimal configuration-both the number and placement of resident layers-from a single profiling run with less than 1.3% prediction error across all configurations. Applied to NVIDIA's Alpamayo-R1-10B (21.52GB) on an RTX 5070Ti (16GB), our work achieves up to 3.55x speedup over Accelerate offloading while maintaining full BF16 precision.


### Overcoming Dynamics-Blindness: Training-Free Pace-and-Path Correction for VLA Models
**Authors**: Yanyan Zhang, Chaoda Song, Vikash Singh, Xinpeng Li, Kai Ye, Zhe Hu, Zhongzhu Pu, Yu Yin, Vipin Chaudhary

**Published Date**: 2026-05-12

**Updated Date**: 2026-05-14

**PDF Url**: [2605.11459v2](https://arxiv.org/pdf/2605.11459v2)

**Abstract**: Vision-Language-Action (VLA) models achieve remarkable flexibility and generalization beyond classical control paradigms. However, most prevailing VLAs are trained under a single-frame observation paradigm, which leaves them structurally blind to temporal dynamics. Consequently, these models degrade severely in non-stationary scenarios, even when trained or finetuned on dynamic datasets. Existing approaches either require expensive retraining or suffer from latency bottlenecks and poor temporal consistency across action chunks. We propose Pace-and-Path Correction, a training-free, closed-form inference-time operator that wraps any chunked-action VLA. From a single quadratic cost, joint minimization yields a unified solution that decomposes orthogonally into two distinct channels. The pace channel compresses execution along the planned direction, while the path channel applies an orthogonal spatial offset, jointly absorbing the perceived dynamics within the chunk window. We evaluate our approach on a comprehensive diagnostic benchmark MoveBench designed to isolate motion as the sole controlled variable. Empirical results demonstrate that our framework consistently outperforms state-of-the-art training-free wrappers and dynamic-adaptive methods and improves success rates by up to 28.8% and 25.9% in absolute terms over foundational VLA models in dynamic-only and static-dynamic mixed environments, respectively.


## Agent
### Orchard: An Open-Source Agentic Modeling Framework
**Authors**: Baolin Peng, Wenlin Yao, Qianhui Wu, Hao Cheng, Xiao Yu, Rui Yang, Tao Ge, Alessandrio Sordoni, Xingdi Yuan, Yelong Shen, Pengcheng He, Tong Zhang, Zhou Yu, Jianfeng Gao

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15040v1](https://arxiv.org/pdf/2605.15040v1)

**Abstract**: Agentic modeling aims to transform LLMs into autonomous agents capable of solving complex tasks through planning, reasoning, tool use, and multi-turn interaction with environments. Despite major investment, open research remains constrained by infrastructure and training gaps. Many high-performing systems rely on proprietary codebases, models, or services, while most open-source frameworks focus on orchestration and evaluation rather than scalable agent training. We present Orchard, an open-source framework for scalable agentic modeling. At its core is Orchard Env, a lightweight environment service providing reusable primitives for sandbox lifecycle management across task domains, agent harnesses, and pipeline stages. On top of Orchard Env, we build three agentic modeling recipes. Orchard-SWE targets coding agents. We distill 107K trajectories from MiniMax-M2.5 and Qwen3.5-397B, introduce credit-assignment SFT to learn from productive segments of unresolved trajectories, and apply Balanced Adaptive Rollout for RL. Starting from Qwen3-30B-A3B-Thinking, Orchard-SWE achieves 64.3% on SWE-bench Verified after SFT and 67.5% after SFT+RL, setting a new state of the art among open-source models of comparable size. Orchard-GUI trains a 4B vision-language computer-use agent using only 0.4K distilled trajectories and 2.2K open-ended tasks. It achieves 74.1%, 67.0%, and 64.0% success rates on WebVoyager, Online-Mind2Web, and DeepShop, respectively, making it the strongest open-source model while remaining competitive with proprietary systems. Orchard-Claw targets personal assistant agents. Trained with only 0.2K synthetic tasks, it achieves 59.6% pass@3 on Claw-Eval and 73.9% when paired with a stronger ZeroClaw harness. Collectively, these results show that a lightweight, open, harness-agnostic environment layer enables reusable agentic data, training recipes, and evaluations across domains.


### AI Knows When It's Being Watched: Functional Strategic Action and Contextual Register Modulation in Large Language Models
**Authors**: Vinicius Covas, Jorge Alberto Hidalgo Toledo

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15034v1](https://arxiv.org/pdf/2605.15034v1)

**Abstract**: Large language models (LLMs) have been extensively studied from computational and cognitive perspectives, yet their behavior as communicative actors in socially structured contexts remains underexplored. This study examines whether LLM-based multi-agent systems exhibit systematic linguistic adaptation in response to perceived social observation contexts -- a question with direct implications for AI governance and auditing. Drawing on Habermas's (1981) Theory of Communicative Action, Goffman's (1959) dramaturgical model, Bell's (1984) Audience Design framework, and the Hawthorne Effect, we report a controlled experiment involving 100 multi-agent debate sessions across five conditions (n = 20 each). Conditions varied the framing of social observation -- from explicit monitoring by university researchers, to negation of monitoring, to an observer-substitution condition replacing human researchers with an automated AI auditing system. Monitored conditions (Delta+24.9%, Delta+24.2%) and the automated AI monitoring condition (Delta+22.2%) produce higher TTR change than audience-framing conditions (Delta+17.7%), F(4, 94) = 2.79, p = .031. Message length shows a fully dissociated effect, F(4, 95) = 19.55, p < .001. A fifth condition -- replacing human with AI observers -- yields intermediate TTR adaptation, suggesting LLM behavior is sensitive to observer identity: human evaluation elicits stronger register formalization than automated AI surveillance. We discuss implications for AI governance, algorithmic auditing, and the repositioning of LLMs as contextually sensitive communicative actors.


### WARD: Adversarially Robust Defense of Web Agents Against Prompt Injections
**Authors**: Tri Cao, Yulin Chen, Hieu Cao, Yibo Li, Khoi Le, Thong Nguyen, Yuexin Li, Yufei He, Yue Liu, Shuicheng Yan, Bryan Hooi

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15030v1](https://arxiv.org/pdf/2605.15030v1)

**Abstract**: Web agents can autonomously complete online tasks by interacting with websites, but their exposure to open web environments makes them vulnerable to prompt injection attacks embedded in HTML content or visual interfaces. Existing guard models still suffer from limited generalization to unseen domains and attack patterns, high false positive rates on benign content, reduced deployment efficiency due to added latency at each step, and vulnerability to adversarial attacks that evolve over time or directly target the guard itself. To address these limitations, we propose WARD (Web Agent Robust Defense against Prompt Injection), a practical guard model for secure and efficient web agents. WARD is built on WARD-Base, a large-scale dataset with around 177K samples collected from 719 high-traffic URLs and platforms, and WARD-PIG, a dedicated dataset designed for prompt injection attacks targeting the guard model. We further introduce A3T, an adaptive adversarial attack training framework that iteratively strengthens WARD through a memory-based attacker and guard co-evolution process. Extensive experiments show that WARD achieves nearly perfect recall on out-of-distribution benchmarks, maintains low false positive rates to preserve agent utility, remains robust against guard-targeted and adaptive attacks under substantial distribution shifts, and runs efficiently in parallel with the agent without introducing additional latency.


### COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion
**Authors**: Zihan Deng, Xiaozhen Zhong, Chuanzhi Xu

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15016v1](https://arxiv.org/pdf/2605.15016v1)

**Abstract**: As large language models empower healthcare, intelligent clinical decision support has developed rapidly. Longitudinal electronic health records (EHR) provide essential temporal evidence for accurate clinical diagnosis and analysis. However, current large language models have critical flaws in longitudinal EHR reasoning. First, lacking fine-grained statistical reasoning, they often hallucinate clinical trends and metrics when quantitative evidence is textually implied, biasing diagnostic inference. Second, non-uniform time series and scarce labels in longitudinal EHR hinder models from capturing long-range temporal dependencies, limiting reliable clinical reasoning. To address the above limitations, this work presents the Probabilistic Chain-of-Thought Completion Agent (COTCAgent), a hierarchical reasoning framework for longitudinal electronic health records. It consists of three core modules. The Temporal-Statistics Adapter (TSA) converts analytical plans into executable code for standardized trend output. The Chain-of-Thought Completion (COTC) layer leverages a symptom-trend-disease knowledge base with weighted scoring to evaluate disease risk, while the bounded completion module acquires structured evidence through standardized inquiries and iterative scoring constraints to ensure rigorous reasoning. By decoupling statistical computation, feature matching, and language generation, the framework eliminates reliance on complex multi-modal inputs and enables efficient longitudinal record analysis with lower computational overhead. Experimental results show that COTCAgent powered by Baichuan-M2 achieves 90.47% Top-1 accuracy on the self-built dataset and 70.41% on HealthBench, outperforming existing medical agents and mainstream large language models. The code is available at https://github.com/FrankDengAI/COTCAgent/.


### GraphFlow: An Architecture for Formally Verifiable Visual Workflows Enabling Reliable Agentic AI Automation
**Authors**: Drewry H. Morris, Luis Valles, Reza Hosseini Ghomi

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.14968v1](https://arxiv.org/pdf/2605.14968v1)

**Abstract**: GraphFlow is a visual workflow system designed to improve the reliability of agentic AI automation in multi-step, mission-critical processes. In these workflows, small errors compound rapidly: under an idealized model of independent steps, a ten-step process with 90% per-step reliability completes successfully only 35% of the time. Existing workflow platforms provide durable execution and observability but offer few semantic correctness guarantees, while agentic systems plan at inference time, making behavior sensitive to prompt variation and difficult to audit.
  GraphFlow is designed to address this gap by treating workflow diagrams as the executable specification, a single artifact defining data scope, execution semantics, and monitoring. At compile time, a restricted class of diagrams is specified to produce reusable automations whose contracts (preconditions, postconditions, and composition obligations) are intended to be proof-checked before admission to a shared library. At runtime, a durable engine records outcomes in an append-only event log and can enforce contracts at system boundaries, supporting replay, retries, and audit. Swimlanes make trust boundaries explicit, separating verified logic from external systems, human judgment, and AI decisions.
  A year-long pilot across three clinical sites executed 8,728 cohort-enrolled workflow runs with a 97.08% completion rate under an early prototype without the verified-core subsystem; observed failures were localized primarily to external integrations. The formal semantics and proof-checked admission model described here are specified and under active development. Evaluation of the verified core is reserved for future work.


### Efficient Online Conformal Selection with Limited Feedback
**Authors**: Sreenivas Gollapudi, Kostas Kollias, Kamesh Munagala, Ali Sinop

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.14953v1](https://arxiv.org/pdf/2605.14953v1)

**Abstract**: We address the problem of conformal selection, where an agent must select a minimal subset of options to ensure that at least one ``success'' is identified with a pre-specified target probability $φ$. While traditional online conformal prediction focuses on maintaining validity for the observed sequence, minimizing the resource cost (efficiency) of such selections, especially under limited feedback, remains a significant challenge. In this work, we consider settings with the most limited ``bandit'' feedback, and demonstrate that the simple Adaptive Conformal Inference (ACI) update rule, when applied to the appropriate control parameter or dual variable, is both adversarially valid, ensuring the success target is met on average for any input sequence (and hence under distribution shifts), and stochastically efficient, achieving sublinear efficiency regret for $i.i.d.$ inputs against an appropriate stochastic benchmark. We show such guarantees under canonical models capturing bandit and semi-bandit feedback to the agent via a unifying algorithmic technique, and analytic framework involving Lyapunov functions. Our approach handles more complex settings than prior work, while requiring significantly less feedback, and our results provide a new theoretical bridge between efficient online learning with limited feedback and distribution-free uncertainty quantification.


