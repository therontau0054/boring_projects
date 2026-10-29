# Abstracts of Papers

## World Model
### ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning
**Authors**: Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37666v1](https://arxiv.org/pdf/2610.37666v1)

**Abstract**: Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning from them faces a fundamental trade-off between scalable data and explicit action grounding. We introduce ThinkWorld, a VLA learning framework that grounds action reasoning in world dynamics and strengthens it through reinforcement learning with world imagination. ThinkWorld represents each action thought as a Chain-of-Dynamics (CoD), a sequence of discrete motion tokens that captures the intermediate dynamics connecting the current world to a future state and serves as a common action representation across embodiments. We first initialize CoD with action-labeled demonstrations, then predict the future induced by each CoD and reinforce those whose predictions better match the observed outcome. This enables videos without action annotations to provide direct supervision from observed state transitions, allowing human and robot experience to refine the same reasoning space. Experiments in simulation and on real robots demonstrate effective human-to-robot transfer and strong generalization to unseen tasks and environments.


### When Should We Intervene at Test Time?
**Authors**: Jiahao Zhang, Xinling Wen, Liangliang Li, Yu Chen

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37658v1](https://arxiv.org/pdf/2610.37658v1)

**Abstract**: Test-time adaptation helps a deployed model respond to changing inputs, but the same intervention can rescue one batch and damage the next. Updating normalization statistics, for example, can improve corrupted images yet fail when a batch contains mostly one class. Average accuracy hides these failures and cannot tell a model when to use an intervention. Target labels can guide this decision, but they are scarce and some choices are already clear. We introduce PORTAL, a controller that chooses when to deploy an intervention, which inputs to label, and when to stop querying. Each available prediction rule is a candidate, and its predictions are fixed before current feedback arrives. Every acquired label therefore evaluates all candidates on the same input. PORTAL combines these shared comparisons and directs queries toward candidates that can still overtake the current leader. It stops when the remaining labels cannot change the choice or when the possible accuracy gain no longer justifies another query. Our analysis links the required feedback to accuracy gaps and shared mistakes, explaining why some choices need much less evidence. Experiments show that this control turns an intervention that loses accuracy overall into a useful choice on selected batches. It prevents severe failures caused by changes in arrival order and preserves gains across complete corruption streams. When a fixed rule already works well, PORTAL uses little feedback to retain its performance. Periodic label checks reveal when past evidence needs refreshing and help the controller recover as conditions change. The acquired labels also train stronger candidates for future batches, and selection brings nearly all of their accuracy gains into deployment. The same feedback therefore improves both the choice made now and the predictions available to later batches.


### Heads of Security: Learned Attention Gates Improve Prompt Injection Robustness
**Authors**: Igor Shilov, Xiaoxue Yang, Alexander Panfilov, Evgenii Kortukov, Matthieu Meeus, Peter Romov, Wojciech Samek, Jonas Geiping, Yves-Alexandre de Montjoye

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37657v1](https://arxiv.org/pdf/2610.37657v1)

**Abstract**: We introduce Heads of Security (HoS), a prompt injection defense that enforces instruction-data separation via a small set of learned per-head attention gates. HoS learns how each head should redistribute attention between trusted and untrusted tokens, enabling models to reason over untrusted content without following injected instructions. We evaluate HoS on Llama-3.3-70B-Instruct and GPT-OSS-20B. We compare it against SecAlign++, a state-of-the-art finetuning-based defense, and ASIDE, a defense that, like ours, builds instruction-data separation into the model architecture. We show that HoS offers greater robustness to adaptive attacks, better performance on standard utility benchmarks, and matches top performance on standard agentic prompt injection benchmarks. More specifically, the black-box RL-Hammer attack reaches 97% ASR against GPT-OSS-20B and 85% against SecAlign, but only 10% against HoS. Claudini, a state-of-the-art white-box attack, strengthened against HoS through autoresearch, requires 3 times more FLOPs to reach the same ASR on HoS as it does on GPT-OSS-20B or SecAlign. HoS preserves base-model utility across standard multiple-choice benchmarks and prompting setups, whereas SecAlign and ASIDE degrade in few-shot settings. On agentic benchmarks with static attacks, HoS and SecAlign perform similarly and substantially improve the security-utility trade-off over the base model. ASIDE struggles with tool use, achieving only 10% utility. These results show that prompt injection robustness can be achieved and improved through targeted attention interventions.


### KPPax: preprocess differentiable kinetic ODE for machine learning in atmospheric chemistry
**Authors**: Wenqing Peng, Michael Boy, Zhi-Song Liu

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37655v1](https://arxiv.org/pdf/2610.37655v1)

**Abstract**: Atmospheric chemical mechanisms are commonly distributed in the language of the Kinetic PreProcessor (KPP), which generates efficient Fortran or C code but does not fit into the differentiable programming frameworks in which machine-learning models are developed. We present KPPax, a kinetic preprocessor that generates differentiable, just-in-time compiled, and vectorisable chemistry code in JAX from mechanisms written in the KPP language. KPPax evaluates the rate law with sparse operations in log space, which keeps it differentiable, and integrates the stiff system with the implicit solvers and the forward- and reverse-mode adjoints of the \texttt{diffrax} library, so that exact sensitivities are obtained without hand-derived adjoint code. We demonstrate two applications with the POLLU benchmark mechanism. In the first, the Fisher information matrix computed from an automatically differentiated Jacobian predicts, before any fit, which of the 25 rate coefficients a flow-tube-like design can identify, and noisy synthetic estimation confirms the predicted uncertainties of the nine identifiable rate coefficients to within about 30\% while revealing clusters of fast reactions of which only ratios are constrained. In the second, a neural-network correction of an emission inventory is trained offline on per-scenario 4D-Var retrievals and then fine-tuned online through the chemical model, which reduces the error of the biogenic correction by a factor of 2.4--5 and recovers information on low-temperature emissions that the individual retrievals lose. KPPax makes KPP mechanisms directly usable for parameter estimation and hybrid physics--machine-learning modelling.


### Can LLMs Uncover Hidden Physical Laws through Free Exploration?
**Authors**: Zhen Yang, Wen Wang, Xander Xu, Ying-Cong Chen

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37649v1](https://arxiv.org/pdf/2610.37649v1)

**Abstract**: Scientific discovery often begins with an unexpected observation that prompts a new research question. In a world with altered physical laws, can large language models (LLMs) notice unexpected behavior, such as heavier objects falling more slowly, and discover the law through experiments without being told what to investigate? To evaluate this ability, we introduce LongChang, an automated framework that creates simulated worlds with altered physics, where one or more laws differ from ordinary physics. The evaluated LLMs act as explorers, manipulating objects and building tools to investigate their own questions without research tasks or hints about these laws. Separate LLM agents generate and review scenes, review tool designs, and evaluate reports for correctness and experimental support using the altered physical laws and exploration records. These records guide scene evolution for further exploration, allowing the full cycle to run without human intervention. Among 12 LLMs, GPT-6-Astra achieves a discovery rate of 16.7%, while the other 11 score 0%. The exploration records reveal uninvestigated anomalies and only partial identification of the altered physical laws.


### Scaling Laws for Tool-Use Agents via Controllable Environment Synthesis
**Authors**: Andrew Szot, Samira Abnar, Omar Attia, Abbas Kazerouni, Michael Kirchhof, Cheng-Yu Hsieh, Raviteja Vemulapalli, Alexander Toshev

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37648v1](https://arxiv.org/pdf/2610.37648v1)

**Abstract**: We explore how to build performant large language model (LLM) tool-use agents that complete complex, multi-step tasks. Specifically, we study how data composition in synthetically generated tool-use environments affects the training of such agents. To do so, we propose the SynthAPI pipeline, which explicitly controls the diversity of generated environments along the axes of tools, tasks, and the databases on which the tools operate. By systematically varying SynthAPI's generation controls in 458,752 tasks across 849 trained models of four different sizes, we derive a scaling law that predicts downstream tool-use agent generalization based on the scale and composition of the synthesized environments. These predictable relationships reveal several lessons for scaling tool-use agent data. As data budgets grow, scaling tool and database diversity becomes more effective than increasing the number of tasks, and increasing data complexity yields larger gains. Scaling according to these findings yields agents that outperform models trained on data from prior work in large-scale tool-use agent and synthetic environment generation across four evaluation benchmarks.


## Generation
### Honeycomb-Surfels: Compact Hexagonal Primitives for Efficient Scene Rendering and Reconstruction
**Authors**: Prakhar Kaushik, Soumava Paul, Alan Yuille

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37668v1](https://arxiv.org/pdf/2610.37668v1)

**Abstract**: Novel view synthesis and 3D reconstruction have advanced rapidly with radiance fields and splatting, yet their memory and computational demands limit their use in resource-constrained settings. We introduce Hexels: novel planar hexagonal surface elements with a first-order spatial color field for efficient 3D scene and 2D image representation. Hexels exploit locally planar regions with smoothly varying appearance using fewer, larger primitives. Their hexagonal support provides an area- and boundary-efficient domain, while the local color field captures appearance variation within each primitive. Across 34 scenes, Hexels improve PSNR over memory-matched 2DGS by 4.53-7.38 dB across datasets while requiring lower training VRAM. We further ablate Hexels by showing that per primitive, Hexels outperform 2DGS by upto 4.74 dB while using lower training VRAM and having 2.31 times faster FPS. Even in unconstrained settings, Hexels offers complementary quality-memory trade-offs. For efficient 3D surface reconstruction, Hexels reduce error by 28.9% compared with memory-matched 2DGS across 15 DTU scans. On 6 Tanks and Temples surface scenes, Hexels achieves the highest mean F1 among compared methods (34.38%, versus 31.72% for 2DGS). We further also show that Hexels, as a general primitive, improves 2D image representation over Image-GS. Hexels push the Pareto frontier on the quality-efficiency trade-off of surface-aligned primitives.


### Attention as Lattice Gauge Theory: Relations Interact Only Through Wilson Loops
**Authors**: Aakash Sarkar, Ananya Mukherjee, Motoshige Sato

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37656v1](https://arxiv.org/pdf/2610.37656v1)

**Abstract**: Relations compose through the entity they share - Alice is Bob's mother and Bob is Carol's father, so Alice is Carol's grandmother - and the order matters, since a father's mother is not a mother's father; verifying a composed relation means closing the loop. We show that if each entity's coordinate frame may be rotated independently (per-entity frame freedom), three things follow. In the pure-gauge sector, relations that share no cycle cannot interact at all. The only gauge-invariant score of a triangle is a class function of its holonomy $H = T_{ij} T_{jk} T_{ki}$ - a Wilson loop. And the only equivariant update of an edge is $U = Ψ(H)\, T_{ij}$ with $Ψ$ conjugation-equivariant. Edge attention by Wilson loops is therefore not one design among many but the unique form the symmetry permits. Three communities hold pieces of this form: the commuting-operator embeddings of knowledge graphs are its abelian (commuting) sector; AlphaFold's triangle update and the Edge Transformer have its shape - an edge updated through the third vertex - without its constraints; and lattice QCD builds it equivariantly on lattices. We instantiate the equivariant sub-family on general relational graphs as holonomy attention. With no training and composition alone, it infers unobserved $S_4$ relations on sparse graphs at 0.88 with a fifth of the edges corrupted, at or slightly below specialist synchronization algorithms, where every commutative architecture is capped at 0.083; its holonomy score flags corrupted triangles at AUC 0.99 where commuting scores are capped at 0.76 by a second selection rule, and it separates clusters without labels.


### Pushing Dexterity and Safety for In-Hand Object Pose Reaching That Works Remarkably Well
**Authors**: Ian Chuang, Hiya Shah, Vamsi Chilamkur, Iman Soltani, Claire Tomlin

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37652v1](https://arxiv.org/pdf/2610.37652v1)

**Abstract**: Dexterous manipulation with multi-fingered hands is the next frontier of robotics, yet learned hand skills remain limited to simple grasps or basic repeated motions, such as rotating an object. As robots attempt more demanding in-hand maneuvers, safety, such as not dropping the object, becomes critical, yet it is rarely measured. We study in-hand object pose reaching, a task that demands diverse and difficult grasps: moving an object to almost any position and orientation within reach of the fingers, at any wrist orientation, through long sequences of consecutive goals. We present a recipe for training such policies for a LEAP hand in simulation without human data, built on a range of insights, from diverse resets and goals via generated grasp datasets to an adaptive friction curriculum. With careful system identification, the policies transfer zero-shot to the real hand, using either motion capture or a single wrist-mounted depth camera, and prove remarkably capable and robust. On top of the task policy, we add a learned residual safety filter with adjustable conservativeness, letting us tune the balance between performance and safety and greatly reduce object drops. In 13.3 hours of real-robot evaluation over 4,800 unseen goals across 4 objects and diverse wrist orientations, the state-based policy reaches 95.2% of goals within 2 cm and 0.4 rad, and the filter cuts its drops by 75% while still reaching 91.5% of goals. The policies can also spin a lightbulb held in an arbitrary pose, reach out-of-distribution goals, withstand fast arm motion and perturbations, and, needing only a wrist camera, serve as portable skills such as screwing in a lightbulb. We release the full recipe as a platform for studying performance, reliability, and safety in high-dimensional dexterous systems. Videos and more are available at https://ian-chuang.github.io/dexsafe/.


### What Improves During Pretraining? Tracking Knowledge Acquisition with Point-in-Time Models
**Authors**: Chang Su, Bin Wu, Emine Yilmaz, Yao Lu

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37631v1](https://arxiv.org/pdf/2610.37631v1)

**Abstract**: Language models pretrained on web corpora collected over multiple years learn both general and domain-specific knowledge. How these different kinds of knowledge are learned as pretraining progresses remains unclear. Recent point-in-time models trained on web snapshots from different years provide a way to probe how knowledge prevalence varies over time. Using these models, we propose a temporal variability score (TVS), defined as the coefficient of variation of an item's negative log-likelihood across models. A higher score suggests that the knowledge may be less consistently represented across years of web text. We evaluate six benchmarks covering diverse topics using six models from multiple open-source model families. We find that low- and high-TVS items are learned similarly early in training, but high-TVS items improve faster later on. At the end of the pretraining run, high-TVS items outperform low-TVS items in 34 of 36 model-benchmark settings, with an average advantage of 7.3 points of chance-normalized accuracy. This pattern is most robust on knowledge-intensive tasks, even when comparing items of similar difficulty. Our findings reveal differences in how knowledge is learned over the course of pretraining, with temporal variability providing a diagnostic of these learning dynamics beyond aggregate benchmark scores.


### VideoLVR: Latent Visual Reasoning over Grounded Video Evidence
**Authors**: Shilong Li, Xingyuan Bu, Hao Shi, Yun Xing, Weixin Feng, Qiangpeng Yang, Shilei Wen

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37613v1](https://arxiv.org/pdf/2610.37613v1)

**Abstract**: Chain-of-thought reasoning has substantially advanced video understanding in multimodal large language models (MLLMs). However, language-based reasoning traces do not provide a reliable mechanism for models to revisit relevant visual evidence, leading to visual forgetting and impairing their ability to reason over video content. Existing approaches maintain visual grounding during reasoning in two main ways: they either refer to evidence using textual coordinates, which specify symbolic locations rather than the visual content itself, or reinsert cropped regions or frames into the multimodal context, preserving visual details at the cost of substantial context expansion. To address these limitations, we introduce VideoLVR, which constructs latent visual evidence from local regions at relevant video moments, thereby providing visual support for intermediate reasoning steps. To supervise latent visual evidence generation, we introduce a visual token prediction objective that formulates visual token reconstruction as prediction over a vocabulary derived from the input video, thereby unifying visual evidence reconstruction and text generation within the same token prediction framework. This shared prediction framework enables MLLMs to reason over interleaved text tokens and latent visual states while integrating evidence from different moments. We further extend VideoLVR to reinforcement learning by treating sampled visual tokens as actions alongside text tokens and jointly optimizing the policy using final-answer rewards. By efficiently revisiting task-relevant visual information during reasoning, VideoLVR improves video understanding without substantially expanding the multimodal context. Experiments on multiple video benchmarks demonstrate its effectiveness, especially on tasks requiring fine-grained visual evidence.


### EnvSched: Environment-Aware Scheduling for Rollout-Efficient Agent Reinforcement Learning
**Authors**: Sihan Yang, Weichen Bai, Ruichuan An, Yiming Cheng, Zhiyuan Feng, Tianyi Jiang, Renye Yan, Ning Ding, Yifan Zhang, Renrui Zhang, Yehui Tang, Wentao Zhang

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37609v1](https://arxiv.org/pdf/2610.37609v1)

**Abstract**: As executable environments for language agents scale, generating and verifying their rollouts becomes increasingly expensive. Under finite rollout budgets, this raises an important question: can data management at the environment level make agentic reinforcement learning (RL) more efficient by organizing, evaluating, and scheduling task instances together with the environments that determine their tools, states, transitions, and verification? To address this question, we introduce EnvSched (Environment-aware Scheduling), an online scheduler that learns from rollout history. EnvSched assigns scheduling value through two complementary modeling choices: exploitation prioritizes tasks likely to provide informative reward differences, while coverage spreads each batch across underobserved environments and interaction patterns. EnvSched organizes environment--task pairs as nodes in a dual-relation graph, with within-environment edges capturing task semantics and shared tool, state, and verifier structure, and cross-environment edges capturing abstract execution and reward topology. By propagating historical rollout statistics along both edge types, it predicts within-task reward variance. These predictions guide a scheduler that allocates each batch to tasks with high predicted reward variance and underobserved environments and tasks. Environment quotas and a similarity penalty further limit concentration and redundancy, yielding informative and diverse batches without additional pilot rollouts. In RL on Qwen3-8B, EnvSched achieves an average score of 48.81 across BFCL-v3, tau-Bench, and ACEBench-Agent after 40 training steps, exceeding the highest score attained by random task selection after 120 steps. It also improves downstream performance across model sizes at the same training budget.


## VLA
### PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations
**Authors**: Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37381v1](https://arxiv.org/pdf/2610.37381v1)

**Abstract**: Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We introduce PDRVLA, whose lightweight Physical Dynamics Module extracts physical tokens from vision--language features to condition action generation without online video generation. The module learns through direct prediction of future RGB, depth, and optical-flow features, with auxiliary supervision through a frozen pretrained video world model. Training relies entirely on publicly available data, expanded through human-to-robot synthesis, subtask annotation, and embodied chain-of-thought (ECoT) annotation. Across four simulation benchmarks, PDRVLA achieves success rates of 99.3% on LIBERO, 89.9% on LIBERO-Plus, 93.6% on RoboTwin~2.0, and 81.5% on SimplerEnv. Ablations show improved future prediction with world-model supervision and evaluate how subtask conditioning, future object-pose supervision, and ECoT training affect action success.


### Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution
**Authors**: Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen, Duc-Duy Nguyen, Hung T. Ho, Linh Dang Le, Trong-Bao Ho, Thien-Loc Ha, Tan Q. Nguyen, Tuan Dam, Vu N. Duong, Daniel Sonntag, Ngan Le, Khoa D. Doan, Jan Peters, An Thai Le, Duy M. H. Nguyen, Vien Anh Ngo

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37215v1](https://arxiv.org/pdf/2610.37215v1)

**Abstract**: Vision-Language-Action (VLA) policies demonstrate remarkable semantic generalization, yet remain highly vulnerable to out-of-distribution (OOD) visual shifts during execution. While existing test-time methods attempt to suppress spurious visual cues, they fundamentally overlook the rich, uncorrupted kinematic priors embedded in the policy's own training experience. We introduce Retrieve to Act (R2A), a test-time scaling framework that formulates OOD robustness purely as a geometric motion primitive retrieval problem. R2A bypasses fragile visual features by structuring successful training demonstrations into an offline spatiotemporal motion primitive graph. During inference, a query-dependent Graph Neural Network dynamically localizes the robot's ongoing execution within this graph, retrieving structurally compatible future motion primitives. These retrieved geometric priors are then seamlessly harmonized with the frozen VLA's predicted actions via a learned, dimension-wise gating mechanism, adaptively rectifying erroneous spatial trajectories while preserving the policy's local reactivity. Extensive experiments across three state-of-the-art VLA architectures, GR00T N1.7, $π_{0.5}$, and StableVLA, demonstrate that R2A consistently and significantly enhances robustness against diverse contextual perturbations. R2A achieves absolute success rate improvements of up to +12% in simulation benchmarks (LIBERO-Plus, RoboTwin2.0-Plus) and +40% in real-world deployments, without requiring any finetuning of the base policies. Project page: https://retrieve2act.github.io/r2a/


### Power-of-Two Leaky Integrate-and-Fire Neurons for Event-Driven Vision-Language-Action Inference
**Authors**: Rui Liu, He Lv, Ziyao Zhang, Rui Ma, Rongxiang Nie

**Published Date**: 2026-10-24

**Updated Date**: 2026-10-24

**PDF Url**: [2610.33658v1](https://arxiv.org/pdf/2610.33658v1)

**Abstract**: Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, yet their reliance on dense, continuous-valued computation presents a fundamental challenge for energy-constrained deployment. Inspired by the sparse, event-driven signaling and temporal integration mechanisms of biological neurons, a promising alternative is to introduce spiking computation into VLA models. However, enabling such computation without restructuring pretrained policies or compromising closed-loop control remains an open challenge. To address this challenge, we introduce the Power-of-Two Leaky Integrate-and-Fire (PoT-LIF) neuron, which emits signed spikes with power-of-two amplitudes. By combining magnitude-coded spike events with residual-preserving membrane dynamics, PoT-LIF enables continuous information to be progressively represented through discrete spikes. The Heartbeat formulation further localizes this process within weighted projections, bridging biologically inspired spiking computation and pretrained VLA architectures without modifying their external inference interfaces. We integrate PoT-LIF into the vision projection, vision-language projection, and action projection of $π_{0.5}$ and evaluate both operating modes over 2,000 paired closed-loop LIBERO episodes per configuration. Standard-mode PoT-LIF VLA achieves success rates of 96.90% and 96.35% at $T = 1$ and $T = 2$, respectively, while Heartbeat mode achieves 97.25% and 96.90% at $T = 2$ and $T = 4$, compared with 96.70% for the original continuous-activation $π_{0.5}$ baseline. At $T = 1$ with a 60.01% firing rate, PoT-LIF uses approximately 1/7.67 of the dense-reference arithmetic energy, corresponding to a modeled reduction of 86.95%.


### TAD: Distilling Vision-Language-Action Policies from Teacher Trajectories Alone
**Authors**: Yun Zhu, Da Wang

**Published Date**: 2026-10-24

**Updated Date**: 2026-10-24

**PDF Url**: [2610.33650v1](https://arxiv.org/pdf/2610.33650v1)

**Abstract**: Online distillation of vision-language-action (VLA) policies commonly relies on teacher action scores that an inference-only interface may not expose. Trajectory-only Adversarial Distillation (\gad{}) instead turns a fixed bank of teacher joint-position features into adaptive feedback: a discriminator compares feature marginals from teacher and student rollouts and supplies rewards for on-policy learning. The student interacts with the environment without online teacher queries or environment task rewards. On ManiSkill \texttt{PutOnPlateInScene25Main}, \gad{} improves OpenVLA-OFT (7B) from $26.2\%$ to $76.6\%$ \successonce{} ($+50.4$ percentage points) and from $20.3\%$ to $58.6\%$ \successend{}. It trails white-box on-policy distillation (OPD) at $81.6\%$ / $59.4\%$ by $5.0$ / $0.8$ percentage points ($n{=}256$ evaluation trajectories per checkpoint). The tested four-epoch continuation achieves the highest \gad{} result without additional teacher data. This best run uses $5\times$ OPD's student interaction budget and $12.5\times$ its complete-rollout batch-passes. The comparison demonstrates online VLA improvement without teacher scoring while quantifying unequal interaction and optimization budgets.


### If at First You Don't Succeed, Backtrack: Lightweight Recovery for Frozen VLAs
**Authors**: Thomas Landeg, Thierry Tambe

**Published Date**: 2026-10-23

**Updated Date**: 2026-10-23

**PDF Url**: [2610.32941v1](https://arxiv.org/pdf/2610.32941v1)

**Abstract**: Vision-Language-Action (VLA) models perform well on robotic manipulation, yet remain brittle once their own actions carry them into states their training data barely covers. Recovering from such failures usually requires recovery demonstrations, policy retraining, or a separate model at inference time. We introduce Backtrack, a lightweight failure detection and recovery mechanism for frozen VLAs that needs none of these. A small failure prediction head, trained only on outcome-labeled rollouts of the frozen policy, reads the VLA's existing internal representations to estimate whether the current episode will fail. When the predicted failure probability exceeds a threshold, a controller pauses the policy, retraces the arm's recently achieved motion, and hands control back to the unchanged policy so it can retry from an earlier configuration. The head adds only 0.48-0.88% to the policy's parameter count. We evaluate Backtrack on LIBERO with three VLAs spanning two action-generation families: SmolVLA and $π$0.5, which use flow-matching action experts, and the autoregressive $π$0-FAST. On LIBERO-Long, the suite of long-horizon multi-step tasks and the one on which all three policies fail most often, Backtrack reduces each policy's failure rate by 19-48%, raising success by up to 7.4 percentage points; on the three shorter suites, where control success is already 85-99%, its effect is smaller. On MetaWorld, all twelve controller configurations tested with SmolVLA improve on the unassisted policy.


### When Human Corrections Travel: Safety in Federated VLA Adaptation
**Authors**: Vigneshwaran Subbaraju, Obaidullah Zaland, Monowar Bhuyan

**Published Date**: 2026-10-23

**Updated Date**: 2026-10-23

**PDF Url**: [2610.32888v1](https://arxiv.org/pdf/2610.32888v1)

**Abstract**: Vision-language-action (VLA) policies can adapt to local human intervention, while federated learning can combine distributed robot experience without pooling raw records. We examine their prospective intersection: sharing adaptations derived from diverse human corrections across tasks, environments, people, and robot embodiments. Corrections differ in modality, safety semantics(urgency, behavioral scope, etc.), and privacy sensitivity. A shared update that improves mean task success may suppress a rare safety intervention or produce an unsafe response on another robot. We argue for three requirements: preserve the context and uncertainty of multimodal corrections when deciding what to share; assess candidate updates in each receiving robot's closed loop before deployment; and evaluate leakage alongside retention of safety-critical evidence. Immediate, legible defensive behavior remains necessary during human interaction. We offer counterexamples and a falsifiable evaluation agenda, not experimental results.


## Agent
### Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions
**Authors**: Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37624v1](https://arxiv.org/pdf/2610.37624v1)

**Abstract**: When an LLM group's discussion is compressed into a short memory for a final decision maker, what should the memory keep? Two natural heuristics keep the rarest claims or the claims relevant to the decision criteria. On hidden-profile tasks both look attractive, because how widely a fact is held is confounded with whether it helps. We introduce CrossProfile, a diagnostic benchmark of 60 templates with automatically verified answer keys, in which the ownership of supporting, decoy, and irrelevant facts is crossed while their text is held fixed (480 tasks). Across Qwen2.5-7B, Llama-3.1-8B, and two DeepSeek models, both heuristics fail in predictable places. Selecting by relevance readmits decoys, because decoys are on topic: even a perfect relevance filter loses 23 to 31 points to rarest-first selection in the classic hidden-profile configuration. Rarest-first selection is no better than random selection on average and wins only where the rare facts happen to be the useful ones. In both cases accuracy follows the balance of evidence the memory keeps, not the policy that kept it. The decision model adds a third failure, a form of social proof: it gives extra weight to facts attributed to many agents. Removing the attribution tags, or reassigning them at random with line order fixed, raises accuracy in the classic configuration by 13 to 24 points. In natural discussions the evidence is lost before any memory acts: the complete transcript yields lower accuracy than no notes at all.


### Understanding the limits of latent world models
**Authors**: Rodrigo Gonzalez Laiz, Steffen Schneider

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37588v1](https://arxiv.org/pdf/2610.37588v1)

**Abstract**: World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limited insight into whether learned world models acquire predictive latent dynamics that reflect the underlying structure of the environment. Here we introduce the concept of faithful latent world models as an equivariance condition between the environment's transition map and the learned latent dynamics. We propose latent rollout consistency (LRC) as a metric to evaluate action-conditioned latent prediction. Strikingly, we find that across the studied state of the art latent world models, none solves the task by actually faithfully modeling the dynamics of the environment.


### TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information
**Authors**: Chanwoo Park, Jaywoong Jeong, Zachary Wojtowicz, Yubin Kim, Taekyun Lee, Kaiqing Zhang, Asuman Ozdaglar

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37571v1](https://arxiv.org/pdf/2610.37571v1)

**Abstract**: Many real-world decisions require teams to integrate information distributed across participants. Yet AI agents are still primarily trained and benchmarked in isolation. We introduce TeamGym, an environment for evaluating and training language model-based agents on team decision-making problems constructed from real-world legal, finance, medical, and software engineering corpora. TeamGym introduces a method to identify a minimal set of facts, each element of which is necessary and all of which are collectively sufficient for a correct final decision, which we call pivotal information. This enables TeamGym to both control the distribution of pivotal information and track how well agents identify and integrate pivotal information when making team decisions. Examining 8 language models on 12 source corpora, we find that current AI agents often fail to effectively share information: Distributing pivotal information across participants lowers success rate by 22.9 percentage points on average relative to giving the same information to a single model (a communication gap). We also document that participants do not effectively retrieve decision-relevant information on their own: A team's success rate is lowered by a further 19.9 points when participants must identify and extract pivotal information from source material rather than receiving it directly (a retrieval gap). To help remedy these deficits, we use TeamGym to train policies through reinforcement learning on team decision loss. Across two policy-training experiments, we find that training improves final-decision quality and induces emergent coordination in participation, speaker selection, and communication, even though the reward evaluates only the final decision.


### Gym-Anything-RT: Scaling Real-Time Environments for Vision-Language Agents
**Authors**: Pranjal Aggarwal, Sean Welleck

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37567v1](https://arxiv.org/pdf/2610.37567v1)

**Abstract**: AI agents have made substantial progress in domains where they have a non-trivial amount of time to deliberate between actions, such as mathematics, software engineering, and performing tasks on desktop applications. It is less clear how such models fare in settings that demand real-time interaction, such as playing a video game or operating a physical device. In these settings, the environment state may evolve as the agent is reasoning, or even as the underlying model is performing a forward pass. To gain insight into the real-time interaction capabilities of vision-language agents, we introduce Gym-Anything-RT. Our key idea is to construct visual minigames that demand a portfolio of capabilities required for interactive real-time settings. Gym-Anything-RT uses an agentic pipeline to automatically generate such environments based on a taxonomy of six capabilities required for real-time interaction, including the ability to perceive the environment and act under an evolving environment state. A key feature of Gym-Anything-RT is that it allows for controlled comparison of real-time interaction capabilities: we can run the same minigame in real time, or pause or slow down the environment to relax the requirement for real-time actions. We use Gym-Anything-RT to construct 100 real-time minigames and evaluate AI agents on them. We find large capability gaps in real-time interaction. For example, GPT-6 Astra (xHigh) achieves a pass rate of only 9.0% on the real-time minigames, which rises to 75.0% when the environment is paused. We also identify intriguing behaviors by the most powerful frontier agents: for instance, when given the ability to write code, these agents write code that bypasses the need to perceive and act in real time. We publicly release Gym-Anything-RT and the generated minigames to spur further research on AI agents in real-time interactive settings.


### Strategyproof Deep Reinforcement Learning for Online Resource Allocation
**Authors**: Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah, Stephanie Gauthier

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37504v1](https://arxiv.org/pdf/2610.37504v1)

**Abstract**: Online resource allocation faces two coupled challenges: (1) allocating scarce resources efficiently under uncertain future demand, and (2) ensuring that agents report task valuations and requirements truthfully (strategyproofness). Reinforcement Learning (RL) adapts allocation decisions through experience but does not necessarily ensure strategyproofness. Existing strategyproof RL uses a linear allocation rule, which limits the resource interactions it can represent. Neural mechanism design methods offer greater expressiveness, but provide only approximate incentive guarantees. Against this background, we introduce the first strategyproof deep RL mechanism for online resource allocation. It integrates three novel components: (i) a monotonic neural network that learns nonlinear interactions by construction (higher reported value cannot reduce acceptance, while a longer reported duration or larger resource requirement cannot increase it); (ii) a generalised critical payment: the lowest accepted value, with all other inputs fixed; and (iii) training by either RL or imitation of an existing rule. Together, monotonicity and the critical payment ensure strategyproofness and individual rationality, while the neural rule provides flexibility and imitation improves training efficiency. Empirically, on a four-resource stream with two partner pairs that a linear difference cannot represent, the neural rule achieves 97.8% of an offline welfare upper bound, compared with 93.8% for a linear learner and 89.0% for first-come, first-served, closing 65% and 80% of the remaining optimality gap, respectively. Moreover, imitation reaches 97.5% in only 261 seconds, about 89 times faster than RL.


### From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents
**Authors**: Ziyang Chen, Qian Li, Chengwei Qin

**Published Date**: 2026-10-27

**Updated Date**: 2026-10-27

**PDF Url**: [2610.37482v1](https://arxiv.org/pdf/2610.37482v1)

**Abstract**: GUI memory should preserve the results of past actions and learn reusable operations. This is difficult in long-horizon workflows, where agents must use information across applications and useful operations are interleaved with failed attempts. We introduce Task Advancement Memory (TAM), which defines task advancement as verified task progress, and supports ongoing task execution and learns reusable operations. During execution, Task Advancement State represents how verified task progress changes the remaining goals, allowing the agent to build on earlier achievements across applications. After each task, advancement supervision identifies and abstracts the interactions that produced a verified local result. The learned operations preserve the relation between required inputs, expected outcomes, and verification conditions. This retains locally successful operations from both successful and failed tasks. On MobileWorld GUI-only tasks, Advancement State alone raises success from 12.0% to 28.2%. Full TAM achieves a 17.6% relative gain in task success over the strongest evaluated baseline and reduces lifecycle tokens per solved task by 38.7%. On SPA-Bench, TAM achieves state-of-the-art task success in the single-app English Level 3 setting.


