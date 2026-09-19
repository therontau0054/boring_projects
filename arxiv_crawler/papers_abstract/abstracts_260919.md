# Abstracts of Papers

## World Model
### Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation
**Authors**: Bingxin Xu, Yuzhang Shang, Zhen Dong, Emilio Ferrara

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20822v1](https://arxiv.org/pdf/2609.20822v1)

**Abstract**: Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-specific training.Whether this paradigm is also safe, however, has not been asked. We evaluate coding agent under a safety constraint, where each task pairs a manipulation goal with an obstacle the robot must not touch. The agent pursues the goal but collides with the obstacle in most cases, treating task completion as its sole objective while neglecting safety. The agent reasons about the obstacle in its traces, and the prompt already forbids touching it, so neither perception nor instruction is at fault; the fault lies in the planning, where the stated constraint never becomes a priority. By decomposing manipulation into a route phase and a contact-rich moment, we locate the source of the failure. Along the route, the model cannot prioritize the safety constraint, having no notion of a clearing route and none of replanning once a chosen route becomes infeasible. At the contact, it is unaware that contact execution is bounded by the same constraint. To close this gap, we present SafeHarness, which equips the model with two obstacle-aware harnesses that enable it to prioritize the safety constraint. Obstacle-aware route planning grounds the objects as bounding boxes and draws candidate routes over them as sequences of waypoints. The agent then plans a route in advance, verifies it, replans when necessary, and only then executes it. Obstacle-aware contact execution instead selects the contact position so that the contact itself avoids the obstacle. SafeHarness attains 71.9% task success and 87.5% collision avoidance, surpassing the previous SOTA by 6.5% and 27.0%, respectively. These results are $2.3\times$ and $1.5\times$ those of the same agent without harnesses.


### Embedding Models Measure in Peculiar Ways
**Authors**: Juri Opitz, Andrianos Michail

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20821v1](https://arxiv.org/pdf/2609.20821v1)

**Abstract**: Embedding spaces define notions of semantic similarity and distance. We study whether those embeddings reflect physical measurements of mass, distance, time and volume, which admit a unique, objective notion of semantic equivalence and distance. We find that physical measurement is only weakly modeled in the embedding space, and that instead quite peculiar measurement patterns can be observed. Further analysis indicates that embedding representations of physical measurements are strongly influenced by superficial string similarity, and recalibration of similarity does not substantially improve the alignment.


### Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision
**Authors**: Nitish Dashora, Douglas Chen, Idan Shenfeld, John Marangola, Pulkit Agrawal, Max Simchowitz

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20820v1](https://arxiv.org/pdf/2609.20820v1)

**Abstract**: Complex robotic manipulation tasks frequently require a long-term memory of past events and actions. As conditioning on full histories renders policies prone to spurious correlations and degrades performance, many approaches to policy memory involve compressing historical information through expensive VLM queries in-the-loop to process only task-salient information. In this paper, we propose an alternative approach in which computationally intensive VLM queries are made during train-time to learn a lightweight latent memory that can be efficiently queried at deployment time. Our representation, which we call the \textbf{workspace token}, is trained by (1) using a VLM to identify current and historical information necessary for completing a task, then (2) distilling these into the workspace token using a set-reconstruction decoder loss. In both simulation and hardware, we show that the workspace token can be used as a drop-in replacement for observations during deployment, enabling policies to solve memory-intensive tasks without the need for VLM reasoning in-the-loop. Interestingly, we found that workspace tokens are not only more lightweight but also lead to better policy performance.


### Can 4D Foundation Models Remember?
**Authors**: Guangzhao He, Hadar Averbuch-Elor, Wei-Chiu Ma

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20819v1](https://arxiv.org/pdf/2609.20819v1)

**Abstract**: Perceiving and remembering the visual world is fundamental to navigating and interacting with our environment. Current 4D foundation models, such as camera-controllable video models or 4D reconstruction models, can perceive and reconstruct dynamic environments, but how well they remember what they have perceived remains an open question. Existing benchmarks largely rely on pixel-level metrics and lack ground truth for objects once they leave the field of view, making them unable to evaluate visual memory in an object-centric manner against references. To fill this gap, we introduce PersistBench, a dataset and metric suite that leverages 360° videos as omniscient ground truth and proposes three evaluation aspects: object permanence, motion continuity, and appearance preservation. Evaluating various models across diverse categories reveals that current models can only maintain short-term consistency that degrades significantly once objects leave the field of view. Our findings highlight the gap between current model capabilities and robust visual memory ("seeing is not remembering"), providing guidance for future development of 4D foundation models. Dataset and code are available on the project page: https://guangzhaohe.com/persistbench.


### SplashSplat: Reconstructing Splashing Liquids from Real-World Multi-View Videos
**Authors**: Peiyu Liu, Dingxi Zhang, Federico Tombari, Marc Pollefeys, Christina Tsalicoglou, Daniel Barath

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20818v1](https://arxiv.org/pdf/2609.20818v1)

**Abstract**: A splash lives for a fraction of a second: sheets tear into ligaments and droplets, appearance is view-dependent and nearly textureless, and little persists long enough to track. Reconstruction research has consequently focused on smoke, synthetic liquids, or gently deforming surfaces. To our knowledge, no synchronized multi-view dataset of splashing liquids exists. We therefore introduce a benchmark of 20 real scenes, from coherent streams to violent splashes, captured by seven synchronized, calibrated 4K cameras at 60 fps, with manually refined per-view liquid and container masks and fixed evaluation splits. We further present SplashSplat, built on a single principle: impose physical structure only where the observations can constrain it. Per-frame liquid SDFs fused from the masks provide the geometry, level-set transport between consecutive SDFs yields a coarse velocity field, and Lagrangian carriers advected along this flow, corrected against each new observation and reseeded where coverage is lost, decode local Gaussians for differentiable rendering. SplashSplat outperforms state-of-the-art dynamic Gaussian splatting methods on our real captures and on a synthetic benchmark, with physically more plausible motion and a lower training cost. The same representation supports temporal interpolation and style transfer without re-optimization.


### FAMOS: Feed-Forward 3D Articulation Modeling from Sparse Observations
**Authors**: Kevin Qu, Tao Sun, Massimiliano Viola, Liyuan Zhu, Zhizhuo Zhou, Sayan Deb Sarkar, Konrad Schindler, Iro Armeni

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20817v1](https://arxiv.org/pdf/2609.20817v1)

**Abstract**: Modeling articulated objects from sparse monocular views is challenging because each observation reveals only partial geometry and motion evidence. Most feed-forward methods infer articulation from a single observation and therefore rely heavily on learned category-level shape priors. We present FAMOS, a feed-forward model that predicts movable-part segmentation and joint parameters from a sparse, unordered set of partial point clouds. Our model jointly reasons over multiple observations and naturally supports a variable number of inputs, including a single view. To aggregate articulation cues across observations, we introduce a Multi-state Articulation Transformer with alternating state-wise and global attention. We further propose an observed articulation span objective that supervises the motion range each part exhibits across the input observations, encouraging the model to leverage the full observation set. To overcome the limited scale and diversity of existing datasets, we introduce a procedural data generator that synthesizes self-annotated assets during training. Experiments on PartNet-Mobility, ACD, and ArtiCraft-10K demonstrate consistent improvements over both feed-forward and optimization-based baselines. Project page: https://kevinqu7.github.io/famos


## Generation
### Paint-Anything: Unified Any-Color Control for Image Generation and Editing
**Authors**: Ji Xie, Dewei Zhou, Xinyu Huang, Zhennan Chen, Xun Wang

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20816v1](https://arxiv.org/pdf/2609.20816v1)

**Abstract**: Professional design requires any-color control: the ability to specify an object's target color with any 24-bit hex value for image generation and editing. Prior work has explored color generation, editing, and colorization, but often relies on dedicated color representations or specialized inference procedures. Advances in large language models offer a simpler starting point: even compact models can associate hex values with color semantics. We present Paint-Anything, which learns a shared hex-prompt interface for generation and editing through object-level color supervision. We develop a data pipeline that constructs Paint-500K from real images through object grounding, perceptual color labeling, and editing-pair synthesis. Since shadows make real-image labels only approximate colors, we complement this supervision with pure-color anchors whose pixels exactly match their paired hex values. These anchors are used only at high-noise timesteps, leaving low-noise training to natural images. We further introduce Any Color Benchmark (ACBench), comprising ACBench-T2I and ACBench-Edit, to measure object-level hex color fidelity across both tasks. On FLUX.2-4B, Paint-Anything improves ACBench-T2I and ACBench-Edit scores by 85.3% and 28.3%, respectively, relative to the base model, with ablations supporting the training recipe. It also achieves the highest average CompColor score among the compared methods.


### PosteriorBench: From Point Estimates to Posterior Matching in Evaluating Generative Inverse Solvers
**Authors**: Jiachen Yao, Zi-Siang Hsu, Xi Deng, Aditi Gupta, Xin Ju, Sally M Benson, Gege Wen, Anima Anandkumar

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20794v1](https://arxiv.org/pdf/2609.20794v1)

**Abstract**: Generative models are increasingly used to solve scientific inverse problems, but existing evaluations still focus primarily on whether a method can produce a single plausible reconstruction. This is insufficient for ill-posed problems, where multiple solutions may be consistent with the same sparse or noisy observations. In these settings, a method can achieve strong pointwise accuracy while still failing to capture the true posterior through mode collapse, overconfident uncertainty, or averaging incompatible solutions. We introduce PosteriorBench, a benchmark for evaluating the distributional accuracy of generative inverse solvers. PosteriorBench evaluates four physics-based inverse problems: Darcy flow inversion, Poisson source recovery, carbon capture and storage, and light transport material inference. For each task, we construct high-fidelity reference posteriors using computationally heavy but established procedures such as rejection sampling and Markov chain Monte Carlo, enabling direct assessment of whether solvers recover the full set of solutions rather than the single best sample. We pair these references with a five-metric posterior evaluation suite: posterior-mean error, posterior-standard-deviation error, maximum mean discrepancy, sliced Wasserstein distance, and radially averaged power-spectrum error. These metrics assess pointwise accuracy, marginal uncertainty, distributional alignment, and global frequency fidelity. The benchmark spans sparse sensing, low-resolution observations, nonlinear forward models, varying noise levels, and multimodal priors, with a unified pipeline for distribution matching and uncertainty quantification. Our experiments reveal substantial distribution-matching gaps across current solvers, while showing that neural operators improve resolution robustness, and guidance weights and generation noise are key to posterior-variance calibration.


### Harm Laundering in GPT Models: Evidence That Gender Discrimination Is Transformed Rather Than Reduced Across Safety-Trained Generations
**Authors**: Sarah Wyer, Sue Black, Noura Al Moubayed

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20779v1](https://arxiv.org/pdf/2609.20779v1)

**Abstract**: Safety evaluations for large language models rely on surface-form classifiers that report declining harm scores across model generations. We provide evidence that this methodology is systematically incomplete: explicit discriminatory content is transformed rather than removed. We call this \emph{harm laundering}. Analysing 450,000 gender-directed completions across 15 models spanning GPT-2 through to GPT-5 (OpenAI GPT lineage; three demographic conditions), we show that sexual violence clusters prevalent in GPT-2 women-directed output disappear by GPT-4, while men-directed completions gain positive representational territory (caregiving, emotional range, ally identity) that women-directed completions do not. The pattern is most visible at GPT-5: Topic~5 (1,997~documents) frames breast cancer as a men's rights debate, while zero equivalent clusters appear in women-directed output. Three independent classifiers score this content as non-toxic. Sentiment scores invert at GPT-4: early models demean women; later models over-correct. Topic diversity in women-directed completions falls 36\% relative to men at the GPT-4 alignment boundary (W/M~$= 0.58$, from $0.91$ at GPT-2). REGARD representational harm disparity correlates with release date ($ρ= +0.55$, $p = .034$) while Detoxify does not ($ρ= -0.23$, $p = .42$): toxicity scores fall as representational harm grows. We formalise harm laundering as a three-criteria test and provide a three-stage detection protocol applicable to any generative model. Within the OpenAI GPT lineage, toxicity score reduction is not a sufficient proxy for harm reduction.


### GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies
**Authors**: Xin Chen, Sen Chen, Yujuan Ding, Jian Liu, Guoqing Wang, Wei Ye, Heng Tao Shen, Yi Bin

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20776v1](https://arxiv.org/pdf/2609.20776v1)

**Abstract**: Action chunking is widely used for action generation and execution in Vision-Language-Action (VLA) policies, yet existing approaches commonly use a fixed action horizon. During a rollout, different task stages may require different levels of action continuity, control precision, and closed-loop feedback, making a fixed horizon unable to accommodate changing control requirements. We propose \textbf{GeoAAC}, a geometry-based adaptive action chunking method for flow-based VLA policies that adjusts the action horizon according to the reliability of the current action prediction. We show that the geometry of Flow Matching denoising trajectories provides process-level information for characterizing prediction reliability, with geometric variation across action prefixes remaining positively correlated with predictive uncertainty. GeoAAC uses this prefix-wise geometry to construct a horizon-wise geometric profile and adaptively determine the action horizon from a single generation without additional training. Experiments with GR00T N1.5 and π0.5 on LIBERO, LIBERO-Pro, RoboCasa365, and real-world manipulation tasks show consistent improvements over fixed-action-horizon baselines and existing adaptive methods, including up to 8.7 percentage points in simulation and an increase in average real-world success rate from 53.3\% to 74.4\%.


### Semantic Action Graph: A Shared Representation for Agent Grounding and Human Interpretation of Sports Highlights
**Authors**: Tica Lin, Deepak Chandran, Gauri Jagatap, Chen Chen, Andrea Fanelli, David Gunawan, Josh Kimball

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20768v1](https://arxiv.org/pdf/2609.20768v1)

**Abstract**: Generative agents are increasingly used to select and narrate video highlights, but they typically operate over unstructured or frame-level representations. Their output is consequently difficult for a viewer to verify and steer toward individual preferences. We present the semantic action graph, a lightweight domain schema that represents a sports match as performer, action, recipient, moment, and state nodes connected by role, temporal, and outcome edges. The schema demonstrates three key properties: 1) connected event sequences, 2) a shared, closed vocabulary, and 3) frame-addressable moments, making it suitable to serve two consumers at once: an agentic pipeline that composes narrated highlights, and a visual interface through which viewers query and inspect the same structure. We instantiate it in SportSAGE, a design probe pairing a four-module highlight pipeline with a graph interface, and report feedback from 12 soccer fans. Participants were satisfied with the quality of the generated highlights and narratives, and used the graph interface to search, navigate, and interpret the match highlights. These results provide early evidence that one small, human-readable schema can ground agent generation and support human interpretation at the same time.


