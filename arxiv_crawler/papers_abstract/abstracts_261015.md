# Abstracts of Papers

## World Model
### SafeDriveVLA: Navigation-Conditioned World Model Dreaming for Conflict-Aware End-to-End Autonomous Driving
**Authors**: Shaoyuan Xie, Zihan Zhang, Jingxuan Wang, Jiashu Qu, Xiaoqing Liang, Lingdong Kong, Junchi Lu, Henrik I. Christensen, Qi Alfred Chen

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20609v1](https://arxiv.org/pdf/2610.20609v1)

**Abstract**: Vision-Language-Action (VLA) models are gaining attention in autonomous driving, inheriting commonsense priors from large language models (LLMs) and widening the navigation interface from a fixed command set to free-form natural-language instructions. However, this open-ended interface exposes a new vulnerability surface: an inattentive driver may issue instructions that are unsafe given the current scene, and a malicious user may issue dangerous ones on purpose. We present the first benchmark suite that evaluates navigation following and conflict awareness together, along with adversarial robustness. Existing VLAs fall short on both: SimLingo completes no language-instructed lane change in closed loop, and all models degrade sharply under conflicting signals. We propose SafeDriveVLA, the first driving VLA that (1) explicitly predicts a three-level navigation-compliance mode to decouple conflict reasoning from action generation, and (2) uses navigation-conditioned world model dreaming to inform this prediction. Unlike prior world models that roll out expert or planned actions, ours dreams of strictly following the navigation signal, showing when following is safe. SafeDriveVLA reaches 88.16 Driving Score (DS) and 68.64% Success Rate (SR) on Bench2Drive, lifts closed-loop language following by 49.3% and reduces collisions under unsafe instructions from 60 to 38 compared to the best SimLingo variant. Video demonstrations are available on our project page.


### Modeling and Understanding Neural Weights of Humanoid Policies with Diffusion
**Authors**: Huixuan Cheng, Bike Zhang, Shankar Sastry, Koushil Sreenath

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20606v1](https://arxiv.org/pdf/2610.20606v1)

**Abstract**: Recent advances in robot learning have driven rapid progress in humanoid control, enabling increasingly agile behaviors in the real world. However, humanoid control networks are typically obtained through conventional training procedures, while comparatively little attention has been given to directly modeling the distribution of their learned weights and generating functional networks in weight space. In this work, we investigate whether high-performing humanoid control networks can be generatively modeled directly through their weights. We adopt a latent diffusion framework that couples a linear autoencoder with a Diffusion Transformer. The autoencoder compresses actor network parameters into a compact latent space, and the Diffusion Transformer models the distribution of these latents. Trained on networks collected from reinforcement learning for the Unitree G1 robot, our approach generates deployable networks that perform various motions in the real world, including walking, dancing, and spin kick. Beyond generation, we further study the learned weight space to better understand the structure captured by these humanoid control networks. We identify a structural principle in the first-layer weights that consistently reflects the robot's kinematic prior. Notably, this kinematic prior emerges under both Reinforcement Learning (RL) and Imitation Learning (IL) training, suggesting that it is not specific to a particular optimization process but may instead reflect common knowledge associated with humanoid embodiment. Together, these results demonstrate the feasibility of generative modeling in humanoid network weight space, while providing initial insights into the information encoded by their learned weights. Additional results are available on our project website: https://humanoid-weight-diffusion.github.io/


### Hierarchical Residual Policy Learning for Real-World Mobile Manipulation with Sparse Human Guidance
**Authors**: Zhefei Gong, Hefeifei Jiang, Zehao Wang, Jiachen Li

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20607v1](https://arxiv.org/pdf/2610.20607v1)

**Abstract**: Mobile Manipulation (MoMa) is a cornerstone of autonomous robotic systems, yet real-world fine-tuning remains a formidable challenge because of high-dimensional action spaces and intricate coupling between heterogeneous modules. In this paper, we propose HiRe-MoMa (Hierarchical Residual Mobile Manipulation), a systematic framework for stable and sample-efficient real-world fine-tuning of complex MoMa systems. At its core, HiRe-MoMa adopts a Hierarchical Residual Architecture that fine-tunes a frozen base policy. A Policy-Agnostic Residual learns additive corrections atop the base policy, while Hierarchical Decoupling splits the residual into mobile-base and manipulator-arm heads with unidirectional conditioning, mitigating gradient interference and aligning corrections with the platform's physical hierarchy. To improve sample efficiency in data-expensive real-world settings, we propose Expert-Guided Value Alignment, which leverages sparse human interventions with under 20% training coverage to reshape the critic's value landscape, effectively guiding autonomous exploration through expert priors. Extensive real-world experiments on the TIAGo++ platform demonstrate that HiRe-MoMa consistently enhances task performance with only around 30 minutes of online interaction, regardless of the base policy architecture. To our knowledge, this is among the first frameworks to enable efficient on-robot fine-tuning for mobile manipulation in the real world, providing a practical paradigm for deploying complex robotic systems in dynamic, human-centric environments. Further details can be found on our project website: https://hire-moma.github.io/


### VITAL: From Visual Motion to Precise Action
**Authors**: Ao Liang, Youquan Liu, Mingxiao Li, Wei Chow, Lingdong Kong, Yue Liao, Dongyue Lu, Yu Yang, Wei Yin, Runnan Chen

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20604v1](https://arxiv.org/pdf/2610.20604v1)

**Abstract**: World-action models aim to turn visual anticipation into driving decisions, yet typically train action experts on trajectory representations defined independently of visual dynamics. This motivates deriving action targets directly from visual motion. We first examine a simpler setting in which trajectories are reconstructed from recorded future images. Even without the need for future prediction, reconstruction captures the dominant maneuver but leaves centimeter-scale errors. We therefore introduce VITAL (Vision-Induced Tokens for Action Learning), an action tokenizer that couples a visually derived motion scaffold with a compact residual encoding the trajectory error left by that scaffold. This representation makes visual motion the principal prediction target and gives small metric corrections a separate, normalized learning scale. Using flow matching, the action expert jointly predicts both components from the current image, ego state, and navigation command, without generating future images at inference. The same residual coordinates support bounded reinforcement post-training that refines execution while keeping the predicted visual scaffold fixed. With only one action denoising step, VITAL achieves 90.8 PDMS on NAVSIM v1 navtest, within 0.13 points of its ten-step score at 3.29x the end-to-end inference speed. Without retraining, it achieves 91.1 EPDMS on NAVSIM v2 navtest and 38.6 on navhard. Project page: https://worldbench.github.io/vital


### Heavy-Heavy-Light-Light correlators from holography on the worldsheet
**Authors**: Matías Colaneri, Diego H. Correa, Víctor I. Giraldo-Rivera, Nicolás A. Ivanovich

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20602v1](https://arxiv.org/pdf/2610.20602v1)

**Abstract**: We study correlation functions of light local operators and defect changing operators on the conformal line set by the 1/2 BPS Wilson line of $\mathcal N=4$ super Yang-Mills. We consider the defect changing operators associated with geometrical and internal cusp angles, which at strong coupling have a large scaling dimension and back-react on the dual $AdS_2$ world-sheet. We set up a holographic computation of correlation functions, in which the light operators are described by fluctuations around the cusped classical string solution, so that correlators of two defect changing operators and an arbitrary number of light protected operators are obtained from the on-shell action of these fluctuations. We implement this prescription in detail for the case of certain 4-point functions, with two light and two defect changing operators. Finally, since for small cusp angles the defect changing operators become light, we manage to derive relations satisfied by integrated correlators of light operators, valid at any coupling. We verify these relations at strong coupling for both internal and geometrical cusps.


### Co-Evolving Acting and Forecasting for Language Agents
**Authors**: Haofei Yu, Yixing Chen, Yining Zhao, Xuyan Ye, Yuxiang Liu, Zhigang Hua, Yan Xie, Shuang Yang, Jiaxuan You

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20597v1](https://arxiv.org/pdf/2610.20597v1)

**Abstract**: Training language agents is bottlenecked by the high cost of long-horizon rollouts, yet standard agentic reinforcement learning (RL) learns only from a terminal scalar reward, leaving the supervision in intermediate steps largely unused. Prior work exploits this supervision through value targets that estimate per-step success probabilities or observation targets that fit environment response. Both are hard to construct well: (1) value targets come from the same single scalar signal for each step in the trajectory, and (2) observation targets, such as web pages and terminal logs, are long and noisy and reach only one step ahead. We propose \name, which adds a third kind of multi-step action targets. On successful on-policy trajectories, \name trains the policy backbone to generate the action sequences that follows each history. Each action is also supervised when forecast from the preceding histories, forming a temporal ensemble that the shared backbone absorbs during training, and this enables acting and forecasting to co-evolve. The policy still acts one step at a time at inference, with no overhead. Across five benchmarks (ALFWorld, ScienceWorld, WebShop, $τ^2$-bench, and AppWorld), \name (1) achieves stronger aggregate performance than GRPO and RL baselines with predictive auxiliary targets across simulated environments, while improving overall performance on both realistic applications; (2) delivers up to $1.9\times$ and $2.0\times$ higher sample efficiency than ECHO and GRPO, respectively, on ScienceWorld; and (3) achieves these gains with a single policy backbone, without additional models, separate pretraining, or inference overhead. The codebase is available at https://github.com/ulab-uiuc/CoPE.


## Generation
### Price of Anarchy of First-Price Auctions in Agentic Markets
**Authors**: Shubhendu Trivedi, Jacob Eisenstein, Alekh Agarwal, Ian Gemp, Michael Kaisers, Adam Fisch

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20587v1](https://arxiv.org/pdf/2610.20587v1)

**Abstract**: An agentic market is a decentralized serving-time market where AI agents bid to claim each user prompt. An agent's bid is based on its expected value for the prompt, which is the expectation of the reward for its response minus its inference costs. First-price auctions (FPAs), in which the highest bidder pays its bid and receives the prompt, are a natural way to allocate prompts in such a market, since they are simple and transparent to run, and do not require central knowledge of private capabilities and costs. However, FPAs are not truthful: participants may bid less than their true value in the hope of a larger profit, and the prompt may then be allocated to someone other than the bidder who values it the most. This welfare loss is quantified by the $\textit{price-of-anarchy}$ (PoA). In this paper, we argue that agentic markets are likely to possess features that reduce the price-of-anarchy. The first is a $\textit{competitive floor}$, which occurs when multiple bidders usually value the prompt above some baseline share of the optimal welfare (e.g., because the best models are often distilled into cheaper alternatives, which perform similarly). We show that competition among them then limits the welfare loss, which can be driven to zero as the floor rises. The second feature is $\textit{near-independence}$ of values after conditioning on the prompt, which occurs when most of the predictable variation in the expected value is determined by the difficulty of the prompt. As the value distribution approaches conditional independence, we can derive an efficiency guarantee that approaches a factor of $1 - 1/e^2$ of the optimal welfare. Thus, both features give rise to welfare lower bounds that are significantly better than the well-known general case of $1 - 1/e$. We validate these results empirically using auctions with strategic bidders simulated on the EmbedLLM prompt routing dataset.


### Continuum Attention
**Authors**: Afshin Khadangi

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20586v1](https://arxiv.org/pdf/2610.20586v1)

**Abstract**: We introduce Continuum Attention (CA), a causal Transformer attention operator that replaces discrete key and value lookup with integration over a continuous, piecewise linear memory curve. Each query induces an exponential relevance density along the curve. Integrating the density and interpolated values yields exact normalized attention from closed form exponential moments, including half token boundary contributions. The gradients follow analytically from moments of order at most two, enabling parallel GPU implementations while retaining quadratic sequence complexity and the standard Transformer decoder. Compared with ordinary softmax and focal attention, CA reduces mean validation negative log likelihood by 0.0200 and 0.0480 nats per byte, respectively, winning all paired comparisons. An additional disjoint validation slice yields a 0.0457 nats per byte advantage over the strongest selected softmax baseline, with a paired 95% confidence interval. These findings motivate continuous integration as a promising attention alternative while leaving larger scale generalization open.


### Player-1: Learning to Play from Synthetic Experience
**Authors**: Mingyu Ouyang, Yiran Wang, Siyuan Hu, Xingyilang Yin, Huiqiang Sun, Guangzhi Wang, Junfu Pu, Cheng Cheng, Honghao Chen, Ying Shan, Mike Zheng Shou, Hwee Tou Ng

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20584v1](https://arxiv.org/pdf/2610.20584v1)

**Abstract**: Computer-use agents have demonstrated strong capabilities in interpreting screens and executing keyboard and mouse actions. However, games, with their visually rich worlds and diverse mechanics, remain challenging and offer a demanding next step toward general digital control. Current game-agent learning pipelines often rely on large-scale demonstrations with limited coverage of dynamic game states, while scalable environments for interactive training remain difficult to obtain. We introduce Player-1, a post-training framework for learning game control beyond demonstrations through synthetic experience. We extend the computer-use action space with relative pointer motion, sustained inputs, and composite actions. For supervised initialization, we fine-tune computer-use models on 6,044 curated gameplay trajectories that pair recorded actions with task instructions and visual reasoning. We construct Player-1-Gym, sixteen synthetic 2D and 3D environments designed around control demands shared across games. Programmatically verifiable rewards and randomized observations and control dynamics support multi-environment reinforcement learning with PPO. The resulting Player-1-9B and Player-1-35B-A3B improve MineDojo-300 success over their SFT policies by 27.8 and 17.7 percentage points, respectively. Player-1-9B reaches 38.33% success compared with 12.63% for the strongest evaluated baseline, with further gains over SFT on ViZDoom-10 and GameWorld. Further analyses show that broader synthetic environment coverage improves transfer, while the use of composite actions that combine multiple keyboard and mouse inputs increases during RL. We demonstrate that learning from synthetic experience substantially improves game control beyond supervised initialization, with gains that generalize beyond the RL training suite.


### Latent Compaction with Test-Time Training
**Authors**: Yingfa Chen, Xingyu Shen, Chaojun Xiao, Xu Han

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20582v1](https://arxiv.org/pdf/2610.20582v1)

**Abstract**: Long contexts enlarge key--value (KV) caches, increasing memory use and attention costs during generation. Compressing these caches must preserve information for unseen questions. We introduce **Latent Compaction**, which learns a compact document-specific cache through test-time training. We initialize cache entries using reconstruction importance, teacher attention, and key-space diversity. Training first fits attention outputs and log-normalizers to those of the full cache, with reconstruction-selected entries held fixed. It then jointly optimizes the entire cache through end-to-end distillation from the full-cache model. Model weights remain frozen throughout, and training uses only generic prompts about the document, without access to downstream questions or answers. Experiments on RULER, LongBench, and Phonebook Lookup demonstrate substantial gains over budget-matched compression baselines. On a RULER, for example, our method achieves 96.7% accuracy at 32$\times$ compression, compared with 40.0% for KVZip+. The method also transfers across model scales and families, with retrieval gains on both Qwen3 and MiniCPM5. These results show that treating the KV cache as a neural network and optimizing it with test-time training can preserve retrieval accuracy under aggressive compression. The code is released at https://www.github.com/THUNLP/latent-compaction


### PhySGA: A Physics-Space Grounded Agentic Framework for Generalizable and Interactive 3D Composition
**Authors**: Weichen Lyu, Chong Xia, Mingyu Dong, Long Xu, Shengjun Zhang, Yueqi Duan

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20560v1](https://arxiv.org/pdf/2610.20560v1)

**Abstract**: 3D object composition is pivotal to digital content creation and robot simulation, while also serving as a critical testbed for physical intelligence in foundation models. Previous methods either leverage large language models to directly predict object coordinates, or utilize generative diffusion priors to synthesize composite images for visual alignment, both of which rely on static priors in digital spaces. However, these methods consistently struggle with complex compositions such as precise hanging, gravity-driven settling and hidden containment, as these tasks require interactive construction processes involving global planning, fine-grained alignment, and physical simulation. To address these challenges, we propose PhySGA, a Physics-Space Grounded Agentic Framework for 3D composition via agent exploration and physical simulation, enabling the universal interactive assembly of rigid, articulated, and deformable objects. Directly applying vanilla LLMs or VLMs to this task proves insufficient, as current models inherently lack grounded physical understanding and interactive construction experience. To overcome this limitation, we design a collaborative feedforward-feedback architecture: an Assembly Agent focuses on geometric and kinematic reasoning for global step planning and coarse adjustment, while a Critic Agent reasons over contact dynamics for simulator state diagnosis and fine-grained closed-loop correction. Furthermore, Action Routers map semantic planning and analysis onto executable physical primitives within the simulator, while a task-specific Self-Evolving Skill Library distills historical trial-and-error feedback into reusable experiences, boosting success rates and minimizing exploration attempts. Extensive experiments within Isaac Sim demonstrate that PhySGA significantly surpasses existing methods in relation fidelity, physical plausibility, and visual quality.


### PerSo: Investigating Facets of LLMs' Social Intelligence in Real-World Persuasion Scenarios
**Authors**: Ali Zamani, Soroush Esfahanian, Erfan Shahabi, Mohammad Taher Pilehvar, Azadeh Shakery, Yadollah Yaghoobzadeh

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20548v1](https://arxiv.org/pdf/2610.20548v1)

**Abstract**: Understanding the social intelligence of large language models (LLMs) is increasingly important for applications involving human-AI interaction and multi-agent environments. Social intelligence comprises two aspects: cognitive intelligence, the ability to infer others' mental states, and behavioral intelligence, the ability to select appropriate social actions based on these inferences to achieve social goals. Persuasion provides a natural testbed in which both aspects are simultaneously at play, yet prior benchmarks typically evaluate them in isolation using synthetic scenarios. We introduce PerSo, a benchmark that evaluates both aspects on real-world persuasion dialogues from Reddit's ChangeMyView community, using an LLM-in-the-loop pipeline to construct the evaluation tasks, validated through human annotation. Our evaluation of diverse LLMs shows that performance generally scales with model size but varies across dimensions. The strongest LLM slightly surpasses the best observed human performance on the behavioral task, while the best human participant remains ahead on the cognitive task.


## VLA
### FoveaVLA: Foveation Actions Replace the Wrist Camera in VLAs
**Authors**: Bingao Chen, Lihan Zha, C. Karen Liu, Guy Tevet

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20064v1](https://arxiv.org/pdf/2610.20064v1)

**Abstract**: We present FoveaVLA, a Vision-Language-Action (VLA) model that replaces the wrist camera with learned foveation actions. Wrist cameras provide close-up detail but restrict the view to the end-effector's surroundings. External cameras see the whole scene, but the policy receives them at low resolution, so the fine detail needed for manipulation is lost. FoveaVLA recovers this detail by predicting, alongside each action chunk, the interaction region to observe at the next policy query. The policy then receives crops of these regions, taken from the original-resolution images, together with the full views. We build FoveaVLA on $π_{0.5}$ in two configurations, Single and Dual, using one or two external stereo cameras with full and foveal RGB and depth inputs, and post-train both on DROID with RoboInter interaction annotations. Across four real-world task suites, FoveaVLA-Single achieves 70.8% success with one external RGB-D view, and FoveaVLA-Dual achieves 77.1%, versus 52.1% for the wrist-equipped $π_{0.5}$. Both match the baseline on plain pick-and-place and improve success with distractors, cloth manipulation, and far-away objects.


### MorphAct: Robot Policies Morphing with the Worlds They Act In
**Authors**: Ziyan Liu, Jiting Liu, Weihong Zhong, Wenda Yu, Yeqiu Chen, Jason Li, Xiaojiang Peng, Shuyuan Hu, Kai Wang, Bo Zhao

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20019v1](https://arxiv.org/pdf/2610.20019v1)

**Abstract**: Progress toward general intelligence in the physical world requires scaling robot learning across diverse environments and interactions. However, existing robot policies use shared parameters that remain fixed across interaction contexts. When different operations favor competing parameter adjustments, fitting their mixture can leave individual operations insufficiently adapted. Our atomic-task diagnostics reveal competing update directions in both vision-language and action parameters, with source-improving updates increasing loss on other tasks. This motivates MorphAct, a contextual parameterization framework that dynamically adjusts robot policy parameters as interaction contexts change. Two coupled generators produce context-dependent low-rank updates for the vision-language and action modules. Their coupling follows the policy's computational dependency: vision-language updates shape the representations that condition action-side parameter generation. Both generators are trained jointly through the native action objective, without operation labels or expert-adapter targets. MorphAct improves performance across three VLA backbones on LIBERO and Meta-World, with gains of up to 16.30%. In real-world evaluation, it achieves gains of up to 14% over $π_{0.5}$. Ablations support the benefits of contextual parameter generation and representation coupling.


### VLRLA: Deployment-Time Adaptation of Vision-Language-Action Models through In-Context Reinforcement Learning
**Authors**: Diyuan Shi, Yiqi Tang, Hongyin Zhang, You Wu, Donglin Wang

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.19517v1](https://arxiv.org/pdf/2610.19517v1)

**Abstract**: Vision-language-action (VLA) models connect visual perception and language understanding with robot control, providing a foundation for instruction-conditioned manipulation. However, conventional pretrained VLA policies lack a mechanism for gradual adaptation through accumulated interaction experience during deployment. We therefore propose VLRLA, a general framework that equips existing VLA models with \textit{in-context reinforcement learning} capabilities for deployment-time adaptation. Our approach augments a VLA model with a reinforcement learning module that learns from historical observations, actions, rewards, and termination signals. During deployment, the policy gradually refines its action generation and progressively improves task success while keeping model parameters fixed. Our approach is also designed for general applicability and compatibility with diverse learning history construction strategies and model training pipelines. Finally, through extensive experiments, we systematically investigate the learning properties of VLRLA in simulation and demonstrate its ability to adapt to unseen scenarios during real-world deployment.


### ChunkAct: Action Chunking for Agentic Robotics
**Authors**: Bingxin Xu, Wenrui Bao, Xinxin Liu, Jiawei Zhou, Yuzhang Shang, Emilio Ferrara

**Published Date**: 2026-10-13

**Updated Date**: 2026-10-13

**PDF Url**: [2610.18874v1](https://arxiv.org/pdf/2610.18874v1)

**Abstract**: Agentic robotics places a large language model (LLM) agent in the robot control loop, where it composes perception, motion, and vision-language-action (VLA) tools under the guidance of a memory and thereby generalizes to new tasks without retraining. This generality comes at a steep price in efficiency. Every primitive requires a round of LLM reasoning over the full interaction history, so the cost of an episode grows with the number of primitives. We find this reasoning largely redundant: once a sub-goal is chosen, its primitives follow a routine already prescribed by memory. We present ChunkAct, which introduces action chunking to agentic robotics. Online, a single call launches a chunk of chained primitives, which executes autonomously and returns control only upon failure. Offline, ChunkAct compiles the memory into these chunks, so execution is memory-free at test time and the planner is reserved for decisions that require reasoning. LLM computation therefore scales with the number of decisions rather than the number of primitives. On LIBERO-Pro, ChunkAct improves task success by 5.0 points over the state of the art in agentic robotics while requiring 2.9x fewer LLM calls, 4.4x fewer input tokens, and 2.3x fewer output tokens.


### What Matters in Quality-Aware VLA Pretraining: A Benchmark and Empirical Study
**Authors**: Mingxuan Yan, Litian Gong, Dihong Huang, Zhixu Li, Tianyu Zhang, Wenqian Zhang, Hefeifei Jiang, Peihao Li, Jian Zhang, Mengfei Zhao, Yikai Tang, Hai Zhai, Zehao Wang, Ruijian Liang, Yanjia Huang, Lin Shao, Changliu Liu, Kaiyu Hang, Zhiwen Fan, Masayoshi Tomizuka, Jianfei Yang, Jiachen Li

**Published Date**: 2026-10-13

**Updated Date**: 2026-10-13

**PDF Url**: [2610.18869v1](https://arxiv.org/pdf/2610.18869v1)

**Abstract**: How should demonstration quality be used during vision-language-action (VLA) pretraining to improve performance after target-task fine-tuning? We compare weighting, filtering, and conditioning across reward definitions and label granularities using 5,000 naturally suboptimal human demonstrations and 24 target tasks. Within each VLA, we match demonstrations and training budgets. Additional comparisons examine pretraining data size and the roles of quality tags during fine-tuning and inference. Across three VLAs, we find that approach-aware episode conditioning improves mean success over plain behavioral cloning; conditioning and filtering favor episode and chunk labels, respectively, on average, with model-dependent reversals; and constant-tag fine-tuning improves mean success after conditioned pretraining with either tagged or untagged inference. We introduce AXIS-Bench to support these controlled comparisons. Built on crowdsourced simulation demonstrations, it provides recorded object and contact states for recomputing quality labels on shared trajectories. Replayable trajectories support workspace-aligned rendering and user-defined real-world target tasks. In our real-world experiment, simulation pretraining raises success from 9.6\% to 31.7\%. Project page: https://axis-bench.github.io/.


### ACCRUE: Continual Off-Policy Reinforcement Learning for Robot Foundation Models
**Authors**: Changyeon Kim, Kimin Lee, Yashraj Narang, Yijie Guo

**Published Date**: 2026-10-13

**Updated Date**: 2026-10-13

**PDF Url**: [2610.18596v1](https://arxiv.org/pdf/2610.18596v1)

**Abstract**: Reinforcement learning (RL) post-training improves robot foundation models (RFMs) beyond their demonstrations, but real-world deployment demands more: learning new tasks efficiently while retaining previously acquired behaviors. Existing continual RL methods on top of VLAs mitigate forgetting but rely on on-policy updates with limited forward transfer, whereas off-policy methods improve single-task sample efficiency without addressing learner persistence across tasks. We propose ACCRUE, a continual off-policy RL framework that carries lightweight actor and critic networks across tasks, allowing each stage to reuse behavioral and value knowledge acquired through prior RL. The inherited critic adapts only on current-task transitions and guides current-task actor learning, while prior behavior is preserved by distilling the actor toward cached targets on a small number of retained episodes. Fixed visual features keep the inherited learner and its replay compatible with base-policy updates. Across contact-rich assembly sequences in simulation and on real-robot hardware, ACCRUE accelerates subsequent-task learning with near-zero forgetting and significantly reduces real-robot training time by 31.0\% to 68.5\%.


## Agent
### One Task, Many Interfaces: Simple Cross-Interface Consistency Training Improves LLM Agent Robustness
**Authors**: Artin Tajdini, Manpreet Kaur, Peng Qi

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20576v1](https://arxiv.org/pdf/2610.20576v1)

**Abstract**: Post-training binds the competence of an LLM agent to the interface it was trained on. Semantics-preserving perturbations of that interface, such as renaming an action or changing the notation, leave the underlying task unchanged yet make the agent worse at it. Scoring each sample independently means interface randomization only broadens this dependence from a single interface to the training interface distribution, so out-of-distribution perturbations still degrade the agent. We propose Cross-Interface Policy Regularization (CIPR), a self-supervised objective that replaces action names with uninformative identifiers and presents each training sample under two interfaces in which equivalent actions are identified by construction. CIPR penalizes the KL divergence between the action distributions induced under the two interfaces, so the policy behaves consistently across them. We evaluate CIPR in both supervised and reinforcement-learning post-training, where it improves robustness. On agentic function calling, held-out interface perturbations reduce the accuracy of a post-trained agent by nearly 25%, and CIPR recovers 10.5% while leaving accuracy on the unchanged interface intact.


### Beyond LLM Judge: Mechanical Verification for Agentic Autoformalization
**Authors**: Anna Mei, Michael R. Douglas

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20573v1](https://arxiv.org/pdf/2610.20573v1)

**Abstract**: We introduce a novel method for verifying Lean formalizations that goes beyond LLM-judged faithfulness. Unlike most verification methods, which rely on LLMs or trained models, our method combines LLM-based semantic review with mechanical numerical and vacuity checks, providing checkable feedback and detecting errors missed by LLM judges. We apply this method, along with our Extract-Verify-Proof autoformalization pipeline, to construct the Formalized Library of Mathematical Functions (FLMF), a partial formalization of the NIST Digital Library of Mathematical Functions (DLMF). On three labeled datasets, our method achieves the lowest accepted-error rate among the evaluated methods, measured as the fraction of incorrect statements accepted by the verification method. Expert review of the results also identifies translation and source defects in existing datasets. Code available at https://github.com/annamei1/FLMF-Ch7ErrFunc-Release.git.


### Scaling Discovery Requires Forgetting
**Authors**: Shangyin Tan, Ben Zhou, Lakshya A Agrawal, Jialin Zhang, Yilin Chen, Qiuyang Mang, Donghyun Lee, Dennis Jacob, Koushik Sen, Alex Dimakis, Matei Zaharia

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20563v1](https://arxiv.org/pdf/2610.20563v1)

**Abstract**: Automated research with LLM agents has shown promising results in various domains. Through iterative refinement and scored verifiers, LLM agents are capable of discovering new ideas. There are different ways to scale automated research: let one agent iterate for longer, run several agents in parallel, or further let the parallel agents communicate and build on one another's candidates. However, we find that all three strategies eventually plateau as the agents accumulate history. Each agent becomes anchored to its own past attempts, making fewer and smaller edits. Beyond this point, additional budget brings little further improvement. In this paper, we show that the key to scaling discovery further is to forget. Periodically discarding the search state, including every agent's session and the candidate history, and restarting from the best candidate found so far, unblocks the search and pushes the same budget further.
  We implement forgetting in a team of agents with communication and evaluate it on four tasks spanning heuristic programming, kernel optimization and model training. The results show up to 15% improvement compared to parallel agents, and up to 39% compared to a single agent. Our results suggest that, for open-ended discovery, what an agent is allowed to remember matters as much as how much compute it is given.


### ActiveEvidence: Decision-Focused Evidence Graphs with Verifiable Acquisition Gaps
**Authors**: Miaobo Hu, Shuhao Hu, Xiaobo Guo, Xin Wang, Bokun Wang, Peng Zhang, Daren Zha, Jun Xiao

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20532v1](https://arxiv.org/pdf/2610.20532v1)

**Abstract**: A multimodal agent must decide whether visual evidence is worth acquiring, which candidate or resolution to query, and when further interaction can no longer change its decision. We study this problem under a strict free-metadata/paid-observation boundary, stochastic vector costs, and a frozen execution trace, and treat it as decision-certifiable active evidence acquisition. A Counterfactual Evidence Interaction Graph (CEIG) represents unary evidence value, signed second-order interaction, and directed conditional harm while maintaining explicit score enclosures for unresolved interactions; a decision-weighted enclosure objective tightens the bounds that can change action identity. Gap-directed refinement evaluates only interactions that can displace the incumbent acquisition and stops once an $ε$-decision certificate shows that unresolved terms cannot change the selected action beyond a declared tolerance. The certificate is model-relative: it verifies policy-consistent optimality under the pinned learned score, and semantic quality is measured separately through post-freeze labels. Paired continuation rollouts learn the downstream value of paid previews, an online operational cost filter is separated from independent finite-policy-family trajectory certification, and an acquisition monitor with an independently implemented verifier binds every certificate to the frozen trace. On 640 cases split into 384/128/128 training, validation, and test cases, the controller reaches task score 0.842, grounding F1 0.816, evidence recall 0.873, 1.74 accepted calls, 286.5K visual tokens, and 742ms p95 latency. Dense replay of issued certificates shows 0.992 action agreement and a 0.988 certificate rate while evaluating 19.6 instead of 191.4 expensive interaction terms per decision.


### The Wealth of Agents: Scaling Agentic AI Across Developers
**Authors**: Austin W. Hanjie, Carlos E. Jimenez, Zirui Wang, Karthik Narasimhan

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20518v1](https://arxiv.org/pdf/2610.20518v1)

**Abstract**: Today's agentic systems are typically designed, built, and deployed by single developers with full control over all participating agents. While this simplifies development, it limits the potential scale of agentic systems. We study multi-developer agentic systems (MDAs) which enable developers to collaboratively build agentic systems to push frontier capability beyond what any individual developer could achieve alone. We construct empirical and theoretical models of developers to compare MDAs with single-developer agentic systems (SDAs). On GAIA, a general assistant benchmark, a population of specialized developers whose individual agents do not exceed 35% accuracy reaches 70% when their agents are combined in an MDA. This MDA performs 12 percentage points above the median general-purpose SDA built with several times each specialist's development budget. Our theoretical models show how MDAs can incentivize specialization and encourage more efficient use of aggregated developer resources. Put together, our results make a preliminary case for MDAs as a new scaling axis by enabling developers with diverse capabilities and resources to advance agentic AI collaboratively.


### Bayesian Learning to Select Fair Classifiers
**Authors**: Saatvik Kher, Hyungrok Do, Judy Zhong, Padhraic Smyth

**Published Date**: 2026-10-14

**Updated Date**: 2026-10-14

**PDF Url**: [2610.20514v1](https://arxiv.org/pdf/2610.20514v1)

**Abstract**: Evaluations of classifiers (AI or human or agents) often assume a batch setting in which every agent produces labels on every example in a test set, which can be expensive or impractical in many contexts. This motivates online policies that adaptively select agents to query as examples arrive and update policies as outcomes are observed. We study the problem of selecting, in an online stream, the agent that best balances (i) predictive performance and (ii) subgroup fairness of a sensitive attribute, and that allows for delayed observations of true class labels. We formulate this as a Bayesian multi-armed bandit problem using Thompson Sampling, explicitly balancing accuracy and fairness. We conduct empirical evaluations on real-world datasets spanning problems involving tabular classifiers, large language models, and human labelers, demonstrating substantial reductions in regret relative to baselines. Our theoretical contributions include guarantees on the performance of the selected agent that incorporate both the accuracy and fairness aspects of the problem.


