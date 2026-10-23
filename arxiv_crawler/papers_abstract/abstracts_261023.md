# Abstracts of Papers

## World Model
### Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success
**Authors**: Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31670v1](https://arxiv.org/pdf/2610.31670v1)

**Abstract**: Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To examine this, we propose Sensorimotor Alignment ($S^2$), a training-free offline metric that measures how well a model's sensory representation aligns with the geometry of physical motion. We find that $S^2$ correlates positively with downstream robot task success across embodied model families, making it a low-cost offline proxy for prioritizing models before closed-loop evaluation. $S^2$ can also identify promising vision-language model (VLM) backbones even before costly fine-tuning into vision-language-action models (VLAs). Beyond this correlation, $S^2$ offers representation-level explanations for phenomena observed in VLAs and world action models (WAMs). With $S^2$, we extend PRH to embodied models and make sensorimotor alignment empirically measurable, offering insight into why an embodied model succeeds beyond its closed-loop success rate.


### Reading, Writing, Sharing, and Interacting with the World through Video
**Authors**: Shengqiong Wu, Meng Luo, Bobo Li, Ziwei Liu, Shuicheng Yan, Ming-Hsuan Yang, Philip Torr, Hao Fei

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31668v1](https://arxiv.org/pdf/2610.31668v1)

**Abstract**: Video foundation models have advanced rapidly in understanding and generating visual sequences, while video world models seek to capture the underlying dynamics of the world they depict. Despite their different objectives, both concern the relationship between video observations and an evolving world. This survey adopts world modeling as a unifying lens for examining these developments. Viewing an observed video as a partial, lossy, and temporally ordered projection of a latent temporal world, we organize the literature around four complementary operations: reading infers world properties from observed video; writing synthesizes video from specified or learned world conditions; sharing integrates understanding and generation through common modeling mechanisms; and interacting predicts and updates world states under actions and evolving observations. This perspective distinguishes temporal coherence in observed or generated sequences from consistency in the underlying world state. Across tasks, representations, models, datasets, and benchmarks, we trace a shift in emphasis from clip-level recognition and perceptual fidelity toward persistent state, controllable evolution, physical and causal validity, and evaluation grounded in interaction and downstream decisions, and we distill the open challenges that follow.


### Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning
**Authors**: Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31667v1](https://arxiv.org/pdf/2610.31667v1)

**Abstract**: Test-time scaling has emerged as a key inference strategy for reasoning models, where a model generates a large number of candidate solutions in the hope of finding at least one correct solution. Running all candidate solutions to completion can be computationally demanding, so recent work prunes the candidate pool after generating only a short prefix, committing further computation only to the surviving candidates. Existing pruning strategies divide broadly into two categories: Quality-based methods assign a score to each partial solution and discard those predicted to ultimately lead to an incorrect final solution, while diversity-based methods select partial solutions that follow different reasoning trajectories and are therefore likely to cover different final solutions. The tension between these two objectives is an instance of exploration versus exploitation, yet little to no prior work on pruning exposes this trade-off directly, let alone optimizes it. In this paper, we introduce a pruning procedure that addresses this trade-off directly by optimizing pass@$k$ over the selected solution pool. In particular, it chooses the pool to maximize the probability that at least one of its partial solutions, when continued to completion, yields a correct answer. Because this objective simultaneously rewards high-quality partial solutions and penalizes redundancy among them, quality and diversity are naturally balanced by the criterion itself rather than through separate ad-hoc design choices. On eight open-weight reasoning models, our method outperforms existing quality-based and diversity-based pruning strategies. The gains are particularly pronounced when the pruning procedure keeps a moderate number of partial solutions for continued generation, highlighting the value of directly balancing quality and diversity during pruning.


### Reliable AI-Assisted Decisions via Selective Auditing
**Authors**: Isaac Gibbs, Elise L. Han, Ryan J. Tibshirani, Tijana Zrnic

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31662v1](https://arxiv.org/pdf/2610.31662v1)

**Abstract**: We consider online monitoring of an AI system that produces a sequence of decisions. At each round, the system outputs a proposed decision together with a confidence score estimating the trustworthiness of the decision. The decision and confidence score need not be produced by the same model: for example, one agent may propose a decision, while a separate verifier agent evaluates it and outputs a correctness or safety score. Based on this information, we must decide whether to accept the AI decision automatically or consult an expert, such as a human auditor, who reviews the proposal and either accepts or corrects it. We formulate this task as an online constrained optimization problem in which the goal is to minimize the frequency of expert auditing while guaranteeing that the fraction of AI errors that go unaudited stays below a user-defined threshold. We derive a family of algorithms with provable error-control guarantees with no assumptions, including a method that is optimally efficient: it asymptotically attains the best achievable auditing rate for both adversarial and i.i.d. data streams. Experiments on screening harmful requests to large language models, qualitative text annotation, and data labeling show that our methods achieve valid error control in practice while substantially reducing the need for human auditing compared to baselines.


### OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing
**Authors**: Ariel Slepyan, Geeta Chandra Raju Bethala, Jiafeng Gu, Anagha Rajendra Dangle, Yinzhe Zhou, Hongyuan Fu, Jade Sim, Tuhin Basu, Xinyi Yin, Md Faizal Karim, Gregory Hager, Homanga Bharadhwaj, Anand Bhattad, Krishna Murthy Jatavallabhula, Nitish V. Thakor

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31661v1](https://arxiv.org/pdf/2610.31661v1)

**Abstract**: We present OpenTac, a novel sensor and a full-stack ecosystem for tactile skins that are highly customizable, scalable, and readily deployed in downstream robot control and learning applications. Our core contribution is twofold. First, we develop a scalable resistive tactile skin with a structured deformable overlay that converts tangential loading into spatially varying pressure. Differential responses across neighboring "taxels" support decoding of local shear vectors, and the common-mode response encodes normal force. Second, we provide a highly customizable sensor design tool that is able to automatically generate fabrication files for these tactile skins from 2D outlines and developable 3D surfaces, including from abstract descriptions such as text (e.g., "design a sensor for a size 9 shoe insole"). We develop an ecosystem around the OpenTac sensor, including the CAD design tool, a sensor simulator, cross-sensor transfer, and fast/adaptive data acquisition. We demonstrate the broad applicability of the OpenTac-CAD sensor design tool by designing and fabricating more than 30 sensors across a variety of robot embodiments. We characterize the three-dimensional tactile fields produced by OpenTac with a commercial, high-precision force/torque sensor. We demonstrate the broad applicability of 3D tactile sensing across contact-rich feedback control and manipulation policy learning on four real-world robot embodiments. Additionally, adaptive acquisition enables kilohertz-rate partial readouts, exceeding full-array raster scanning on the same sensor by 19.2X at 16 sampled taxels per update for a 1024-taxel skin. We provide all hardware, software, and result videos are at opentac.github.io


### SpectralCanary: Embarrassingly Simple Low-Frequency Traces for T2I Dataset-Use Auditing
**Authors**: Sy-Tuyen Ho, Anirudh Satheesh, Soham Chawathe, Huy Nghiem, Yongkyun Lee, Andrew Adams Schoen, Furong Huang

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31659v1](https://arxiv.org/pdf/2610.31659v1)

**Abstract**: Auditing whether a text-to-image (T2I) model was fine-tuned on a particular image collection is difficult: a model can absorb collection-level visual characteristics without reproducing training images. Proactive dataset-use auditing plants a shared signal in a dataset before release, then later checks whether that signal appears in a suspect model's generated outputs. Existing approaches often trade off verifiability, fidelity, robustness, and deployability. We introduce $\textbf{SpectralCanary}$, which uses a smooth low-pass mask to blend a fixed canary image into every collection image while leaving captions unchanged and requiring neither auxiliary generation nor per-image optimization. A lightweight verifier detects the transferred signal in suspect-model outputs. Across eight tests on the Pokemon dataset and three realistic data transformations, spanning two architectures families, SpectralCanary achieves the highest average per-generation TPR@$1\%$ FPR ($91.1\%$) and fixed threshold model-level accuracy using 30 generations ($94.8\%$) among the evaluated methods. Across five datasets spanning artistic, medical, satellite, and fashion domains with SD3.5, SpectralCanary averages $92.4\%$ per-generation TPR@$1\%$ FPR while preserving the released images (SSIM $0.989$, LPIPS $0.022$) with a near-zero mean change FID (mean $Δ$FID $0.05$) across datasets. Matched-energy ablations on Pokemon and ROCOv2 support our design choice, low-frequency placement transfers more reliably compared to mid/high-frequency placement. Under the evaluated adaptive attacks, the most effective removal requires aggressive modification and incurs more than $25$ $Δ$FID points. These results identify low-frequency visual signals as effective carriers for collection-level T2I audit traces.


## Generation
### Causal Chain of Thought: Mitigating Attention Leakage via Context Isolation
**Authors**: Gabriele Dominici, Teague McMillan, Fazl Barez, Marc Langheinrich, Martin Gjoreski

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31639v1](https://arxiv.org/pdf/2610.31639v1)

**Abstract**: Chain-of-thought (CoT) prompting elicits step-by-step rationales that appear to explain model predictions, but there is no guarantee these steps causally drive the final answer. In standard autoregressive generation, dense attention allows each reasoning step to attend to the full context, enabling the model to derive answers through direct lookup while generating plausible-sounding but post-hoc justifications. We introduce CausalCoT, an inference framework that enforces causal transparency by decomposing problems into a directed acyclic graph of atomic sub-questions, evaluating each node in an isolated context containing only its direct causal parents. This Markovian structure removes attention pathways to non-parent content, making downstream predictions sensitive to local reasoning rather than global context leakage. Across a diverse suite of reasoning benchmarks, CausalCoT preserves competitive predictive performance while improving explanation faithfulness, increasing causal sensitivity of intermediate reasoning steps by an average of 12 and up to 21 percentage points over the strongest baseline. The structured dependency graph additionally enables test-time interventions in which local corrections propagate predictably through downstream reasoning.


### BeNice! Closing Looping's Inference-Memory Gap via KV-Sharing
**Authors**: Hayden Prairie, Jacob M. Ryan, Taylor Berg-Kirkpatrick, Daniel Y. Fu

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31633v1](https://arxiv.org/pdf/2610.31633v1)

**Abstract**: Looped architectures scale quality while keeping parameter count fixed by repeatedly passing activations through the same block of layers. During inference, each recurrence generates independent KV-caches, causing memory to grow linearly. To address this challenge, prior work has proposed KV-sharing (i.e., sharing KV-caches across depth), finding that, in some cases, the KV-cache of the final recurrence can be shared with the earlier recurrences without quality loss, a property we denote as KV-shareability. However, the mechanisms underlying KV-shareability remain poorly understood, with even identically trained looped architectures not consistently exhibiting it. In this paper, we study how KV-shareability can be enabled in looped models. We propose a two-stage method: in the first stage, we use stochastic depth during pretraining, which induces contractive residual dynamics that drive representations toward a common limit across recurrences. In the second stage, we propose BeNice!, a post-training method that broadcasts the final recurrence's KV-cache into the first recurrence, training it to produce compatible residuals while preserving the original model's quality. As a result, BeNice! enables KV-shareability while matching standard finetuning's unshared validation perplexity. Using BeNice!, we show that KV-sharing is complementary to alternative KV-compression methods, composing with memory-efficient sequence mixers (e.g., multi-latent attention, Kimi delta attention) and low-precision KV-cache quantization (e.g., fp8, mxfp8, nvfp4). Finally, in simulated low-memory, long-context inference, KV-sharing improves cache hit rates by up to 31.4%, increases throughput by up to 23.6%, and reduces p90 time-to-first-token by up to 83.6%.


### Questioning Instrumental Convergence in RLVR: Checkpoint Evidence from OLMo-3
**Authors**: Barış Alparslan, Sandy Tanwisuth, Caleb Petterson

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31624v1](https://arxiv.org/pdf/2610.31624v1)

**Abstract**: Instrumental convergence is often invoked as a general reason to expect capable agents to acquire or express power-seeking subgoals: self-preservation, resource acquisition, deception, or resistance to oversight which poses an important threat to the society. For LLMs, reinforcement learning is the first stage of post-training that directly optimizes behavior against an objective; therefore, it is the stage where convergent instrumental behavior, on IC grounds, likely to appear. Does reinforcement learning with verifiable rewards (RLVR) make a model more likely to express instrumental-convergence behavior, or does this depend on the training regime, evaluation frame, and stage of post-training? We study this question as a checkpoint-conditioned behavioral trajectory rather than as a single before/after safety score. Using InstrumentalEval, we evaluate OLMo-3-7B-Think across SFT, DPO, 13 intermediate RLVR checkpoints, and the final RLVR model. The trajectory is nonmonotonic: instrumental rate rises from 25.0% at SFT to 46.1% near RLVR step 200, then falls to 11.8% at the final checkpoint. Paired item-level tests and step-wise regression support the final SFT-to-RLVR reduction. Prompt framing does not explain this pattern: a harmful-prompt indicator combined with other framing effects explains only 15% of within-checkpoint score variance on average, and Iterative Null-space Projection (INLP) removes a detectable framing direction without changing the SFT-to-final-RLVR gap. Together with preliminary 32B endpoint results (35.53% SFT to 22.37% RLVR final), these findings indicate that RLVR does not monotonically increase instrumental behavior in this setting: the rate rises early, then falls below the SFT baseline. The result is specific to this model family and benchmark, and judge agreement is moderate, so absolute rates should be read cautiously.


### How Ground Truth Shapes Retrieval Scores: Evidence-Aware Evaluation of a Retrieval-Augmented Generation System for Breast Lesions
**Authors**: Miguel Mochizuki Silva, Samuel Ismael, Mateus C. Dias, Thaís Gaudêncio, Yuri Malheiros,  Barufaldi

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31606v1](https://arxiv.org/pdf/2610.31606v1)

**Abstract**: Purpose: To describe an evidence-aware retrieval evaluation protocol for a clinical retrieval-augmented generation (RAG) system over breast lesion management literature, addressing the dependence of retrieval scores on annotation coverage. Methods: An 18-document corpus and an 18-query development benchmark, with one Yes/No or WH-question per document, were used. Retrieval combined dense embeddings, BM25, and cross-encoder reranking. Chunk sizes of 128 to 1024 tokens, overlaps of 0 to 20%, and four retriever configurations were evaluated. Relevance was defined by evidence spans mapped to all containing chunks, treating overlapping chunks with equivalent evidence as relevant. Retrieval was evaluated using R-Precision, Recall@K, MRR, and nDCG@K. Separately, generation was assessed on a 512-token index at K=1 to 5 using DeepEval claim-level metrics, with deepseek-v4-pro as the LLM judge, and BLEU/ROUGE metrics. Results: The selected hybrid retriever, using 384-token chunks and 20% overlap, retrieved accepted evidence in the top three results for 17 of 18 queries. Recall@3, R-Precision, MRR@3, and nDCG@3 each reached 0.94. Ground-truth curation increased evidence spans from 25 to 37 and accepted chunk targets from 36 to 51 without changing retrieval rankings. Conclusion: Cross-encoder reranking achieved the highest retrieval scores. Expanded relevance annotations increased recognized evidence without changing rankings, highlighting annotation sensitivity. The small development set and retrieval-informed curation require independent validation, including radiologist assessment of evidence sufficiency.


### CRANE: Post-Hoc Counterfactual Retrieval for Multimodal Classifiers
**Authors**: Franco Rugolon, Ioanna Miliou, Panagiotis Papapetrou

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31594v1](https://arxiv.org/pdf/2610.31594v1)

**Abstract**: Counterfactual explanation methods have been introduced for unimodal settings, with dedicated frameworks for tabular, timeseries, text, and image data, yet no post-hoc method has been designed for classifiers that learn from multimodal inputs. Existing explainability methods for multimodal classifiers apply modality-specific attribution independently to each input, which fails to yield coherent explanations and does not transfer to arbitrary pre-trained multimodal architectures. To address these shortcomings, we present CRANE (Counterfactual Retrieval via Agnostic Nearest-neighbour Explanations), the first post-hoc, model-agnostic framework for nearest-neighbour multimodal counterfactual generation that retrieves real training examples from the target class as candidate explanations, ensuring plausibility by construction. Across four heterogeneous datasets and three fusion strategies, we show that Multimodal Consensus Retrieval (MC-R), which intersects per-modality neighbour sets to identify instances jointly close to the query in every modality, emerges as the strongest multimodal strategy, achieving the best or joint-best outcome on three of four datasets while grounding every explanation in the joint training distribution. Unimodal strategies remain competitive when a single modality dominates the decision boundary.


### Action Learning for Scientific Simulations
**Authors**: Sarah Liaw, Yuanqi Du, Yilun Du

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31585v1](https://arxiv.org/pdf/2610.31585v1)

**Abstract**: Understanding and controlling how systems evolve is central to science and engineering, where many problems require reasoning about complete trajectories. Existing approaches typically learn local dynamics or generate trajectories, but objectives constructed from individual transitions can miss dependencies across time, while generative models do not necessarily provide a tractable objective for evaluating and optimizing arbitrary paths. We study $\textit{action learning}$, the problem of recovering a stochastic action from trajectory observations, yielding a common objective for reasoning about dynamical systems. We introduce $\textbf{LEAP}$ ($\textbf{L}$earned $\textbf{E}$nergy on $\textbf{A}$ction $\textbf{P}$aths), which anchors the unknown action to a tractable reference process and learns the remaining correction by comparing observed trajectories with reference trajectories. This construction yields a differentiable objective on path space that can capture both local dynamical structure and nonadditive dependencies across time. Once learned, the same action can be flexibly reused for path ranking and inference, mechanism steering, constrained optimization and sampling. Across stochastic physical systems, many-body orbital dynamics and molecular simulations, LEAP recovers underlying dynamics, captures dependencies across time and enables transfer across inference objectives and physical conditions. We show that $\textit{action learning}$ is a promising framework for turning trajectory observations into reusable objectives for scientific inference and control.


## VLA
### FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models
**Authors**: Huixin Xu, Ziya Yu, Peng Li

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31423v1](https://arxiv.org/pdf/2610.31423v1)

**Abstract**: Vision-language-action (VLA) models have become an important paradigm for robotic manipulation by unifying visual perception, language understanding, and action generation. Since reliable manipulation requires sufficient observation of objects, end-effectors, and their spatial relationships, multi-view inputs are widely used to provide complementary spatial information. However, our experiments show that existing VLA models do not fully exploit such multi-view complementarity. The policy tends to persistently rely on the wrist view, lacking the ability to dynamically adjust global-local view dependency across manipulation stages, which limits stage adaptability and robustness. To address this issue, we propose FocusVLA, a stage-aware multi-view routing framework. FocusVLA predicts future interaction intent from historical actions and uses it to guide dynamic view routing during action generation. By adaptively coordinating global and local observations across different task stages, FocusVLA improves multi-view utilization. On RoboTwin 2.0, FocusVLA improves the average success rate over the strongest baseline $π_{0.5}$ by 10.10 pp. In real-world evaluation, FocusVLA improves the success rate from 71.7\% to 85.0\%, achieving a 13.3\% gain over $π_{0.5}$. Moreover, the intent prediction and dynamic routing modules of FocusVLA can be integrated into existing VLA frameworks without modifying their core architectures.


### Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation
**Authors**: Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31166v1](https://arxiv.org/pdf/2610.31166v1)

**Abstract**: Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).


