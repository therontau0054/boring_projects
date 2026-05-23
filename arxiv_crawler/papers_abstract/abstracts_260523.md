# Abstracts of Papers

## World Model
### Tokenisation via Convex Relaxations
**Authors**: Jan Tempus, Philip Whittington, Craig W. Schmidt, Dennis Komm, Tiago Pimentel

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22821v1](https://arxiv.org/pdf/2605.22821v1)

**Abstract**: Tokenisation is an integral part of the current NLP pipeline. Current tokenisation algorithms such as BPE and Unigram are greedy algorithms -- they make locally optimal decisions without considering the resulting vocabulary as a whole. We instead formulate tokeniser construction as a linear program and solve it using convex optimisation tools, yielding a new algorithm we call ConvexTok. We find ConvexTok consistently improves intrinsic tokenisation metrics and the bits-per-byte (BpB) achieved by language models; it also improves downstream task performance, but less consistently. Furthermore, ConvexTok allows the user to certify how far their tokeniser is from optimal, with respect to a certain objective, via a lower bound, and we empirically find it to be within 1\% of optimal at common vocabulary sizes.


### Which Way Did It Move? Diagnosing and Overcoming Directional Motion Blindness in Video-LLMs
**Authors**: Jongseo Lee, Hyuntak Lee, Sunghun Kim, Sooa Kim, Jihoon Chung, Jinwoo Choi

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22823v1](https://arxiv.org/pdf/2605.22823v1)

**Abstract**: Video Large Language Models (Video-LLMs) have made rapid progress on temporal video understanding, yet many fail at a basic perceptual primitive: signed image-plane motion direction. On simple videos of a single object moving left, right, up, or down, most Video-LLMs perform near chance, with above-chance cases largely attributable to prediction biases rather than genuine direction understanding. We call this failure directional motion blindness. We localize the failure by tracing motion direction information through the Video-LLM pipeline. Motion direction remains linearly accessible from the vision encoder, projector, and LLM hidden states, but the readout fails to bind this signal to the correct verbal answer option, revealing a direction binding gap. Although synthetic motion direction instruction tuning reduces this gap on the source domain, motion direction concept vector analysis shows that visual complexity weakens the signal magnitude and limits out-of-domain generalization. We introduce MoDirect, a dataset family for motion direction instruction tuning and evaluation, and DeltaDirect, a diagnosis-driven, projector-level objective that predicts normalized 2-D motion vectors from adjacent-frame feature deltas. On MoDirect-SynBench, instruction tuning with DeltaDirect improves motion direction accuracy from 25.9% to 85.4%. On MoDirect-RealBench, DeltaDirect improves real-world motion direction accuracy by 21.9 points over the vanilla baseline without real-world tuning data, while preserving standard video-understanding performance. Code: https://github.com/KHU-VLL/DeltaDirect


### Integrable Elasticity via Neural Demand Potentials
**Authors**: Carlos Heredia, Daniel Roncel

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22820v1](https://arxiv.org/pdf/2605.22820v1)

**Abstract**: We propose the Integrable Context-Dependent Demand Network (ICDN), a demand-first neural model for multiproduct retail demand. The model learns log-demand as a smooth, context-conditioned function of log-prices, allowing elasticities to be derived exactly from the learned demand surface. On the Dominick's beer dataset, ICDN improves out-of-sample generalization over a directed log-log benchmark and yields more stable, economically plausible elasticity estimates, especially for weakly identified cross-price effects.


### Cambrian-P: Pose-Grounded Video Understanding
**Authors**: Jihan Yang, Zifan Zhao, Xichen Pan, Shusheng Yang, Junyi Zhang, Bingyi Kang, Hu Xu, Saining Xie

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22819v1](https://arxiv.org/pdf/2605.22819v1)

**Abstract**: Camera pose matters. The position and orientation of each viewpoint define a shared spatial coordinate frame that relates observations across video frames. Yet this signal is largely absent from multimodal LLMs (MLLMs) for video understanding, which process frames as isolated 2D snapshots, instead of the persistent scene humans perceive. We revisit pose as a lightweight supervisory signal and introduce Cambrian-P, a video MLLM augmented with per-frame learnable camera tokens and a pose regression head. With a carefully designed sampling scheme, the model achieves substantial gains of 4.5-6.5% on spatial reasoning benchmarks such as VSI-Bench, generalizes across eight additional spatial and general video QA benchmarks, and, as a byproduct, achieves state of the art streaming pose estimation on ScanNet. Surprisingly, training on pseudo-annotated poses from in-the-wild video further improves general video QA benchmarks, showing pose helps beyond spatial reasoning. Together, these results position camera pose as a fundamental signal for video models that reason about the physical world.


### Vector Policy Optimization: Training for Diversity Improves Test-Time Search
**Authors**: Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong, Pulkit Agrawal

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22817v1](https://arxiv.org/pdf/2605.22817v1)

**Abstract**: Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Policy Optimization (VPO), an RL algorithm that explicitly trains policies to anticipate diverse downstream reward functions and to produce diverse solutions. VPO exploits that rewards are often vector-valued in practice, like per-test-case correctness in code generation or, say, multiple different user personas or reward models. VPO is essentially a drop-in replacement for the GRPO advantage estimator, but it trains the LLM to output a set of solutions where individual solutions specialize to different trade-offs in the vector reward space. Across four tasks, VPO matches or beats the strongest scalar RL baselines on test-time search (e.g. pass@k and best@k), with the gap widening as the search budget grows. For evolutionary search, VPO models unlock problems that GRPO models cannot solve at all. As test-time search becomes more standardized, optimizing for diversity may need to become the default post-training objective.


### Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration
**Authors**: Lily Goli, Justin Kerr, Daniele Reda, Alec Jacobson, Andrea Tagliasacchi, Angjoo Kanazawa

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22814v1](https://arxiv.org/pdf/2605.22814v1)

**Abstract**: Exploration is a prerequisite for learning useful behaviors in sparse-reward, long-horizon tasks, particularly within 3D environments. Curiosity-driven reinforcement learning addresses this via intrinsic rewards derived from the mismatch between the agent's predictive model of the world and reality. However, translating this intrinsic motivation to complex, photorealistic environments remains difficult, as agents can become trapped in local loops and receive fresh rewards for revisiting forgotten states. In this work, we demonstrate that this failure stems from a lack of spatial persistence and episodic context. We show that effective curiosity requires a model of the world that is persistent and continuously updated, paired with an agent that maintains an episodic trajectory history to navigate toward novel regions. We achieve this using an online 3D reconstruction as a persistent model of the world, while the agent policy is parameterized as a sequence model over RGB observations to maintain episodic context. This design enables effective exploration during training while allowing the agent to navigate using solely RGB frames at deployment. Trained purely via curiosity on HM3D, our agent outperforms RL-based active mapping baselines and generalizes zero-shot to Gibson and AI-generated worlds. Our end-to-end policy enables efficient adaptation to downstream tasks, such as apple picking and image-goal navigation, outperforming from-scratch baselines. Please see video results at https://recuriosity.github.io/.


## Generation
### Finite-Particle Convergence Rates for Conservative and Non-Conservative Drifting Models
**Authors**: Krishnakumar Balasubramanian

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22795v1](https://arxiv.org/pdf/2605.22795v1)

**Abstract**: We propose and analyze a conservative drifting method for one-step generative modeling. The method replaces the original displacement-based drifting velocity by a kernel density estimator (KDE)-gradient velocity, namely the difference of the kernel-smoothed data score and the kernel-smoothed model score. This velocity is a gradient field, addressing the non-conservatism issue identified for general displacement-based drifting fields. We prove continuous-time finite-particle convergence bounds for the conservative method on $\R^d$: a joint-entropy identity yields bounds for the empirical Stein drift, the smoothed Fisher discrepancy of the KDE, and the squared center velocity. The main finite-particle correction is a reciprocal-KDE self-interaction term, and we give deterministic and high-probability local-occupancy conditions under which this term is controlled. We keep the quadrature constants explicit and track their possible bandwidth dependence: the root residual-velocity rate $N^{-1/(d+4)}$ holds under an additional $h$-uniform quadrature regularity condition, while a more general growth condition yields the optimized root rate $N^{-(2-β)/(2(d+4-β))}$, where $0\le β<2$. We also analyze the non-conservative drifting method with Laplace kernel, corresponding to the original displacement-based velocity proposed in~\cite{deng2026drifting}. For this method, a sharp companion kernel decomposes the velocity into a positive scalar preconditioning of a sharp-score mismatch plus a Laplace scale-mismatch residual, producing an analogous finite-particle rate with an unavoidable residual term. Finally, we explain how the continuous-time residual-velocity bounds translate into one-step generation guarantees through the explicit drift size $η$.


### MOSS: Self-Evolution through Source-Level Rewriting in Autonomous Agent Systems
**Authors**: Qianshu Cai, Yonggang Zhang, Xianzhang Jia, Wei Xue, Jun Song, Xinmei Tian, Yike Guo

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22794v1](https://arxiv.org/pdf/2605.22794v1)

**Abstract**: Autonomous agentic systems are largely static after deployment: they do not learn from user interactions, and recurring failures persist until the next human-driven update ships a fix. Self-evolving agents have emerged in response, but all confine evolution to text-mutable artifacts -- skill files, prompt configurations, memory schemas, workflow graphs -- and leave the agent harness untouched. Since routing, hook ordering, state invariants, and dispatch live in code rather than in any text artifact, an entire class of structural failure is physically unreachable from the text layer. We argue that source-level adaptation is a fundamentally more general medium: it is Turing-complete, a strict superset of every text-mutable scope, takes effect deterministically rather than through base-model compliance, and does not erode under long-context drift. We present MOSS, a system that performs self-rewriting at the source level on production agentic substrates. Each evolution is anchored to an automatically curated batch of production-failure evidence and proceeds through a deterministic multi-stage pipeline; code modification is delegated to a pluggable external coding-agent CLI while MOSS retains stage ordering and verdicts. Candidates are verified by replaying the batch against the candidate image in ephemeral trial workers, then promoted via user-consent-gated, in-place container swap with health-probe-gated rollback. On OpenClaw, MOSS lifts a four-task mean grader score from 0.25 to 0.61 in a single cycle without human intervention.


### Gated DeltaNet-2: Decoupling Erase and Write in Linear Attention
**Authors**: Ali Hatamizadeh, Yejin Choi, Jan Kautz

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22791v1](https://arxiv.org/pdf/2605.22791v1)

**Abstract**: Linear attention replaces the unbounded cache of softmax attention with a fixed-size recurrent state, reducing sequence mixing to linear time and decoding to constant memory. The hard part is not just what to forget, but how to edit this compressed memory without scrambling existing associations. Delta-rule models subtract the current read before writing a new value, and Kimi Delta Attention (KDA) sharpens forgetting with channel-wise decay. But the active edit still uses a single scalar gate to control two different things: how much old content to erase on the key side and how much new content to commit on the value side. We introduce Gated DeltaNet-2, which generalizes both Gated DeltaNet and KDA by inheriting adaptive forgetting and channel-wise decay while addressing their shared limitation, the scalar tie between erasing and writing. Gated Delta Rule-2 separates these roles with a channel-wise erase gate b_t and a channel-wise write gate w_t, reducing to KDA when both gates collapse to the same scalar and to Gated DeltaNet when the decay also collapses. We derive a fast-weight update view, a chunkwise WY algorithm with channel-wise decay absorbed into asymmetric erase factors, and a gate-aware backward pass that preserves efficient parallel training. At 1.3B parameters trained on 100B FineWeb-Edu tokens, Gated DeltaNet-2 achieves the strongest overall results among Mamba-2, Gated DeltaNet, KDA, and Mamba-3 variants across language modeling, commonsense reasoning, and retrieval. Its advantage is most pronounced on long-context RULER needle-in-a-haystack benchmarks, where it improves the evaluated multi-key retrieval setting and remains strong in both recurrent and hybrid settings. Code is available at https://github.com/NVlabs/GatedDeltaNet-2.


### FAME: Failure-Aware Mixture-of-Experts for Message-Level Log Anomaly Detection
**Authors**: Huanchi Wang, Zihang Huang, Yifang Tian, Kristina Dzeparoska, Hans-Arno Jacobsen, Alberto Leon-Garcia

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22779v1](https://arxiv.org/pdf/2605.22779v1)

**Abstract**: Production systems generate millions of log lines daily, yet most anomaly detectors operate at the session or window-level, flagging groups of lines rather than identifying the specific message responsible. This coarse granularity forces operators to inspect many routine lines per alert. Message-level detection offers finer granularity, but remains challenging. A single event template may correspond to both normal and anomalous messages, failures arise from heterogeneous subsystems, and line-level labeling at scale is impractical. Although large language models (LLMs) can reason over log semantics, applying them to every line is too costly for continuous monitoring. We present FAME (Failure-Aware Mixture-of-Experts), a label-efficient message-level mixture-of-experts framework that uses an LLM only once offline. We annotate at most K labeled lines per template to derive binary normal/anomaly indicators and representative examples. The LLM proposes a partition of templates into failure domains, and a certification step validates the proposal before training. FAME trains a lightweight router and domain experts that run on-premise and output anomaly predictions and failure-domain labels. On BGL, FAME achieves F1 = 98.16 at K = 100 reducing annotation effort by 76x and detects 86.3% of anomalies from unseen EventIDs. On Thunderbird, FAME reaches F1 = 99.95 with perfect recall.


### SDPM: Survival Diffusion Probabilistic Model for Continuous-Time Survival Analysis
**Authors**: Stanislav R. Kirpichenko, Andrei V. Konstantinov, Lev V. Utkin

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22776v1](https://arxiv.org/pdf/2605.22776v1)

**Abstract**: Survival analysis aims to estimate a time-to-event distribution from data with censored observations. Many existing methods either impose structural assumptions on the hazard function or discretize the time axis, which may limit flexibility and introduce approximation errors. We propose the Survival Diffusion Probabilistic Model (SDPM), a generative approach to continuous-time survival analysis. SDPM models the conditional distribution of the survival outcome, represented by the pair of observed time and censoring indicator, $\mathbb{P}(T,δ\mid \mathbf{x})$, using a denoising diffusion model. Under the assumption of conditionally independent censoring, conditional samples generated by the model can be transformed into survival function estimates using the Kaplan-Meier estimator. This formulation avoids parametric assumptions on the event-time distribution and does not require a discretization of the output time space. The model operates in a transformed target space, using standardized log-times and a continuous Gaussian-mixture representation of the censoring indicator. We evaluate SDPM on ten real survival datasets and compare it with five strong baselines, including tree-based, boosting-based, and neural survival models. Results show that SDPM achieves competitive predictive performance across C-index, integrated time-dependent AUC, and integrated Brier score. A study on synthetic Cox-Weibull data demonstrates that SDPM can recover the shape of an underlying continuous survival distribution more accurately than a strong nonparametric baseline when sufficiently many samples are generated. An ablation study confirms the importance of the proposed target-space transformations, which improve event-rate calibration, reduce invalid generated times, and provide consistent gains in predictive discrimination. Codes implementing the proposed model are publicly available.


### CogAdapt: Transferring Clinical ECG Foundation Models to Wearable Cognitive Load Assessment via Lead Adaptation
**Authors**: Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin, Leslie Neely, John Davis, John Quarles

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22774v1](https://arxiv.org/pdf/2605.22774v1)

**Abstract**: Real-time cognitive load assessment is essential for adaptive human-computer interaction but remains challenging due to limited labeled data and poor cross-subject generalization. Recent ECG foundation models pre-trained on millions of clinical recordings offer rich representations, but cannot be directly applied to wearable devices due to sensor configuration mismatch and task differences. In this paper, we propose CogAdapt, a framework that adapts clinical ECG foundation models to wearable cognitive load assessment. CogAdapt introduces LeadBridge, a learnable adapter that transforms 3-lead wearable signals into anatomically consistent 12-lead representations, and ProFine, a progressive fine-tuning strategy that gradually unfreezes encoder layers while preventing catastrophic forgetting. Evaluations on two public datasets (CLARE and CL-Drive) under leave-one-subject-out cross-validation show that CogAdapt substantially outperforms baselines trained from scratch, achieving macro-F1 scores of 0.626 and 0.768. These results demonstrate the promise of foundation model adaptation for subject-independent cognitive load assessment from wearable sensors.


## VLA
### Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts
**Authors**: Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu, Jiachi Ji, Shengzhe Ji, Junwu Xiong, Zhijun Meng

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22446v1](https://arxiv.org/pdf/2605.22446v1)

**Abstract**: While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. Low-quality actions may cause physical failures during execution or lead to misleading world-model rollouts with redundant rendering costs. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity assessment before physical execution or world-model imagination. Pre-VLA leverages an efficient multimodal backbone with modality-aware pooling and a lightweight dual-branch head to predict both safety confidence and critic-derived advantage scores for candidate action chunks. To handle severe class imbalance and unstable boundary decisions, we train Pre-VLA with a multi-task objective combining Focal classification, advantage regression, and soft-threshold calibration. During deployment, a dual-mode preemptive resampling scheduler filters low-quality actions and triggers adaptive resampling under a limited computation budget. Experiments on the LIBERO benchmark show that Pre-VLA improves the average closed-loop success rate across four suites from 30.79\% to 37.62\% over RynnVLA-002, reduces task execution steps, achieves 183.9 ms average forward verification time per action chunk, and mitigates error accumulation in world-model rollouts.


### Action with Visual Primitives
**Authors**: Weilong Guo, Yuchen Wang, Renping Zhou, Yunfeng Zhang, Rui Fang, Yue Meng, Wenda Xu, Yuan He, Gao Huang

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22183v1](https://arxiv.org/pdf/2605.22183v1)

**Abstract**: Vision-Language-Action (VLA) models have emerged as a promising paradigm for generalist robotic manipulation. A common design in current architectures maps language instructions and visual observations to actions in a single forward pass. While conceptually simple, this formulation entangles instruction comprehension, spatial scene understanding, and motor control within a single learning objective. As a result, the action expert must implicitly relearn cognitive and perceptual capabilities already present in the pretrained VLM, which can limit both learning efficiency and generalization. We introduce AVP (Action with Visual Primitives), an end-to-end architecture that implements this visual-primitive-centric interface: the VLM infers the next-stage target and emits visual-primitive tokens that condition a flow-matching action expert, with supervision derived from end-effector kinematics. Real-robot experiments on general pick-and-place tasks show that AVP improves the success rate by 27.61% over pi_0.5 and outperforms other recent methods, with consistent gains in data efficiency, spatial-compositional generalization, and object-level transfer.


### LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model
**Authors**: Xiaodong Mei, Diankun Zhang, Hongwei Xie, Guang Chen, Hangjun Ye, Dan Xu

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22089v1](https://arxiv.org/pdf/2605.22089v1)

**Abstract**: Vision-Language-Action (VLA) models have emerged as a promising framework for end-to-end autonomous driving. However, existing VLAs typically rely on sparse action supervision, which underutilizes their powerful scene understanding and reasoning capabilities. Recent attempts to incorporate dense visual supervision via world modeling often overemphasize pixel-level image reconstruction, neglecting semantically meaningful scene representation learning. In this work, we propose LVDrive, a Latent Visual representation enhanced VLA framework for autonomous driving. LVDrive introduces a future scene prediction task into the VLA paradigm, where future representations are learned entirely in a high-level latent space under auxiliary supervision from a pretrained vision backbone. Departing from inefficient autoregressive generation, we jointly model future scene and motion prediction within a unified embedding space, processed in a single forward pass to conduct the future-aware reasoning. We further design a two-stage trajectory decoding strategy that explicitly leverages the learned latent future representations to refine trajectory generation. Extensive experiments on the challenging Bench2Drive benchmark demonstrate that LVDrive achieves significant improvements in closed-loop driving performance, outperforming both action supervised methods and image-reconstruction-based world model approaches.


### EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control
**Authors**: Chushan Zhang, Ruihan Lu, Jinguang Tong, Xuesong Li, Yikai Wang, Hongdong Li

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.21862v1](https://arxiv.org/pdf/2605.21862v1)

**Abstract**: Chunked vision-language-action (VLA) policies predict multi-step robot controls, conditioning each update on the current visual observation alone. Yet robot actions cause contact, occlusion, and object motion, and the geometry that later decisions depend on can change before the next visual update arrives. Spatial VLAs improve current-frame geometry. Temporal VLAs aggregate past frames. Neither maintains an action-updated scene prior across chunks. We argue for a persistent action-updated scene state across control calls, and introduce EvoScene-VLA. Its recurrent scene prefix carries a geometry-aware scene state across chunks. At each vision-language model (VLM) call, the VLM combines scene information from the current observation with the action-updated prior from the previous chunk; the action decoder outputs both the next action chunk and a compact scene update. This update becomes the next prior, which the VLM corrects against the new observation when the next call arrives. Each control call therefore starts from a scene prior that reflects both recent actions and fresh visual evidence. During training, \textbf{Scene Predictor} supplies future scene-token targets, and Geometric Anchor aligns scene slots with frozen depth and 3D teachers. We discard both modules at deployment. On 31 RoboTwin tasks, EvoScene-VLA raises average success from 87.2% to 89.1% in fixed evaluation and from 86.1% to 88.5% in randomized evaluation. On the Galaxea R1-Lite real robot, EvoScene-VLA outperforms all baselines.


### CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models
**Authors**: Zhi Liu

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.21854v1](https://arxiv.org/pdf/2605.21854v1)

**Abstract**: Vision-Language-Action (VLA) models have rapidly converged on a small set of architectural patterns: discrete-token autoregression (e.g. OpenVLA) and continuous-action flow-matching (e.g. pi-0.5). Yet preference alignment via Direct Preference Optimisation (DPO) -- the de-facto post-training step in language models -- has been studied almost exclusively on autoregressive VLAs. We present CrossVLA, an empirical study of cross-paradigm VLA post-training. Three contributions: (i) a surrogate flow-matching log-probability estimator that lets DPO operate on continuous-action backbones without probability-flow ODE integration; (ii) a head-to-head comparison of LoRA and DoRA as the parameter-efficient layer for VLA DPO, finding DoRA improves over OpenVLA SFT by a mean +10.4 pp across LIBERO 4-suite (600 trials, 3 seeds) -- per-suite +20.0 Object, +11.0 Long-horizon, +8.0 Goal, +2.7 Spatial -- with zero seed variance on Object (38/50 on each of 3 seeds); (iii) an inference-time anatomy showing the denoise loop dominates 78.6% of sample_actions latency and prefix-K/V caching a la VLA-Cache caps at a 21% acceleration ceiling -- both chunk-level and token-level cache strategies degrade success rate to 0-80% in our benchmarks. We further pretrain a multi-view + temporal projection head on 6000 LIBERO frames, achieving 99.5% k-NN recall@1 for same-task retrieval (36x over random), available as a downstream initialisation. All code, ckpts, training logs, and reproduction scripts are open at https://github.com/lz-googlefycy/vla-lab.


### Learn Where Outcomes Diverge: Efficient VLA RL via Probabilistic Chunk Masking
**Authors**: Vaidehi Bagaria, Nikshep Grampurohit, Pulkit Verma

**Published Date**: 2026-05-15

**Updated Date**: 2026-05-15

**PDF Url**: [2605.16154v1](https://arxiv.org/pdf/2605.16154v1)

**Abstract**: Reinforcement learning (RL) allows vision-language-action (VLA) policies to generalize beyond their training distribution by optimizing directly for task success, but post-training is computationally expensive. A natural response has been to speed rollout collection through faster simulators and world models. In GRPO-based VLA RL, we find that the dominant cost lies elsewhere: gradient computation accounts for approximately 78% of wall-clock time per step in our runs, while rollout collection accounts for only 21%. Gradient cost dominates because much of this computation is spent on phases that contribute little to learning. GRPO's learning signal is driven by advantage variance: only phases where successful and failed rollouts diverge produce learning signal. However, GRPO assigns the same advantage to every chunk in a rollout. As a result, actor-update compute is spent uniformly across the trajectory, including phases the policy already handles after pre-training and supervised fine-tuning. This paper presents Probabilistic Chunk Masking (PCM), a drop-in modification to GRPO that allocates gradient computation to a small, probabilistically selected subset of chunks per trajectory. PCM scores semantic phases using success-failure action variance, a rollout-derived proxy for per-phase gradient variance, and samples a fixed chunk budget with online-updated phase-level keep probabilities. We formalize per-phase gradient variance as the quantity determines where gradient computation is useful and show that success-failure action variance provides a measurable proxy for it. PCM requires no reward model or learned critic. On three LIBERO benchmarks, PCM matches the final success rate of standard GRPO while achieving 2.38 times wall-clock speedup, 4.8 times faster gradient updates, and 60% lower peak activation memory, while backpropagating through fewer than 20% of trajectory chunks.


## Agent
### LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems
**Authors**: Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Prasanna Sattigeri, Karthikeyan Natesan Ramamurthy

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22786v1](https://arxiv.org/pdf/2605.22786v1)

**Abstract**: Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque channel through which sensitive content may propagate across agents without explicit textual disclosure. To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems. LCGuard treats shared KV caches as latent working memory and learns representation-level transformations before cache artifacts are transmitted across agents. We formalize representation-level sensitive information leakage operationally through reconstruction: a shared cache artifact is unsafe if an adversarial decoder can recover agent-specific sensitive inputs from it. This leads to an adversarial training formulation in which the adversary learns to reconstruct sensitive inputs, while LCGuard learns transformations that preserve task-relevant semantics and reduce reconstructable information. Empirical evaluations across multiple model families and multi-agent benchmarks show that LCGuard consistently reduces reconstruction-based leakage and attack success rates while maintaining competitive task performance compared to standard KV-sharing baselines.


### DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback
**Authors**: Yunpeng Dong, Jingkai He, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Yubin Xia, Haibo Chen

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22781v1](https://arxiv.org/pdf/2605.22781v1)

**Abstract**: LLM-powered AI agents require high-frequency state exploration (e.g., test-time tree search and reinforcement learning), relying on rapid checkpoint and rollback (C/R) of the complete sandbox state, including files and process state (e.g., memory, contexts, etc.). Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R, which severely bottlenecks deep search and large-scale fan-outs.
  This paper observes that subsequent checkpoints in AI agents are highly similar. Therefore, instead of full duplication, a sandbox should only duplicate the changes between consecutive checkpoints (Key Insight). However, it is non-trivial to realize the idea, mainly due to the missing OS supports. This paper proposes a new OS-level abstraction, DeltaState, to enable the change-based transactional C/R for AI agents with two co-designed OS mechanisms. First, DeltaFS enables change-based filesystem C/R by organizing the file states into layers and dynamically freezing the writable layer and inserting a new one during checkpoint, reducing file updates to copy-on-write, and making rollback a simple layer switch. Second, DeltaCR enables change-based process state C/R using incremental dumps, and accelerates rollback by bypassing traditional pipelines to directly fork() from a frozen template process. We then present DeltaBox, a novel agent sandbox achieving millisecond level C/R through the two new mechanisms. Evaluations on SWE-bench and RL micro-benchmarks show DeltaBox completes checkpoint and rollback in millisecond-level latency (14ms and 5ms, respectively), empowering agents to explore substantially more nodes under fixed time budgets.


### Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals
**Authors**: Yu Tang, Muhammad Zakwan, Efe Balta, John Lygeros, Alisa Rupenyan

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22773v1](https://arxiv.org/pdf/2605.22773v1)

**Abstract**: The Flexible Job Shop Scheduling Problem (FJSP) is the optimal allocation of a set of jobs to machines. Two primary challenges persist in FJSP: the unpredictable arrival of future jobs and the combinatorial complexity of the problem, rendering it intractable for conventional mixed-integer linear programming solvers. This paper proposes an event-based \gls{DRL} approach to solve FJSP with random job arrivals. Specifically, we employ the Proximal Policy Optimization algorithm and use lightweight Multi-Layer Perceptrons to train the \gls{DRL} agent for minimizing the total completion time of all jobs. We design the state representation to be directly accessible from the environment, and limit the learning agent to selecting from among a set of well-established dispatching rules. Simulations show that our \gls{DRL} approach outperforms any of the individual dispatching rules on datasets with varying heterogeneity and job arrival rates. We benchmark our \gls{DRL} against an arrival-triggered mixed-integer linear programming solution and show that our method achieves good performance especially when the datasets are heterogeneous.


### Advancing Mathematics Research with AI-Driven Formal Proof Search
**Authors**: George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz Firsching, Gergely Bérczi, Francisco J. R. Ruiz, Arun Suggala, Adam Zsolt Wagner, Eric Wieser, Lei Yu, Aja Huang, Miklós Z. Horváth, Andrew Ferrauiolo, Henryk Michalewski, Codrut Grosu, Thomas Hubert, Matej Balog, Pushmeet Kohli, Swarat Chaudhuri

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22763v1](https://arxiv.org/pdf/2605.22763v1)

**Abstract**: Large language models (LLMs) increasingly excel at mathematical reasoning, but their unreliability limits their utility in mathematics research. A mitigation is using LLMs to generate formal proofs in languages like Lean. We perform the first large-scale evaluation of this method's ability to solve open problems. Our most capable agent autonomously resolved 9 of 353 open Erdős problems at the per-problem cost of a few hundred dollars, proved 44/492 OEIS conjectures, and is being deployed in combinatorics, optimization, graph theory, algebraic geometry, and quantum optics research. A basic agent alternating LLM-based generation with Lean-based verification replicated the Erdős successes but proved costlier on the hardest problems. These findings demonstrate the power of AI-aided formal proof search and shed light on the agent designs that enable it.


### Towards a General Intelligence and Interface for Wearable Health Data
**Authors**: Girish Narayanswamy, Maxwell A. Xu, A. Ali Heydari, Samy Abdel-Ghaffar, Marius Guerard, Kara Vaillancourt, Zhihan Zhang, Jake Garrison, Levi Albuquerque, Dimitris Spathis, Hong Yu, Hamid Palangi, Xuhai "Orson" Xu, David G. T. Barrett, Joseph Breda, Jed McGiffin, Yubin Kim, Yuwei Zhang, Naghmeh Rezaei, Samuel Solomon, Karan Ahuja, Tim Althoff, Jake Sunshine, Ming-Zher Poh, Benjamin Yetton, Ari Winbush, Nicholas B. Allen, James M. Rehg, Isaac Galatzer-Levy, Yun Liu, John Hernandez, Anupam Pathak, Conor Heneghan, Yuzhe Yang, Ahmed A. Metwally, Pushmeet Kohli, Mark Malhotra, Shwetak Patel, Xin Liu, Daniel McDuff

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22759v1](https://arxiv.org/pdf/2605.22759v1)

**Abstract**: While ubiquitous wearable sensors capture a wealth of behavioral and physiological information, effectively transforming these signals into personalized health insights is challenging. Specifically, converting low-level sensor data into representations capable of characterizing higher-level states is difficult due to high phenotypic diversity and variation in individual baseline health, physiology, and lifestyle factors. Moreover, collecting wearable data paired with health outcome annotations is laborious and expensive, and retrospective annotation remains practically unfeasible, contributing to a scarcity of data with high-quality labels. To overcome these limitations, we propose a foundation model for wearable health that is pretrained on more than one trillion minutes of unlabeled sensor signals drawn from a large cohort of five million participants. We demonstrate that the joint scaling of model capacity and pretraining data volume leads to systematic improvements in performance, as evaluated on a diverse set of 35 health prediction tasks, spanning cardiovascular, metabolic, sleep, and mental health, as well as lifestyle choices and demographic factors. We find that this population scale representation unlocks label-efficient few-shot learning and generative capabilities for robust daily metric estimation. To further leverage this learned representation, we deploy a classroom of LLM agents to autonomously search the space of downstream predictive heads built on the model embeddings, showing broad performance improvements that increase with LLM model capacity. Finally, we show how integrating these downstream predictors into a Personal Health Agent can support model responses that are more relevant, contextually aware, and safe, and we validate this via 1,860 ratings from a cohort of clinicians.


### Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning
**Authors**: Ismail Geles, Leonard Bauersfeld, Markus Wulfmeier, Davide Scaramuzza

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22748v1](https://arxiv.org/pdf/2605.22748v1)

**Abstract**: Autonomous systems have achieved superhuman performance in isolation or simulation, yet they remain brittle in shared, dynamic real-world spaces. This failure stems from the dominant single-agent paradigm for physical applications, where other actors are ignored or treated as environmental noise, preventing effective coordination. Here we show that multi-agent reinforcement learning provides the essential safety scaffolding required for real-world interaction. Using high-speed quadrotor racing as a high-stakes testbed, we train agents to navigate complex aerodynamic interactions and strategic maneuvering with a variable number of racers. Through league-based self-play, agents evolve sophisticated anticipatory behaviors, including proactive collision avoidance, overtaking, and handling multi-agent physical interactions, including aerodynamic downwash. Our agents outperform a champion-level human pilot in multi-player races at speeds exceeding 22 m/s, while simultaneously reducing collision rates by 50 % compared to state-of-the-art single-agent baselines. Crucially, training with diverse artificial agents enables zero-shot generalization to safer human interaction. These results suggest that the path to robust robotic co-existence lies not in isolated safety constraints, but in the rigorous demands of multi-agent interaction. Multimedia materials are available at: https://rpg.ifi.uzh.ch/marl


