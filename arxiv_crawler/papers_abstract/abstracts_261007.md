# Abstracts of Papers

## World Model
### World Models' Last Exam in Physics
**Authors**: Mingju Gao, Qingle Liu, Yuzhao Peng, Xinjie Lin, Ziming Qin, Zheng Jiang, Wenyi Li, Calvin Xiao, Youjie Zheng, Kaisen Yang, Qinhuai Na

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08791v1](https://arxiv.org/pdf/2610.08791v1)

**Abstract**: Video world models can produce visually convincing yet physically inconsistent sequences, raising concerns about their reliability for prediction and planning in embodied AI systems. Existing evaluations often rely on model-based judgments or reference videos, while direct physical tests largely focus on mechanics. We introduce World Models' Last Exam in Physics, a measurement-based benchmark for evaluating physical consistency in video world models. The benchmark comprises 40 controlled tasks spanning mechanics, optics, fluids, thermal and phase-change phenomena, electromagnetism, and surface tension. Each task pairs an initial image and a generation prompt with predefined physical criteria, enabling interpretable tests of observable physical relationships without requiring reference videos. Its evaluator combines task-observability screening with task-specific quantitative physical measurements. Experiments on eight video generation models across 1,280 videos reveal persistent physical inconsistencies and substantial variation across tasks, with the best model achieving an overall score of 57.76 out of 100. Evaluation on synthetic videos with known physical relationships provides evidence for the validity of the measurement module under controlled conditions. The evaluator also achieves higher agreement with human judgments than a direct vision-language model baseline in both within-task rankings and pairwise comparisons. By combining coverage across physical domains with scores grounded in measurable evidence and explicit measurement limitations, the benchmark provides an interpretable basis for diagnosing physical inconsistencies and tracking progress toward physically consistent video world models.


### Conformal Prediction Sets Quantify Information Gain: A Theoretical Perspective
**Authors**: Kevin Zhang, Stephen Bates

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08785v1](https://arxiv.org/pdf/2610.08785v1)

**Abstract**: Conformal prediction is a popular tool for uncertainty quantification that outputs prediction sets with finite-sample coverage guarantees. While prediction set size is commonly used as a heuristic measure of uncertainty, the information-theoretic basis for this interpretation remains poorly understood. In this work, we provide such a foundation using a decision-theoretic generalization of entropy tailored to set-valued prediction. In particular, we introduce a family of generalized information measures based on the size and coverage of conformal prediction sets. Notably, Shannon mutual information admits an exact integral representation in terms of these measures. We then show that, in standard classification settings, the reduction in conformal set size from additional information (i) is sandwiched between calibration-dependent members of this family and (ii) obeys a data processing inequality, both up to finite-sample calibration and model error terms. Together, our results formally relate conformal prediction to classical information-theoretic quantities and justify using set-size reduction as an information gain metric. Empirically, we validate our theory across 11 classification settings and show that set-size reduction and Shannon mutual information can rank features differently in a greedy feature selection experiment.


### PEARS: Physical-Prior-Guided Efficient Adaptation via Failure Reasoning and Diffusion Steering for Tactile Manipulation
**Authors**: Kun Song, Yiming Wang, Yilin Chen, Tianyi Ding, Jiaxin Tian, Tianqi Gong, Daolin Ma, Jia Pan

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08784v1](https://arxiv.org/pdf/2610.08784v1)

**Abstract**: Pretrained robotic policies can suffer substantial performance degradation under out-of-distribution (OOD) conditions encountered during deployment, motivating post-training through real-world interaction. However, reinforcement-learning (RL)-based post-training typically requires substantial environment interactions, a burden that is especially significant in manipulation, where each trial can be slow, costly, or destructive. Therefore, we present PEARS, a physics-prior-guided hybrid RL framework for sample-efficient online adaptation of pretrained policies with tactile feedback. After each episode, its physics-guided force reasoning (PFR) module uses physical priors encoded in a vision-language model (VLM) to diagnose failures from the visual outcome and tactile interaction history and update task-appropriate contact-force bounds. A high-frequency hybrid force-position controller then enforces these bounds during contact. Complementarily, tactile-conditioned diffusion steering reinforcement learning adjusts the latent noise of the frozen flow-matching policy to correct errors in free-space motion and contact timing without updating the base model. In simulation, PEARS improves success rates by 12.4-37.4 percentage points over the strongest per-task baselines. PEARS also reduces the number of interaction episodes required for a certain success threshold by up to 53.2% relative to the fastest baseline. In real-world experiments, PEARS achieves success rates of 95% on Whiteboard Erasing and 90% on Pipette Liquid Aspiration. These results show that combining the PFR module with policy steering can accelerate adaptation while reducing costly interactions. The project website is available at https://song-kun.github.io/pears.


### 4D-HOF: Hand-Object Flow Matching for Feed-Forward 4D Interaction Reconstruction
**Authors**: Shiqi Li, Sean Cho, Yijie Li, Fengzhi Guo, Bowen Wen, Cheng Zhang

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08782v1](https://arxiv.org/pdf/2610.08782v1)

**Abstract**: Existing methods for 4D hand-object reconstruction often rely on costly per-sequence optimization, while generative approaches typically synthesize interactions from random noise, which can lead to unstable interaction prediction. We introduce 4D-HOF, a feed-forward framework that reconstructs 4D hand-object interactions from coarse but informative estimates produced by vision foundation models. Concretely, we learn a conditional flow matching model that transports foundation-model-derived hand-object states toward an interaction manifold, allowing the model to correct errors in translation, rotation, and alignment in a feed-forward manner. A key advantage of our generative formulation is that it naturally enables test-time guidance within the transport process. Rather than applying a separate post-hoc optimization after reconstruction, we directly steer the evolving generative states using physical interaction constraints and observed 2D evidence, allowing the reconstruction to be refined as part of the generative process itself. By training the generative model on diverse datasets, 4D-HOF generalizes robustly to challenging in-the-wild scenarios. Experiments on out-of-domain benchmarks show that 4D-HOF achieves state-of-the-art performance, producing more stable and accurate 4D hand-object reconstructions.


### IdeaAnchor: Teaching LLMs to Turn Literature into Research Ideas
**Authors**: Ziyu Chen, Yilun Zhao, Jiashuo Sun, Yiling Ma, Manasi Patwardhan, Arman Cohan

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08781v1](https://arxiv.org/pdf/2610.08781v1)

**Abstract**: Scientific research often begins by synthesizing ideas from a set of related papers to identify gaps and formulate new directions. However, training language models to perform this form of literature-grounded ideation remains challenging, as existing approaches based on prompting or feedback lack structured supervision for how papers should be synthesized. We introduce IdeaAnchor, a paradigm for training LLMs to perform research ideation using structured specifications as privileged signals. Each IdeaAnchor instance encodes how each input paper should be synthesized into a successful idea, including their functional roles, relationships, and target synthesis criteria. We build this paradigm by mining instances from published papers, capturing how real ideas emerge from prior literature. We then train models via demonstration, self-distillation, and reinforcement learning, and further enhance generation with retrieval at inference time. Experiments show consistent improvements in ideation quality. Our analysis reveals a functional decomposition: anchor-based training strengthens creative synthesis, retrieval enhances detail elaboration, and combining both yields the best performance.


### DepthWorld: 3D World Model for Robot Manipulation
**Authors**: Jai Bardhan, Josef Sivic, Vladimir Petrik

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08780v1](https://arxiv.org/pdf/2610.08780v1)

**Abstract**: World models offer a data-driven alternative to traditional simulators for robotics, with applications spanning policy evaluation, improvement, and planning. All of these uses depend on faithful 3D geometry, yet current video-based world models are trained on RGB alone and produce rollouts that look correct frame-by-frame but do not compose into a consistent 3D world. Closing this gap requires progress on two fronts: large-scale 3D supervision for manipulation, and an architecture that can absorb it without disturbing strong pretrained video priors. We introduce a calibration pipeline that combines learned stereo depth with a joint factor graph, pooling all episodes collected from the same physical robot to recover its shared kinematic parameters alongside per-scene extrinsics. Applied to the DROID dataset, this yields DROID-3D, a calibrated 3D dataset providing dense metric depth and recalibrated multi-view extrinsics (achieving <0.7 px reprojection error on 90% of episodes for external cameras). We then train DepthWorld, a Stable Video Diffusion-based world model that jointly predicts multi-view RGB and depth via spatial latent tiling, leaving the pretrained Variational Autoencoder (VAE) unchanged. Depth supervision improves RGB prediction itself by +1.48 dB PSNR over an identical RGB-only baseline at equal training budget, while simultaneously yielding accurate metric depth for downstream geometric reasoning.


## Generation
### Agent in a Bottle: Can LLM Agents Turn Their Capabilities Into Cheap, Scalable Artifacts?
**Authors**: Ankit Sonthalia, Haritz Puerto, Alexander Rubinstein, Martin Gubri, Seong Joon Oh

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08775v1](https://arxiv.org/pdf/2610.08775v1)

**Abstract**: Large language models (LLMs) can solve many narrow tasks, but querying them separately for millions of related instances can be prohibitively expensive. Can LLM agents autonomously create cheaper solutions for such workloads? We call this ability "bottling": the ability to turn general capabilities into task-specific solutions that balance answer quality and amortised cost. We introduce BOTTLED, a benchmark in which agents receive an entire unlabelled workload and must complete it under fixed time, compute and LLM API budgets. Agents choose their own approach, such as training a small model or writing a reusable program. Across ten models and three tasks, we find that strong zero-shot task performance does not reliably translate into strong bottling capabilities. Models with similar zero-shot scores can differ substantially after bottling, and 48 of 60 bottling runs score below the lower bound of the 95% confidence interval of their model's zero-shot performance. Moreover, 31 of 60 runs underperform the stronger of two small-model distillation baselines with the same token budget. Nevertheless, bottling can yield substantial savings: on query-product relevance classification, Opus 5 retains about 82% of its zero-shot macro-F1 at roughly 657 times lower reported cost. Bottling is also competitive with Jev, a "system one" model built especially for cheap, repetitive inference: Opus 5 on the same task recovers about 94% of Jev's macro-F1 at a quarter of Jev's projected full-workload cost. BOTTLED provides a basis for evaluating and improving agents' ability to invest limited resources in reusable solutions for large, repetitive workloads.


### WorldSonus: Bringing Sound to Worlds
**Authors**: Pengjun Fang, Jingyi Fa, Kam Man Wu, Jiaming Wang, Haoyuan Huang, Yaguang Wu, Xiangjun Huang, Ziyang Ma, Weijia Chen, Hongyu Liu, Zeyue Tian, Qifeng Chen

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08760v1](https://arxiv.org/pdf/2610.08760v1)

**Abstract**: Recent advances in world models have enabled increasingly realistic visual synthesis. However, these generated environments remain largely silent. Bringing sound to world models poses three core challenges: real-time generation to keep pace with interactive video streams, interactive control to respond to mid-stream sound instructions, and spatially aligned stereo to reflect scene geometry and camera motion. To address these demands, we introduce WorldSonus, an interactive video-to-audio framework designed for real-time spatial sound synthesis in world models. For real-time generation, WorldSonus employs a streaming causal autoregressive diffusion architecture that synthesizes audio chunks at a low real-time factor (RTF) of 0.41. For interactive control, we incorporate an audio-centric captioning pipeline with chunk-indexed prompt scheduling, enabling dynamic manipulation of sound events during generation. For spatial alignment, we leverage high-quality stereo supervision curated from diverse stereo and ambisonic data. Extensive experiments demonstrate that while tailored for world models, WorldSonus generalizes effectively to open-domain video-to-audio benchmarks, matching or outperforming state-of-the-art bidirectional models in both acoustic quality and spatial alignment. Project page: https://noizai.github.io/WorldSonus/


### Linear Bandits under Exact Sliding-Window Constraints
**Authors**: Seyed Mohammad Hadi Hosseini, Yasin Abbasi-Yadkori, Sattar Vakili

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08745v1](https://arxiv.org/pdf/2610.08745v1)

**Abstract**: We study linear bandits under exact sliding-window constraints, where every consecutive block of actions must belong to a prescribed feasible set. In the offline setting, where the reward function is known, we show that convexity and cyclic-shift invariance make a stationary solution optimal when $w\mid T$ and within an additive $O(w)$ gap otherwise. In the online setting, we show that geometric structure alone is insufficient for learning, and sublinear regret can be impossible. We introduce a transition diameter $τ$ that quantifies feasible reachability and develop a rare-switching OFUL algorithm with regret $\widetilde{O}(d\sqrt{T}+τd+w)$ against the offline-optimal feasible trajectory. Finally, we remove cyclic invariance and consider general sliding-window constraints, where optimal behavior may be non-stationary. We represent recent action history as the state of a finite-memory control problem and introduce a history-state diameter $D$ that measures feasible communication between viable histories. Combining optimistic remaining-horizon planning with rare policy updates, we obtain a regret bound of $\widetilde{O}(d\sqrt{T}+dD+w)$. We evaluate our approach on real-world and synthetic benchmarks, showing that it maintains exact feasibility while achieving reward and regret comparable to baselines with substantially fewer policy updates.


### On the Computational Tractability of Robust Bandits
**Authors**: Vanessa Kosoy, Vinayak Pathak

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08740v1](https://arxiv.org/pdf/2610.08740v1)

**Abstract**: Learning when the environment does not belong to the learner's hypothesis class is typically handled using agnostic learning guarantees. However, for anything beyond supervised learning, agnostic guarantees are difficult to come by. Recently, imprecise bandits (Kosoy, 2025) (later renamed to robust bandits in Appel and Kosoy, 2025) were introduced as another approach to unrealizable learning in the bandits setting and a $Θ(\sqrt{T})$ regret learner was shown for a large class. However, no computational guarantees were provided. In this paper we identify a special case that admits a polynomial-time learner with $\tilde{O}(\sqrt{T})$ regret. We also show that several small generalizations of this special case are NP-hard thus indicating that the special case is at the boundary of what is tractable. It has been recently suggested (Kosoy, 2018) that computationally efficient learners for unrealizable learning problems are crucial for solving the AI alignment problem. This work is a small step in that direction.


### Denoising Hierarchical Representations: Joint Continuous Diffusion for Language Modeling
**Authors**: Mathias Ollu, Nikos Komodakis

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08738v1](https://arxiv.org/pdf/2610.08738v1)

**Abstract**: Diffusion Language Models (DLMs) hold the promise of order-agnostic, parallel text generation. Recently, continuous diffusion and flow matching models have seen substantial gains, driven by carefully crafted token representations and diffusion/flow spaces. In this work, we introduce Hierarchical Continuous Diffusion Language Models (H-CDLMs), a simple framework that further improves continuous DLMs with minimal compute and parameter overhead. Drawing on the discrete DLM and continuous image diffusion literature on joint diffusion, we diffuse multiple modalities in parallel. These modalities represent tokens at different semantic granularities: in our instantiation, the tokens themselves and coarser clusters obtained by clustering pretrained token embeddings. We propose a general setup that allows per-modality samplers and schedules to enhance the interplay between modalities. Applied to CoBit, this yields H-CoBit, which delivers large empirical gains across benchmarks. At dataset entropy, H-CoBit improves MAUVE and reaches a generative perplexity (GenPPL) of 49.4 on LM1B and 50.4 on OWT, improving on the baseline by 24.2 and 20.7 points and surpassing even discrete DLMs of comparable size. On GSM8K, it reaches 27.4% accuracy, outperforming prior continuous diffusion and flow-based models. We further apply H-CDLM to the flow matching model FLM, obtaining consistent gains with H-FLM and demonstrating that the framework generalizes across continuous generative paradigms. Our code will be made publicly available at https://github.com/matol-16/HCDLM.git .


### WorldSolver: Can LLM Agents Simulate the Physical Dynamics via Solver Generation?
**Authors**: Siru Jiang, Yongzhe Lyu, Shuo Lu, Yubin Wang, Yuxiang Zhang, Yue Liao, Bin Wang, Jian Liang, Tieniu Tan

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08720v1](https://arxiv.org/pdf/2610.08720v1)

**Abstract**: LLM-based agents are increasingly advancing scientific and engineering problem solving, with physics simulation emerging as a challenging yet practical testbed for reproducing complex physical phenomena with application in embodied AI, games and films. As the workhorse of such simulation, a solver computes how the state of a dynamic system evolves over time. Building such solvers requires physical understanding to identify appropriate models, mathematical reasoning to formulate the underlying dynamics, and software engineering to implement them as executable code, yet this capability of LLM agents remains underexplored. To this end, we introduce WorldSolver, a benchmark of 168 simulation tasks derived from physical phenomena in 61 classic computer graphics papers, spanning 7 physical domains. Each task contains a code scaffold that provides a fixed simulation environment for the scene, with the solver implementation left for the agent to complete. Specifically, we evaluate them along three dimensions: Execution Checks for successful execution, Visual Fidelity for reproducing the intended dynamic behavior in the rendered simulation, and Physical Plausibility for physics-grounded verification of the generated dynamics. Experiments on frontier agents reveal that producing executable solvers is difficult itself, and satisfying visual and physical correctness is even harder. GPT-5.6-Sol and Claude-Opus-5 perform comparatively better than the other evaluated agents, yet achieve overall scores of only 48.7% and 46.7%, respectively. WorldSolver is an early step toward agentic solver generation, and we hope it helps drive progress toward agents that can faithfully simulate the dynamic physical world. Code is available at https://github.com/sirujiang/WorldSolver.


## VLA
### EgoLAP: Learning from Egocentric Human Data through Language-Action Reasoning
**Authors**: Lihan Zha, Shresth Grover, Tenny Yin, Samuel M. Bateman, Hengkai Pan, Mengchao Zhang, Aykut Onol, Allen Z. Ren, Dhruv Shah, Anirudha Majumdar

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08726v1](https://arxiv.org/pdf/2610.08726v1)

**Abstract**: Egocentric human data offer a path to scaling robot learning beyond costly robot demonstrations, yet the embodiment gap makes raw human trajectories a poor supervisory target for control. Our key insight is that, although low-level actions are embodiment-specific, their underlying motion intent can capture task-relevant structure that transfers across humans and robots. We introduce EgoLAP, a VLA pre-training framework that jointly learns from human and robot trajectories through a shared language-based action chain-of-thought. EgoLAP expresses motion intent as structured, temporally abstracted language actions and pairs them with motion-level reasoning grounded in scene geometry, physics, and object affordances. Across extensive real-world and simulated experiments, EgoLAP transfers human experience to robot control more effectively than alternative action representations and reaches 80.1% mean real-world task progress, a 2.3x performance gain over alternative action representations. Motion-level reasoning also outperforms a composite reasoning format that combines subtask, object-box, and visual-trace reasoning.


### VOMMI: Collecting and Leveraging Portable Demonstrations for Mobile Manipulation
**Authors**: Yutian Zhang, Xingrui Xiong, Siyuan Ma, Yang Li, Jiawen Wen, Jiaqi Zhai, Liwen Yang, Ce Hao, Haozhen Chi, Yangkun Zhu, Yifan Zhu, Xiaowen Chu, Dong Wei, Qiaojun Yu, Dibo Hou

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08220v1](https://arxiv.org/pdf/2610.08220v1)

**Abstract**: Portable mobile-manipulation demonstrations can help alleviate data scarcity for embodied intelligence, but obtaining reliable, low-cost, and robot-free motion supervision from RGB observations remains challenging. Existing approaches often rely on teleoperation or specialized devices equipped with additional sensing hardware, while directly using estimated visual odometry (VO) trajectories can introduce inconsistencies due to accumulated drift and imperfect motion supervision. We present the Visual-Odometry-Conditioned Mobile Manipulation Interface (VOMMI), a portable demonstration collection and learning framework that connects portable RGB demonstrations to vision-language-action (VLA) post-training through offline trajectory reconstruction and online visual-motion conditioning. VOMMI synchronizes body and hand views to capture navigation context and local object interactions without requiring human-robot kinematic correspondence calibration. R2-VO refines offline demonstration trajectories using sparse geometric anchors and produces causal local-motion tokens over multiple prediction horizons for online policy conditioning. An action-group residual adapter incorporates these tokens only into the base branch. Experiments use a 500-trajectory portable for each task, with 75 trajectories held out for RGB-VO evaluation, and 200 robot demonstrations as references. Our policy, post-trained only on portable demonstrations, achieves 18.2% lower base-velocity error than a policy trained with robot-collected demonstrations, while maintaining comparable end-effector translation accuracy. Offline reconstruction reduces absolute trajectory errors for the body and hand streams by 24.6% on average relative to the best evaluated baseline for each stream. The complete system improves the mean success rate by 8.3 percentage points over OpenPI 0.5 across three real-robot tasks.


### Adapting Vision-Language-Action Models to Unknown Visual Disruptions During Execution
**Authors**: Ahin Lee, Jinwoo Seo, Youngsoo Jang, Taesik Gong

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.07946v1](https://arxiv.org/pdf/2610.07946v1)

**Abstract**: Visual disruptions can arise while a robot is executing a task, leaving a vision-language-action (VLA) policy to respond without knowing the disruption type or timing. We introduce Self-supervised Adaptation from Leftover Trajectories (SALT), which uses the leftover trajectory, the unexecuted part of the previous action chunk, as self-supervision for test-time adaptation. Because consecutive chunks overlap in time, the leftover provides a temporally aligned target for the current prediction over the same future control interval. At the onset of a visual shift, the leftover can retain a plan formed before the corruption, so updating the policy toward it anchors the adaptation across the shift (Transition Anchoring). SALT keeps the adapted policy and regenerates the current chunk, whose leftover becomes the target at the next replan, carrying the correction forward along the execution trajectory (Sequential Correction Propagation). Supervision comes entirely from the policy's own predictions, requiring no disruption annotations, expert actions, or target-domain demonstrations, and a lightweight adaptation gate calibrated only on nominal trajectories decides when updates begin. On LIBERO-10, SALT increases average success across five persistent visual corruptions from 43.9% to 53.2% with SmolVLA and from 58.7% to 66.0% with GR00T N1.7, while largely preserving nominal performance. On a real robot, it raises task progress averaged over digital and physical disruptions from 0.49 to 0.61.


### SMART: Zero-Shot Sim-to-Real Articulated Object Manipulation via Large-Scale Synthetic Pretraining
**Authors**: Jicong Ao, Shuhan Jiang, Yuling Zhong, Yanwen Liu, Yuhan Gao, Jiangyuan Zhao, Yang Zhang, Shiqiang Zhu, Chenjia Bai, Xuelong Li

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.07652v1](https://arxiv.org/pdf/2610.07652v1)

**Abstract**: The ability to interact with articulated objects is essential for embodied intelligent systems, but collecting large-scale real-world demonstrations for these interactions remains challenging due to the precise contact and constraint-following motions involved. Although simulation provides a promising alternative, existing synthetic data efforts cover limited articulated-object categories, while general-purpose synthesis pipelines lack explicit designs for part-level semantics and articulation constraints, hindering agentic task generation and scalable synthesis of high-quality articulated-manipulation demonstrations. To bridge this gap, we introduce SMART, a scalable system leveraging large-scale Synthesized Manipulation demonstrations for ARTiculated-object manipulation. At its core, we develop SMART-Sim, a simulation platform with articulation-aware design that enables effective task generation and efficient demonstration collection. Building on SMART-Sim, we apply agentic task generation and design a scalable distributed synthesis system, using them to synthesize SMART-Data, comprising over 1M demonstrations across 44 atomic task types, 5 robot setups, and 2,507 articulated objects. The vision-language-action (VLA) model pretrained on SMART-Data shows competitive performance on simulation benchmarks and achieves zero-shot sim-to-real transfer and scalable performance in real-world articulated-object manipulation tasks. This highlights the potential of synthetic demonstrations in providing effective and scalable supervision for improving VLA model performance in contact-rich articulated-object manipulation.


### Seeing the Invisible: Physics-Guided Visual Prompting for Temperature- and Radiation-Aware VLA Navigation
**Authors**: Hojoon Son, Fan Zhang

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.07558v1](https://arxiv.org/pdf/2610.07558v1)

**Abstract**: Vision-Language-Action (VLA) models have become a major paradigm for Vision-and-Language Navigation (VLN). However, in safety-critical facilities, invisible risks such as radiation or temperature spikes cannot be detected by an RGB camera, and handling each risk is expensive, requiring a new encoder, new data, and model retraining. We propose Physics-Guided Visual Prompting (PG-VP), a plug-and-play multimodal perception module that instead reuses what a frozen VLA model already does well: avoiding visible obstacles. Given a proximal radiation or thermal source, PG-VP performs a physics-guided risk assessment to determine the avoidance direction and overlays a corresponding virtual obstacle that moves across consecutive frames (Dynamic Visual Prompting). The navigation policy then naturally detours around this invisible hazard. The identical virtual obstacle is used regardless of hazard type, so the visual prompting pattern remains fixed as sensors are added. When no hazard is detected, nothing is rendered, and the policy behaves exactly as it would without PG-VP. We evaluate PG-VP on OmniNav using the val-unseen splits of R2R-CE and RxR-CE, where it guides the policy toward intended low-risk actions in 84.9% and 83.2% of cases, at a cost of 6.8 and 7.9 percentage points in navigation success rate. We further test it with distinct scenarios on a real robot in the presence of actual thermal and radiation sources, all without any retraining. The real test shows that PG-VP effectively avoids these invisible hazards, improving worst-10% average trajectory safety by 63.45% and 32.59% against thermal and radiation sources, respectively.


### Recursive Video In-Context Learning for Agentic Robot
**Authors**: Wenrui Bao, Xinxin Liu, Bingxin Xu, Yuzhang Shang

**Published Date**: 2026-10-05

**Updated Date**: 2026-10-05

**PDF Url**: [2610.06843v1](https://arxiv.org/pdf/2610.06843v1)

**Abstract**: LLM agents that orchestrate frozen vision-language-action (VLA) policies improve across episodes through text memory, which records what the agent did but not how the task is done. A demonstration video shows it, but fits poorly into an agent's context. The full video slows every turn, fixed keyframes lose the contact detail that decides whether a grasp holds, and what the agent needs shifts from the task's structure while planning to the frames around each contact. We introduce Recursive Video In-Context Learning (RV-ICL), a training-free method that turns a demonstration into a hierarchy the agent navigates rather than a prompt it receives. The hierarchy is built from the sub-events of the demonstration, such as grasps and releases. Its levels grow finer, from keyframes of the whole task to phases, moments and short clips, and are exposed through read-only tools. The agent reads the coarse levels before planning. During execution it re-enters the hierarchy whenever a step needs more detail and loads only the clip of its current sub-goal. One demonstration per task is enough. Built on RPent, RV-ICL raises success from 92.6% to 96.5% on LIBERO-PRO and from 86.7% to 95.8% on LIBERO-Plus.


## Agent
### AdvSim2Real : Training Web Agents Against Adaptive Prompt Injection in a Web World Model
**Authors**: Sarim Hashmi, Mukul Ranjan, Kshitij Mishra, Mikhail Kuznetsov, Praneeth Vepakomma, Nils Lukas

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08773v1](https://arxiv.org/pdf/2610.08773v1)

**Abstract**: Web agents complete user requests by reading and acting on pages that third parties write, so an instruction planted on a page can redirect the agent away from the user's goal. The agent cannot simply ignore the page, because the page also holds the values and controls the task requires. Current defenses fine-tune the agent on injections fixed before training, and attackers that adapt to the trained model bypass them. Adversarial training lets the attacker adapt but keeps the tasks fixed, so a task stops teaching once the agent solves it. We introduce AdvSim2Real, which co-evolves a task curriculum, an injection adversary, and the agent inside a frozen web world model. The curriculum is rewarded for tasks the agent solves about half of the time, and the adversary only for a success flip, an injection that turns a judged success into a failure. Training in the simulator makes a 4B agent both more capable and more robust: its completion rises with and without attacks, holds against a frontier-model adversary it never trained against, and its capability gain carries over to a real browser. On 150 web tasks, AdvSim2Real raises completion under this unseen adversary by 33.6\% relative to the base agent.


### VeriFine: Scaling Verification for Self-Improvement in Embodied Reasoning
**Authors**: Zewei Zhou, Rachel Luo, Yulong Cao, Chaowei Xiao, Chensheng Peng, Boyi Li, Thomas Tian, Zheng Lian, Yan Wang, Jiaqi Ma, Boris Ivanovic, Marco Pavone, Wenhao Ding

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08761v1](https://arxiv.org/pdf/2610.08761v1)

**Abstract**: Self-improving policies continually expose new failure patterns, changing what their judges must be able to verify. However, current fixed judges constrain both optimization feedback and the discovery of useful training examples, limiting further self-improvement. This challenge is even more acute in embodied reasoning, where reliable evaluation must account for spatial grounding, causal reasoning, and safety-aware decision-making. We introduce VeriFine, an agent harness framework that scales verification through the co-evolution of the policy, training curriculum, and judge. The Policy Improvement Loop uses a rubric judge to diagnose recurring failures, construct an adaptive curriculum, and optimize the policy. When progress plateaus and verification becomes a bottleneck, the Judge Improvement Loop selectively queries human guidance on informative failure cases and refines the judge through coactive calibration, in which humans and agents resolve disagreements and converge toward the objective rubric of physical reasoning. The revised judge then guides the next stage of data selection and policy optimization. Experiments on driving and robot navigation tasks demonstrate continuous self-improvement in both policy and judge capability across reinforcement and supervised fine-tuning. These results show how scaling verification supports continuous self-improvement as policy failure patterns evolve.


### Does an Agent's History Tell You When Compaction Will Hurt? A Modest, Bounded Effect on the TRACE Paired-Replay Corpus
**Authors**: Egor Pakhomov, Erik Nijkamp

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08722v1](https://arxiv.org/pdf/2610.08722v1)

**Abstract**: Many long-horizon agents compact their context on a global rule, usually a token budget, blind to what the agent was doing. We ask whether the agent's recent behaviour predicts when a compaction will hurt. TRACE's public corpus of 590 harness-triggered AppWorld compaction boundaries replays each boundary from a re-executed prefix state under the pre-compaction context and under the summary, and records the burden of the next actions: calls that error or repeat a call already made. We find that pre-boundary history predicts post-compaction harm only weakly. An internally prespecified contrast by prefix placement is a wide null, and the naive "has-written" label behind it turns out to measure trajectory phase. The best extension-protocol trigger reaches held-out AUROC 0.66 (0.64 on the replicate's own label) against a same-boundary replicate of 0.72; the best frozen, interpretable trigger avoids 21% of harmful (positive-burden) boundaries while keeping 84% of compaction opportunities, and exceeds the random-rule expectation on count but not on burden mass (a post hoc comparison). Whether the best trigger beats a token-budget rule at matched retention cannot be evaluated on the release. We state what corpora should ship to answer it.


### nanoMuse: An Open-Source Personal Agent for Every Device You Own
**Authors**: Guangyi Liu, Yong Liu, Jiangning Zhang

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08699v1](https://arxiv.org/pdf/2610.08699v1)

**Abstract**: Assistants from 2011 answered and waited, and agents from 2023 did a task and stopped. In September 2026 Meta's Muse showed an agent for one person, with accounts, devices, memory and a conversation that lasts, closed, in a vendor's cloud, in one country. Such an agent is expected to act on a person's accounts and devices, remember them across weeks, speak first when it is worth it, and answer for what it did. It is a kind of software, not a model, and until now had no open counterpart. This report defines the personal agent in five questions and three horizons. It reads how Muse is built from Meta's public record and a copy of its production prompt, each statement marked by its source. It then presents nanoMuse, the open-source counterpart under the GPL-3.0, one agent on every device a person owns, with hands on the phone's screen and the computer's. They share one conversation over a relay anyone can run; every action goes through a Sentinel, memory is files the person can read, and the model is their choice. Its size and cost are given as estimates. What is open, memory with provenance, an evaluation suite for the hands and an open model for them, is set out as a roadmap.


### ScienceClaw: Benchmarking Continual Self-Evolution of AI-for-Science Agents Across the Natural and Social Sciences
**Authors**: Mingda Zhang, Wenjin Liu, Tiesunlong Shen, Zikai Xiao, Zhenghong Lin, Qing Xu, Erik Cambria, Xiaoying Tang, Haoran Luo

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08691v1](https://arxiv.org/pdf/2610.08691v1)

**Abstract**: Large language model agents are accelerating scientific automation, yet verified executions rarely become persistent program-level improvements, and existing evaluations do not examine this process across sequential tasks in both the natural and social sciences. We formalize ScienceClaw as fixed-parameter program self-evolution that unifies task solving, scientific verification, and program updates. ScienceClaw-Eval spans 23 disciplines and measures scientific correctness, evolutionary gain, retention, cross-dataset transfer, and evolution cost through sequential streams and independent reset evaluation. Our framework repairs executable workflows through multi-turn interaction, converts re-execution-verified failure--success trajectories into linked Skill and Operator candidates, and retains an update only when source-task replay reproduces the repair and independent scientific tasks improve. Code is available at https://github.com/beita6969/ScienceClaw.


### Coupled but Late: Turn-Taking Between Full-Duplex Speech Models in Unscripted Dialogue
**Authors**: Lichen Zhu, Yueqian Lin, Yiheng Wang, Hai "Helen" Li, Yiran Chen

**Published Date**: 2026-10-06

**Updated Date**: 2026-10-06

**PDF Url**: [2610.08683v1](https://arxiv.org/pdf/2610.08683v1)

**Abstract**: Full-duplex speech models are trained to converse with a person, but they are increasingly made to converse with each other, in self-play data generation, agent societies, and model-based evaluation. In that loop no human absorbs a timing error: each model's turn-taking is the other's input. We ask what timing the loop settles into. Two PersonaPlex-7B instances exchange audio tokens on a shared clock in unscripted conversation, and one floor-transfer rule is applied to them and to Switchboard. Their timing is coupled: re-pairing speakers across conversations destroys it. But the floor changes hands late, at a median of 400-560 ms against 137 ms for humans, and the last 120 ms of the partner's turn, where human projection places a tenth of its transfers, holds 1% of theirs. Delaying one direction of the channel shifts the response one-for-one and leaves the run-up to it empty, consistent with a reactive wait after the perceived end rather than the turn-end projection human timing requires.