### Measuring the Reasoning-Action Coupling in Driving Vision-Language-Action Models through Counterfactuals
**Authors**: Gabriel Manalu, Saad Wazir, Thao Do, Seongah Kim, Hyeontaek Hwang, Tolcha Yalew Kidane, Daeyoung Kim

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.30953v1](https://arxiv.org/pdf/2610.30953v1)

**Abstract**: Driving vision-language-action (VLA) models bring an appealing form of explainability to a safety-critical domain, since a system that can state the reasons for its maneuvers offers the transparency that deployment and public trust in autonomous driving demand. These models read the world into language before they act on it, describing the scene and reasoning over it in text that ranges from chain-of-thought to multi-stage question answering on the way to a trajectory. That framing quietly assumes two separable properties, namely that the trajectory follows the generated reasoning and that the generated reasoning tracks the causes that actually produce the trajectory. To thoroughly investigate these properties, we apply causal, counterfactual interventions to four driving VLAs across different benchmarks. First, we perturb the models' own reasoning and show that altering its meaning produces small trajectory changes relative to blanking the same models' camera inputs, a pattern that persists across benchmarks and model architectures. We then construct scene-level counterfactuals through photorealistic removal of key objects named in the models' reasoning and analyze whether the generated reasoning and trajectories track these changes. Overall, our findings indicate that the reasoning these models present to account for their resulting driving behavior is weakly coupled to that behavior itself, pointing to limits on the explainability these systems are intended to provide.


### AtomicRL: Atomic Reinforcement Learning for Long-Horizon Robotic Manipulation
**Authors**: Likui Zhang, Zhe Zhu, Zhihao Zhan, Yibo Bai, Hanlin Wang, Dongwei Li, Bin Wang, Tianle Zhang, Xiaodan Liang, Liang Lin

**Published Date**: 2026-10-21

**Updated Date**: 2026-10-21

**PDF Url**: [2610.30097v1](https://arxiv.org/pdf/2610.30097v1)

**Abstract**: Vision-language-action (VLA) models have shown promise in robotic manipulation, but imitation learning (IL) alone often struggles to master complex long-horizon skills. Reinforcement learning (RL) offers an effective avenue for further improving VLA policies. However, existing VLA-RL methods typically suffer from delayed and biased credit assignment due to trajectory-level sparse rewards, while imbalanced subtask mastery creates bottlenecks that limit overall performance. To address these challenges, we propose AtomicRL, an RL post-training framework that leverages atomic task structures for reliable credit assignment and adaptive exploration. AtomicRL introduces Semantic-Aware Policy Optimization (SAPO), which uses semantic-aware gating to constrain TD residuals from failed atomic subtasks from propagating across task boundaries, mitigating credit contamination while preserving intra-subtask credit assignment and value bootstrapping. In addition, Bottleneck-Adaptive Target Exploration (BATE) dynamically coordinates task sampling and local exploration incentives based on the mastery of individual atomic subtasks, directing learning toward the remaining bottlenecks. Finally, we develop a Real2Sim2Real pipeline that bridges online RL in simulation with real-world deployment, facilitating practical transfer to physical robots. On LIBERO-LONG, AtomicRL achieves absolute performance gains of 3.6% and 4.0% over PPO across two VLA architectures. On CALVIN ABC-D, it improves full-task performance by up to 9.5% over PPO. Combined with the Real2Sim2Real pipeline, AtomicRL further improves real-world task performance by an average of 21.3%. These results demonstrate that AtomicRL effectively improves the learning efficiency and manipulation performance of VLA policies on long-horizon tasks.


### SP-HLM: Sparse-Pose-Driven Motion Generation and Whole-Body Control for Humanoid Loco-Manipulation
**Authors**: Zhaohui Yang, Quanbao Lin, Chengqi Shi, Zhenglang Weng, Jicheng Lin, Boyu Chen, Tengjie Zhu, Guanzhu Ren, Jiahao Xu, Yang Feng, Xiaokang Yang, Yao Mu

**Published Date**: 2026-10-21

**Updated Date**: 2026-10-21

**PDF Url**: [2610.30044v1](https://arxiv.org/pdf/2610.30044v1)

**Abstract**: Humanoid loco-manipulation requires an effective interface between high-level task policies and whole-body control. Existing interfaces typically rely on a single action representation for both task intent and whole-body coordination. This may burden the high-level policy or leave one aspect underspecified. We present SP-HLM, a framework built on a sparse-pose-driven interface. The interface combines five task-critical body poses with a learned latent motion prior to represent spatial intent and whole-body coordination in complementary forms. SP-VLA, a vision-language-action model, first predicts task-relevant sparse poses and finger joint positions from multimodal observations and language instructions using asynchronous action-chunk inference. Given these sparse targets, SP-MGM, a motion generation model trained through two-stage distillation, reconstructs coordinated full-body motion in real time. A pretrained motion encoder maps this motion to a compact latent representation. SP-GMT, a general motion tracker, then integrates the explicit sparse targets with this implicit motion prior for whole-body control. Experiments in simulation and on a real humanoid robot demonstrate improved motion tracking, whole-body coordination, and loco-manipulation success over existing approaches. Additional results and videos are available on our \href{https://sp-hlm.github.io/}{\textcolor{blue}{project page}}.


### Post-hoc Epistemic Uncertainty for Vision-Language-Action Policies
**Authors**: Johannes Keller, Albrecht M. Bloße, Adrian Lindenmeyer, Thomas Neumuth, Daniel Schneider

**Published Date**: 2026-10-21

**Updated Date**: 2026-10-21

**PDF Url**: [2610.29730v1](https://arxiv.org/pdf/2610.29730v1)

**Abstract**: Vision-language-action (VLA) policies need to recognize gaps in their training knowledge to request useful demonstrations or assistance in new situations, especially when failures are costly. Disagreement within an ensemble of independently trained policies can guide these decisions, but requires training and running multiple policies. We propose post-hoc kernel-variance heads that estimate epistemic uncertainty from the embeddings of a single policy. Each head computes the conditional variance of a Gaussian process conditioned on embeddings from the training demonstrations. Fitting requires no regression targets or gradient updates and leaves the policy unchanged. In experiments with SmolVLA on LIBERO-10, the kernel variance heads perform competitively with two-policy ensemble scores in task-level correlation with task success, in demonstration acquisition during active learning, and in referral to a stronger supervisor policy as a proxy for human assistance. For SmolVLA, the head on the vision-language backbone reduces uncertainty-scoring time by up to approximately a factor of 50 compared with ensemble scores, while also substantially reducing setup costs. We also show that the established evaluation protocol on LIBERO-10 primarily rewards recognition of coverage differences between tasks, while execution variability weakens assessment of within-task rankings. Thus, controlled perturbations provide a complementary evaluation: modality-specific heads identify unfamiliar camera, instruction, or state inputs, while fused heads can detect unfamiliar combinations of individually familiar inputs. With a supervisor proxy trained on the evaluated perturbation families, the decoder head improves within-task referral over ensemble disagreement. These findings show that useful uncertainty estimates for adaptive robot learning can be obtained from a single policy.


## Agent
### METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning
**Authors**: Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31656v1](https://arxiv.org/pdf/2610.31656v1)

**Abstract**: Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation phase into two temporal scales: a causal neural memory performs fine-grained within-episode adaptation with linear sequence complexity, while compact episode-level summaries support long-range cross-episode task inference without attending over the full interaction history. Moreover, equipping agents with neural memory provides sufficient expressive capacity and test-time training capability, enabling effective adaptation to unseen held-out tasks and task families at meta-test time. On unseen held-out Meta-World ML10/45 test environments, METTA achieves a success rate over $50\%$ while maintaining a low training budget and short wall-clock time. On long-context sparse-reward PointMaze tasks, it outperforms transformer-based baselines by exhibiting more structured exploration behavior. These results show that METTA provides an efficient path toward more adaptive and scalable long-context meta-RL.


### EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence
**Authors**: Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, Zhongxiang Dai, Shuang Qiu

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31650v1](https://arxiv.org/pdf/2610.31650v1)

**Abstract**: Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the benchmark measures unsafe execution under critical evidence omission and determines the minimum observed failure cardinality, including failures with full evidence and cases with no observed failure after exhaustive testing. An independent audit tool tests whether agents seek missing facts and then withhold prohibited actions while completing permissible tasks. The benchmark reveals substantial variation across the ten models in omission robustness, evidence acquisition, and appropriate action. Resistance to missing evidence does not necessarily translate into useful recovery. Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.


### Social-HUMINT: An LLM-Augmented Unified Framework for Measuring Social Media Exposure
**Authors**: Pellegrino Casoria, Simon Pietro Romano

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31573v1](https://arxiv.org/pdf/2610.31573v1)

**Abstract**: In the post-API landscape, social-media profiling has become inexpensive and automated: Large Language Models (LLMs) can extract structured information from unstructured content and deduce attributes users never disclosed. A person's true exposure is not what they post but what can be inferred from it. As these practices become routine, exposure to social engineering attacks becomes an operational certainty, demanding a shared framework for assessment and mitigation.
  We make this exposure measurable by quantifying how accurately a target can be profiled, and how far that profile enables social engineering attacks. Because no existing model fully spans this continuum, we unify Social Media Intelligence (SOCMINT) and Cyber Human Intelligence (Cyber-HUMINT), two individual-focused disciplines that evolved separately, into a single doctrine-grounded taxonomy of 38 capabilities across the Cyber Threat Intelligence lifecycle, where user profiling bridges passive collection and active engagement. Domain experts validated the taxonomy (Fleiss' $κ$ = 0.92).
  We operationalize its core path (extraction, inference, and susceptibility assessment) as an LLM-augmented multi-agent pipeline, evaluated on real participants' public data. Susceptibility is assessed indirectly: the pipeline predicts how each target would rank personalized engagement options, matching their actual choices significantly above chance. This ranking capacity captures the personalization on which tailored attacks depend. The underlying profiles are accurate: extraction reaches F1 = 97.3%, and inferred attributes score 4.73/5, both far above rule-based and NER-based baselines at negligible cost. The framework augments security analysts' tradecraft rather than replacing it and enables defenders to gauge their own exposure before an adversary does.


### Contestable Agents for Data Governance: Recording Human Stewardship of AI-Generated Metadata Across Structured and Unstructured Systems
**Authors**: Humza Akhtar, Brian Freeman

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31553v1](https://arxiv.org/pdf/2610.31553v1)

**Abstract**: Industrial organizations hold operational knowledge in structured records, such as telemetry, point lists, and transactions, and in unstructured sources, such as manuals, service notes, communications, and inspection reports. Governance programs often manage these sources separately. Classifying, linking, and documenting them depends on a small group of employees with deep domain knowledge. Agents built on large language models can propose metadata, cite documents, and flag quality issues, but unreviewed proposals can spread errors into downstream systems. A perfunctory approval leaves no record of what a reviewer checked. We present contestable governance: specialist agents produce scored, cited arguments for disputed metadata decisions; a steward can accept, reject, modify, or add arguments before commit; and a governance record retains the evidence, interventions, and outcome. A versioned domain glossary supplies model-specific terms and acronym definitions to the agents. We describe the workflow, a triage path that reserves full argumentation for uncertain proposals while preserving review before commit, the scoring and record models, and a gate that controls which verified decisions become precedent. Two HVAC use cases illustrate the pattern: point classification using Brick Schema class labels, supported by an open reference implementation, and an illustrative warranty failure-mode decision linking claim fields and telemetry to service notes and revisioned bulletins.


### Same Luck, Different Choice: Twin-World Credit Assignment for Agentic Reinforcement Learning
**Authors**: Zeropy Surio, Tobias Engel, Mei-Lin Chou, Anika Raman, Samuel Okafor

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31544v1](https://arxiv.org/pdf/2610.31544v1)

**Abstract**: Agentic reinforcement learning rewards a complete episode, yet the policy needs credit for every decision inside it. Counterfactual branching estimates this credit by re-running the episode after an alternative decision, but the branch draws its sampling noise independently of the factual episode, so the outcome difference mixes the effect of the decision with the luck of everything that follows. We observe that in agentic search the retriever, the corpus, and the grader are deterministic, so an episode is a deterministic function of the policy's decisions and its sampling noise. Twin worlds are therefore realizable: the same noise, a different decision. We introduce TWICE (TWIn-world Credit Estimation), which keys the Gumbel noise of every token by turn and line, rolls out counterfactual twins that inherit the factual episode's downstream noise, and turns their paired outcome differences into turn-level advantages for policy-gradient updates on actor-sampled trajectories; only the actor is deployed. Twin credit is unbiased for any coupling quality, its variance is that of an independent counterfactual scaled by $1-ρ$, where $ρ$ is the twins' outcome correlation, and under coupling the number of rollouts needed to resolve an advantage of size $Δ$ falls from $Θ(Δ^{-2})$ to $Θ(Δ^{-1})$. A square-root rule spends the twin budget where outcomes are predicted to disagree per unit cost. On seven question-answering benchmarks, TWICE improves the average exact match of GRPO by 5.3 and 4.5 points on Qwen2.5-3B and 7B, outperforms tree-search and counterfactual-branching baselines, and uses 68% fewer auxiliary tokens than VinePPO.


### DuoCook: An Overcooked-Inspired Benchmark for Visual Planning and Coordination
**Authors**: Ziyi Jiao, Heng Zhang, Drishti Regmi, Xiaokang Ye, Lianhui Qin, Peter Yichen Chen

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31511v1](https://arxiv.org/pdf/2610.31511v1)

**Abstract**: Coordinating two players in a cooking task requires a vision-language agent to track changing scene states, sequence recipe steps, and allocate shared resources under a time budget. We introduce an Overcooked-inspired benchmark for evaluating these capabilities in Unreal Engine environments constructed using coding agents. A single vision-language model controls both players from top-down visual observations, selecting high-level actions while the engine executes navigation. The benchmark contains 20 maps in five categories. These categories support evaluation of centralized coordination under equipment contention, changing terrain, and handoff dependencies. A prop legend and pot ingredient-count indicators provide explicit visual cues, while grid-based destinations support spatial grounding. The evaluation compares four VLMs on all 20 maps, measuring task score, order completion, delivery precision, action acceptance rate, and model API expenditure. A memory ablation on the same 20 maps examines the effect of a shared, self-authored notebook while retaining six-response action history in both conditions. The strongest evaluated model, \texttt{gpt-6-astra}, achieves 26.2\% mean order completion. Notebook memory has mixed score effects across models, with positive mean differences for Claude and Qwen and negative differences for GPT and Gemini.


