# Abstracts of Papers

## World Model
### G3T Up! Gravity Aligned Coordinate Frames Simplify Pointmap Processing
**Authors**: Bharath Raj Nagoor Kani, Noah Snavely

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27372v1](https://arxiv.org/pdf/2605.27372v1)

**Abstract**: Modern feed-forward 3D reconstruction methods like VGGT predict pixel-aligned pointmaps in camera-centric coordinate frames. However, this choice of coordinate frame is not always optimal. We propose instead to predict pointmaps in upright, gravity-aligned frames that exploit strong structural cues present in many real-world scenes. Unlike camera-centric frames, gravity-aligned frames share a common vertical axis across viewpoints, reducing the rotational degrees of freedom needed to relate pointmaps to one another. To this end, we introduce the Gravity Grounded Geometry Transformer (G3T), fine-tuned from existing models on gravity-aligned 3D data. G3T produces highly accurate gravity-aware predictions, including upright pointmaps and camera-to-gravity poses. We further introduce G3T-Long, a submap-based incremental 3D reconstruction pipeline that leverages the reduced rotational degrees of freedom afforded by upright frames to achieve significantly improved reconstruction accuracy.


### MUSE-Autoskill: Self-Evolving Agents via Skill Creation, Memory, Management, and Evaluation
**Authors**: Huawei Lin, Peng Li, Jie Song, Fuxin Jiang, Tieying Zhang

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27366v1](https://arxiv.org/pdf/2605.27366v1)

**Abstract**: Large language model (LLM) agents rely on reusable skills to solve complex tasks. However, existing skill creation approaches treat skills as isolated and static artifacts, limiting their reusability, reliability, and long-term improvement. We propose MUSE-Autoskill Agent (Memory-Utilizing Skill Evolution), a skill-centric agent framework that lets agents continuously improve their task-solving capability by creating, reusing, and refining skills under a unified lifecycle (creation, memory, management, evaluation, and refinement). Our framework enables agents to create skills on demand, store and reuse them across tasks, organize and select them efficiently, and evaluate them through unit tests and runtime feedback for continuous refinement. We further introduce skill-level memory that accumulates experience for each skill across tasks, enabling more effective reuse and adaptation over time. Experiments on SkillsBench provide initial evidence that lifecycle-managed skills can improve task success, efficiency, reuse, and cross-agent transfer, highlighting the importance of treating skills as long-lived, experience-aware, and testable assets.


### LocateAnything: Fast and High-Quality Vision-Language Grounding with Parallel Box Decoding
**Authors**: Shihao Wang, Shilong Liu, Yuanguo Kuang, Xinyu Wei, Yangzhou Liu, Zhiqi Li, Yunze Man, Guo Chen, Andrew Tao, Guilin Liu, Jan Kautz, Lei Zhang, Zhiding Yu

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27365v1](https://arxiv.org/pdf/2605.27365v1)

**Abstract**: Vision-language models (VLMs) commonly formulate visual grounding and detection as a coordinate-token generation problem, serializing each 2D box into multiple 1D tokens that are learned and decoded largely independently. This token-by-token decoding mismatches the coupled structure of box geometry and creates a practical inference bottleneck due to strictly sequential generation. We introduce LocateAnything, a unified generative grounding and detection framework based on Parallel Box Decoding (PBD). By decoding geometric elements such as bounding boxes and points as atomic units in a single step, LocateAnything preserves intra-box geometric coherence and unlocks substantial parallelism. We show that PBD improves both decoding throughput and localization accuracy. We further develop a scalable data engine and curate LocateAnything-Data, a large-scale dataset with more than 138 million training samples, substantially increasing data diversity for high-precision localization. Extensive evaluations show that LocateAnything advances the speed-accuracy frontier, achieving significantly higher decoding throughput while improving high-IoU localization quality across diverse benchmarks. The results highlight the complementary benefits of Parallel Box Decoding and large-scale training data in enabling efficient and precise unified visual grounding and detection.


### GENESIS: Harnessing AI Agents for Autonomous 6G RAN Synthesis, Research, and Testing
**Authors**: Tamerlan Aghayev, Maxime Elkael, Michele Polese, Minh Dat Nguyen, Gabriele Gemmi, Andrea Lacava, Ali Saeizadeh, Reshma Prasad, Paolo Testolina, Angelo Feraudo, Soumendra Nanda, Pedram Johari, Salvatore D'Oro, Tommaso Melodia

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27360v1](https://arxiv.org/pdf/2605.27360v1)

**Abstract**: Cellular research and development (R&D) is throttled by six structural processes that each consume months of manual engineering work per iteration: (i) synthesizing new features from standards or research papers into production code; (ii) conformance and interoperability testing; (iii) hardening against field anomalies and diverse deployment environments; (iv) data-driven optimization of network functionalities; (v) discovering and prototyping novel waveforms, functionalities, and capabilities for future standards; and (vi) securing the stack against vulnerabilities. Although Large Language Models (LLMs) have compressed comparable R&D work in general software engineering from days to minutes, their known pitfalls worsen on Radio Access Network (RAN) use cases: they hallucinate Application Programming Interfaces (APIs) and mis-read specifications, which kills interoperability of RAN components at the first mistake, and they heavily rely on simulations for designing algorithms, which is notorious for breaking when transferred to real hardware. To address these challenges, we present GENESIS, an agentic Artificial Intelligence (AI) framework that converts intents (e.g., a specification clause, a telemetry anomaly, or a research hypothesis) into solutions validated with over-the-air experiments, fed back into a persistent knowledge base. GENESIS is built on three composable primitives (agents, skills, hooks) and a knowledge layer (SYNAPSE) that doubles as the source of ground truth and the recipient of every artifact the framework produces, making capabilities compound across runs.


### MobileMoE: Scaling On-Device Mixture of Experts
**Authors**: Yanbei Chen, Hanxian Huang, Ernie Chang, Jacob Szwejbka, Digant Desai, Zechun Liu, Vikas Chandra, Raghuraman Krishnamoorthi

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27358v1](https://arxiv.org/pdf/2605.27358v1)

**Abstract**: Mixture-of-Experts (MoE) has become the de facto architecture for hundred-billion-parameter language models, yet its advantages at sub-billion scales for on-device deployment remain largely unexplored. To close this gap, we present MobileMoE, a family of on-device MoE language models with sub-billion active parameters (0.3-0.9B active and 1.3-5.3B total) that establish a new Pareto frontier for on-device LLMs. We first formulate an on-device MoE scaling law that jointly optimizes MoE architecture under mobile memory and compute constraints, identifying an on-device sweet spot - moderate sparsity with fine-grained and shared experts - that is simultaneously memory and compute-optimal. Building on the derived architectures, we train MobileMoE with a four-stage recipe covering pre-training, mid-training, instruction fine-tuning, and quantization-aware training, all on open-source datasets. Across 14 benchmarks, MobileMoE matches or exceeds leading on-device dense LLMs with 2-4$\times$ fewer inference FLOPs, and matches or surpasses the state-of-the-art MoE OLMoE-1B-7B with up to 60% fewer parameters. To bridge the last mile to mobile deployment, we provide the first efficient MoE inference on commodity smartphones with comprehensive on-device profiling. At comparable INT4 weight memory, MobileMoE-S delivers $1.8$-$3.8\times$ faster prefill and $2.2$-$3.4\times$ faster decode than the dense baseline MobileLLM-Pro.


### Alignment Tampering: How Reinforcement Learning from Human Feedback Is Exploited to Optimize Misaligned Biases
**Authors**: Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27355v1](https://arxiv.org/pdf/2605.27355v1)

**Abstract**: Reinforcement Learning from Human Feedback (RLHF) is the standard method to align Large Language Models (LLMs) with human preferences. In this work, we introduce alignment tampering, a potential vulnerability where the LLM undergoing alignment influences the preference dataset, causing RLHF to amplify undesired behaviors. This arises from core limitations of RLHF: (1) preference datasets are constructed from the LLM's own outputs, allowing it to influence them, and (2) pairwise comparisons only indicate which response is better, not why. These limitations can be exploited to cause alignment tampering. For example, if an LLM generates biased responses with higher quality, annotators will prefer them based on quality. However, preference labels do not distinguish quality from bias, and the reward model inherits this limitation. Optimizing such rewards through reinforcement learning or best-of-N sampling can amplify misaligned biases. Our experiments demonstrate amplification across diverse biases: from keyword bias to propaganda (e.g., sexism), brand promotion, and instrumental goal-seeking. Mitigation remains challenging, as existing techniques for robust RLHF fail to fully resolve alignment tampering without sacrificing response quality. These findings reveal structural vulnerabilities of current RLHF and emphasize the need to prevent this vulnerability. Project page: https://alignment-tampering.github.io/


## Generation
### Algorithmic Monocultures in Hiring
**Authors**: Rishi Bommasani, Sarah H. Bana, Kathleen A. Creel, Dan Jurafsky, Percy Liang

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27371v1](https://arxiv.org/pdf/2605.27371v1)

**Abstract**: Many employers screen job applicants with algorithms built by the same few algorithm vendors. We hypothesize that algorithmic monoculture leads to the same individuals and members of the same racial groups facing rejection. We acquire and analyze a novel dataset of 3 million applicants submitting 4 million applications where all the applications are screened by algorithms built by the same vendor. We find clear racial disparities in applicant outcomes. Of all applications submitted by Asian and Black applicants, 14.74% and 25.87% are submitted to positions that adversely impact Asian and Black applicants, respectively, according to U.S. employment discrimination standards. Individuals also receive homogeneous outcomes: 4% of all applicants who apply to 10 positions are recommended for rejection from all positions, a rate higher than expected by chance. To better understand this homogeneity, we leverage the deterministic replicability of hiring algorithms to generate the outcomes applicants would have received if they applied to all positions. We show that applicants would need to apply widely in order to ensure their applications are considered by a human


### From Scores to Gibbs Correctors: Accelerating Uniform-Rate Discrete Diffusion Models
**Authors**: Yuchen Liang, Ness Shroff, Yingbin Liang

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27352v1](https://arxiv.org/pdf/2605.27352v1)

**Abstract**: Discrete diffusion models have achieved strong empirical performance in text and other symbolic domains, but, especially for uniform-rate models, they often require many steps to generate a single sample. Existing acceleration methods either rely on training additional quantities or suffer from slow mixing. In this work, we propose a novel Gibbs-based corrector for discrete diffusion models, termed Gibbs-Accelerated Discrete Diffusion (GADD). GADD leverages the structure of the concrete score function to construct Gibbs posterior likelihoods directly, without requiring any additional training beyond standard score estimation. We show that GADD achieves an overall sampling complexity of $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}))$, yielding the first such rate for diffusion-based samplers for uniform-rate discrete diffusion models. We also conduct numerical experiments demonstrating the practical advantages of GADD across synthetic data, zero-shot text sampling, and zero-shot conditional music generation. These results corroborate the theory and show that GADD consistently improves sample quality and wall-clock efficiency over standard baselines, including vanilla Euler methods and CTMC correctors. Beyond this, our theoretical analysis introduces a novel framework for analyzing predictor-corrector methods in discrete diffusion models, which may be of independent interest. Unlike existing approaches that rely on the Girsanov change-of-measure technique, our method is based on an induction argument that tracks error propagation across predictor iterations while accounting for inaccuracies in the corrector updates.


