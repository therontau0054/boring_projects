# Abstracts of Papers

## World Model
### ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both
**Authors**: Ziyu Guo, Rain Liu, Xinyan Chen, Pheng-Ann Heng

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15198v1](https://arxiv.org/pdf/2605.15198v1)

**Abstract**: Visual reasoning, often interleaved with intermediate visual states, has emerged as a promising direction in the field. A straightforward approach is to directly generate images via unified models during reasoning, but this is computationally expensive and architecturally non-trivial. Recent alternatives include agentic reasoning through code or tool calls, and latent reasoning with learnable hidden embeddings. However, agentic methods incur context-switching latency from external execution, while latent methods lack task generalization and are difficult to train with autoregressive parallelization. To combine their strengths while mitigating their limitations, we propose ATLAS, a framework in which a single discrete 'word', termed as a functional token, serves both as an agentic operation and a latent visual reasoning unit. Each functional token is associated with an internalized visual operation, yet requires no visual supervision and remains a standard token in the tokenizer vocabulary, which can be generated via next-token prediction. This design avoids verbose intermediate visual content generation, while preserving compatibility with the vanilla scalable SFT and RL training, without architectural or methodological modifications. To further address the sparsity of functional tokens during RL, we introduce Latent-Anchored GRPO (LA-GRPO), which stabilizes the training by anchoring functional tokens with a statically weighted auxiliary objective, providing stronger gradient updates. Extensive experiments and analyses demonstrate that ATLAS achieves superior performance on challenging benchmarks while maintaining clear interpretability. We hope ATLAS offers a new paradigm inspiring future visual reasoning research.


### RefDecoder: Enhancing Visual Generation with Conditional Video Decoding
**Authors**: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15196v1](https://arxiv.org/pdf/2605.15196v1)

**Abstract**: Video generation powers a vast array of downstream applications. However, while the de facto standard, i.e., latent diffusion models, typically employ heavily conditioned denoising networks, their decoders often remain unconditional. We observe that this architectural asymmetry leads to significant loss of detail and inconsistency relative to the input image. To address this, we argue that the decoder requires equal conditioning to preserve structural integrity. We introduce RefDecoder, a reference-conditioned video VAE decoder by injecting high-fidelity reference image signal directly into the decoding process via reference attention. Specifically, a lightweight image encoder maps the reference frame into the detail-rich high-dimensional tokens, which are co-processed with the denoised video latent tokens at each decoder up-sampling stage. We demonstrate consistent improvements across several distinct decoder backbones (e.g., Wan 2.1 and VideoVAE+), achieving up to +2.1dB PSNR over the unconditional baselines on the Inter4K, WebVid, and Large Motion reconstruction benchmarks. Notably, RefDecoder can be directly swapped into existing video generation systems without additional fine-tuning, and we report across-the-board improvements in subject consistency, background consistency, and overall quality scores on the VBench I2V benchmark. Beyond I2V, RefDecoder generalizes well to a wide range of visual generation tasks such as style transfer and video editing refinement.


### FutureSim: Replaying World Events to Evaluate Adaptive Agents
**Authors**: Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab, Moritz Hardt, Maksym Andriushchenko, Jonas Geiping

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15188v1](https://arxiv.org/pdf/2605.15188v1)

**Abstract**: AI agents are being increasingly deployed in dynamic, open-ended environments that require adapting to new information as it arrives. To efficiently measure this capability for realistic use-cases, we propose building grounded simulations that replay real-world events in the order they occurred. We build FutureSim, where agents forecast world events beyond their knowledge cutoff while interacting with a chronological replay of the world: real news articles arriving and questions resolving over the simulated period. We evaluate frontier agents in their native harness, testing their ability to predict world events over a three-month period from January to March 2026. FutureSim reveals a clear separation in their capabilities, with the best agent's accuracy being 25%, and many having worse Brier skill score than making no prediction at all. Through careful ablations, we show how FutureSim offers a realistic setting to study emerging research directions like long-horizon test-time adaptation, search, memory, and reasoning about uncertainty. Overall, we hope our benchmark design paves the way to measure AI progress on open-ended adaptation spanning long time-horizons in the real world.


### VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction
**Authors**: Kaixin Zhu, Yiwen Tang, Yifan Yang, Renrui Zhang, Bohan Zeng, Ziyu Guo, Ruichuan An, Zhou Liu, Qizhi Chen, Delin Qu, Jaehong Yoon, Wentao Zhang

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15186v1](https://arxiv.org/pdf/2605.15186v1)

**Abstract**: High-quality 3D scene reconstruction has recently advanced toward generalizable feed-forward architectures, enabling the generation of complex environments in a single forward pass. However, despite their strong performance in static scene perception, these models remain limited in responding to dynamic human instructions, which restricts their use in interactive applications. Existing editing methods typically rely on a 2D-lifting strategy, where individual views are edited independently and then lifted back into 3D space. This indirect pipeline often leads to blurry textures and inconsistent geometry, as 2D editors lack the spatial awareness required to preserve structure across viewpoints. To address these limitations, we propose VGGT-Edit, a feed-forward framework for text-conditioned native 3D scene editing. VGGT-Edit introduces depth-synchronized text injection to align semantic guidance with the backbone's spatial poses, ensuring stable instruction grounding. This semantic signal is then processed by a residual transformation head, which directly predicts 3D geometric displacements to deform the scene while preserving background stability. To ensure high-fidelity results, we supervise the framework with a multi-term objective function that enforces geometric accuracy and cross-view consistency. We also construct the DeltaScene Dataset, a large-scale dataset generated through an automated pipeline with 3D agreement filtering to ensure ground-truth quality. Experiments show that VGGT-Edit substantially outperforms 2D-lifting baselines, producing sharper object details, stronger multi-view consistency, and near-instant inference speed.


### Quantitative Video World Model Evaluation for Geometric-Consistency
**Authors**: Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15185v1](https://arxiv.org/pdf/2605.15185v1)

**Abstract**: Generative video models are increasingly studied as implicit world models, yet evaluating whether they produce physically plausible 3D structure and motion remains challenging. Most existing video evaluation pipelines rely heavily on human judgment or learned graders, which can be subjective and weakly diagnostic for geometric failures. We introduce PDI-Bench (Perspective Distortion Index), a quantitative framework for auditing geometric coherence in generated videos. Given a generated clip, we obtain object-centric observations via segmentation and point tracking (e.g., SAM 2, MegaSaM, and CoTracker3), lift them to 3D world-space coordinates via monocular reconstruction, and compute a set of projective-geometry residuals capturing three failure dimensions: scale-depth alignment, 3D motion consistency, and 3D structural rigidity. To support systematic evaluation, we build PDI-Dataset, covering diverse scenarios designed to stress these geometric constraints. Across state-of-the-art video generators, PDI reveals consistent geometry-specific failure modes that are not captured by common perceptual metrics, and provides a diagnostic signal for progress toward physically grounded video generation and physical world model. Our code and dataset can be found at https://pdi-bench.github.io/.


### When Are Two Networks the Same? Tensor Similarity for Mechanistic Interpretability
**Authors**: ML Nissen Gonzalez, Melwina Albuquerque, Laurence Wroe, Jacob Meyer Cohen, Logan Riggs Smith, Thomas Dooms

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15183v1](https://arxiv.org/pdf/2605.15183v1)

**Abstract**: Mechanistic interpretability aims to break models into meaningful parts; verifying that two such parts implement the same computation is a prerequisite. Existing similarity measures evaluate either empirical behaviour, leaving them blind to out-of-distribution mechanisms, or basis-dependent parameters, meaning they disregard weight-space symmetries. To address these issues for the class of tensor-based models, we introduce a weight-based metric, tensor similarity, that is invariant to such symmetries. This metric captures global functional equivalence and accounts for cross-layer mechanisms using an efficient recursive algorithm. Empirically, tensor similarity tracks functional training dynamics, such as grokking and backdoor insertion, with higher fidelity than existing metrics. This reduces measuring similarity and verifying faithfulness into a solved algebraic problem rather than one of empirical approximation.


## VLA
### Hand-in-the-Loop: Improving Dexterous VLA via Seamless Interventional Correction
**Authors**: Zhuohang Li, Liqun Huang, Wei Xu, Zhengming Zhu, Nie Lin, Xiao Ma, Xinjun Sheng, Ruoshi Wen

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15157v1](https://arxiv.org/pdf/2605.15157v1)

**Abstract**: Vision-Language-Action (VLA) models are prone to compounding errors in dexterous manipulation, where high-dimensional action spaces and contact-rich dynamics amplify small policy deviations over long horizons. While Interactive Imitation Learning (IIL) can refine policies through human takeover data, applying it to high-degree-of-freedom (DoF) robotic hands remains challenging due to a command mismatch between human teleoperation and policy execution at the takeover moment, which causes abrupt robot-hand configuration changes, or "gesture jumps". We present Hand-in-the-Loop (HandITL), a seamless human-in-the-loop intervention method that blends human corrective intent with autonomous policy execution to avoid gesture jumps during bimanual dexterous manipulation. Compared with direct teleoperation takeover, HandITL reduces takeover jitter by 99.8% and preserves robust post-takeover manipulation, reducing grasp failures by 87.5% and mean completion time by 19.1%. We validate HandITL on tasks requiring bimanual coordination, tool use, and fine-grained long-horizon manipulation. When used to collect intervention data for policy refinement, HandITL yields policies that outperform those trained with standard teleoperation data by 19% on average across three long-horizon dexterous tasks.


### IntentVLA: Short-Horizon Intent Modeling for Aliased Robot Manipulation
**Authors**: Shijie Lian, Bin Yu, Xiaopeng Lin, Zhaolong Shen, Laurence Tianruo Yang, Yurun Jin, Haishan Liu, Changti Wu, Hang Yuan, Cong Huang, Kai Chen

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.14712v1](https://arxiv.org/pdf/2605.14712v1)

**Abstract**: Robot imitation data are often multimodal: similar visual-language observations may be followed by different action chunks because human demonstrators act with different short-horizon intents, task phases, or recent context. Existing frame-conditioned VLA policies infer each chunk from the current observation and instruction alone, so under partial observability they may resample different intents across adjacent replanning steps, leading to inter-chunk conflict and unstable execution. We introduce IntentVLA, a history-conditioned VLA framework that encodes recent visual observations into a compact short-horizon intent representation and uses it to condition chunk generation. We further introduce AliasBench, a 12-task ambiguity-aware benchmark on RoboTwin2 with matched training data and evaluation environments that isolate short-horizon observation aliasing. Across AliasBench, SimplerEnv, LIBERO, and RoboCasa, IntentVLA improves rollout stability and outperforms strong VLA baselines


### AttenA+: Rectifying Action Inequality in Robotic Foundation Models
**Authors**: Daojie Peng, Fulong Ma, Jiahang Cao, Qiang Zhang, Xupeng Xie, Jian Guo, Ping Luo, Andrew F. Luo, Boyu Zhou, Jun Ma

**Published Date**: 2026-05-13

**Updated Date**: 2026-05-13

**PDF Url**: [2605.13548v1](https://arxiv.org/pdf/2605.13548v1)

**Abstract**: Existing robotic foundation models, while powerful, are predicated on an implicit assumption of temporal homogeneity: treating all actions as equally informative during optimization. This "flat" training paradigm, inherited from language modeling, remains indifferent to the underlying physical hierarchy of manipulation. In reality, robot trajectories are fundamentally heterogeneous, where low-velocity segments often dictate task success through precision-demanding interactions, while high-velocity motions serve as error-tolerant transitions. Such a misalignment between uniform loss weighting and physical criticality fundamentally limits the performance of current Vision-Language-Action (VLA) models and World-Action Models (WAM) in complex, long-horizon tasks. To rectify this, we introduce AttenA+, an architecture-agnostic framework that prioritizes kinematically critical segments via velocity-driven action attention. By reweighting the training objective based on the inverse velocity field, AttenA+ naturally aligns the model's learning capacity with the physical demands of manipulation. As a plug-and-play enhancement, AttenA+ can be integrated into existing backbones without structural modifications or additional parameters. Extensive experiments demonstrate that AttenA+ significantly elevates the ceilings of current state-of-the-art models. Specifically, it improves OpenVLA-OFT to 98.6% (+1.5%) on the Libero benchmark and pushes FastWAM to 92.4% (+0.6%) on RoboTwin 2.0. Real-world validation on a Franka manipulator further showcases its robustness and cross-task generalization. Our work suggests that mining the intrinsic structural priors of action sequences offers a highly efficient, physics-aware complement to standard scaling laws, paving a new path for general-purpose robotic control.


### D-VLA: A High-Concurrency Distributed Asynchronous Reinforcement Learning Framework for Vision-Language-Action Models
**Authors**: Yucheng Guo, Yongjian Guo, Zhong Guan, Wen Huang, Haoran Sun, Haodong Yue, Xiaolong Xiang, Shuai Di, Zhen Sun, Luqiao Wang, Junwu Xiong, Yicheng Gong

**Published Date**: 2026-05-13

**Updated Date**: 2026-05-14

**PDF Url**: [2605.13276v2](https://arxiv.org/pdf/2605.13276v2)

**Abstract**: The rapid evolution of Embodied AI has enabled Vision-Language-Action (VLA) models to excel in multimodal perception and task execution. However, applying Reinforcement Learning (RL) to these massive models in large-scale distributed environments faces severe systemic bottlenecks, primarily due to the resource conflict between high-fidelity physical simulation and the intensive VRAM/bandwidth demands of deep learning. This conflict often leaves overall throughput constrained by execution-phase inefficiencies. To address these challenges, we propose D-VLA, a high-concurrency, low-latency distributed RL framework for large-scale embodied foundation models. D-VLA introduces "Plane Decoupling," physically isolating high-frequency training data from low-frequency weight control to eliminate interference between simulation and optimization. We further design a four-thread asynchronous "Swimlane" pipeline, enabling full parallel overlap of sampling, inference, gradient computation, and parameter distribution. Additionally, a dual-pool VRAM management model and topology-aware replication resolve memory fragmentation and optimize communication efficiency. Experiments on benchmarks like LIBERO show that D-VLA significantly outperforms mainstream RL frameworks in throughput and sampling efficiency for billion-parameter VLA models. In trillion-parameter scalability tests, our framework maintains exceptional stability and linear speedup, providing a robust system for high-performance general-purpose embodied agents.


### Towards Long-horizon Embodied Agents with Tool-Aligned Vision-Language-Action Models
**Authors**: Zixing Lei, Changxing Liu, Yichen Xiong, Minhao Xiong, Yuanzhuo Ding, Zhipeng Zhang, Weixin Li, Siheng Chen

**Published Date**: 2026-05-13

**Updated Date**: 2026-05-13

**PDF Url**: [2605.13119v1](https://arxiv.org/pdf/2605.13119v1)

**Abstract**: Vision-language-action (VLA) models are effective robot action executors, but they remain limited on long-horizon tasks due to the dual burden of extended closed-loop planning and diverse physical operations. We therefore propose VLAs-as-Tools, a strategy that distributes this burden across a high-level vision language model (VLM) agent for temporal reasoning and a family of specialized VLA tools for diverse local physical operations. The VLM handles scene analysis, global planning, and recovery, while each VLA tool executes a bounded subtask. To tightly couple agent planning with VLA tool execution in long-horizon tasks, we introduce a VLA tool-family interface that exposes explicit tool selection and in-execution progress feedback, enabling efficient event-triggered agent replanning without continuous agent polling. To obtain diverse specialized VLA tools that faithfully follow agent invocations, we further propose Tool-Aligned Post-Training (TAPT), which constructs invocation-aligned training units for instruction following and adopts tool-family residual adapters for efficient tool specialization. Experiments show that VLAs-as-Tools improves the success rate of $π_{0.5}$ by 4.8 points on LIBERO-Long and 23.1 points on RoboTwin, and further enhances invocation fidelity by 15.0 points as measured by Non-biased Rate. Code will be released.


### Reinforcing VLAs in Task-Agnostic World Models
**Authors**: Yucen Wang, Rui Yu, Fengming Zhang, Junjie Lu, Xinyao Qin, Tianxiang Zhang, Kaixin Wang, Li Zhao

**Published Date**: 2026-05-12

**Updated Date**: 2026-05-12

**PDF Url**: [2605.12334v1](https://arxiv.org/pdf/2605.12334v1)

**Abstract**: Post-training Vision-Language-Action (VLA) models via reinforcement learning (RL) in learned world models has emerged as an effective strategy to adapt to new tasks without costly real-world interactions. However, while using imagined trajectories reduces the sample complexity of policy training, existing methods still heavily rely on task-specific data to fine-tune both the world and reward models, fundamentally limiting their scalability to unseen tasks. To overcome this, we argue that world and reward models should capture transferable physical priors that enable zero-shot inference. We propose RAW-Dream (Reinforcing VLAs in task-Agnostic World Dreams), a new paradigm that completely disentangles world model learning from downstream task dependencies. RAW-Dream utilizes a world model pre-trained on diverse task-free behaviors for predicting future rollouts, and an off-the-shelf Vision-Language Model (VLM) for reward generation. Because both components are task-agnostic, VLAs can be readily finetuned for any new task entirely within this zero-shot imagination. Furthermore, to mitigate world model hallucinations, we introduce a dual-noise verification mechanism to filter out unreliable rollouts. Extensive experiments across simulation and real-world settings demonstrate consistent performance gains, proving that generalized physical priors can effectively substitute for costly task-dependent data, offering a highly scalable roadmap for VLA adaptation.


## Agent
### Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands
**Authors**: Pratinav Seth, Vinay Kumar Sankarapu

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15164v1](https://arxiv.org/pdf/2605.15164v1)

**Abstract**: This position paper argues that behavioural assurance, even when carefully designed, is being asked to carry safety claims it cannot verify. AI governance frameworks enacted between 2019 and early 2026 require reviewable evidence of properties such as the absence of hidden objectives, resistance to loss-of-control precursors, and bounded catastrophic capability; current assurance methodologies (primarily behavioural evaluations and red-teaming) are epistemically limited to observable model outputs and cannot verify the latent representations or long-horizon agentic behaviours these frameworks presume to regulate. We formalize this structural mismatch as the audit gap, the divergence between required and achievable verification access, and introduce the concept of fragile assurance to describe cases where the evidential structure does not support the asserted safety claim. Through an analysis of a 21-instrument inventory, we identify an incentive gradient where geopolitical and industrial pressures systematically reward surface-level behavioral proxies over deep structural verification. Finally, we propose a technical pivot: bounding the weight of behavioral evidence in legal text and extending voluntary pre-deployment access with mechanistic-evidence classes, specifically linear probes, activation patching, and before/after-training comparisons.


### Self-Distilled Agentic Reinforcement Learning
**Authors**: Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weiming Lu, Jun Xiao, Yueting Zhuang, Yongliang Shen

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15155v1](https://arxiv.org/pdf/2605.15155v1)

**Abstract**: Reinforcement learning (RL) has emerged as a central paradigm for post-training LLM agents, yet its trajectory-level reward signal provides only coarse supervision for long-horizon interaction. On-Policy Self-Distillation (OPSD) complements RL by introducing dense token-level guidance from a teacher branch augmented with privileged context. However, transferring OPSD to multi-turn agents proves problematic: compounding multi-turn instability destabilizes supervision, while skill-conditioned privileged guidance requires asymmetric treatment for negative teacher rejections may arise from imperfect skills retrieval or utilization. We introduce SDAR (Self-Distilled Agentic Reinforcement Learning), which treats OPSD as a gated auxiliary objective while keeping RL as the primary optimization backbone. SDAR maps detached token-level signals into a sigmoid gate, strengthening distillation on teacher-endorsed positive-gap tokens and softly attenuating negative teacher rejections. Across the Qwen2.5 and Qwen3 families on ALFWorld, WebShop, and Search-QA, SDAR substantially improves over GRPO (+9.4% on ALFWorld, +7.0% on Search-QA, +10.2% on WebShop-Acc), avoids the instability of naive GRPO+OPSD, and consistently outperforms hybrid RL--OPSD baselines across model scales.


### APWA: A Distributed Architecture for Parallelizable Agentic Workflows
**Authors**: Evan Rose, Tushin Mallick, Matthew D. Laws, Cristina Nita-Rotaru, Alina Oprea

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15132v1](https://arxiv.org/pdf/2605.15132v1)

**Abstract**: Autonomous multi-agent systems based on large language models (LLMs) have demonstrated remarkable abilities in independently solving complex tasks in a wide breadth of application domains. However, these systems hit critical reasoning, coordination, and computational scaling bottlenecks as the size and complexity of their tasks grow. These limitations hinder multi-agent systems from achieving high-throughput processing for highly parallelizable tasks, despite the availability of parallel computing and reasoning primitives in the underlying LLMs. We introduce the Agent-Parallel Workload Architecture (APWA), a distributed multi-agent system architecture designed for the efficient processing of heavily parallelizable agentic workloads. APWA facilitates parallel execution by decomposing workflows into non-interfering subproblems that can be processed using independent resources without cross-communication. It supports heterogeneous data and parallel processing patterns, and it accommodates tasks from a wide breadth of domains. In our evaluation, we demonstrate that APWA can dynamically decompose complex queries into parallelizable workflows and scales on larger tasks in settings where prior systems fail completely.


### Why Neighborhoods Matter: Traversal Context and Provenance in Agentic GraphRAG
**Authors**: Riccardo Terrenzi, Maximilian von Zastrow, Serkan Ayvaz

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15109v1](https://arxiv.org/pdf/2605.15109v1)

**Abstract**: Retrieval-Augmented Generation can improve factuality by grounding answers in external evidence, but Agentic GraphRAG complicates what it means for citations to be faithful. In these systems, an agent explores a knowledge graph before producing an answer and a small set of citations. We frame citation faithfulness as a trajectory-level problem: final citations should not only support the answer, but also account for the graph traversal, structure, and visited-but-uncited entities that may influence it. Through controlled ablation experiments, we compare the effects of isolating, removing, and masking cited and uncited graph entities. Our results show that cited evidence is often necessary, as removing it substantially changes answers and reduces accuracy. However, citations are not sufficient, because accurate answers can also depend on uncited traversal context and surrounding graph structure. These findings suggest that citation evaluation in Agentic GraphRAG should move beyond source support toward provenance over the broader retrieval trajectory.


### Concurrency without Model Changes: Future-based Asynchronous Function Calling for LLMs
**Authors**: Guangyu Feng, Huanzhi Mao, Prabal Dutta, Joseph E. Gonzalez

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15077v1](https://arxiv.org/pdf/2605.15077v1)

**Abstract**: Function calling, also known as tool use, is a core capability of modern LLM agents but is typically constrained by synchronous execution semantics. Under these semantics, LLM decoding is blocked until each function call completes, resulting in increasing end-to-end latency. In this work, we introduce AsyncFC, a pure execution-layer framework that decouples LLM decoding from function execution, enabling overlap between model decoding and function execution as well as inter-function parallelism when dependencies permit. AsyncFC layers over existing models and unmodified function implementations, requiring no fine-tuning or changes to the standard synchronous function-calling protocol. Across standard function-calling benchmarks and adapted software engineering benchmarks, AsyncFC significantly reduces end-to-end task completion time while preserving task accuracy. Furthermore, these results reveal that LLMs possess a native capability to reason over symbolic futures that represent unresolved execution results, enabling an asynchronous paradigm for model-tool interaction.


### SpeakerLLM: A Speaker-Specialized Audio-LLM for Speaker Understanding and Verification Reasoning
**Authors**: KiHyun Nam, Jungwoo Heo, Siu Bae, Ha-Jin Yu, Joon Son Chung

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15044v1](https://arxiv.org/pdf/2605.15044v1)

**Abstract**: As audio-first agents become increasingly common in physical AI, conversational robots, and screenless wearables, audio large language models (audio-LLMs) must integrate speaker-specific understanding to support user authorization, personalization, and context-aware interaction. This requires modeling who is speaking, how the voice sounds, and how recording conditions affect speaker cues. Conventional speaker verification systems provide strong scalar scores but little linguistic evidence, while current audio-LLMs and speaker-aware language models have limited ability to organize speaker information beyond binary labels or descriptive profiles. We present SpeakerLLM, a speaker-specialized audio-LLM framework that unifies single-utterance speaker profiling, recording-condition understanding, utterance-pair speaker comparison, and evidence-organized verification reasoning within a natural-language interface. We construct verification-reasoning targets and a decision-composition policy that separate profile-level evidence from the final same-or-different decision and organize recording condition, profile evidence, and the decision into a structured trace. At its core, SpeakerLLM uses a hierarchical speaker tokenizer designed to capture multiple granularities of speaker evidence. Utterance-level speaker embeddings summarize identity and profile-level cues, whereas frame-level speaker features preserve fine-grained acoustic descriptors. Experiments show that SpeakerLLM-Base improves speaker-profile and recording-condition understanding over general audio-LLMs, while SpeakerLLM-VR preserves strong generated-verdict accuracy and produces decision traces grounded in the supervised verification reasoning schema. We will release the metadata-enriched supervision dataset and target-construction code for reproducibility.


