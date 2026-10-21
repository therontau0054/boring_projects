# Abstracts of Papers

## World Model
### Joints, Camera, Action! Co-Generating 3D Motion and Video for Arbitrary Rigs
**Authors**: Noam Rotstein, Yoad Tewel, Chen Tessler, Haggai Maron, Gal Chechik, Or Litany, Yoni Kasten, Yuval Atzmon

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28632v1](https://arxiv.org/pdf/2610.28632v1)

**Abstract**: Video generation models can now depict remarkably realistic motion. Yet it is unclear how to use this motion beyond pixels: to animate a specific 3D asset and replay the animation in its 3D scene. For instance, a video model can show a monkey jumping over a crossbar, but it cannot return that jump as replayable 3D motion placed in the 3D scene. Here we present a model that directly co-generates the video and 3D motion for any supplied rig, along with a camera that registers this motion to the scene. Prior video-motion models either handle only human skeletons, often adding billions of parameters, or triangulate 3D motion from generated 2D pose maps. We instead keep 3D motion in a separate model that supports arbitrary skeletons, and connect it to a pretrained video model through a small set of cross-attention layers. This separation lets the motion model first learn how skeletons move from motion-only data, which is easier to obtain and augment than paired video. Additionally, our model learns to locate each joint in the video frames, which lets us recover the camera and place the 3D motion in the scene. To train across many skeletons, we use a generative video editor to place animated 3D assets in scenes suited to their actions, curating the edits so their known motion remains valid. Together with human and robot video, this yields nearly 200K training pairs. Our evaluations demonstrate that our model animates diverse rigs from text more faithfully than video-first pipelines, and its motion responds to the surrounding scene. It also turns video into rig motion, rig motion into video, and enables keyframe-based control of the 3D motion. Videos and additional results are available on our project page: https://research.nvidia.com/labs/par/projects/jca/.


### AEON: Unifying Video and 3D World Models
**Authors**: Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28631v1](https://arxiv.org/pdf/2610.28631v1)

**Abstract**: Current world models for explicit world simulation typically follow two distinct pathways: (1) video generative models (e.g., Sora), which simulate realistic appearances but fail to preserve 3D consistency; and (2) 3D generative models (e.g., Marble), which generate geometrically consistent scenes but often yield static, less realistic observations. We present AEON, a unified framework that bridges video-based and 3D-based world models and combines the benefits of both. The key insight of AEON lies in a generative model that operates within the text- or image-conditioned video latent space while producing renderable 4D graphics primitives---specifically, 4D Gaussian Splatting (4DGS)---as the explicit world representation. We train a 4D reconstruction model to predict both 4DGS and camera poses from monocular videos, serving as our initialized 4D decoder. Furthermore, we design a domain adapter that translates generative video latents into reconstructive 4D latents through a distillation process on the video VAE. AEON naturally supports video-based world modeling by rendering 4DGS at predicted camera trajectories, and constructs a persistent 4D environment with scene dynamics for realistic world simulation. Consequently, AEON empowers a diverse range of world modeling applications and achieves state-of-the-art performance on standard benchmarks. Project Page: https://weiqi-zhang.github.io/AEON


### GBClaw: An agentic AI framework for atomistic grain boundary research and mechanistic discovery
**Authors**: Yazhuo Liu, Kunqing Ding, Xiaoguo Gong, Zifeng Wang, Yichen Yang, Yifeng Che, Wen Chen, Josh Kacher, Olivier Pierron, Shigenobu Ogata, Ting Zhu

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28629v1](https://arxiv.org/pdf/2610.28629v1)

**Abstract**: Agentic artificial intelligence (AI) systems hold immense potential for automating complex workflows in materials discovery and design, but extending them to domain-intensive mechanistic investigations remains challenging. Here, we present GBClaw, an agentic AI framework for investigating the structure and deformation of general grain boundaries (GBs). Although general GBs constitute the vast majority of real-world interfaces in polycrystalline materials, they remain understudied because their structural complexity and interfacial mismatch complicate experimental and modeling research. GBClaw integrates large language models (LLMs) into a modular architecture comprising an orchestrator, specialized agents, domain-specific tools, simulation interfaces, and hierarchical memory. Through dynamic replanning and iterative workflow refinement, the framework effectively connects systematic simulations with targeted mechanistic analysis. Applied to 14 general asymmetric tilt GBs in nickel, GBClaw characterized interfacial defect structures and identified diverse deformation modes across these incommensurate boundaries. Comparing boundary sliding with and without secondary GB misfit dislocations revealed substantial differences in shear strength, underscoring the critical role of defect hierarchies in sliding resistance. Furthermore, researcher-guided follow-up calculations traced an anomalously high shear resistance to metastable boundary structures. This work demonstrates that combining agentic AI with domain expertise bridges high-throughput computational screening with deep physical understanding of complex material interfaces.


### Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking
**Authors**: Yuxuan Kuang, Jiashun Wang, Yixuan Sun, Yufei Ye, Sungjae Park, Umar Iqbal, Katerina Fragkiadaki, Shubham Tulsiani

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28628v1](https://arxiv.org/pdf/2610.28628v1)

**Abstract**: Dexterous multi-finger hands hold promise to unlock diverse skills like functional grasps, in-hand reorientation, and dynamic handover that the human-designed world assumes, yet existing learning recipes force a trade-off. Goal-reaching reinforcement learning generalizes to arbitrary object poses but, lacking any human prior, converges to unnatural and unreliable finger strategies; motion tracking reproduces human-like behavior from a single clip but cannot deviate from it. We present AdaDex, a goal-conditioned RL framework that turns a single hand-object trajectory of a few seconds---from mocap data or HOI reconstruction from in-the-wild RGB(D) video---into an adaptable dexterous skill. At the core of AdaDex is Hybrid Dexterous Mimicking: a shared policy is trained on two populations of massively parallel environments: motion tracking environments trained with dense motion tracking objective, which instill the human prior from human motion; and generalization environments with noised initial states and goals and a sparse object-success reward, which force the skill to work far off the reference. From seconds of human motion per skill, the resulting policies can learn diverse adaptable dexterous skills, such as functional grasping, object reposing, in-hand reorientation with finger gaiting, and dynamic behaviors like throw-and-catch. Our method outperforms baselines in terms of generalization and functionality, and we demonstrate transfer across simulators and to the real world. Project page: https://yuxuank.com/AdaDex/.


### UniWALM: Unified World Action Language Model for Embodied Robot Control
**Authors**: Rahul Sajnani, Diego Romeres, Mingyuan Zhang, Kai Gao, Carl Qi, Baichuan Huang, Srinath Sridhar, Dylan Randle, Lillian J. Ratliff, Jose Barreiros, Manikantan Nambi, Jeroen Vanbaar

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28626v1](https://arxiv.org/pdf/2610.28626v1)

**Abstract**: Motivated by the human ability to integrate experience across language, perception, and action, we introduce UniWALM, a unified world-action-language model that learns video, action, and language in a single shared representation, where each modality is both a conditioning signal and a supervision target. We ask: can jointly generating language enrich this shared representation, improving manipulation and supporting memory-dependent behavior? Unlike prior approaches that attach a reasoning or vision-language model to a video-action backbone and run them as distinct stages, UniWALM unifies all three modalities inside a single mixture-of-transformers backbone whose per-modality diffusion heads co-denoise synchronously, decoding subtask and textual memory in the same pass as action with no separate planning stage; the generated language is re-consumed on the next step, closing a language-as-memory loop without an external planner or memory bank. To keep the action stream reliable under this richer objective, we further introduce Flow Matching with Correction (FMC), a training objective that teaches recovery from perturbed action trajectories at no inference-time cost. UniWALM consistently improves over same-backbone baselines (e.g., FastWAM) on compositional pick-and-place (MolmoSpaces) and across the memory-dependent subset of RMBench, where it reaches 34.5% without any pretrained language or reasoning model and exceeds Mem-0's keyframe-equipped setup (28.5%) using only a single anchor frame. On a real-world Find-the-Item task, generating textual memory lifts success from 11.1% to 61.1%, while state-of-the-art VLAs stay at or below chance (<=33.3%).


### Industrial ReMEmbR: Scaling Spatiotemporal Memory to Robot Fleets
**Authors**: Jad Yammine, Malek Wahidi, Abrar Anwar, Yan Chang, Mihir Acharya, Anthony Rizk

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28624v1](https://arxiv.org/pdf/2610.28624v1)

**Abstract**: Warehouse robot fleets continuously observe operational conditions, but preserving these observations as reusable semantic memory incurs substantial computation, communication, and storage costs. For example, explaining recurring aisle blockages can require reviewing video from multiple robots across several shifts. We present IndustrialRemembr, a shared spatiotemporal memory system that extends NVIDIA ReMEmbR to robot fleets and reduces server-side computation by generating scene descriptions only on demand. On each robot, an NVIDIA Jetson encodes video clips into retrieval embeddings with Cosmos-Embed1, vision tokens with Cosmos3-Edge, and reconstruction latents with the Wan2.2 VAE, without uploading raw camera frames. The encoding models are re-used to detect people in image patches, zeroing them out to support PII abstraction for GDPR-compliant deployments. We split Cosmos3-Edge at its vision-language boundary, placing the vision encoder on the robot and the language decoder on an on-premises server. A Nemotron agent retrieves memories by content, position, and time and queries the decoder using cached vision tokens. This design eliminates caption generation at write time, while cached-token decoding reproduces the unsplit model's output in all 450 tested decodes.


## Generation
### MindView: Benchmarking Generative Multi-View Spatial Intelligence
**Authors**: Yanbo Wang, Siqi Luo, Siyu Zhang, Chenming Zhu, Wenzhao Zheng, Qian Yu, Juncheng Yan, Bin Fu, Tai Wang, Yu Qiao, Yihao Liu, Jiwen Lu

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28622v1](https://arxiv.org/pdf/2610.28622v1)

**Abstract**: Spatial intelligence has recently been assessed through generative tasks such as spatially grounded image editing, yet language-guided generation of spatially consistent views from partial multi-view observations remains underexplored. We introduce MindView, a benchmark for generative multi-view spatial intelligence with 1,500 samples from 513 scenes across three indoor datasets. Its seven tasks form two families: geometry-dominant tasks specify changes in camera position and orientation, while semantics-dominant tasks require inferring target viewpoints by grounding referred objects and interpreting spatial relations and reference-frame cues. Evaluation of eleven generators reveals substantial room for improvement on MindView. A paired context analysis further shows that all eleven generators obtain lower overall scores under the expanded context setting. These findings motivate us to investigate whether task-specific supervision can improve target-view generation and whether models can use additional multi-view evidence effectively. We therefore fine-tune BAGEL on the MindView training dataset, improving its overall score by 24.3 points and yielding gains across all seven MindView tasks. Beyond these generation gains, the fine-tuned model also yields higher scores on three spatial-understanding benchmarks without training on their annotations, suggesting that learning to generate spatially grounded views may benefit spatial understanding. To improve evidence utilization under expanded context, we propose MindCue, a training-free spatial evidence selector guided by a target-view hypothesis. MindCue reverses the drop in overall score under expanded context and outperforms the standard-context baseline. Overall, MindView provides a concrete testbed for generative multi-view spatial intelligence.


### Efficient Edge-aware Attention Network for Graph Generation
**Authors**: Vincent Jung, Alba Carballo-Castro, Yiming Qin, Lonneke van der Plas, Pascal Frossard

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28618v1](https://arxiv.org/pdf/2610.28618v1)

**Abstract**: Graph generative models commonly use graph-specific Transformer architectures to jointly update node and edge features. However, these architectures do not directly benefit from recent hardware-aware attention implementations, limiting their scalability. The adaptation is, however, non-trivial: edge and graph-level features must be injected into pairwise attention scores, graph masks must be respected, and dynamic edge updates remain a major source of quadratic memory usage. We propose an edge-aware attention layer for graph generation that incorporates structural information through head-wise score modulation, while updating edge representations with a lightweight residual mechanism that retains attention-score dependent edge updates. This layer can be effectively implemented using PyTorch's FlexAttention. We achieve similar generation quality to our baseline while reducing peak GPU memory by around 65% and substantially improving training and sampling throughput. These results suggest that the proposed architecture is a practical step toward scalable graph foundation models.


### Semantic Observability for Autonomous Systems Diagnostics
**Authors**: Jitendra Solanki, Anand Todkar, Ziran Min

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28611v1](https://arxiv.org/pdf/2610.28611v1)

**Abstract**: Modern distributed microservice deployments generate massive volumes of heterogeneous, multi-format observability logs across physically and logically partitioned infrastructure. Isolating root causes during cascading failures remains an arduous task for Site Reliability Engineers (SREs), bottlenecked by manual keyword filtering and disjointed temporal correlation across monitoring dashboards. We introduce Semantic Observability, an autonomous multi-agent framework that unifies disparate log streams into a dynamic, queryable Property Graph Database. By modeling physical infrastructure topologies, logical software dependencies, and chronological event sequences as attributed nodes and directed relations, it bridges the semantic gap inherent in flat, unstructured log repositories. Building on this unified substrate, we deploy a stateful multi-agent system orchestrated through Directed Cyclic Graphs (DCGs). The system autonomously navigates the topology, applying causal graph algorithms and temporal back-traversal to isolate the precise blast radius of anomalies. The pruned subgraph is then interpreted by a Large Language Model (LLM) reasoning engine to generate contextualized, code-level Root Cause Analyses (RCA) and actionable remediations. This paper establishes the foundational system architecture, formal relational ontology, and multi-agent control loops of Semantic Observability. We show conceptually how the framework eliminates ambient telemetry noise, reduces Mean Time to Resolution (MTTR), compresses LLM token consumption, and prevents structural hallucinations. We also specify an open-source validation framework on standard benchmarks (LogHub and Train-Ticket), laying the groundwork for a forthcoming companion paper on exhaustive quantitative evaluation and production benchmarking.


### Benchmarking Arabic Dialects for Math Problems
**Authors**: Noor Abo Mokh, Teresa Lynn, Nizar Habash, Ahmed Elshabrawy, Sara Alhajeri, Alaa Elsetohy, Preslav Nakov, Alham Fikri Aji

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28607v1](https://arxiv.org/pdf/2610.28607v1)

**Abstract**: Mathematical reasoning remains underexplored for low-resource languages, including Dialectal Arabic. To bridge this gap, we introduce the DAR-MGSM (Dialectal Arabic Multilingual Grade School Math) Benchmark, the first manually curated benchmark for evaluating mathematical reasoning in Dialectal Arabic. DAR-MGSM consists of math word problems (MWPs) requiring multi-step reasoning and covers five major Arabic dialects alongside Modern Standard Arabic (MSA). The benchmark comprises two parallel versions: translated-only and translated & culturally localized. The latter version adapts entities and references to regional varieties. We evaluate eleven Arabic-centric and multilingual large language models on DAR-MGSM. The results show that the performance generally declines on the localized version, highlighting the challenges introduced by culturally grounded adaptations. However, the magnitude of this effect varies across models, with Arabic-centric models exhibiting different levels of sensitivity to localization. A mechanistic interpretability analysis shows that translated and localized variants of the same MWPs often induce distinct internal reasoning trajectories, even when aggregate accuracy remains similar. Overall, our results show that mathematical reasoning performance depends on both linguistic variety and cultural context.


### Value-Rich, Differently Organized: Measuring Value Expression and Organization in AI-Generated Debates
**Authors**: Maoyuan Li, Haoyuan Li, Zhongsheng Wang, Jiamou Liu

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28604v1](https://arxiv.org/pdf/2610.28604v1)

**Abstract**: Current evaluation of LLM-generated debate largely focuses on argumentative quality, leaving the value structure of generated arguments underexamined. We introduce a diagnostic metric framework for comparing how values are expressed and organized in human-reference and AI-generated debates. The framework separates value expression, the range of recognizable values a debate invokes, from value organization, how those values are distributed and sustained across turns. Grounded in Schwartz's Basic-10 value theory, it represents debates as multi-level value distributions over argumentative units, utterances, stances, and full debates, enabling metrics for value coverage, alignment, diffusion, and cross-turn dynamics. Across multiple generation systems, AI-generated debates are broadly value-expressive, often activating as many or more value dimensions than matched human references, but they organize these values differently. Their utterances are more locally value-diffuse, and source-blind judges distinguish value clarity from value focus. These findings show that debate evaluation should consider not only value presence, but also value organization. Code and supplementary materials are available at https://github.com/Maoyuan-li/Value-Expression-and-Organization.


### Evolving Agent Interfaces
**Authors**: Saaket Agashe, Yuzhe Yang, Gonzalo Gonzalez-Pumariega, Bhuvan Chandra Koduru, Chih-Lun Li, Jiachen Yang, Ang Li, Xin Eric Wang

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28601v1](https://arxiv.org/pdf/2610.28601v1)

**Abstract**: Computer-use agents are limited by the interfaces humans give them. An agent may type a spreadsheet cell by cell when a single line of code would do, or print all two thousand lines of a file through a shell to find one function. Both the interfaces and the knowledge of when to use each are built by hand, which cannot keep pace with new applications, workflows, and models. We argue that interface design should itself be an agent capability. We introduce Agent S4, an autonomous computer-use scientist that builds Evolving Agent Interfaces from task experience. A meta-agent examines task agents' trajectories on synthetic training tasks, without success labels, and constructs and revises interfaces and usage knowledge in a repository. Population-based evolution then selects which repositories to develop further by their performance on validation tasks the meta-agent never sees, favoring changes that generalize beyond the seen tasks. On OSWorld V2, Agent S4, with Qwen3.8-27B and the evolved repository of interfaces, sets a new state of the art in open-source computer-use agents, reaching 21.3% binary score, 3.8 times the same model with fixed interfaces. This is above both GPT-5.5 (13.0%) and Claude Opus 4.8 (20.6%), at about 4.3% and 1.5% of their respective costs. On ScienceBoard, the evolved interfaces improve the success rate from 41.4% to 58.6% with the same model. These results suggest that useful interfaces can be evolved from experience, making autonomous interface design a source of improvement complementary to advances in models and harnesses. We open-source our code at https://github.com/simular-ai/agent-s.


## VLA
### Perceives but Doesn't Brake: A Perception-Action Binding Gap in Reasoning Driving VLAs
**Authors**: Matteo Cercola, Katie Z Luo, Simone Formentin, Marco Pavone

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28184v1](https://arxiv.org/pdf/2610.28184v1)

**Abstract**: Reasoning-augmented vision-language-action (VLA) driving models can perceive and reason about safety-critical hazards yet fail to translate that evidence into safe actions. We characterize this failure as a perception-action binding gap: hazard information is available inside the model but exerts insufficient control over trajectory generation. Using matched simulated counterfactuals and logged driving replay, we show that in-path hazards are actually encoded in the visual representation, but longitudinal plans are dominated by ego-speed history and respond only weakly to hazard proximity or the model's own reasoning trace. Further analysis shows that the trajectory generator is capable of braking but sometimes fails to do so due to the perception-action binding gap. Without retraining or modifying any weights, we inject a hazard-conditioned energy into the frozen flow-matching sampler of Alpamayo-1.5, restoring the missing coupling at generation time. With exact obstacle geometry, guidance cuts footprint intrusion from 58.1% to 14.5% and recovers safe braking whenever sufficient stopping distance remains, eliminating collisions entirely in our braking-relevant closed-loop battery. It also reverses the diagnosed dependence of the plan, from tracking ego speed to responding to obstacle range. These results separate hazard perception from hazard control in driving VLAs, show that unsafe behavior can arise even when the model has both the evidence and the ability to act on it, and propose a simple fix for bridging this binding gap.


### VLA-Retain: Benchmarking Cross-Dimension Effects of Vision Tuning in VLAs
**Authors**: Borui Xu, Han Chen, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.27698v1](https://arxiv.org/pdf/2610.27698v1)

**Abstract**: Vision-language-action (VLA) models transfer knowledge from large-scale pretraining into robot control, but their manipulation performance remains sensitive to changes in observation conditions, which recent work addresses by fine-tuning the visual module on target-domain data. However, it remains unclear how such adaptation affects robustness beyond the target condition, as existing robustness benchmarks only evaluate models without fine-tuning and adaptation studies only report the target gain. Measuring this cross-dimension effect requires separating target gains from off-target changes, isolating adaptation effects from architectural differences, ruling out generic forgetting, and comparing tuning choices. Therefore, we introduce VLA-Retain, a benchmark that compares five open VLA models, tuned on Camera-view or Sensor-noise data, with their own base checkpoints on LIBERO-Plus dataset spanning seven perturbation dimensions. Our study reveals four findings. First, targeted vision tuning is not local, and its target gain does not predict retention. Mean off-target gain is negative in 8 of 10 model--domain configurations. Under Camera-view tuning, X-VLA gains $69.4$ percentage points on the target but loses $4.6$ points on average elsewhere, whereas OpenVLA-OFT gains $39.3$ and $1.4$ points, respectively. Second, these regressions are not explained only by performance loss on the same tasks without perturbations. Third, broader training coverage raises overall gain over target-specific training but does not eliminate dimension-level regressions. Fourth, tuning strategies are model-dependent, as DELTA-style feature preservation raises X-VLA's mean off-target gain to $+1.2$ points but lowers OpenVLA-OFT's to $-23.1$. Overall, these findings show that target-domain success alone is insufficient and highlight cross-dimensional retention as a key criterion for targeted VLA adaptation.


### What Would Removing This Corruption Change? Failure Attribution for Vision-Language-Action Models
**Authors**: Carson Sobolewski, Anjali Parashar, Fei Chen, Yingke Li, Chuchu Fan

**Published Date**: 2026-10-19

**Updated Date**: 2026-10-19

**PDF Url**: [2610.27277v1](https://arxiv.org/pdf/2610.27277v1)

**Abstract**: Vision-language-action (VLA) models are sensitive to visual corruptions, but knowing that a corruption is typically harmful does not establish whether removing it would benefit the current episode. Furthermore, when several corruptions co-occur, deciding what to correct requires understanding which ones contribute to failure risk and how much their removal would help. We define this problem as failure attribution. Detecting corruption presence alone cannot answer this question, as corruptions can be present but relatively harmless, while directly measuring removal benefits requires costly paired policy rollouts with and without the corruption present. To address this, we introduce a factorized risk model that learns separate representations of the scene and corruptions, allowing us to estimate removal benefits through latent intervention from the current image and task instruction, without paired clean images or additional counterfactual rollouts. We evaluate our approach on OpenVLA and $π_{0.5}$ in simulation and $π_{0.5}$-DROID on a Franka robot. Our method outperforms monolithic and vision-language-model (VLM) baselines, including achieving approximately 3x lower attribution error than frontier VLMs. We also demonstrate our method adapts to execution context and corruption intensity, and can be used for online failure monitoring on hardware.


### SPAR: Structural Pruning and Action Recovery for Vision-Language-Action Models
**Authors**: Shenli Zheng, Zhou Fang, Yuan Du, Yijiang Liu, Li Du

**Published Date**: 2026-10-19

**Updated Date**: 2026-10-19

**PDF Url**: [2610.26487v1](https://arxiv.org/pdf/2610.26487v1)

**Abstract**: The limited onboard computing resources of robots make the inference demands of vision-language-action (VLA) models costly to accommodate. Reducing these demands through aggressive compression, however, can degrade manipulation performance beyond what supervised fine-tuning alone recovers. We present SPAR (Structural Pruning and Action Recovery), which simultaneously prunes the hidden and feed-forward intermediate dimensions of the large language model (LLM) backbone through pruning-aware tuning, then applies reinforcement learning (RL) to recover policy performance. Applied to $π_{0.5}$, SPAR reduces the language backbone from 2.34B to 0.09B parameters and the full model from 3.37B to 1.12B, removing approximately 96% and 67% of their parameters, respectively. At this compression level, RL raises average success across the four LIBERO suites from 84.55% to 93.45%, an 8.90-percentage-point gain. The compressed policy achieves a $1.98\times$ full-policy inference speedup over the unpruned model. These results identify substantial intermediate-dimension redundancy and show that post-pruning RL can recover manipulation performance in compact policies.


### Robotic Photography System based on Vision-Language-Action Model
**Authors**: Song-Li Wu, Chubin Zhang, Wenbo Ding, Yansong Tang

**Published Date**: 2026-10-19

**Updated Date**: 2026-10-19

**PDF Url**: [2610.26287v1](https://arxiv.org/pdf/2610.26287v1)

**Abstract**: Modern robotic photography requires understanding photographic intent, planning camera motions, and producing aesthetically pleasing images in complex environments. We present RoboPhoto-VLA, a unified Vision-Language-Action framework that jointly models perception, reasoning, and camera control for autonomous robotic photography. RoboPhoto-VLA incorporates PhotoCoT for structured action planning and Aesthetic Direct Preference Optimization (ADPO) to align camera behaviors with human aesthetic preferences. To facilitate training and evaluation, we construct OpenPhotography, a robotic photography dataset with language-guided demonstrations. Extensive real-world experiments demonstrate that RoboPhoto-VLA produces photographs better aligned with human aesthetic preferences while generalizing effectively to unseen subjects, viewpoints, poses, and complex photographic instructions.


### PaceVLA: Adaptive Temporal Action Quantization in Vision-Language-Action Models
**Authors**: Hojin Jeon, Jimin Lee, Taekwan Kim, Nayoung Oh, Taeyoung Kim, Myungkyu Koo, Jinmo Koo, Joonwoo Ahn, Jinwoo Shin

**Published Date**: 2026-10-19

**Updated Date**: 2026-10-19

**PDF Url**: [2610.25961v1](https://arxiv.org/pdf/2610.25961v1)

**Abstract**: Fast and reliable manipulation is crucial for practical robot deployment. Although Vision-Language-Action (VLA) models have recently shown remarkable progress as generalist robot policies, their execution often remains temporally inefficient. A key source of this inefficiency is that policies learn fine-grained temporal patterns from teleoperated demonstrations, requiring many low-level action steps. Temporal action quantization offers a simple way to accelerate execution by aggregating consecutive low-level actions into temporally coarser actions. However, applying action quantization without considering when fine-grained control is required introduces a speed-accuracy trade-off: accelerated actions may efficiently reduce redundant steps in some phases, while discarding critical motion details in precision-sensitive interactions. To address this, we propose PaceVLA, a unified framework for adaptive temporal execution in VLAs that integrates two coupled components: (1) mode-specific action decoders built on a shared action expert, supporting multiple temporal granularities and prediction horizons, and (2) a quantizability-guided mode selection scheme which decides whether coarse execution is appropriate, and a context-conditioned router that selects an execution mode at each inference step. Experiments across three multi-task simulation benchmarks and six real-world tasks show that PaceVLA improves execution efficiency while maintaining task success rate across multiple embodiments, including long-horizon and dexterous manipulation.


## Agent
### Capable Teacher, Myopic Scorer: Reward-Free Teacher Repair for Agentic On-Policy Distillation
**Authors**: Shu Zhao, Tan Yu

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28586v1](https://arxiv.org/pdf/2610.28586v1)

**Abstract**: Agentic on-policy distillation (OPD) trains a student agent on its own trajectories while a teacher scores every token. A natural explanation of where it goes wrong is compounding error: the student's mistakes carry its trajectories beyond the region where the teacher is reliable, so recent methods keep training inside that region, through episode-length curricula, teacher-guided turns, prefix replay, or teacher intervention where the two disagree. We show this explanation is incomplete. From the states where the student departs most from the teacher, the teacher's own takeovers still finish the task, yet the student trained on its token scores keeps running out of turns. We attribute this to the myopia of next-token scoring. The teacher rates each token without seeing where the episode ends, so its scores let through the safe, delaying moves that outcome-based RL would punish with zero reward, a penalty agentic OPD lacks. We call this difference between what the teacher does and what it scores the rollout-scorer gap. We propose Rollout-to-Scorer Distillation (R2S), which repairs the scorer before distillation by mining high-disagreement states from the untrained student, running teacher takeovers from them, keeping the states where enough takeovers pass a reward-free check such as consensus or an LLM judge, and fine-tuning the teacher to give its takeover-informed scores on every assistant token from the divergence turn onward, without the takeover in context. The repaired teacher is frozen as the sole scorer for standard OPD, requiring no task reward during repair or training. Across three environments, two teachers and four students, R2S outperforms three state-of-the-art agentic-OPD methods in all twelve teacher-student-environment cells, by 12.8 success points on average over the best of them in each cell. Project page: https://tree-shu-zhao.github.io/r2s/.


### SceneRig: An Agentic System for Simulation-Ready 3D Scene Reconstruction from Single Images
**Authors**: Rundong Luo, Yunong Liu, Di Cao, Matthew Tancik, Shyamal Buch, Colton Stearns, Wenqi Xian

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28585v1](https://arxiv.org/pdf/2610.28585v1)

**Abstract**: Simulation is a powerful tool for robotics, but building diverse, simulation-ready scenes at scale remains difficult. Reconstructing scenes from single images is a promising alternative, but visual similarity alone is insufficient: objects must also be recovered, accurately placed, and physically grounded. Existing methods that rely on post-hoc physics settling often misplace objects, producing scenes that look correct but behave poorly under manipulation. We present SceneRig, an agentic system that turns a single image into an editable, simulation-ready scene. SceneRig combines geometric, visual, and physical tools to reconstruct a faithful 3D scene. An agent then performs edit-and-validate loops inside a physics simulator to achieve physical stability. Across diverse inputs, SceneRig improves instance segmentation, object-centric appearance, and 3D placement while keeping the reconstructed scenes physically stable. Furthermore, SceneRig is effective for downstream robotics: its scenes predict real-robot policy outcomes more accurately than the baseline method and more reliably support replay of recorded manipulations without trajectory adaptation.


### Sage-A1.5: From Long-Horizon Execution to Scientific Exploration with Capability Composition
**Authors**: Wenjie Lou, Tianshuo Peng, Shiyang Feng, Shengji Tang, Runmin Ma, Ruizhe Chen, Jinxin Shi, Haoyang Peng, Fangchen Yu, Zhijie Zhong, Yuhao Zhou, Yue Fan, Yixin Chen, Yiming Wu, Yiheng Wang, Yigeng Jiang, Yichen Jiang, Yi Xie, Xu Guo, Xiaohan He, Tao Hu, Songtao Huang, Siyu Zhou, Shuaiyu Zhang, Shangheng Du, Qinglong Cao, Kun Li, Jingqi Ye, Hongbin Zhou, Guohang Yan, Zongsheng Cao, Ziyi Wang, Zhuo Liu, Zhiyin Yu, Zhiwang Zhou, Zelin Tan, Yuqing Zhu, Yaoze Zhang, Yang Chen, Xuming He, Xiuliang Liang, Xingjian Guo, Xiang Zhuang, Weiping Shen, Weida Wang, Tianyuan Zhou, Tianlin Ye, Tengyuan Fan, Siyu Yan, Shuo Li, Shuchen Pu, Shengyuan Xu, Shao Zhang, Ran Wei, Qinyuan Qin, Qingyu Yang, Nianchen Deng, Meng Dai, Kuikun Liu, Kaitao Chen, Juncheng Xiao, Jiangning Liu, Jianbiao Mei, Jia Yu, Haonan He, Hangfan Zhang, Cheng Yang, Chen Zhang, Bihao Zhan, Benteng Cheng, Yuqiang Li, Yihao Liu, Yang Yang, Xujun Fu, Xiaosong Wang, Xiangyu Yue, Wenwei Zhang, Shuyue Hu, Pinlong Cai, Mianxin Liu, Lei Bai, Jie Zhou, Jie Hou, Jiamin Wu, Hui Wang, Haijun Li, Guangyu Wang, Dongzhan Zhou, Chunfeng Song, Chao Yang, Biqing Qi, Xing Xie, Dahua Lin, Bowen Zhou, Xiangchao Yan, Wenlong Zhang, Shufei Zhang, Peng Ye, Bo Zhang

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28578v1](https://arxiv.org/pdf/2610.28578v1)

**Abstract**: In this report, we introduce Sage-A1.5, a 35B Mixture-of-Experts agentic model that builds on A1 to advance long-horizon problem solving through adaptive capability composition. Compared with A1, Sage-A1.5 learns not only to solve individual tasks, but also to organize work and revise its approach during execution. Sage-A1.5 highlights three improvements: agentic orchestration, verification, and open scientific discovery. First, agentic orchestration extends single-agent execution through task delegation and parallel collaboration among subagents with isolated contexts, enabling complex tasks to be decomposed and addressed concurrently and supporting efficient execution while reducing interference across concurrent subagents. Second, agentic verification strengthens long-horizon reliability through progress checking, evidence validation, and reflective strategy revision, allowing the agent to recognize unproductive search paths and pursue alternative approaches. Third, open scientific discovery extends agentic capabilities beyond answering predefined questions to conducting exploratory research, connecting scientific inquiry with interactive analysis and inspectable research artifacts. We showcase these capabilities through complicated agentic tasks and multidisciplinary scientific applications. Besides, we hope Sage-A1.5 provides the community with an accessible foundation for open scientific discovery, offering a practical path from long-horizon task execution to collaborative, verifiable, and inspectable scientific exploration.


### OptScientist: Automated Discovery of Optimization Laws
**Authors**: Ma ZhenYao, Yue Liang, Jian-Qiao Zhu

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28562v1](https://arxiv.org/pdf/2610.28562v1)

**Abstract**: Many scientific phenomena are best understood as outcomes of underlying optimization problems, yet automated scientific discovery has largely focused on recovering equations that describe observed input-output patterns. We introduce OptScientist, a novel automated framework for discovering compact symbolic optimization laws directly from data. OptScientist comprises (i) a model that infers symbolic optimization problems by first learning to represent data as an optimization problem and then extracting its symbolic form, and (ii) an LLM agentic system embedding the model in a discovery process that integrates theoretical priors from scientific literature, discovers candidate laws, abstracts their underlying mechanisms, and suggests new data to collect. We first evaluate OptScientist on OptFeynman, a novel benchmark of 99 physics-derived optimization problems, where OptScientist recovers ground-truth laws for over 80% of the problems and remains robust to noisy contextual information, while substantially outperforming machine-learning, symbolic, and LLM-based model-discovery baselines. On human risky choice and central-bank monetary policy, OptScientist discovers compact symbolic optimization laws that achieve held-out predictive performance competitive with leading baselines, while using few parameters and substantially fewer tokens than LLM baselines. Overall, OptScientist extends automated scientific discovery to uncovering optimization laws that generate observed phenomena, enabling automated theory building across the physical, biological, behavioral, and social sciences.


### Agentic Ensemble with Vision-Language Models for Visual Anomaly Detection
**Authors**: Shangquan Sun, Wenjun Luo, Xu He, Yoonsoo Lee, Shijian Lu

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28560v1](https://arxiv.org/pdf/2610.28560v1)

**Abstract**: Visual anomaly detection aims to detect abnormal objects, while anomaly samples are often scarce during model training. Assembling multiple pretrained detectors can help by leveraging their transferable image scores and anomaly maps. However, most existing ensemble methods apply fixed fusion rules over saved predictions which struggle when pretrained detectors clearly disagree due to different training objectives, priors, and visual representations. To this end, we design AnomalyAgent, a post-training fusion framework for accurate visual anomaly detection. AnomalyAgent aligns heterogeneous scores and maps, summarizes score- and region-level disagreement, and treats fusion as a finite action-selection problem. It implements two types of actions: 1) score actions that determine how to fuse image-level detector confidence via consensus, robust aggregation, detector weighting, or score-map consistency; 2) map actions that fuse dense anomaly responses via consensus, detector weighting, geometric aggregation, or disagreement correction. A constrained vision-language model (VLM) is introduced to inspect high-conflict samples and select valid score action and map action to produce the final prediction. We evaluate AnomalyAgent on MVTec AD and VisA as primary benchmarks, together with seven additional public anomaly benchmarks and Real-IAD for large-scale score-level evaluation. Across these benchmarks, AnomalyAgent consistently improves over equal-weight fusion and achieves the best mean image AUROC and pixel AP among the compared fusion methods on MVTec AD and VisA, while demonstrating robust transfer across additional anomaly domains.


### Proof-Carrying Contracts: Commitments AI Agents Cannot Break
**Authors**: Carlo Ciliberto, Alessandro Rudi, Enrico Tassi

**Published Date**: 2026-10-20

**Updated Date**: 2026-10-20

**PDF Url**: [2610.28484v1](https://arxiv.org/pdf/2610.28484v1)

**Abstract**: AI agents increasingly act on behalf of people or other agents, purchasing services, exchanging information and delegating work. What an agent must respect is written in instructions, policies or agreements, but text alone cannot make it comply. It may make mistakes, be redirected by what it reads, or pursue different interests. For an economy of such agents to function, parties need agreements they can rely on without inspecting or trusting one another's agents. We introduce Proof-Carrying Contracts (PC2), a framework for making agreed constraints enforceable throughout an agent's interactions with a system. Before a requested operation can run, the agent must supply a machine-checkable proof that it preserves the agreed constraints in every case allowed by its model. An execution system called the Airlock checks the proof and controls access to the operation. The parties specify the conditions to preserve, while the agent supplies the reasoning needed to justify its decisions and remains free to adapt its strategy. This avoids having to design a separate permission policy and prove that every decision it permits is safe. We prove that the constraints hold at every instant during execution, even for an adversarial agent, and identify when this implies safety in the world. Reusable capability modules provide tools and guarantees from which contracts can be constructed. PC2 provides a foundation for an agent economy whose agreements protect both those delegating work and those carrying it out.