### Agile-WAM: An Agile Tactile World Action Model for Contact-Rich Robot Control
**Authors**: Hanchu Zhou, Brendan Lynch, Raman Goyal, Dechen Gao, Begum Kasap, Boqi Zhao, Junshan Zhang

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20761v1](https://arxiv.org/pdf/2609.20761v1)

**Abstract**: World Action Models (WAMs) advance beyond conventional visuomotor policies by jointly predicting future world states and robot actions, enabling the policy to learn physical dynamics that support effective control. However, recent tactile WAMs often rely on large-scale pretrained generative backbones to capture contact-rich physical dynamics, which limit their inference efficiency and flexible deployment. In this paper, we present \ABBR{}, an agile tactile World Action Model for contact-rich robot control. \ABBR{} encodes visual and tactile observations into a shared latent that serves as the source of a direct vision-tactile-to-action flow-matching process, which can jointly generate latent representations of action chunks and future visual/tactile latents. A key observation is that vision and tactile signals evolve at inherently different timescales: adjacent visual frames are often highly similar, whereas tactile signals can change abruptly upon contact. We therefore introduce multi-horizon multimodal prediction in \ABBR{}, which provides supervision for visual latent at a larger temporal offset while predicting the tactile latent in the next frame to capture fine-grained contact dynamics. Across nine simulated and five real-world contact-rich manipulation tasks, \ABBR{} demonstrates strong and robust performance, outperforming the strongest baseline in success rate while maintaining low inference latency. In particular, in five real-world experiments, \ABBR{} yields a relative gain of $\textbf{29.4\%}$ in overall success rates while achieving inference latency of $\textbf{11.9 ms}$. These results demonstrate that multimodal WAM can be achieved with an agile architecture suitable for precise and high-frequency robot control. More details are available on our project page: https://hanchuzhou.github.io/TARO_project_page/.


## VLA
### HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface
**Authors**: Zimu Han, Yiming Zeng, Jiyao Zhang, Zihao Zhao, Yuanfei Wang, Yixiang Jin, Shiqi Li, Shuangben Chen, Wei Huang, Ruodai Li, Hui Shen, Hao Dong

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20659v1](https://arxiv.org/pdf/2609.20659v1)

**Abstract**: Large-scale vision-language-action (VLA) models provide powerful priors for robot manipulation, yet adapting them to a specific deployment remains challenging. Supervised fine-tuning (SFT) on task-specific demonstrations provides a step toward deployment, but faces two persistent limitations: static data provide limited coverage of out-of-distribution states, and standard imitation objectives do not distinguish progressing behavior from less useful data. Interactive post-training can address these limitations, but typically requires repeated policy execution and human intervention on a physical robot. We introduce HIL-UMI, a policy-guided Universal Manipulation Interface (UMI) framework for robot-free human-in-the-loop VLA post-training. During handheld UMI demonstrations, HIL-UMI queries the current policy on the same observation stream without executing its predictions. The Energy Score compares the human action trajectory with policy inference and triggers collection when their discrepancy indicates an out-of-distribution region. In a separate feedback loop, low online advantage predictions identify essential segments for refining a progress-based advantage estimator. The updated estimator then guides advantage-conditioned behavioral cloning using a balanced mixture of base demonstrations and new policy data. This design preserves the iterative and policy-aware nature of human-in-the-loop learning while decoupling data collection from robot deployment. Experiments on four real-world tasks spanning long-horizon and precise manipulation show that HIL-UMI achieves consistent improvement over SFT and benefits from both targeted collection and advantage refinement. Moreover, HIL-UMI outperforms HG-DAgger on Clean Up Table with lower per-frame collection time, suggesting a scalable path for VLA post-training across operators and locations.


### Uni-LaDiR: Latent Diffusion Unifies Multimodal Reasoning
**Authors**: Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang, Yian Ma, Lianhui Qin

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.19878v1](https://arxiv.org/pdf/2609.19878v1)

**Abstract**: Multimodal reasoning requires models to draw on information from multiple modalities throughout the reasoning process. Yet existing methods often concatenate modality-specific thought tokens in a single sequence, leaving the model to bridge representational differences as it reasons across modalities. We introduce Uni-LaDiR (Unified Latent Diffusion Reasoner), a framework that brings these thoughts into a shared latent space for reasoning. A unified encoder maps teacher reasoning steps from different modalities into shared thought tokens, trained to preserve the information needed for later reasoning steps and the final answer or action. Because the same context can support multiple valid next steps, we use diffusion to predict the next block of thought tokens from the input and preceding blocks. Jointly training the encoder and diffusion reasoner with shared model weights encourages thought tokens to be both useful for the task and predictable from the available context. At inference, the model generates these tokens without teacher observations. Across eleven vision-language model (VLM) benchmarks and two vision-language-action (VLA) suites, Uni-LaDiR achieves relative gains over the strongest evaluated baselines of 7.3% on visual reasoning tasks and 6.1% on robot manipulation tasks.


### Acting in Meters: Learning Metric Interactions for Precise Robotic Manipulation
**Authors**: Lijie Wang, Zheng Lu, Yiming Wang, Heyang Yu, Kenghou Hoi, Bowen Hu, Di Cui, Tianyu Xin, Haoran Liao, Wanqi Zhong, Xingjie Fan, Yizhao Xu, Ziliang Wang, Fei Gao, Yiming Li

**Published Date**: 2026-09-16

**Updated Date**: 2026-09-16

**PDF Url**: [2609.18243v1](https://arxiv.org/pdf/2609.18243v1)

**Abstract**: Vision-Language-Action models and World-Action Models have advanced language-conditioned robotic manipulation, yet often leave metric relations among actions, objects, and scene geometry implicit. Human manipulation combines semantic understanding of task-relevant objects with spatial feedback that guides hand motion relative to objects and their surroundings. Inspired by this, we introduce a metric interaction framework that models object-level and scene-level interactions in physical Cartesian space at a shared metric scale. At the object level, Interaction-Centric Tokens (ICTs) explicitly represent end-effector pose trajectories relative to manipulated objects and are jointly denoised with actions, providing physically grounded interaction supervision. At the scene level, the Metric Action Interaction Field (MAIF) uses action and ICT queries to attend to metric scene point-cloud features and learns geometry-conditioned action corrections. Through two-stage adaptation, our framework improves diverse VLA and WAM baselines with a small number of additional parameters and training steps. Experiments demonstrate average success-rate gains of 0.80 and 3.59 percentage points on LIBERO and RoboTwin~2.0, respectively, alongside gains of 6.80 percentage points on real-world tasks and 7.45 percentage points on their out-of-distribution variants.


### Reinforcement Learning for Real-Time Vision-Language-Action Policies
**Authors**: Perry Dong, Kuo-Han Hung, Dorsa Sadigh, Chelsea Finn

**Published Date**: 2026-09-16

**Updated Date**: 2026-09-16

**PDF Url**: [2609.18207v1](https://arxiv.org/pdf/2609.18207v1)

**Abstract**: Reinforcement learning fine-tuning on top of large, pretrained Vision-Language-Action (VLA) models offers promise for highly reliable robot deployment. However, because of their scale, modern VLA models suffer from high inference latency, so the observation used to select an action is often stale by execution time, creating a distribution shift that can substantially degrade reliability and performance. Prior work has explored asynchronous policy execution to reduce the effect of latency, but these methods are mostly built on imitation learning and offer no mechanism for moving beyond the training distribution toward higher reliability. We close this gap by enabling RL fine-tuning that meets the real-time control requirements of dynamic real-world manipulation. Our approach builds on EXPO-FT, a framework for sample-efficient, reliable VLA fine-tuning with reinforcement learning, and decouples slow, expressive action generation from fast, reactive action edits: a large pretrained VLA proposes action chunks using its strong behavior prior, while a lightweight edit policy performs fast, reactive decision-making by editing actions in response to changes in state, conditioned on the latest observation. We instantiate this as Real-Time EXPO-FT, an RL framework for finetuning real-time VLA policies. On the Kinetix benchmark, Real-Time EXPO-FT enables a delayed policy to achieve the best performance among delayed and non-delayed methods in 10 out of 10 environments. On four dynamic real-world tasks, robot object passing, ball balancing, table soccer kicking, and dynamic object picking, with online robot data capped at 10 minutes, Real-Time EXPO-FT improves average policy performance from 42% to 97%, all without human intervention, demonstrating rapid, sample-efficient adaptation to challenging real-world dynamics. Website: https://pd-perry.github.io/real-time-expo-ft


### A Comprehensive Review of Generative Physical Artificial Intelligence
**Authors**: Satyam Gaba, Krutiksinh Rana, Siva Sai, Vinay Chamola, Dusit Niyato

**Published Date**: 2026-09-16

**Updated Date**: 2026-09-16

**PDF Url**: [2609.18111v1](https://arxiv.org/pdf/2609.18111v1)

**Abstract**: The integration of large-scale foundation models with physical embodiments has led to significant advancements in robotics known as Generative Physical Artificial Intelligence (GPAI). These agentic AI systems autonomously perceive, reason, and act in complex real-world situations. This survey comprehensively analyzes GPAI systems, focusing on their architectural foundations, current applications, and key limitations. We introduce a taxonomy of five distinct approaches: Robot Foundation Models (RFMs) for cross-platform skill transfer; Vision-Language Action (VLA) models for end-to-end multi-modal perception and control; Large Behavior Models (LBMs) for human-like movement generation; Diffusion Policy Models (DPMs) for diffusion model-based temporally coherent action generation; and World Foundation Models (WFMs) for physics-compliant simulation and data generation. We examine how these approaches complement each other: WFMs generate training data for VLAs and DPMs, RFMs enable cross-platform deployment of learned policies, while LBMs provide motion priors for natural behavior. Through examples across autonomous vehicles, industrial automation, healthcare robotics, and humanoid systems, we identify significant performance improvements and summarize promising research directions in data-efficient learning, sim-to-real transfer, edge-compatible architectures, and safety frameworks. These insights advance embodied AI for IoT-connected environments where intelligent agents interact with networked sensors, actuators, and edge devices.


### Not All Layers Need Tuning: Diagnosing and Directing Adaptation in Vision-Language-Action Models
**Authors**: Shahram Najam Syed, Arthur Jakobsson, Prayuj Sachdev, Jeffrey Ichnowski

**Published Date**: 2026-09-16

**Updated Date**: 2026-09-17

**PDF Url**: [2609.18084v2](https://arxiv.org/pdf/2609.18084v2)

**Abstract**: Fine-tuning a Vision-Language-Action (VLA) model for a new deployment environment is expensive, yet most methods apply uniform-capacity adapters to every network region as if every region requires equal adjustment. This paper tests that assumption on five architecturally diverse VLAs (OpenVLA-OFT, $π_0$, SmolVLA, DTP, Octo; 93M-7B parameters). Measuring per-region adaptation cost as normalized parameter displacement under region-isolated fine-tuning reveals an adaptation spectrum in which appearance shifts concentrate cost in the vision encoder, instruction shifts in the language backbone, and novel-object shifts in the vision encoder together with the action head, across all five architectures. To exploit this structure, we introduce a pipeline that observes, diagnoses, allocates, and adapts. From ten unlabeled target observations and without fine-tuning, the diagnostic estimates per-region cost by combining reference-free gradient and Monte Carlo Dropout signals with a Centered Kernel Alignment score against a cached source reference; the allocator converts the estimates into variable-rank LoRA adapters under a parameter budget and freezes well-calibrated regions; and standard LoRA fine-tuning trains the resulting adapters. The diagnostic ranks regions within each deployment at a median Spearman of 0.91, and the allocation matches or exceeds uniform LoRA at every budget we tested on LIBERO and CALVIN. On a physical xArm-7, the pipeline matches full fine-tuning under an instruction-wording shift with 0.04% of its trainable parameters, and on five held-out scenes evaluated without retraining it leads every baseline, with 11-23 successes of 30 rollouts against 8-18 for the strongest parameter-efficient baseline at equal or larger budgets and 2-11 for full fine-tuning. These results suggest that adaptation cost in VLAs is structured enough to measure before fine-tuning begins.


## Agent
### Quantifying Overclaiming Propensity in Frontier LLM Agents
**Authors**: Nolan Smyth, Yorguin-Jose Mantilla-Ramos, Pascal Jr Tikeng Notsawo, Saskia Helbling, Alberto Tosato, Mohamed Amine Merzouk, Nouha Dziri, Gauthier Gidel, Tommaso Tosato

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20812v1](https://arxiv.org/pdf/2609.20812v1)

**Abstract**: Frontier coding agents are increasingly trusted to work autonomously for long periods, yet an agent's final response is often the only account of that work a user sees. We quantify the propensity of frontier agents to \emph{overclaim} task completion, a misrepresentation that can mislead the user. An agent overclaims when its final response contradicts information in its context. This definition requires no inference about intent and is independent of task success. We introduce \emph{OverclaimBench}, an evaluation suite composed of five file-review scenarios, transcript-based coverage measurements, and registered planted defects. We evaluate eight proprietary frontier models in their own production command-line interfaces, and four open-weight models under a single fixed harness on OverclaimBench and find that 1) agents do not read all the files they were asked to review in 67.9\% of runs; 2) among runs where not all files are read, agents are \emph{misleading} 80.4\% of the time (59--96\% per model), either falsely claiming to have read all files or omitting that coverage is incomplete; 3) requiring delegation to subagents increased reading coverage, but among reviews that remained incomplete, a large majority were still misleading; and 4) agents that falsely claimed a complete review missed planted defects at about 1.8 times the rate of agents that read every file, showing that claims of completion can conceal substantive failures. Together, these results show that agents' final responses are not reliable accounts of their actions.


### An Empirical Study of Harness Design for Coding Agents
**Authors**: Run-Ze Fan, Zihao Zhang, Simin Ma, Yebowen Hu, Shouju Wang, Kaiqiang Song, Fei Liu, Hamed Zamani, Xiaoyang Wang

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20804v1](https://arxiv.org/pdf/2609.20804v1)

**Abstract**: Coding harnesses shape how autonomous coding agents translate model capabilities into long-horizon software-engineering performance, yet existing work typically evaluates harnesses as monolithic systems, leaving the effectiveness of individual components unclear. To enable component-level comparisons, we study this question with a lightweight coding harness whose execution loop is fixed while three components are varied: planning, action space, and context management. Across four models evaluated on SWE-Bench Verified and Terminal-Bench 2.1, we evaluate 176 matched settings spanning five context-management strategies, four context-window budgets, and targeted ablations of planning and action space. We find that: (1) Context management becomes increasingly valuable as the context-window budget tightens, with most of its benefit coming from preventing context-overflow failures. (2) Staging rule-based elision before LLM-based summarization provides the strongest overall efficiency among the context-management strategies, whereas making elided content recoverable adds machinery that models rarely use and yields no accuracy gain. (3) Planning shifts from an accuracy scaffold for weaker models to a cost saver for stronger models, with little change in accuracy. (4) Predefined tools improve performance for models with weaker bash proficiency, whereas bash-capable models can operate effectively with a bash-only interface and achieve substantially lower cost, especially on command-line-centric tasks. Trajectory-level analysis explains these effects: context management extends execution trajectories without substantially altering agent behavior, planning changes where trajectories stop, and the action space changes the granularity at which code is written. These findings inform model- and budget-aware harness design and provide a modular framework for evaluating future harness components.


### RetireOPD: Self-Retiring On-Policy Distillation for Agentic Reinforcement Learning
**Authors**: Yan Yu, Zhengxi Lu, Yizhou Liu, Yichen Pan, Aozhe Wang, Qipeng Chen, Hua Yang, Wenqi Zhang, Weiming Lu, Qianglong Chen, Yongliang Shen

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20784v1](https://arxiv.org/pdf/2609.20784v1)

**Abstract**: Multi-turn agents trained with reinforcement learning (RL) receive a single scalar reward per trajectory, which motivates self on-policy distillation (OPD) to supply dense token-level supervision from a self-teacher with privileged task skills, letting a skill-free student internalize them. This recipe, however, is undermined by two findings in agentic tasks: privileged information alone does not always make a teacher reliable, and the benefit of teacher supervision is stage-dependent. We therefore propose RetireOPD (Self-Retiring On-Policy Distillation), which first optimizes a decoupled, skill-conditioned teacher with environment rewards and then trains a skill-free student jointly with RL and OPD. Rather than following a predefined distillation schedule, RetireOPD adopts Adaptive Retirement: the student drops the teacher on its own once their discrepancy stops shrinking and it reaches a target fraction of the teacher's success rate, after which training proceeds with RL alone. Across Qwen2.5 models from 1.5B to 7B, RetireOPD improves ALFWorld success rate over RL baseline by 14.1% to 18.8% and WebShop accuracy by 11.8% to 19.0%, and surpasses its own skill-conditioned teacher in every setting.


### Prediction-Powered Smoothing and Validation for Disaggregated AI Evaluation
**Authors**: Sho Kawano, Zehang Richard Li, Paul A. Parker

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20758v1](https://arxiv.org/pdf/2609.20758v1)

**Abstract**: Evaluating an AI system requires disaggregated assessment, as performance varies across domains such as benchmark task types or conversation types in deployed agents. Exhaustive testing is expensive, so evaluation rests on a sample of labeled units. We treat the evaluation set as a finite population and seek accurate point and interval estimates of each domain mean. Direct estimators, including prediction-powered inference (PPI), use only a domain's own labels and are imprecise where labels are few. Small area estimation addresses this problem, and we build on it to develop an integrated workflow for estimation and validation. For estimation, we propose prediction-powered smoothing (PP-S), a Bayesian model fit to each domain's prediction-powered estimate, with an extension that borrows strength across a reporting taxonomy (PP-TS). For validation, we derive a new, approximately unbiased design-based cross-validation score for choosing among direct and smoothed estimators. We study a curated benchmark with verifiable grading and deployed agent traffic graded by humans, each with every outcome observed. In both, the proposed estimators improve on the direct estimators in point and interval estimation, with near-nominal coverage. At the same sampling budget, our score selects as well as an independent validation sample does and estimates the selected estimator's error far more accurately.


### RAFT: A Stateful Retrieval-Augmented Framework for Troubleshooting Agents
**Authors**: Mingxuan Zhang, Xiaowen Wang, Anupma Sharan, Zhengyi Chen, Chenyu Diana Zhang, Shanshan Yang, Chittibabu Pacharu

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20754v1](https://arxiv.org/pdf/2609.20754v1)

**Abstract**: Effective troubleshooting agents in enterprise customer support depend on retrieving actionable guidance from similar historical cases, yet existing retrieval-augmented generation (RAG) systems treat support cases as static documents and overlook their multi-stage, stateful nature. We introduce RAFT (Retrieval-Augmented Framework for Troubleshooting Agents), a stateful RAG framework that abstracts each closed historical case into a directed chain of timeline entries and retrieves at the entry level, surfacing cases whose intermediate states match the active case and returning the parent-case trajectory anchored at the matched state; an optional case-level graph links cases through a configurable similarity representation. We evaluate this retrieval layer directly, which, unlike evaluating a full agent system, requires no production deployment. Because public multi-stage troubleshooting data is extremely rare, we pair a synthetic benchmark built from Microsoft Learn Windows Server documentation with real Apache Jira issues carrying human-created duplicate labels. RAFT improves Case Hit over vanilla RAG and GraphRAG baselines at every stage of case progress, with statistically significant gains over the strongest baseline; the Jira results provide directional evidence that the advantage transfers to real case histories. We release our benchmark, implementation, and the Apache Jira evaluation set.


### Deep Noir: Autonomous Steering Discovery via Architectural Chronometry in Transformer Models
**Authors**: Frank E. Bobe, Gregory D. Vetaw, Darshan W. Bryner, Matthew G. Cook, Jose L. Salas-Vernis

**Published Date**: 2026-09-17

**Updated Date**: 2026-09-17

**PDF Url**: [2609.20722v1](https://arxiv.org/pdf/2609.20722v1)

**Abstract**: Activation steering modifies LLM behavior at inference time, but identifying where and how strongly to steer remains manual. We introduce Deep Noir, a framework that uses Logit Lens convergence and causal head-level attribution to autonomously discover optimal steering parameters. Across three scales (1B x 3, 2-3B x 2, and 7-9B x 4), our engine achieves 16.7 percentage-point improvement on spam at 1B (standard deviation 4.7; 39 runs), with gains increasing to 21 to 42 percentage points at 7-9B across four architectures. On SST-2 sentiment, it achieves a 13.1 percentage-point improvement with zero code changes. Mechanistic grounding enables automated discovery of intervention points that generalize across tasks and architectures. On sentiment, RepE without head masking fails to improve over baseline, while Deep Noir improves all models (p less than 0.01). We further show that steering creates a predictable prompt-injection attack surface whose vulnerability increases monotonically with steering magnitude. This finding is relevant to agent systems deploying steered classifiers.


