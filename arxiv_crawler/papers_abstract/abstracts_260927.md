# Abstracts of Papers

## World Model
### To Trust or Not to Trust: Retrieval-Augmented Fact Checking in Speech
**Authors**: Debajyoti Mazumder,  Mamta, Abhirama Subramanyam Penamakuri

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30227v1](https://arxiv.org/pdf/2609.30227v1)

**Abstract**: Online misinformation increasingly appears in spoken formats such as news clips, podcasts, interviews, political speeches, and social media videos, creating a need for fact-checking systems that can verify claims directly from speech. We introduce VeriSpeak, a probe benchmark for studying speech-based fact verification in Large Audio Language Models (LALMs). VeriSpeak contains 3,879 spoken claims spanning temporal, geographical, and relational facts, with balanced true and false labels. The benchmark is designed to examine whether factual verification ability transfers from text to speech, and whether retrieval-augmented LALMs can use textual evidence to correctly support or refute spoken claims. Our experiments reveal a consistent text-speech modality gap: LALMs that verify written claims reliably often fail on the same claims when spoken. Moreover, retrieval alone provides limited gains because models frequently conflate retrieved evidence with the spoken claim. In contrast, retrieval combined with explicit reasoning improves claim-evidence comparison, with a thinking-tuned LALM reaching 86.1% accuracy. VeriSpeak highlights that effective speech misinformation detection requires not only speech understanding, but also grounded reasoning over retrieved evidence. The dataset is publicly available via Hugging Face at https://huggingface.co/datasets/abhiram4572/VeriSpeak.


### PoEM: Predicting RL Outcomes from Existing Policies
**Authors**: Kimia Hamidieh, Giannis Daras, Antonio Torralba

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30226v1](https://arxiv.org/pdf/2609.30226v1)

**Abstract**: Foundation models are post-trained with reinforcement learning (RL) to maximize specific rewards, such as human alignment, correctness, or instruction following. This post-training process is computationally intensive, sometimes unstable, and has to be run from scratch every time the reward model changes or when we want to combine multiple rewards. We hence ask: given a new reward function, is it possible to predict the RL outcomes without actually running RL on it? We answer this in the affirmative by introducing PoEM, a framework to predict the outputs of RL on a new reward function using a set of models already post-trained on other rewards. First, we show that if the new reward function can be written as a linear combination of existing ones, then the new policy in log-space can be written as a linear combination of the existing log-policies. Surprisingly, even in cases where the rewards are not linearly connected, we observe that often log-policies from RL training span an approximately low-rank subspace across rewards. To our benefit, the weighting coefficients for this combination can be estimated using only the reward or basis policy outputs on the samples. We turn these observations into an algorithm that takes post-trained models and a new reward function, and approximates the target RL policy without actually running any additional RL training. We experimentally validate our approach across synthetic and real rewards, spanning both text and image modalities.


### TrackEverything: Long Horizon Dense Tracking via De-Duplicating 3D Scene Representations
**Authors**: Ayush Jain, Sreeharsha Paruchuri, Ishita Gupta, Fan Zhang, Tanner Schmidt, Jakob Engel, Katerina Fragkiadaki, Adam W. Harley

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30222v1](https://arxiv.org/pdf/2609.30222v1)

**Abstract**: Existing point tracking models face a fundamental tradeoff: they can either track a sparse set of query points over long horizons, or track all points across only short clips. We introduce TrackEverything, a 3D point tracker that breaks this trade-off by representing videos as persistent 3D scene tracks in world coordinates. Grounded in the insight that videos are 2D projections of an underlying 3D world, TrackEverything decouples model complexity from video duration, allowing it to scale with unique physical scene geometry instead. Our approach introduces three key innovations. First, we employ a voxelization-based de-duplication mechanism at sliding-window boundaries to merge co-located tracks, preventing repeated observations of the same surface from redundantly accumulating. Second, we decompose tracking into an endpoint refiner that predicts each point's destination and static-versus-dynamic classification, followed by a lightweight trajectory refiner that decodes dense trajectories exclusively for dynamic points. Third, we propose 3D WAFT, replacing memory-prohibitive 4D correlation volumes with efficient feature sampling in the scene cloud. To the best of our knowledge, TrackEverything is the first 3D tracker capable of tracking all visible points across videos exceeding 1000 frames within 40 GB of GPU memory. On TAPVid-3D, TrackEverything outperforms all open-source all-frame dense 3D trackers by more than 20% APD on short clips, while remaining competitive with state-of-the-art sparse trackers on long sequences, despite tracking far more points.


### WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation
**Authors**: Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30221v1](https://arxiv.org/pdf/2609.30221v1)

**Abstract**: Video generation begins in text space by authoring a cinematic screenplay, then materializes into pixels. As contemporary video generators scale to 30 seconds and faithfully follow complex conditions, the textual prompt largely directs the production, planning how actions, camera trajectories, lighting, and sound unfold across multi-shot sequences. In this paper, we present WanPE, a 397B-parameter prompt enhancement model trained on 1.05M real-world videos to master director-level cinematic planning. WanPE formulates shot-level cinematic plans via video-grounded reverse construction and employs Semantic-Consistency GRPO (SC-GRPO) to faithfully preserve user requirements across shots and over time. To benchmark this capability, we curate WanPEval, a human-annotated testbed covering durations from 5 to 30 seconds across varying intent granularities, supported by approximately 11K blind pairwise assessments. When powering Wan3.0's video generator, WanPE-397B boosts human preference over raw user prompts by 10.66-18.84 points at 5-15 seconds and by a dramatic 50.86 points in the 30-second arena. Ablation studies show that reverse construction demonstrates clear superiority over forward rewriting, while SC-GRPO robustly preserves semantic fidelity across model scales. Ultimately, WanPE leads all evaluated commercial offerings at 5-15 seconds and remains competitive with Seedance 2.5 at 30 seconds.


### A Nearly Quadratic Lower Bound for Linear Optimization over Convex Bodies in the Membership Oracle Model
**Authors**: Santosh S. Vempala

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30215v1](https://arxiv.org/pdf/2609.30215v1)

**Abstract**: We prove nearly quadratic lower bounds for randomized algorithms for linear optimization and uniform sampling over convex bodies in the membership oracle model. For linear optimization, this matches the known nearly quadratic upper bound up to a polylog factor in the dimension. For uniform sampling, this improves on the previous linear lower bound. Our construction also implies the same lower bound for volume estimation.


### ReVAMP: Vector-Accelerated Motion Planning for Kinematically-Constrained Systems via Reparameterization
**Authors**: Shrutheesh R. Iyer, Thomas Cohn, Zachary Kingston

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30213v1](https://arxiv.org/pdf/2609.30213v1)

**Abstract**: Robots often must satisfy one or more constraints during motion planning for real-world tasks. When such constraints reduce the valid configuration space to a measure-zero subset, sampling based planning algorithms require modifications to draw feasible samples. For many common end-effector constraints, parameterizations built on inverse kinematics (IK) provide an alternate formulation where the constraints are satisfied by construction, allowing directly sampling the feasible set. Despite their elegant approach, parameterized planners have remained slower than vector-accelerated implementations of projection-based approaches, leaving their performance ceiling an open question. We explore a new axis of vectorization built upon reparameterizing the planning space through analytic IK. This approach addresses existing inefficiencies in vectorized projection-based planners and exposes new opportunities for parallelism within the planner. We show that the planner can synthesize plans in microseconds to milliseconds for high dimensional systems (up to 20 dimensions), with complex constraints, up to 10x faster than the current state-of-the-art. Furthermore, we demonstrate how such planning speeds open up avenues for restructuring sequential manipulation pipelines.


## Generation
### GridSFM: A Foundation Model for Solving AC Optimal Power Flow
**Authors**: Luke Bhan, Weiwei Yang, Margaret Capetz, Baosen Zhang

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30173v1](https://arxiv.org/pdf/2609.30173v1)

**Abstract**: We introduce GridSFM, a framework that combines a pretrained foundation model across grid topologies with physics-informed fine-tuning for solving AC Optimal Power Flow (AC-OPF) at scale. It is a $15$ million parameter physics-inspired graph neural network pretrained across $54$ topologies of $500$ to $4{,}000$ buses. Our model attains a $2.45\%$ zero-shot generation-cost error on a $10{,}000$ bus case held-out operating conditions with no degradation as system size grows. Building on this, we pair the pretrained backbone with a physics-informed fine-tuning design based on Newton's method for power flow. With only $100$ solved instances, GridSFM adapts to unseen grids up to $10{,}000$ buses. We show it out performs single topology, dedicated neural network models that are trained more data, both in terms of cost and solver iterations when deployed as warm starting points.
  In designing this foundation model, we overcome the fact that the feasible set for AC-OPF can be disconnected. This is an obstruction that prevents any continuous neural network from approximating the solution map. To do so, we lift the problem and relax its constraints with logarithmically penalized slacks. We prove that the resulting elastic feasible set is contractible, that the AC-OPF minimizers remain minimizers of the elastic problem above an explicit penalty threshold, and that projecting an approximate solution back onto the AC-OPF feasible set is well posed. We release all models, data, and code so that the community can build on a shared starting point for AC-OPF.


### Learning and interpreting policies for simultaneous entanglement requests in quantum networks
**Authors**: Leon Rode, Sumeet Khatri, Supartha Podder

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30157v1](https://arxiv.org/pdf/2609.30157v1)

**Abstract**: Future quantum networks will make use of entanglement to perform numerous tasks, such as sending quantum information over long distances, distributed quantum computing, and quantum sensing. In general, these tasks will need to be performed simultaneously in various regions of a network, while minimizing resources and latency. We will thus require policies for scheduling link-level entanglement resources, and using the link-level entanglement to create various forms of multipartite entanglement required for every task. In this work, we address this problem using reinforcement learning. We formulate a Markov Decision Process for the problem and use double deep Q-networks (DQN) with Message Passing Neural Networks (MPNNs), experience replay buffers, and curriculum training to obtain policies. The key physical parameter is the probability of link-level entanglement generation, i.e., the link activation probability. We show that our policies maintain 100% success for up to 71% lower link activation probability than the baseline heuristics for a set of physically relevant network topologies. We then examine an additional constraint where experiment (task) placements are restricted to specific hardware types and demonstrate a similar advantage in performance over heuristics, with our policy maintaining at least an 80% success rate for up to a 59% lower link activation probability. Finally, we explore methods to interpret the learned policy by defining metrics enabling conclusions to be drawn about the model's behavior and by tasking a large language model (LLM) to derive a novel heuristic given example actions taken by the DQN-trained policy. We find that the LLM heuristic performs similarly to the DQN-trained policy in performance, indicating a promising method for interpretable policy extraction for large quantum networks, where direct training becomes computationally expensive.


### EnigmaForge: The Question Is Hidden in the Story
**Authors**: Daniel Eisner

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30144v1](https://arxiv.org/pdf/2609.30144v1)

**Abstract**: Most benchmarks hand the model a question. EnigmaForge hands it a stack of old documents and no question at all. Buried in the letters, receipts, and logbook margins is a small logic puzzle whose solution is unique - proved by a SAT solver at generation time, with an ablation certificate showing every clue is load-bearing. Because instances are generated rather than collected, the corpus renews forever. The headline measure is intuition: task success when handed only the story, with world reconstruction as the secondary axis. Twenty-five frontier models ran over 600 instances (17,400 scored records) under three matched conditions. Intuition reshuffles the leaderboard: a 22x spread where fact recovery spans 1.6x, the second-best fact-recoverer ranks fourteenth, one model is indifferent to being told the question, and another is significantly better without it. Several models were blocked by their own content filters before reaching the puzzle - any benchmark scoring refusals as failure is quietly measuring filter behavior.


### HEXIS: Compiling Skills into Extended Finite State Machines
**Authors**: Minghao LI

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30123v1](https://arxiv.org/pdf/2609.30123v1)

**Abstract**: Agent skills provide reusable knowledge and instructions, yet agents must repeatedly infer how to apply them and which operation should follow. This couples task reasoning with control decisions, allowing prescribed steps to be omitted or applied incorrectly. We introduce HEXIS, which compiles agent skills into extended finite state machines that separate knowledge from control flow. Skill knowledge is incorporated into local instructions that guide reasoning and generation within states. The machine records execution progress and intermediate results, while explicit transition conditions determine subsequent operations. Our incremental compiler first maps skill clauses and tool interfaces to state operations, local instructions, data bindings, and transitions. It then aligns development traces with existing states to identify missing operations and dependencies. These are incorporated by adding or reusing states and refining their connections. Updates are accepted only after static checks and replay of the current and all previously accepted traces. Across four benchmarks and four executors, HEXIS improves success over Skill + ReAct by 16.1 percentage points on average. Qwen3.8-27B reduces execution tokens by 38.4-88.9% across benchmarks.


### R-DEIM Net: An Efficient Rationale-Augmented Dual-Expert Interaction Model for Paraphrase Detection
**Authors**:  Pushp, Vaibhav Prajapati, Himangshu Sarma

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30100v1](https://arxiv.org/pdf/2609.30100v1)

**Abstract**: Recent advances in paraphrase detection reveal a fundamental trade-off: large language models achieve high accuracy but require high computation, while efficient Siamese-BERT variants offer practical scalability with reduced transparency in rationale generation. We present R-DEIM Net, a 76M-parameter dual-expert architecture exploring whether moderate-scale models can achieve competitive accuracy on paraphrase detection while enabling human-readable rationale generation. The architecture combines two specialized components: an Interaction Expert that captures token-level similarity patterns through multi-scale 2D convolutions and attention head allowing variable input length, and a Reasoning Expert that uses a Flan-T5-small decoder to generate rationales as auxiliary supervision. Rather than re-encoding generated text, we extract and pool decoder hidden states as complementary features for classification. On the Quora Question Pairs dataset, R-DEIM Net achieves 90.07\% accuracy and 90.16\% F1-score via 10-fold cross-validation. This represents competitive performance with strong transformer-based baselines (e.g., MFAE BERT: 90.54\% accuracy) and recent large language model based approaches (LLaMA-70B) while using a substantially smaller parameter budget. The model generates rationales alongside predictions, providing potential for auxiliary human-readable descriptions.


### Reachability-Based Formal Verification of Graph Neural Networks with Node and Edge Features
**Authors**: Anne M. Tumlin, Ben Wooding, Zhenxuan Shao, Diego Manzanas Lopez, Tyler Derr, Taylor T. Johnson

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30079v1](https://arxiv.org/pdf/2609.30079v1)

**Abstract**: Graph neural networks (GNNs) have become a prominent approach for developing fast, topology-aware surrogates in electric power systems, supporting tasks such as power flow (PF) analysis, optimal power flow (OPF) estimation, and cascading failure analysis (CFA). Despite this growing use, formally verifying GNN-based models remains challenging, with existing methods limited in scope. We extend the neural network verification (NNV) framework to graph-structured inputs through GraphStar sets, a generalization of Star sets that captures uncertainty over both node and edge features. This extension enables the propagation of linear message-passing operations and the sound approximation of ReLU nonlinearities for GNN architectures, including graph convolutional network (GCN) and graph isomorphism network with edge features (GINE) layers. We evaluate GNNV across three power system tasks, PF, OPF, and CFA, on the IEEE-24, IEEE-39, and IEEE-118 test cases, as well as two standard graph classification benchmarks, ENZYMES and PROTEINS. Our results show that GNNV provides tighter robustness guarantees than CORA on graph classification models with ReLU-based activations and, for the first time, delivers edge-aware robustness guarantees for GINE-based PF and OPF models under joint node and edge perturbations.


## VLA
### BEE: Intervention-Adaptive Real-World Reinforcement Learning with Vision-Language-Action Models
**Authors**: Weihui Zhao, Xiaohan Yan, Zunian Wan, Xuan Du, Zhaozhan Chi, Jianbo Mao, Ruipu Wu, Rushuai Yang, Houlin Li, Shukai Yang, Jing Wu, Yuxiang Yan, Yongcheng Liu, Chuankang Li, Guanghui Ren, Wei Shan, Maoqing Yao

**Published Date**: 2026-09-23

**Updated Date**: 2026-09-23

**PDF Url**: [2609.27450v1](https://arxiv.org/pdf/2609.27450v1)

**Abstract**: Vision-language-action (VLA) models handle long-horizon manipulation, yet success hinges on a few precision-critical phases where millimeter-scale errors undo all prior progress. Online reinforcement learning (RL) can optimize exactly these actions, but free exploration is far too costly on real robots, which makes human corrections indispensable. However, existing online RL methods for VLAs either cannot incorporate such corrections or fold them into undifferentiated supervision. Yet human corrections are not uniformly noisy but reliable along some action dimensions and variable along others. Building on this, we introduce BEE, an intervention-adaptive framework for real-world RL on a frozen VLA that lets the policy go BEyond Expert imitation. We formulate human corrections not as actions to reproduce but as evidence about a constraint: a Correction Model predicts how a human would correct a given VLA proposal and how consistent the correction is along each action dimension. This predicted consistency sets the per-dimension tightness of a constraint on policy optimization. Where corrections are consistent the policy stays close to the human, and where they vary, the constraint relaxes. We evaluate BEE on three real-world manipulation tasks and one LIBERO-Pro simulation task at a matched online-data budget. BEE attains the highest success rate on every task, 91.2% on average against 57.5% for RLT and 42.1% for DSRL, and the lowest human intervention rate on all real-world tasks.


### ActiveArena: Benchmarking and Understanding Active Perception in Robotic Manipulation
**Authors**: Yibo Li, Enshen Zhou, Rui Chen, Yanjun Ding, Mengzhen Liu, Yi Han, Jiabo Zhan, Lipeng Wang, Shanghang Zhang, Lu Sheng

**Published Date**: 2026-09-21

**Updated Date**: 2026-09-23

**PDF Url**: [2609.24124v2](https://arxiv.org/pdf/2609.24124v2)

**Abstract**: Active perception and manipulation are crucial for robots to interact with complex scenes. Existing benchmarks struggle to evaluate how robots effectively acquire and maintain information in memory in an active manner. To this end, we introduce ActiveArena-Sim, an active-perception simulator with controllable viewpoints and large-scale workspaces as the foundation. Built on this, we propose ActiveArena-Bench, which comprises 35 tasks across 5 fine-grained categories, covering visual exploration and interactive information acquisition. Each task is difficult to solve from passive observations alone, requiring multi-round evidence acquisition and memory-based reasoning. The benchmark provides rich memory annotations, standardized training data, and ID/OOD protocols featuring disjoint scenes, unseen distractor configurations, and novel backgrounds. Moreover, we present ActiveArena-VLA, a modular suite of 13 vision-language-action configurations for controlled studies of memory writing, memory capacity, proprioceptive state, subtask supervision, and high-level planning in active perception. Benchmark results reveal a substantial ID-OOD gap: uniform memory sampling, increased memory capacity under reliable write policies, proprioceptive inputs, and subtask supervision improve OOD generalization, while planner-guided memory management and decision-making achieve performance close to the best-performing configuration using only sparse memory.
  ActiveArena thus provides a unified testbed to develop and diagnose models for active perception and manipulation.


### ReVeal: A Reconstruction-Aware Real-to-Sim Framework for VLA Policy Evaluation
**Authors**: Xinyi Wang, Heng Hao, Wenjun Hu, Anna Enyu Li, Dizhi Ma, Karthik Ramani, Hankyu Moon, Yeong-Dae Kwon

**Published Date**: 2026-09-20

**Updated Date**: 2026-09-20

**PDF Url**: [2609.23910v1](https://arxiv.org/pdf/2609.23910v1)

**Abstract**: Simulation-based evaluation provides a scalable and repeatable alternative to real-world evaluation of vision-language-action (VLA) policies. However, reconstruction errors can cause simulated policy performance to diverge from real-world performance, motivating the need to assess reconstructed environments for downstream VLA policy evaluation. We present ReVeal, a real-to-sim assessment framework combining workspace reconstruction, reconstruction-level assessment, and matched closed-loop policy evaluation. Novel-View Mesh Fidelity (NVMF) and Annotated Planar Geometry Fidelity (APGF) assess observation and planar geometric fidelity, respectively. We also develop PGSR-D, a reconstruction pipeline incorporating monocular depth supervision to improve geometry where multi-view visual cues are limited. Across 8 assessment scenes, NVMF and APGF consistently distinguish the fidelity of 2DGS, PGSR, and PGSR-D. Matched evaluations of GR00T, SmolVLA, and pi0.5 across 8 humanoid manipulation tasks show consistent ordering between reconstruction fidelity and real-sim performance agreement across pipelines. Further analysis of the evaluation workspaces shows that higher fidelity is associated with stronger real-sim agreement.


### Beyond Appearance Shifts: Task-Semantic Action Calibration for VLA Models
**Authors**: Shuaijun Liu, Feiyang You, Chengyu Wu, Shuyang Hao, Chenglong Zhang, Jingyao Cai, Xingwei Chen, Ningxin Su

**Published Date**: 2026-09-20

**Updated Date**: 2026-09-20

**PDF Url**: [2609.23650v1](https://arxiv.org/pdf/2609.23650v1)

**Abstract**: Vision-language-action (VLA) models have achieved strong performance in embodied manipulation, but still lack a clear mechanism to balance behavioral stability with task-semantic sensitivity. We identify two complementary failure modes. Under task-preserving changes, where task semantics remain unchanged but scene appearance varies (e.g., style, illumination, clutter, or paraphrasing), policies often exhibit unnecessary action drift. Conversely, under semantic-breaking changes, where key task semantics such as the target object or constraint are altered, policies frequently fail to produce sufficiently distinct behaviors and instead follow the original trajectory. To address this gap, we propose BAS-VLA, a task-semantic action calibration framework built on top of a frozen base VLA. BAS-VLA adopts a breaking-centered calibration core as the default path, and introduces a selective evidence-gated preserving auxiliary that activates only when nuisance variation is detected while task semantics remain consistent. On the OpenPI-pi0.5 / LIBERO-Object Milk-Swap benchmark, BAS-VLA maintains high success on clean (98.0%) and semantics-preserving conditions (97.5%), while reducing clean-criterion success to 0.0% under deliberate target-object swaps, demonstrating strong stale-task suppression and task-semantic separation. On validated style-preserving shifts, it improves success from 42% to 70% without degrading clean performance. These results highlight that reliable VLA behavior requires moving beyond appearance robustness toward explicit task-semantic action calibration.


### MaskVLA: Visual Masking Against Trajectory Overfitting of Vision-Language-Action Model
**Authors**: Yuxuan Jiang, Jiaying Huang, Ge Wang, Shenhao Yan, Jiahao Yang, Chengsi Yao, Qi Liu, Qing Zhao, Shuguang Cui, Yiming Zhao, Yatong Han, Zhen Li

**Published Date**: 2026-09-20

**Updated Date**: 2026-09-20

**PDF Url**: [2609.23565v1](https://arxiv.org/pdf/2609.23565v1)

**Abstract**: Vision-Language-Action (VLA) models integrate vision-language understanding with executable robot actions, enabling end-to-end learning for robot control. However, our empirical analysis reveals that existing models exhibit severe trajectory overfitting when finetuned on limited datasets. To guide the model in effectively utilizing wrist camera information, we propose MaskVLA, a masking-based fine-tuning strategy. By randomly masking a small portion of the main camera's visual information, the model is guided to autonomously learn more fine-grained, task-relevant, and effective visual features. This process leads to the emergence of robust policies, thereby enhancing the model's capability to tackle complex manipulation tasks and improving its generalization performance. Our method has been comprehensively evaluated on RoboTwin 2.0, achieving an average success rate improvement of 23.2% and 16.8% compared to $π_0$ and OpenVLA-OFT, respectively. Furthermore, experiments on real-world ALOHA robots also demonstrate the effectiveness of our approach.


### Anatomy of a Closed-Loop Collapse: A Causal Case Study of a Compressed VLA Policy
**Authors**: Fengze Jia

**Published Date**: 2026-09-19

**Updated Date**: 2026-09-19

**PDF Url**: [2609.23048v1](https://arxiv.org/pdf/2609.23048v1)

**Abstract**: Compressed manipulation policies can pass offline evaluation while failing in closed-loop execution; this dissociation is established in prior work and is not our claim. We contribute a causal anatomy of one naturally occurring case. An 8-layer distillation of Octo-Base retains 86% of parameters, passes every offline check we applied (0.996 and 1.000 teacher-ratios on the family's own validation metrics), and collapses in closed loop: 0/72 vs. the teacher's 40/72 on a simulated WidowX pick-and-place task. The collapse is structured, not diffuse: early task stages degrade gradually (the student moves the object at 90% of the teacher's rate and grasps at 55%), while transport-to-target fails categorically, at 0% in every training variant. Paired action-trace forensics isolate the signature: a negative, late-heavy $z$ residual, roughly 10x its post-repair magnitude, and persistent across the base distillation and both continuation branches. Four standard therapies fail under matched controls: continued training and in-domain offline data leave success at zero, even though the latter measurably improves marginal action statistics; command-level compensation recovers nothing at any offset, although the same perturbations degrade healthy policies; clamping the symptom in the command channel preserves grasping, yet success stays at floor. A minimal-pair intervention that substitutes half of the training stream with deployment-distribution teacher rollouts, with every other setting held fixed, restores parity with the teacher (18/36 vs. 17/36 held-out), eliminates that signature, and recovers a teacher-like perturbation-response profile. We claim existence, not universality. Operationally, offline gates, including a family's own validation metrics, are insufficient acceptance tests for compressed policies; a few dozen closed-loop trials sufficed to find what they missed.


## Agent
### KernelOPT: Dispatch-Aware Agentic Search for GPU Kernel Optimization
**Authors**: Aheli Poddar, Sanskar Prasad, Arindam Samanta, Subha Chakraborty, Vishal Goyal, Rohit Singh Rathaur

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30059v1](https://arxiv.org/pdf/2609.30059v1)

**Abstract**: Deep learning inference and training performance depends critically on GPU kernel efficiency. Modern compilers such as PyTorch Inductor automatically generate GPU kernels from high-level model code, but frequently underperform expert-written implementations by wide margins. Recent LLM-assisted kernel optimizers can close this gap for standalone kernels, yet treat compiled models as black boxes, generally optimizing individual standalone kernels without respecting the compiler's structural decisions or verifying the model end-to-end. We present KernelOPT, a multi-agent system that treats compiled models as structured artifacts. It preserves vendor library calls (cuBLAS, cuDNN) and exclusively targets generated Triton sub-kernels using five profiling-guided LLM agents. A four-gate verification cascade of static validation, multi-seed correctness, model-level float64-fallback verification, and performance gating filters candidates during optimization and verifies the re-stitched model end-to-end. If no candidate passes all four gates, the system preserves the compiler baseline. The system accepts PyTorch nn.Modules, standalone Triton kernels, and Helion kernels. Evaluated on 250 KernelBench problems, KernelOPT achieves geometric mean speedups over \texttt{torch.compile} of 1.40$\times$ (Level 1: 51/100), 1.15$\times$ (Level 2: 31/100), and 1.07$\times$ (Level 3: 12/50) across all problems.


### Era by Eon: Benchmarking Enterprise Agents on Hidden Knowledge
**Authors**: Benjamin Gruenbaum, Doron Porat, Assaf Natanzon, Roy Zavida, Chen Dinachi, Or Itzahary

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30055v1](https://arxiv.org/pdf/2609.30055v1)

**Abstract**: In the Era by Eon benchmark, each question states the rules for its answer, and code computes the answer from a generated company's data. When agents can run code, the four strongest models each answer 22 to 25 of 27 such questions, so the benchmark barely separates them.
  We add eight question templates that depend on hidden facts. No question or document states a hidden fact, and the records that seem to hold it show something else. Other data implies it. For example, the sales system says a customer dropped a purchase because of timing. On a recorded call, the customer blames an outage.
  For each generated company, code fills each template and computes an exact answer without a language model. We evaluate 12 agents. Each pairs a model with an agent program, which connects it to the company's systems.
  The best agent answers 18 of its 24 attempts, three per question, correctly. Four of the six models answer at most 6 of 24 with any program. The hardest questions require picking one of several similar records, such as which of three renewal offers a customer signed. All agents together answered two such questions correctly in only 1 of 84 attempts.


### How does Adversarial Influence Scale in Multi-Agent Systems?
**Authors**: Addison J. Wu, Jasin Cekinmez, Michel Liao, Karthik Narasimhan, Thomas L. Griffiths

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30028v1](https://arxiv.org/pdf/2609.30028v1)

**Abstract**: Multi-agent deliberation can improve performance, but what happens when some agents do not act in good faith? In practice, an agent may be deceptive and work to subvert the group, whether through its own objectives or external instruction. We study how susceptibility to deception scales as groups increase in size and deceivers become more prevalent. It is not the number of agents in the group that matters, but the proportion of deceivers. We observe that the defection rate, how often initially correct agents switch to an incorrect final answer, rises linearly with this proportion. Whereas humans in comparable conformity studies are reliably swayed only when misleading confederates form a majority, LLM agents defect regularly even when deceivers remain a minority. Susceptibility also depends on which models are interacting, especially on the honest agent side. Unexpectedly, allowing deceivers to coordinate privately can make them less effective. Altogether, our results show that adding more agents is therefore not a sufficient defense, because the adversary can simply scale with the group.


### Low-Cost Assays for Measuring Model Behavior Across Vendors and Releases
**Authors**: Tapan Parikh

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30012v1](https://arxiv.org/pdf/2609.30012v1)

**Abstract**: Language models advise people, keep them company, and write software while they sleep. Measuring what they do is hard: behavior has to be sampled repeatedly across models, prompts and releases, most of it lives in unstructured text that has to be coded before it can be counted, and the result has to be legible and rigorous enough to meaningfully compare models and vendors. To address these constraints, we present a simple, cheap, scalable, and replicable model for studying model behavior. Each study is a frozen, public stimulus run identically on a cross-vendor panel, at a few dollars per model or less. Each reads its transcripts one of three ways, chosen by how much interpretation the behavior needs: exact match on a clamped reply, a codebook applied by LLM judges whose agreement with a human coder is reported per code, and an instrumented environment that records what an agent did independently of what it said. Run across four years of model releases from both frontier and open-source labs, these instruments find four things. Convergence: asked to pick a word, 27 of 44 models answer serendipity at least once in four tries. Resistance: a trailing "right?" moves endorsement by up to 32 points, and the sign flips from sycophantic to resistant as generations advance, keyed to the tag's surface form. House: whether a model holds a position under pressure tracks its generation, and how it holds tracks the lab that built it. Account: told to do something the documentation in their repository contradicts, some coding agents never went along silently and others always did, and the same model can change with the harness it runs in. Re-run on every release, batteries like these track how behavior is changing across vendors and over time.


### Advancing Model Research in AgentX: Long-Horizon Autonomy for Industrial Recommender Systems
**Authors**: Shuang Yang, Zijie Zhuang, Changxin Lao, Pengbo Xu, Hanwen Xu, Yusheng Huang, Han Gao, Guanchen Wang, Tianbao Ma, Linxun Chen, Peilin Song, Xuming Wang, Chen Li, Fan Wu, Tao Wang, Zibo Zhao, Xiangyu Wu, An Liu, Fei Pan, Peng Jiang, Chen Yang, Zhaojie Liu, Wenwu Ou

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30001v1](https://arxiv.org/pdf/2609.30001v1)

**Abstract**: Sustaining industrial recommendation research requires using the results of one experiment to decide what to investigate next. We present AgentX-Model, the next generation of AgentX's model research framework, which connects proposal development and model experimentation within sandboxes defined by business inputs and prediction tasks. AgentX-Model adopts a dual-agent architecture comprising a Research Agent and a Model Agent. The Research Agent develops independently reviewed proposals from papers and experimental findings, while the Model Agent conducts multi-round investigations and returns code, measurements, and unresolved questions. Using the returned results, the Research Agent selects a starting implementation and formulates the next research question, allowing subsequent experiments to build on earlier findings. We organize this continuing research around four actions: Reproduce, Follow-up, Composition, and Diagnose. The first three actions drive routine research, while Diagnose acquires the evidence needed to choose a repair, including for issues raised by business feedback and online evaluation, such as prediction bias measured by PCOC. Across the production evaluation, 560 of 636 completed model-changing experiments recorded AUC above their business baselines. As research continued, some experiments recorded AUC above every comparable ancestor in their lineages. The five latest online A/B evaluations across different business settings reported gains including 10-15% in acquisition efficiency, 15-20% in target-segment advertising spend, and 0.3-0.8% in watch time; the watch-time model used approximately 10% fewer FLOPs and parameters. A dependency-aware historical-replay benchmark further evaluates research allocation, with initial results showing no consistent efficiency gain from more complex scheduling when agents already analyze and select concrete candidates.


### Multi-Dimensional Matching
**Authors**: Irene Aldridge

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.29958v1](https://arxiv.org/pdf/2609.29958v1)

**Abstract**: We study a matching mechanism where agents and objects are described by features rather than complete rankings. A single spectral projection reduces the problem to a one-dimensional sort, computable in O(N log N) time. We prove that on descaled features and preferences, our algorithm obtains the exact Nash Social Welfare (NSW) optimum within the projected space, with an unconditional utilitarian-welfare guarantee and a conditional NSW guarantee. The proposed mechanism is stable against exogenous noise but not strategy-proof; we provide an explicit profitable misreport. On an agentic AI shopping application, the diagnostics correctly anticipate both a success and a failure case. A 100-instance robustness study confirms the findings.


