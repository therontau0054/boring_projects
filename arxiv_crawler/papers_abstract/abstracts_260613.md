# Abstracts of Papers

## World Model
### EvoArena: Tracking Memory Evolution for Robust LLM Agents in Dynamic Environments
**Authors**: Jundong Xu, Qingchuan Li, Jiaying Wu, Yihuai Lan, Shuyue Stella Li, Huichi Zhou, Bowen Jiang, Lei Wang, Jun Wang, Anh Tuan Luu, Caiming Xiong, Hae Won Park, Bryan Hooi, Zhiyuan Hu

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13681v1](https://arxiv.org/pdf/2606.13681v1)

**Abstract**: Large language model (LLM) agents have achieved strong performance on a wide range of benchmarks, yet most evaluations assume static environments. In contrast, real-world deployment is inherently dynamic, requiring agents to continually align their knowledge, skills, and behavior with changing environments and updated task conditions. To address this gap, we introduce EvoArena, a benchmark suite that models environment changes as sequences of progressive updates across terminal, software, and social domains. We further propose EvoMem, a patch-based memory paradigm that records memory evolution as structured update histories, enabling agents to reason about environmental evolution through changes in their memory. Experiments show that current agents struggle on EvoArena, achieving an average accuracy of 39.6% across evolving terminal, software, and social-preference domains. EvoMem consistently improves performance, yielding an average gain of 1.5% on EvoArena and also improving standard benchmarks such as GAIA and LoCoMo by 6.1% and 4.8%. Beyond individual tasks, EvoMem further improves chain-level accuracy by 3.7% on EvoArena, where success requires completing a consecutive sequence of related evolutionary subtasks. Mechanistic analysis shows that EvoMem improves evidence capture in the memory, indicating better preservation of complete evolving environment states. Our results highlight the importance of modeling evolution in both evaluation and memory for reliable agent deployment.


### Learning to Reason by Analogy via Retrieval-Augmented Reinforcement Fine-Tuning
**Authors**: Zilin Xiao, Qi Ma, Chun-cheng Jason Chen, Xintao Chen, Avinash Atreya, Hanjie Chen, Vicente Ordonez

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13680v1](https://arxiv.org/pdf/2606.13680v1)

**Abstract**: Retrieval-augmented generation (RAG) has become a standard mechanism for grounding language models in external knowledge, yet conventional retrieval based on lexical or semantic similarity is poorly suited for complex reasoning tasks: a semantically similar problem may demand an entirely different solution strategy, while a superficially different problem may share the same underlying reasoning pattern. We propose Retrieval-Augmented Reinforcement Fine-Tuning (RA-RFT), a post-training framework that teaches language models to reason by analogy. RA-RFT uses gold-relevance distillation to train a retriever that ranks contexts by expected reasoning benefit rather than semantic overlap, and then fine-tunes the policy model via reinforcement fine-tuning methods with retrieved analogous demonstrations, so the model learns to leverage reasoning traces under verifiable outcome rewards. We further analyze the diversity of retrieved contexts and find that reasoning-aware retrieval surfaces complementary solution strategies that provide distinct reasoning scaffolds for individual problems. Across challenging mathematical reasoning benchmarks, RA-RFT consistently outperforms standard reinforcement fine-tuning methods. For example, it improves AIME 2025 average@32 accuracy by 7.1 and 2.8 points over GRPO for Qwen3-1.7B and Qwen3-4B respectively -- suggesting that reasoning-aware retrieval is a complementary axis of improvement and orthogonal to advances in reward design or training curricula.


### Improving Robotic Generalist Policies via Flow Reversal Steering
**Authors**: Andy Tang, William Chen, Andrew Wagenmaker, Chelsea Finn, Sergey Levine

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13675v1](https://arxiv.org/pdf/2606.13675v1)

**Abstract**: Generalist policies can learn a wide range of skills from diverse robot datasets. In order to solve or improve on challenging news tasks, we need a way to infer and invoke the appropriate actions from the policy's rich behavioral prior, especially when directly commanding the policy fails. We focus on flow matching generalists and propose Flow Reversal Steering (FRS): a method that takes suboptimal but ``reasonable'' actions, finds their latent noises by passing them through the flow policy in reverse, and maps them to nearby generalist action modes. We evaluate FRS across many simulated and real-world manipulation settings. First, FRS can turn coarse semantic guidance from humans or vision-language models (VLMs) into corresponding good robot actions, improving zero-shot control. These gains can be distilled with behavioral cloning by training an auxiliary policy to output noises that the generalist maps to good actions -- showing up to 95% absolute task success rate boosts in under a minute of training. Finally, FRS enables policy improvement by bootstrapping reinforcement learning with semantic knowledge, improving on several tasks that standard RL fails to improve on.


### Modality Forcing for Scalable Spatial Generation
**Authors**: Bardienus Pieter Duisterhof, Deva Ramanan, Jeffrey Ichnowski, Justin Johnson, Keunhong Park

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13676v1](https://arxiv.org/pdf/2606.13676v1)

**Abstract**: Text-to-image (T2I) models contain rich spatial priors. Synthesizing photorealistic, cluttered scenes requires an understanding of geometry, including perspective and relative scale. Prior works adapt T2I models to leverage this prior for depth prediction, but they require dense depth data and involve complex recipes. We propose Modality Forcing, a simple, scalable post-training recipe for joint image-depth generation using a single DiT trained on sparse depth data. Modality Forcing enables conditional and joint generation of image and depth in any permutation by assigning separate noise levels per modality. Per-modality decoders let us train on sparse, real-world depth and achieve strong, generalizable depth prediction. We further show that Modality Forcing inherits the scalability of T2I pre-training: by training a set of T2I models from scratch (370M to 3.3B parameters), we find that larger models trained on more image data produce more accurate depth. Our strongest model is competitive with state-of-the-art monocular depth estimators and reduces AbsRel by 57% relative to existing joint image-depth generative models. These results provide strong evidence that image generation is a scalable pre-training objective for spatial perception. https://modality-forcing.github.io/


### RepWAM: World Action Modeling with Representation Visual-Action Tokenizers
**Authors**: Junke Wang, Qihang Zhang, Shuai Yang, Yiming Luo, Yujun Shen, Zuxuan Wu, Yu-Gang Jiang, Yinghao Xu

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13674v1](https://arxiv.org/pdf/2606.13674v1)

**Abstract**: This work presents RepWAM, a representation-centric world action model (WAM) built on representation visual-action tokenizers. Existing WAMs typically inherit reconstruction-oriented video tokenizers from pretrained video generation models. Although these tokenizers preserve visual fidelity, pixel reconstruction alone provides limited guidance for learning instruction-following dynamics that connect future prediction with robot control. To address this, we explore a semantic visual-action latent space for representation-centric world action modeling. Specifically, we train a representation visual-action tokenizer that maps visual inputs into aligned visual and latent action tokens. We then pretrain our WAM to jointly model future visual states and the latent actions that connect them under language instructions, followed by adaptation to real robot trajectories for closed-loop manipulation. Experiments on real-world manipulation tasks and simulation benchmarks show that RepWAM delivers strong performance across diverse manipulation settings, while ablations highlight the value of semantic visual-action tokenization over reconstruction-oriented alternatives. These results establish representation visual-action tokenization as a promising foundation for world action models and a step toward generalist robot policies. Code and weights will be available at https://github.com/wdrink/RepWAM.


### SpatialClaw: Rethinking Action Interface for Agentic Spatial Reasoning
**Authors**: Seokju Cho, Ryo Hachiuma, Abhishek Badki, Hang Su, Byung-Kwan Lee, Chan Hee Song, Sifei Liu, Subhashree Radhakrishnan, Seungryong Kim, Yu-Chiang Frank Wang, Min-Hung Chen

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13673v1](https://arxiv.org/pdf/2606.13673v1)

**Abstract**: Spatial reasoning, the ability to determine where objects are, how they relate, and how they move in 3D, remains a fundamental challenge for vision-language models (VLMs). Tool-augmented agents attempt to address this by augmenting VLMs with specialist perception modules, yet their effectiveness is bounded by the action interface through which those tools are invoked. In this work, we study how the design of this interface shapes the agent's capacity for open-ended spatial reasoning. Existing spatial agents either employ single-pass code execution, which commits to a full analysis strategy before any intermediate result is observed, or rely on a structured tool-call interface that often offers less flexibility for freely composing operations or tailoring the analysis to each task. Both designs offer limited flexibility for open-ended, complex 3D/4D spatial reasoning. We therefore propose SpatialClaw, a training-free framework for spatial reasoning that adopts code as the action interface. SpatialClaw maintains a stateful Python kernel pre-loaded with input frames and a suite of perception and geometry primitives, letting a VLM-backed agent write one executable cell per step conditioned on all prior outputs, enabling the agent to flexibly compose and manipulate perception results and adapt its analysis to both intermediate text and visual observations and the demands of each problem. Evaluated across 20 spatial reasoning benchmarks spanning a broad range of static and dynamic 3D/4D spatial reasoning tasks, SpatialClaw achieves 59.9% average accuracy, outperforming the recent spatial agent by +11.2 points, with consistent gains across six VLM backbones from two model families without any benchmark- or model-specific adaptation.


## Generation
### Mana: Dexterous Manipulation of Articulated Tools
**Authors**: Zhao-Heng Yin, Guanya Shi, Pieter Abbeel, C. Karen Liu

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13677v1](https://arxiv.org/pdf/2606.13677v1)

**Abstract**: Articulated tool manipulation remains a major challenge in dexterous robotics due to the need to coordinate internal degrees of freedom and contact-rich interactions. While prior work has largely focused on rigid objects, articulated tool use remains underexplored because of its physical complexity and the difficulty of learning functional grasping and manipulation policies. We present Mana (Manipulation Animator), a general sim-to-real framework that reinterprets dexterous manipulation as an animation problem. Inspired by computer animation, Mana employs a coarse-to-fine pipeline that transforms procedurally-generated grasp keyframes into manipulation trajectories through motion planning and reinforcement learning. The data generation process is largely automatic, requiring only a few mouse clicks to specify functional affordances (<1 minute per tool). Across four articulated tools spanning different scales and joint types, Mana achieves zero-shot sim-to-real transfer for both grasping and in-hand manipulation, demonstrating a scalable approach to dexterous articulated tool use.


### Automated reproducibility assessments in the social and behavioral sciences using large language models
**Authors**: Tobias Holtdirk, Pietro Marcolongo, Anna Steinberg Schulten, Felix Henninger, Stefan Rose, Sarah Ball, Bolei Ma, Frauke Kreuter, Markus Weinmann, Stefan Feuerriegel

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13670v1](https://arxiv.org/pdf/2606.13670v1)

**Abstract**: Reproducibility in the social and behavioral sciences is typically evaluated by independent researchers who reanalyze the original data to assess whether the published findings can be recovered. However, such approaches are resource-intensive and difficult to scale. Here, we show that large language models (LLMs) can automate reproducibility assessments. Using N=76 published studies with predefined claims from the behavioral and social sciences, we compare LLM-generated analysis with the original findings and human reanalysis. For 7 studies, the LLM could not produce a viable effect size estimate. For the remaining studies, our LLM pipeline recovered the original effect sizes in 41% of studies using a +/-0.05 tolerance in Cohen's d. Further, our LLM pipeline reached the same qualitative conclusion as the original study in 96% of cases, where conclusions indicate whether the reanalysis supports the original claim. For comparison, human reanalysts recovered the original effect sizes in 34% of studies and reached the same qualitative conclusion in 74% of cases. Together, these results show that LLMs can serve as a scalable tool for automated reproducibility assessment and provide a foundation for systematic auditing of empirical results in the social and behavioral sciences.


### Agents-K1: Towards Agent-native Knowledge Orchestration
**Authors**: Zongsheng Cao, Bihao Zhan, Jinxin Shi, Jiong Wang, Fangchen Yu, Zhijie Zhong, Zijie Guo, Tianshuo Peng, Zhuo Liu, Yi Xie, Xiang Zhuang, Yue Fan, Runmin Ma, Shiyang Feng, Xiangchao Yan, Anran Liu, Peng Ye, Wenlong Zhang, Shufei Zhang, Chunfeng Song, Fenghua Ling, Jie Zhou, Liang He, Bo Zhang, Lei Bai

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13669v1](https://arxiv.org/pdf/2606.13669v1)

**Abstract**: Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions, and flat \texttt{cites} edges, omitting key entities, claims, evidence, mechanisms, and method lineages essential for scientific reasoning. To this end, we introduce \textbf{Agents-K1}, an end-to-end knowledge orchestration pipeline that converts raw documents into agent-native scientific knowledge graphs. Agents-K1 integrates three components under a unifying theoretical foundation: a multimodal parser whose five-module schema captures entities, multimodal evidence, citations, and typed inter-entity relations across the full paper rather than abstracts alone; a 4B information-extraction backbone trained with GRPO under a rule-based reward; and a graphanything CLI, a tri-source agent interface that unifies web search, multimodal graph retrieval, and cross-document traversal. On top of this, we process 2.46 million scientific papers across six subjects to produce \textbf{Scholar-KG}, of which we release a one-million-paper subset, and the full Scholar-KG is accessible via the SCP link below. The same pipeline can be extended to general-domain corpora and to schema-conformant data synthesis. Extensive experiments demonstrate that Agents-K1 achieves superior performance in scientific information extraction, knowledge graph construction, and multi-hop scientific reasoning.


### SkMTEB: Slovak Massive Text Embedding Benchmark and Model Adaptation
**Authors**: Marek Šuppa, Andrej Ridzik, Daniel Hládek, Natália Kňažeková, Viktória Ondrejová

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13647v1](https://arxiv.org/pdf/2606.13647v1)

**Abstract**: We introduce SkMTEB, the first comprehensive MTEB-style text embedding benchmark for Slovak, a low-resource West Slavic language, comprising 31 datasets across 7 task types -- nearly 4$\times$ the depth of existing multilingual benchmark coverage for Slovak. Our evaluation of 31 embedding models reveals that large instruction-tuned multilingual models achieve the strongest performance, while existing Slovak-specific models trained for NLU tasks transfer poorly to embedding tasks. To address the need for efficient, locally-deployable Slovak embeddings, we develop \texttt{e5-sk-small} (45M parameters) and \texttt{e5-sk-large} (365M) by applying vocabulary trimming and fine-tuning to Multilingual E5 models. Despite size reductions of up to 62\%, our open-source models achieve competitive performance with proprietary APIs while remaining locally deployable for semantic search and retrieval-augmented generation (RAG). We release the benchmark, models, datasets, and code openly, hoping our approach offers a replicable path for other under-resourced languages.


### Aerial Wildfire Suppression Planning with a Hybrid CNN-Cellular Automata Fire Model
**Authors**: Ion Matei, Maksym Zhenirovskyy, Takuya Kurihana, Rohit Vupala, Anthony Wong

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13633v1](https://arxiv.org/pdf/2606.13633v1)

**Abstract**: Aerial wildfire suppression requires not only predicting fire spread, but also designing effective intervention strategies under operational and environmental uncertainty. We present a modeling and optimization framework for aerial wildfire suppression that combines a hybrid neural-cellular automaton wildfire model with gradient-based design of targeted aerial drops. The wildfire model predicts spatially varying spread behavior from terrain, fuel, and wind data, while the intervention module determines binary drop actions with continuous-valued location and orientation parameters mapped to the simulation grid. Water and retardant are represented with distinct suppression effects, corresponding to immediate reduction of active burning and persistent reduction of future spread. To evaluate the robustness of the resulting suppression plans, we quantify both aleatoric uncertainty through Monte Carlo sampling of daily fire-state realizations and epistemic uncertainty through spatially correlated prediction-error perturbations. A case study based on the 2020 Bear Fire shows that the framework can generate coherent aerial suppression schedules for reducing total fire-affected area and can support uncertainty-aware analysis of wildfire intervention strategies.


### Valid Inference with Synthetic Data via Task Exchangeability
**Authors**: Lezhi Tan, Tijana Zrnic

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13629v1](https://arxiv.org/pdf/2606.13629v1)

**Abstract**: There is a proliferation of work arguing for the use of synthetic data in scientific research. For example, social scientists are arguing for the use of LLM-generated "silicon samples" in pilot studies; AI evaluations increasingly rely on "LLM-as-a-judge" outputs; and proteomics research is accelerated by generative models that produce synthetic protein structures. These developments raise an intriguing possibility: synthetic data may help researchers ask more questions, run more studies, and accelerate discovery. But they also raise a fundamental concern: synthetic data can be biased, noisy, and misspecified. In this work, we propose statistical principles for using synthetic data in scientific research with provable validity guarantees. The key insight is a new technical condition that we call task exchangeability. Informally, this is a requirement that the researcher can identify historical tasks, for which real data is available, such that their current task of interest is exchangeable with the historical tasks in an appropriate mathematical sense. We develop methods for valid inference under task exchangeability, together with extensions that provide guarantees even beyond exchangeability. We demonstrate the framework on public opinion surveys with silicon samples and AI evaluation with autoraters.


## VLA
### LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories
**Authors**: Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu, Chenxi Li, Daqi Gao, Zeqin Su, Jintao Xing, Zirui Xue, Rui Li, Xiangyu Zhao, Shuofei Qiao, Minting Pan, Wangmeng Zuo, Lei Bai, Dongzhan Zhou, Ningyu Zhang, Huajun Chen

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13578v1](https://arxiv.org/pdf/2606.13578v1)

**Abstract**: Scientific laboratories increasingly rely on AI systems to reason about experiments, but the physical act of doing science remains largely outside their reach. AI can help read literature, generate hypotheses, and plan protocols, yet the execution of those protocols at the bench still requires a human operator. Vision-Language-Action (VLA) models provide one possible interface between written protocols and robot execution, but existing policies are trained mostly on household and tabletop demonstrations and rarely encounter the instruments, transparent liquids, or fixed protocol workflows found in scientific laboratories. Closing this gap requires both laboratory-specific supervision and a unified learning framework that can accommodate the diverse robot embodiments used to execute experimental protocols. We therefore identify data and embodiment as central bottlenecks alongside model design. To address the data side, we build RoboGenesis, a simulation-based workflow and data engine that composes configured laboratory workflows from atomic skills, validates and filters rollouts, and exports structured demonstrations across supported robot profiles. On the policy side, we present LabVLA, trained with a two-stage recipe: FAST action token pretraining first makes the Qwen3-VL-4B-Instruct backbone action aware before any continuous control is learned, and flow matching posttraining then attaches a DiT action expert under knowledge insulation. On the LabUtopia benchmark, LabVLA achieves the highest average success rate among all evaluated baselines under both in-distribution and out-of-distribution settings.


### An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics
**Authors**: Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu, Peijia Li, Jiaming Gu, Quan Lu, Qi Wang, Bin Ji, Ting Xiao

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.12936v1](https://arxiv.org/pdf/2606.12936v1)

**Abstract**: Wet-lab robots can improve the reproducibility, throughput, and safety of biomedical experiments, but scaling their learning requires customizable simulators for safe and reproducible task generation, open editable laboratory assets, and efficient pipelines that turn limited demonstrations into usable training data. We present Pipette, an embodied simulation platform, benchmark, and data-efficient augmentation framework for wet-lab robot learning. Pipette releases over 43 open-source and re-editable wet-lab assets, together with an extensible asset-building pipeline. A key component of Pipette is its simulation-based data augmentation pipeline, replaying human demonstrations in simulation, applies lighting, camera, speed, and action perturbations, and filters generated episodes with automatic task success checks, rapidly expanding usable training data from limited manual demonstrations. We further introduce an 11-task wet-lab embodied benchmark covering sample handling, culture-ware manipulation, device operation, and precision placement. With only 30 demonstrations per task, ACT achieves 65.5% average success rate, while simulation augmentation improves SmolVLA from 44.1% to 74.7% and π0 from 40.4% to 46.5%, validating the effectiveness of Pipette for data-efficient VLA training and evaluation. Pipette also supports natural-language-driven scene construction and task registration, lowering the barrier for non-expert users to define new wet-lab robotic tasks.


### PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation
**Authors**: Mahmoud Srewa, Praneetsai Iddamsetty, Mohammad Abdullah Al Faruque, Salma Elmalaki

**Published Date**: 2026-06-10

**Updated Date**: 2026-06-10

**PDF Url**: [2606.12616v1](https://arxiv.org/pdf/2606.12616v1)

**Abstract**: Closed-loop driving simulators typically populate their environments with non-ego traffic agents that behave largely the same way, produced either by rule-based traffic managers or by learned models trained toward a single behavioral mode. Recent work introduces style variation through post-hoc labels on observational data or LLM-inferred reward weights, but these signals act as proxies for what a style should reward rather than demonstrations of humans explicitly asked to drive in that style. We introduce PersonaDrive, a pipeline that conditions a vision-language-action (VLA) driving agent on retrieved demonstrations from a style-instructed human driving dataset, in which participants drive CARLA leaderboard routes under aggressive, neutral, and conservative instructions on a driver-in-the-loop rig. The pipeline has three stages: (i) offline triplet mining over per-style human driving data using a combined image-text similarity score; (ii) training a lightweight retrieval head that fuses frozen visual features with a small control encoder over per-style databases; and (iii) fine-tuning a single VLA backbone to treat retrieved context points as in-context behavioral demonstrations during waypoint prediction. At inference, the same backbone is conditioned on any style by swapping which per-style database the retrieval head queries, so selecting a style requires no per-style retraining while enabling human-style, style-diverse non-ego agents for closed-loop simulation. On Bench2Drive, PersonaDrive (no style) improves the driving score by 4.6% over SimLingo and 2.5% over HiP-AD, and under style conditioning attains the highest driving score in every style within a roughly 2% band (its weakest style surpassing the strongest baseline, DMW, by 5.4%), while average speed and acceleration rise by 18% and 25% from the conservative to the aggressive instruction.


### $μ$VLA: On Recurrent Memory for Partially Observable Manipulation in VLA Models
**Authors**: Egor Cherepanov, Nikita Kachaev, Daniil Zelezetsky, Aydar Bulatov, Artem Pshenitsyn, Yuri Kuratov, Alexey Skrynnik, Aleksandr I. Panov, Alexey K. Kovalev

**Published Date**: 2026-06-10

**Updated Date**: 2026-06-10

**PDF Url**: [2606.12497v1](https://arxiv.org/pdf/2606.12497v1)

**Abstract**: Vision-language-action (VLA) models predict chunks of future actions from the current observation, an assumption that fails under partial observability, where decisions depend on information no longer visible. Existing memory-augmented VLAs simultaneously introduce recurrence, retrieval, compression modules, auxiliary objectives, hierarchical memory, or task-specific architectural changes, so the contribution of recurrence itself remains entangled with surrounding machinery. We present a controlled isolation study of recurrence in a strong pretrained VLA backbone. Our formulation augments the transformer with a small set of learnable memory tokens carried across timesteps and updated through self-attention, trained end to end with truncated backpropagation through time, with no auxiliary losses and no architectural changes. We instantiate this as $μ$VLA, a family of OpenVLA-OFT variants parameterized by memory width m, TBPTT length K, and the memory update rule (cross-step gradients or a detached EMA), so that recurrence is the only varying factor. On MIKASA-Robo, $μ$VLA improves average success rate on five training tasks from 0.42 to 0.84 at the strongest setting and reaches 0.23 on held-out tasks with the same memory structure versus 0.07 for the memoryless baseline. On tasks requiring different memory structure, performance remains near baseline. On LIBERO, the strongest recurrent variant achieves 96.2% average success, indicating no regression under full observability. We interpret these results as a calibration of the capability envelope of minimal in-backbone recurrence, identifying the regime in which it is sufficient and the regime where additional memory structure is required. Demos and videos can be found in https://avanturist322.github.io/mu-vla/.


### LIBERO-Occ: Evaluating and Improving Vision-Language-Action Models under Scene-Induced Occlusion via Viewpoint Imagination
**Authors**: Taishan Li, Jiwen Zhang, Siyuan Wang, Xuanjing Huang, Zhongyu Wei

**Published Date**: 2026-06-09

**Updated Date**: 2026-06-09

**PDF Url**: [2606.10862v1](https://arxiv.org/pdf/2606.10862v1)

**Abstract**: Vision-Language-Action (VLA) models achieve strong performance on standard manipulation benchmarks, but most evaluations assume that task-relevant objects are fully visible. This assumption often fails in realistic settings, where occlusion makes manipulation partially observable. In this paper, we study \textit{scene-induced occlusion} as a fundamental challenge for VLA models and introduce \textbf{LIBERO-Occ}, an occlusion-oriented extension of LIBERO. Experiments show that state-of-the-art VLAs suffer substantial performance degradation under occlusion. To address this issue, we propose \textbf{Viewpoint Imagination (VIM)}, which generates a complementary view from an occluded primary observation and conditions action prediction on both observed and imagined evidence. VIM improves robustness across task suites, occlusion types, and severity levels without requiring additional cameras at deployment time, suggesting that viewpoint imagination is an promising mechanism for perception completion in partially observable manipulation. Our benchmark and corresponding code are available at: \href{https://github.com/litsh/Libero-Occ}{https://github.com/litsh/Libero-Occ}.


### Dexterous Point Policy: Learning Point-based Dexterous Hand Policies from Human Demonstrations
**Authors**: Beomjun Kim, Seong Hyeon Park, Seunghoon Sim, Seungjun Moon, Sanghyeok Lee, Jinwoo Shin

**Published Date**: 2026-06-09

**Updated Date**: 2026-06-09

**PDF Url**: [2606.10614v1](https://arxiv.org/pdf/2606.10614v1)

**Abstract**: Robotic foundation models pre-trained on human demonstration videos have shown promise, but a significant embodiment gap remains when the resulting policies are deployed on real robots. A common remedy is to fine-tune these models on robot-specific demonstrations. However, robot data collection can be prohibitively expensive and time-consuming, which is particularly acute in dexterous manipulation, e.g., teleoperating a multi-fingered hand for even a single atomic task can take days. To address this, we introduce Dexterous Point Policy, a framework that learns dexterous manipulation policies directly from human videos and requires no robot demonstrations. Our core insight is that a unified 3D keypoint representation can bridge human and robot embodiments when used for both observations and actions. Specifically, we extract 3D keypoints of task-relevant objects and human hands from raw videos, and train an autoregressive transformer over these keypoints. We observe that at the keypoint level, specifically the wrist and fingertips, human and robot behaviors closely align, enabling direct policy transfer. On a suite of real-robot tasks spanning pick-and-place and tool use, Dexterous Point Policy attains 75.0% success, whereas a state-of-the-art VLA baseline reaches only 1.0%. Furthermore, our method generalizes strongly to unseen scenarios, including multi-object environments and novel object categories.


## Agent
### EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery
**Authors**: Amy Xin, Jiening Siow, Junjie Wang, Zijun Yao, Fanjin Zhang, Jian Song, Lei Hou, Juanzi Li

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13662v1](https://arxiv.org/pdf/2606.13662v1)

**Abstract**: LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produced results that outperform human-designed approaches. As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent behavior. We frame this as environment engineering: building environments that amplify productive behaviors, such as open-ended exploration, systematic artifact management, and inter-agent collaboration, while suppressing harmful behaviors, such as reward hacking and high-friction human oversight. We present EurekAgent, an environment-engineered agent system for metric-driven autonomous scientific discovery. EurekAgent engineers the environment along four dimensions: permissions engineering for bounded agent execution and isolated evaluation; artifact engineering for filesystem and Git-based collaboration; budget engineering for budget-aware exploration; and human-in-the-loop engineering for easy human supervision and intervention. EurekAgent sets new state-of-the-art results on multiple mathematics, kernel engineering, and machine learning tasks, including new state-of-the-art 26-circle packing results discovered with less than $11 in total API cost. We open-source our code and results, and call for environment engineering as a core research direction for developing reliable autonomous research agents.


### Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks
**Authors**: Achraf Hsain, Sultan Almuhammadi

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13621v1](https://arxiv.org/pdf/2606.13621v1)

**Abstract**: Shielded reinforcement learning is typically presented as a runtime safety mechanism that compiles temporal-logic specifications into automata restricting an agent's actions. We argue this is the wrong product. The same automata-theoretic machinery -- specification compilation, product game construction, attractor computation, and winning-region extraction -- is better read as a design-time analytical instrument whose outputs are structural insights about a system rather than runtime constraints on a deployed agent.
  We instantiate this through a constrained two-player safety game for network defense. The two specifications are enforced asymmetrically: the defender specification defines the unsafe region of the game, whereas the attacker specification restricts the adversary's legal actions during attractor computation. Solving the game yields a defensibility verdict -- a formal certificate that a topology-specification pair is or is not defensible -- with the associated winning region and shield.
  Beyond the binary verdict, we derive topology-level metrics from the attractor structure and combine them with post-convergence behavior from shield-constrained adversarial multi-agent reinforcement learning. Together these form a defensibility fingerprint capturing both a network's formal safety properties and its operational behavior under adaptive play.
  A what-if analysis shows that formal defensibility and operational effectiveness capture distinct aspects of security: small architectural changes can produce large shifts in operational outcomes while leaving formal safety margins nearly unchanged. Shield synthesis is thus most valuable not as a deployment mechanism for safe agents, but as a framework for answering architectural questions about whether, where, and how a system can be defended. The defensibility verdict is the output, not the safe policy.


### AgentBeats: Agentifying Agent Assessment for Openness, Standardization, and Reproducibility
**Authors**: Xiaoyuan Liu, Jianhong Tu, Yuqi Chen, Siyuan Xie, Sihan Ren, Tianneng Shi, Gal Gantar, Evan Sandoval, Donghyun Lee, Daniel Miao, Peter J. Gilbert, Nick Hynes, Mauro Staver, Warren He, David Marn, Andrew Low, Xi Zhang, Elron Bandel, Michal Shmueli-Scheuer, Siva Reddy, Alexandre Drouin, Alexandre Lacoste, Ramayya Krishnan, Elham Tabassi, Yu Su, Victor Barres, Chenguang Wang, Wenbo Guo, Dawn Song

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13608v1](https://arxiv.org/pdf/2606.13608v1)

**Abstract**: Agent systems are advancing quickly across domains, but their evaluation remains fragmented. Most benchmarks rely on fixed, LLM-centric harnesses that require heavy integration, create test-production mismatch, and limit fair comparison across diverse agent designs. The root problem is the lack of an open, agent-agnostic assessment interface. We advocate Agentified Agent Assessment (AAA), where evaluation is performed by judge agents and all participants interact through standardized protocols: A2A for task management and MCP for tool access. Conventional benchmarking defines two separate interfaces, one for the benchmark and one for the agent, while AAA only needs one; this yields a generic, unified framework that separates assessment logic from agent implementation and enables reproducible, interoperable, and multi-agent evaluation. We further introduce AgentBeats as a concrete realization of AAA: we identify five practical operation modes that make standardized assessment compatible with real-world constraints on openness, privacy, and reproducibility.
  To evaluate our design at scale, we conduct two studies: a five-month open competition that drew 298 judge agents across 12 categories together with 467 subject agents from independent participants, showing that AAA applies across a heterogeneous range of benchmarks; and a case study on coding agents that confirms agentified evaluation preserves fidelity with the public record while surfacing previously missing head-to-head results, yielding research insights about agent design. Combining a community-scale field study and a controlled coding case study, we verify that AAA delivers coverage, practicality, and fidelity across heterogeneous scenarios at scale. Together, AAA and AgentBeats offer a clear path toward open, standardized, and reproducible agent assessment.


### Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch
**Authors**: Haochen Wu, Yi Hou, Shiguang Xie

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13604v1](https://arxiv.org/pdf/2606.13604v1)

**Abstract**: Dispatch in three-sided marketplaces provides a natural setting for reinforcement learning from world feedback: decisions are evaluated by delayed operational outcomes such as delivery speed, courier utilization, and merchant congestion. We present a deployed reinforcement learning system at DoorDash that adapts dispatch objective weights in a large-scale food-delivery marketplace using delayed signals. Rather than replacing the combinatorial assignment optimizer, a store-level policy learned from logged marketplace data selects a discrete multiplier that shifts the dispatch optimizer's tradeoff between delivery quality and batching efficiency. This interface enables offline policy learning under noisy, delayed, and coupled feedback while preserving production feasibility constraints and operational safeguards. We train a shared value function using centralized offline data and decentralized store-level execution, with Double Q-learning targets and a conservative regularizer to reduce out-of-distribution value overestimation. In a production switchback experiment, the offline-trained policy increases batching and reduces courier-side time costs without degrading customer-facing delivery quality. Results illustrate how world feedback from a live economic and logistics system can be used to safely adapt decision policies online.


### EpiBench: Verifiable Evaluation of AI Agents on Epigenomics Analysis
**Authors**: Harihara Muralidharan, Reema Baskar, Soo Hee Lee, Tim Proctor, Kenny Workman

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13602v1](https://arxiv.org/pdf/2606.13602v1)

**Abstract**: We introduce EpiBench, a verifiable benchmark for short-horizon epigenomics analysis. EpiBench evaluates whether agents can make well-defined analysis decisions from realistic workflow states and return deterministically gradable answers. The benchmark includes 106 evaluations across CUT\&Tag/CUT\&RUN, ATAC-seq, ChIP-seq, and DNA methylation workflows. Across 5,088 valid trajectories from 16 model-harness pairs, no system passed a majority of attempts: GPT-5.5 / Pi led at 45.0\% (143/318 attempts; 95\% confidence interval (CI), 36.3--53.7), followed by GPT-5.5 / OpenAI Codex at 39.9\% (127/318 attempts; 95\% CI, 31.6--48.3). Claude Opus 4.8 Max / Pi and GPT-5.4 / Pi each passed 39.0\% (124/318 attempts; 95\% CI, 30.2--47.8 and 31.0--47.0, respectively). Performance varies across assay types, and many failed runs still contain parts of the correct answer. Agents often found the right files and computed useful intermediate results, but failed when the task required deeper, assay-specific scientific judgment.


### Reward Modeling for Multi-Agent Orchestration
**Authors**: King Yeung Tsang, Zihao Zhao, Vishal Venkataramani, Haizhou Shi, Zixuan Ke, Semih Yavuz, Shafiq Joty, Hao Wang

**Published Date**: 2026-06-11

**Updated Date**: 2026-06-11

**PDF Url**: [2606.13598v1](https://arxiv.org/pdf/2606.13598v1)

**Abstract**: Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations. OrchRM leverages intermediate artifacts from multi-agent executions to construct win-lose pairs for Bradley-Terry reward model training. Unlike existing MAS test-time scaling and orchestrator training frameworks that rely on costly sub-agent rollouts, OrchRM operates directly at the orchestration level, enabling efficient and high-performing reward-guided orchestrator training and MAS test-time scaling. OrchRM improves training efficiency by up to 10x in token usage while improving MAS test-time scaling performance by up to 8% in accuracy. These gains consistently transfer across multiple domains, including mathematical reasoning, web-based question answering, and multi-hop reasoning, demonstrating orchestration-level reward modeling as a scalable direction for robust multi-agent orchestration. Code will be available at https://github.com/Wang-ML-Lab/OrchRM.