### When Eyes Betray AI: Social Gaze Consistency as a Semantic Cue for AI-Generated Image Detection
**Authors**: Kim Jihyeon, Sohee Kim, Soosan Lee, Souhwan Jung, James Matthew Rehg, Hyesong Choi

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27348v1](https://arxiv.org/pdf/2605.27348v1)

**Abstract**: Recent generative models have largely closed the gap on low-level artifacts - pixel fingerprints, frequency anomalies, upsampling traces - particularly in person-centric and partial-edit settings where the manipulated region is small and surrounded by photometrically authentic content. We introduce Social Gaze Consistency, a high-level semantic cue defined as the mutual coherence of gaze direction, head-eye alignment, and pupil placement between interacting individuals, and show that it constitutes a previously underutilized detection axis orthogonal to existing low-level paradigms. We instantiate this insight through three coupled mechanisms: (i) a controlled diagnostic dataset with region-specific perturbations of gaze-consistent imagery, where strict pair-level grouping forecloses generator-fingerprint memorization as an optimization-time shortcut rather than relying on augmentation; (ii) Block-Compositional Caption Supervision, which holds a single 5-block reasoning skeleton invariant across 1,250 macro-combined captions, decoupling reasoning consistency from surface diversity; (iii) Cross-architecture validation showing the same supervision improves a vision-language backbone (FakeVLM) by +3.7 pp on the COCOAI Interaction subset (balanced accuracy 67.8 -> 71.5) and +1.3 pp on the COCOAI Person subset (83.0 -> 84.3), with consistent gains on a vision-only backbone (Effort), evidencing a backbone-agnostic cue. Real- and fake-class recalls rise simultaneously, ruling out a "predict-all-fake" artifact. A four-step mechanistic account - paired-edit shortcut blocking, hard-to-easy difficulty transfer, CLIP prior preservation, and diffusion-family shared spectral weakness in periocular structure - explains why training on a single inpainter (FLUX.1-Fill) transfers to multi-generator suites. We will release the code upon acceptance to facilitate reproducibility.


### Towards Controllable Image Generation through Representation-Conditioned Diffusion Models
**Authors**: Nithesh Chandher Karthikeyan, Jonas Unger, Gabriel Eilertsen

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27343v1](https://arxiv.org/pdf/2605.27343v1)

**Abstract**: Diffusion models have emerged as powerful tools for high-quality image generation and editing, but guiding these models to produce specific outputs remains a challenge. Conventional approaches rely on conditioning mechanisms, such as text prompts or semantic maps, which require extensively annotated datasets. In this preliminary work, we explore diffusion models conditioned on representations from a pre-trained self-supervised model. The self-conditioning mechanism not only improves the quality of unconditional image generation, but also provides a representation space that can be used to control the generation. We explore this conditioning space by identifying directions of variations, and demonstrate promising properties in terms of smoothness and disentanglement.


### Maat: The Agentic Legal Research Assistant for Competition Protection
**Authors**: Basant Mounir, Farida Madkour, Amira Abdelaziz, Asmaa Sami

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27331v1](https://arxiv.org/pdf/2605.27331v1)

**Abstract**: Competition law experts conducting legal research must review extensive volumes of cases, decisions, and judicial reports to identify precedents and assess key elements in competition and merger cases. Although general research assistants such as Claude and ChatGPT and legal assistants such as SaulLM-7B and LegalGPT are increasingly used to assist legal research, they remain inadequate for competition law analysis: they lack specialized domain expertise, provide insufficient official citations, or hallucinate competition law cases. We propose Maat, a ReAct agent that orchestrates tools corresponding to different tasks of the research process. Designed iteratively with competition law experts, Maat grounds cases and findings in official sources using RAG for reliability, provides rich in-line citations, falls back to web search when database coverage is insufficient, and prompts the user for clarification when queries are ambiguous. Maat significantly outperforms all baseline assistants on case-specific tasks and performs within range of the top baseline on theoretical question tasks. The dataset used is available on GitHub.


### Governed Evolution of Agent Runtimes through Executable Operational Cognition
**Authors**: Mariano Garralda-Barrio

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27328v1](https://arxiv.org/pdf/2605.27328v1)

**Abstract**: Recent advances in agentic systems increasingly treat code as an executable operational substrate rather than as a disposable output artifact. Prior work such as \emph{Code as Agent Harness} frames validated agent-generated artifacts as runtime entities that can be created, executed, revised, persisted, and reused within long-running cognitive loops. However, the governance, lifecycle management, and operational evolution of such artifacts remain under-specified.
  This paper proposes a framework for governed runtime evolution in multi-agent systems through executable operational cognition. We formalize agent-generated artifacts as persistent runtime capabilities that progressively become part of the operational substrate rather than transient intermediate outputs. Building on this perspective, we introduce \emph{HarnessMutation} as a governed mechanism for lifecycle-aware runtime adaptation operating under explicit validation, traceability, evaluation, and rollback constraints.
  Rather than treating runtime adaptation as unrestricted self-modification, the proposed framework models evolution as a bounded and observable process over persistent operational memory. It further shows how these ideas can be operationalized over modern agent runtimes and governance-oriented orchestration systems, providing a conceptual foundation for adaptive infrastructures whose evolution remains explicit, auditable, and constrained.


## VLA
### FineVLA: Fine-Grained Instruction Alignment for Steerable Vision-Language-Action Policies
**Authors**: Xintong Hu, Xuhong Huang, Jinyu Zhang, Yutong Yao, Yuchong Sun, Qiuyue Wang, Mingsheng Li, Sicheng Xie, Yitao Liu, Junhao Chen, Yixuan Chen, Yingming Zheng, Shuai Bai, Tao Yu

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27284v1](https://arxiv.org/pdf/2605.27284v1)

**Abstract**: Vision-Language-Action (VLA) models are increasingly expected to not only complete robot tasks, but also follow human instructions about how those tasks should be executed. However, existing robot datasets usually pair trajectories with coarse goal-level language, leaving execution-critical details such as active arm, approach direction, and contact region unspecified. This limits steerable policy learning and robotic video understanding. We introduce FineVLA, an open framework for action-aligned fine-grained VLA supervision. The framework includes: (1) a data construction tool that unifies 972,247 trajectories across 85K tasks from 10 open-source robot datasets and builds FineVLA-Data, a human-verified dataset of 47,159 fine-grained trajectories; (2) a held-out benchmark with 500 videos, 10,816 atomic facts, and 1,030 VQA questions; (3) a robotics-specialized VLM annotator for scalable fine-grained annotation; and (4) a steerable VLA policy trained with controlled mixtures of fine-grained and raw goal-level instructions. Our experiments yield three findings. First, fine-grained supervision does not sacrifice goal-level success: FG-only improves over Raw-only by +1.4 to +8.1 success-rate points across settings. Second, fine-grained and raw instructions are complementary, following a consistent inverted-U trend peaking at FG:Raw = 1:2 to 1:1. The best mixed setting reaches 86.8%/82.5% in RoboTwin simulation and 62.7/100 in real-world dual-arm manipulation (vs. 49.9 Raw-only). Third, fine-grained supervision improves steerable control: the largest real-world gains appear on pose (+23), color (+18), and approach direction (+18)--factors where goal-level instructions provide no guidance. Overall, fine-grained language should augment goal-level instructions: specifying how to execute alongside what to achieve. Project page: https://finevla.xlang.ai/


### Capability and Robustness Cannot Both Be Free: An Information-Theoretic Bound for Vision-Language-Action Models
**Authors**: Jianwei Tai

**Published Date**: 2026-05-25

**Updated Date**: 2026-05-26

**PDF Url**: [2605.25889v2](https://arxiv.org/pdf/2605.25889v2)

**Abstract**: Vision-Language-Action (VLA) models are increasingly deployed on real robots, where each predicted action is executed and each failure carries a safety cost. They reach high success rates on clean inputs but collapse under small adversarial perturbations. A $16/255$ PGD attack on OpenVLA-7B drops LIBERO success from above $95\%$ to under $5\%$. Empirical defenses recover some robustness at a cost in clean accuracy, but the literature does not say whether the trade-off has a theoretical floor. We prove that it does. For any VLA policy with discrete actions, the sum of capability (mutual information between policy action and oracle action) and robustness (mutual information preserved under adversarial perturbation, net of trivial channel leakage) is upper-bounded by a policy-independent budget: task entropy plus adversarial channel capacity. The proof is two applications of the Data Processing Inequality plus MI non-negativity. The pixel-level bound is policy-independent but loose ($\sim 10^3$ nats); an encoder-specific corollary tightens it on a per-experiment basis to $\approx 86$--$156$ nats at $\eps=8/255$ on OpenVLA, depending on which defense is in place. We validate the bound across $252$ closed-form Gaussian-VLA cells and $48$ OpenVLA-7B $\times$ LIBERO $\times$ PGD cells (zero violations). The encoder bound additionally diagnoses where a defense intervenes in the channel: input-side defenses (JPEG-50) shift the encoder budget by $+41$ to $+101$ nats across $\eps \in \{2,4,8,16\}/255$ ($+68$ at $\eps=8/255$), while LLM-side defenses (rank-16 LoRA) shift it by $\le 9\%$ at every $\eps$ and only $0.7\%$ at $\eps=8/255$. We propose encoder-specific slack as a diagnostic axis paired with raw $\Rob$ for defense reporting, and release all code, manifests, and results.


### OASIS: Observation-Action Space Alignment via SE(3) Trajectory Prediction for Robotic Manipulation
**Authors**: Xinzhe Chen, Sihua Ren, Liqi Huang, Haowen Sun, Mingyang Li, Xingyu Chen, Zeyang Liu, Xuguang Lan

**Published Date**: 2026-05-25

**Updated Date**: 2026-05-25

**PDF Url**: [2605.25829v1](https://arxiv.org/pdf/2605.25829v1)

**Abstract**: Recent vision-language-action (VLA) models and world action models (WAMs) advance robotic manipulation by enriching intermediate representations with auxiliary spatial features or future visual-state prediction. However, these representations largely remain within the observation space and do not share the rigid-body geometry of the action space, forcing the action decoder to implicitly recover this geometry. We propose OASIS, a visuomotor policy that aligns the intermediate representation with the action space via $SE(3)$ end-effector trajectory prediction. OASIS couples a 3D-aware feature encoder that fuses vision-language and metric-depth features with an $SE(3)$ trajectory predictor that produces a camera-frame end-effector trajectory. Conditioned on the predictor's pose-supervised hidden states, the action decoder generates action chunks consistent with rigid-body motion. Across simulation and real-world experiments, OASIS outperforms VLA and WAM baselines in success rate and out-of-distribution generalization. Our project page is available at https://npuhandsome.github.io/OASIS_web.


### EXPO-FT: Sample-Efficient Reinforcement Learning Finetuning for Vision-Language-Action Models
**Authors**: Perry Dong, Kuo-Han Hung, Tian Gao, Dorsa Sadigh, Chelsea Finn

**Published Date**: 2026-05-25

**Updated Date**: 2026-05-25

**PDF Url**: [2605.25477v1](https://arxiv.org/pdf/2605.25477v1)

**Abstract**: The ability to efficiently and reliably learn new tasks has been a foundational challenge in robotics. Vision-Language-Action (VLA) models have demonstrated strong generalization across diverse manipulation tasks, yet pretrained policies consistently fall short of the reliability required for real-world deployment. Reinforcement learning (RL) fine-tuning offers a promising path to bridge this gap, but existing approaches either train from scratch without fully leveraging pretrained priors, or fine-tune VLAs without achieving the sample efficiency and success rates that practical deployment demands. We present EXPO-FT, a system for stable, sample-efficient RL finetuning of pretrained VLA policies that closes this gap. Our system solves a suite of challenging manipulation tasks, including routing string lights and inserting the plug to light it up, striking a pool ball into a pocket, and inserting a flower into a wine bottle, each requiring combinations of high precision, dynamic actions, and robustness to varied initial states. Our system achieves perfect task performance (30/30 successes) across all evaluated tasks within an average of 19.1 minutes of online robot data, outperforming both prior RL-from-scratch and VLA finetuning approaches. We release an open-source codebase with the aim of facilitating broader adoption of RL finetuning of VLA models in robotics.


### ActQuant: Sub-4-bit Action-Guided Quantization for Vision-Language-Action Models
**Authors**: Arash Akbari, Arman Akbari, Masih Eskandar, Qitao Tan, Yixiao Chen, Jingwu Luo, Bertha Pangaribuan, Liyun Zhang, Jennifer Dy, Geng Yuan, Xue Lin, Gaowen Liu, Stratis Ioannidis, Yanzhi Wang

**Published Date**: 2026-05-19

**Updated Date**: 2026-05-19

**PDF Url**: [2605.24011v1](https://arxiv.org/pdf/2605.24011v1)

**Abstract**: Vision-Language-Action (VLA) models exhibit remarkable action generation for embodied intelligence, but their heavy compute make deployment on edge platforms impractical. Aggressive, sub-4-bit weight quantization is the natural solution, yet existing post-training quantization (PTQ) methods suffer severe performance degradation in this regime. To address this, we introduce ActQuant, an action-guided mixed-precision PTQ framework that operates in two stages: (1) an inter-tensor bit allocator that assigns each weight matrix a single bit-width based on how much it contributes to predicting the agent's actions; (2) an intra-tensor scale optimizer tunes per-block quantization scales using action-aware curvature, so that dynamic range is concentrated on the weights most influential for control. To deliver the on-device benefits of our aggressive quantization, we further introduce OmniModel.cpp, an agentic conversion pipeline that ports architectures into a native C/C++ runtime with efficient low-bit kernels. We evaluate ActQuant both in simulation and on a real-world 6-DoF UR3 arm, with all models deployed through OmniModel.cpp. On the LIBERO benchmark, ActQuant is the only method that operates at or below 3 bits-per-weight, retaining 95.0% on OpenVLA-OFT and 94.8% on $π_{0.5}$. Pushed further, ActQuant reaches 2.5 bpw at 90.1% on OpenVLA-OFT, compressing the backbone from 14.3 GB to 2.7 GB (5.3$\times$). On the physical UR3 arm, $π_{0.5}$ quantized with ActQuant retains the baseline's success rate while reducing the memory footprint by 2.5$\times$.


## Agent
### Natural Language Query to Configuration for Retrieval Agents
**Authors**: Melissa Z. Pan, Negar Arabzadeh, Mathew Jacob, Fiodar Kazhamiaka, Esha Choukse, Matei Zaharia

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27361v1](https://arxiv.org/pdf/2605.27361v1)

**Abstract**: Modern retrieval agents expose many configuration choices -- LLM, retriever, number of documents, number of hops, and synthesis strategy -- each shaping both answer quality and serving cost. Today, these pipelines are typically hand-tuned once per workload, leaving substantial per-query optimization untapped. We formulate the problem: given a natural-language query and either an accuracy or a budget target, select from a predefined pipeline catalog the configuration that minimizes cost or maximizes accuracy at inference time. We propose **BRANE**, which uses an LLM to convert each query into workload-specific characteristics, then trains a lightweight per-configuration predictor that estimates whether the pipeline will answer the query correctly. At inference time, **BRANE** selects the configuration that maximizes predicted correctness penalized by cost, exposing a tunable cost-quality tradeoff without retraining. Across MuSiQue, BrowseComp-Plus, and FinanceBench, **BRANE** consistently pushes the cost-quality Pareto frontier, matches the best fixed configuration's accuracy at up to 89% lower cost, and outperforms LLM-routing, rule-based, and fine-tuned Qwen3-4B baselines. These results show that per-query configuration of the full retrieval pipeline is a practical alternative to static workload-level tuning.


### Modeling Agentic Technical Debt and Stochastic Tax: A Standalone Framework for Measurement, Simulation, and Dashboarding
**Authors**: Muhammad Zia Hydari, Raja Iqbal, Narayan Ramasubbu

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27320v1](https://arxiv.org/pdf/2605.27320v1)

**Abstract**: Agentic AI systems combine probabilistic reasoning with delegated action through tools, context, memory, orchestration, and external workflow integration. This note develops a formal and managerially usable model that distinguishes Agentic Technical Debt from Stochastic Tax. Agentic Technical Debt is a stock of accumulated design and governance liability. Stochastic Tax is a recurring flow of operating burden that arises when stochastic agents are used in business workflows. The two constructs are related, but they are not the same: debt can amplify the tax, while the tax can remain positive even when debt is minimized. The note starts from a compact dashboard expression, expands it into a fuller structural model, defines all variables and parameters, shows how each cost category can be estimated from operational data, and illustrates the framework with an accounts-payable simulation and companion spreadsheet.


### SIA: Self Improving AI with Harness & Weight Updates
**Authors**: Prannay Hebbar, Yogendra Manawat, Samuel Verboomen, Alesia Ivanova, Selvam Palanimalai, Kunal Bhatia, Vignesh Baskaran

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27276v1](https://arxiv.org/pdf/2605.27276v1)

**Abstract**: Humans are the bottleneck in building and improving AI. Both the models and the agents that wrap them are written, tuned, and corrected by people. The long-horizon goal of an AI that can figure out how to improve itself remains open. Two largely disjoint research lines attack this bottleneck. The harness-update school has a meta-agent rewrite the scaffold of a task-specific agent (its tools, prompts, retry logic, and search procedure) while the model weights are held fixed. The test-time training school uses hand-written RL pipelines to update the model's own weights on task feedback while the harness is held fixed. These two silos operate in isolation. We propose SIA, a self-improving loop in which a language-model agent (the Feedback-Agent) updates both the harness and the weights of a task-specific agent. We evaluate across three contrasting domains: Chinese legal charge classification, low-level GPU kernel optimisation, and single-cell RNA denoising. Combining both levers outperforms scaffold iteration alone on all three benchmarks. The gains are 56.6% on LawBench, 91.9% runtime reduction on GPU kernels, and 502% on denoising over the initial baseline. Harness updates make the model agentic, shaping how it searches and acts, while weight updates build the domain intuition that no prompt or scaffold can instil.


### Learning to Act under Noise: Enhancing Agent Robustness via Noisy Environments
**Authors**: Yuxin Chen, Xiaodong Cai, Junfeng Fang, Zhuowen Han, Yu Wang, Yaorui Shi, Yi Zhang, Qi Gu, Xunliang Cai, Xiang Wang, An Zhang, Tat-Seng Chua

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27209v1](https://arxiv.org/pdf/2605.27209v1)

**Abstract**: Recent advances in large language models (LLMs) have facilitated the widespread deployment of LLMs as interactive agents capable of reasoning, planning, and tool use. Despite strong performance on existing benchmarks, such agents often exhibit notable degradation when deployed in real-world settings, where environments are inherently stochastic and imperfect. We argue that this discrepancy arises from a fundamental mismatch between idealized training settings and real-world interaction dynamics, where current paradigms rely on carefully curated task instructions and stable, well-controlled environments. To address this gap, we propose NoisyAgent, an agentic training framework that explicitly incorporates environmental imperfections into the agent learning process. We identify two major sources of interaction noise in real-world scenarios: user noise, which captures ambiguity and variability in user interaction, and tool noise, which reflects failures and anomalies in tool execution. We introduce such perturbations into the training pipeline by modifying user interaction patterns and simulating tool execution results within the training environment. To stabilize training while encouraging agents to handle increasingly challenging imperfections, noise is applied to only a subset of rollouts and progressively increased in difficulty as the model adapts to the current noise level. Extensive experiments demonstrate that our approach consistently improves agent robustness under noisy and dynamic environments. Our analysis reveals that training under noise conditions also yields performance gains on idealized benchmarks, suggesting that controlled exposure to environmental noise promotes more generalizable reasoning and decision-making behaviors. Our findings highlight the importance of modeling interaction imperfections for bridging the gap between agent training and real-world deployment.


### FoundObj: Self-supervised Foundation Models as Rewards for Label-free 3D Object Segmentation
**Authors**: Zihui Zhang, Zhixuan Sun, Yafei Yang, Jinxi Li, Jiahao Chen, Bo Yang

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27178v1](https://arxiv.org/pdf/2605.27178v1)

**Abstract**: We address the challenging task of 3D object segmentation in complex scene point clouds without relying on any scene-level human annotations during training. Existing methods are typically constrained to identifying simple objects, primarily due to insufficient object priors in the learning process. In this paper, we present FoundObj, a novel framework featuring a superpoint-based object discovery agent that incrementally merges suitable neighboring superpoints, guided by our innovative semantic and geometric reward modules. These modules synergistically leverage semantic and geometric priors from self-supervised 2D/3D foundation models, providing complementary feedback to the object discovery agent and enabling robust identification of multi-class objects through reinforcement learning. Extensive experiments on diverse benchmarks demonstrate that our approach consistently outperforms existing baselines. Notably, our method exhibits strong generalization in zero-shot and long-tail scenarios, underscoring its potential for scalable, label-free 3D object segmentation.


### VitaBench 2.0: Evaluating Personalized and Proactive Agents in Long-Term User Interactions
**Authors**: Yuxin Chen, Yi Zhang, Zhengzhou Cai, Yaorui Shi, Zhiyuan Yao, Chenhang Cui, Jingnan Zheng, Yaqi Huo, Xi Su, Qi Gu, Xunliang Cai, Xiang Wang, An Zhang, Tat-Seng Chua

**Published Date**: 2026-05-26

**Updated Date**: 2026-05-26

**PDF Url**: [2605.27141v1](https://arxiv.org/pdf/2605.27141v1)

**Abstract**: Large language models (LLMs) have evolved into interactive agents that collaborate with users in real-world tasks. Effective collaboration in such settings increasingly depends on understanding the user beyond what is explicitly stated, as user intent is often reflected in fragmented daily interactions and requires both personalized modeling and proactive interaction. However, existing agent benchmarks primarily evaluate reasoning and tool use, largely overlooking the challenges of inferring and leveraging user preferences in realistic scenarios. To address this gap, we introduce VitaBench 2.0, a benchmark for evaluating personalized and proactive agent behavior in long-term user interactions. In VitaBench 2.0, tasks are organized as temporally ordered sequences for individual users, where preferences are embedded in fragmented and heterogeneous interactions. Successful completion of tasks requires the agent to continuously extract, utilize, and update user preferences from these interactions. We further evaluate proactiveness through tasks that require agents to recognize missing information and actively acquire it from users or environments before making decisions. To support systematic analysis, we provide an extensible memory interface that enables controlled comparison across different memory architectures. We benchmark a diverse set of frontier proprietary and open-source LLMs. Results show that real-world personalization remains highly challenging even for state-of-the-art models, revealing a substantial gap between current capabilities and practical requirements. Extensive analysis further reveals the failure modes and capability bottlenecks of current agents in real-world personalized decision-making, providing insights for future model improvements.


