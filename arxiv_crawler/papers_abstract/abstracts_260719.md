# Abstracts of Papers

## World Model
### Decoding Market Emotion from Blockchain Activity: A Data-Driven Sentiment Classifier
**Authors**: Arthur G. Bubolz, Abreu Quevedo, Giancarlo Lucca, Rafael A. Berri, Eduardo Borges, Bruno L. Dalmazo

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15258v1](https://arxiv.org/pdf/2607.15258v1)

**Abstract**: The growing use of Bitcoin as a decentralized digital asset and investment tool has sparked strong interest in understanding its market behavior. This study presents a new approach to analyze Bitcoin market sentiment by combining on-chain and financial data with social media posts. Unlike models that aim to predict prices, this work focuses on explaining market sentiment using blockchain transactions, historical price data of Bitcoin, and daily Twitter sentiment classifications. The method merges sentiment trends with on-chain and financial metrics, normalized into a dataset for detailed market analysis. Multiple machine learning models were tested using cross-validation, with Gradient Boosting (XGBoost) emerging as the most reliable model for classifying sentiment, achieving an average F1-score of about 0.84. SHAP (SHapley Additive exPlanations), a game theory-based method for model interpretability, was used to quantify the contribution of on-chain features to the model's predictions, improving transparency. The results indicate that this data combination yields meaningful predictive signals and insights, supporting data-driven cryptocurrency analysis and future improvements with deep learning.


### Mutable Low-Rank Sketches for Retrain-Free Recommendation
**Authors**: Hector J. Garcia, Nick Clayton

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15242v1](https://arxiv.org/pdf/2607.15242v1)

**Abstract**: A common bottleneck in two-stage recommendation is embedding staleness: when a user rates a new item, their embedding remains fixed until the next retrain cycle. We propose mutable sketches, which store each user's preferences in a KP-tree (a sparse segment tree with sum aggregation), fit a low-rank projection once, and recompute embeddings on-the-fly as ratings arrive. We prove that each new observation monotonically tightens the prediction error envelope (Theorem 1), a guarantee that FunkSVD and eALS lack. On KuaiRec, the mutable sketch achieves 0.810 RMSE at 1.8% data read vs. ALS 0.822 at 100%, with 8x faster per-batch updates. A new user receives personalized recommendations in <1 ms after their first rating, with no model retraining required. A comparison of sampling strategies across density regimes shows that the KP-tree's norm-proportional sampling provides 40-130% better item coverage on sparse data (<1% density), while uniform sampling suffices on dense matrices.


### In-Place Tokenizer Expansion for Pre-trained LLMs
**Authors**: Jimmy T. H. Smith, Tarek Dakhran, Alberto Cabrera, Simon S. Lee, Paul Pak, Aditya Tadimeti, Tim Seyde, Maxime Labonne, Alexander Amini, Mathias Lechner

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15232v1](https://arxiv.org/pdf/2607.15232v1)

**Abstract**: A tokenizer fixed at the start of pre-training allocates vocabulary in proportion to the pre-training corpus, reflecting the deployment priorities at that time. When those priorities shift, languages added later are split into many more tokens per word, which can raise latency, compute, and energy consumption for users of those languages. Cloud models can afford a broad vocabulary because the embedding and LM-head matrices are a small fraction of their parameters. On a compact model those matrices are a material share of per-token decode bandwidth, so on-device models ship small vocabularies and accept fragmentation outside a fixed language set. We present tokenizer expansion, an in-place recipe for upgrading a pre-trained model's tokenizer when the model producer controls its design. We continue the existing tokenizer's BPE merges on a multilingual corpus, so most source tokens carry over unchanged as single tokens and every new token has an exact decomposition into source tokens. We copy the carried-over embedding rows unchanged and initialize new rows as the mean of their source sub-token embeddings. A two-stage adaptation, embedding-only training then full-model continued pre-training, recovers source-checkpoint quality. We apply the recipe to a continued pre-trained checkpoint of LFM2-8B-A1B, an 8B-parameter Mixture-of-Experts model, to help produce LFM2.5-8B-A1B with a 128K tokenizer. The expanded tokenizer encodes Hindi and Vietnamese in roughly $2.4\times$ and $2.6\times$ fewer tokens than the source (up to $4.0\times$ on Thai). Combining these reductions with the measured per-token cost of the larger vocabulary, we estimate a $2.2$-$3.7\times$ per-character decode speedup for these languages across our reference devices. We release the model weights and the expanded tokenizer, and report the negative findings that shaped the recipe.


### CRISP: Constrained Refinement via Iterative Squeezing Process for Robust Medical Image Segmentation under Domain Shift
**Authors**: Yizhou Fang, Pujin Cheng, Yixiang Liu, Xiaoying Tang, Longxi Zhou

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15231v1](https://arxiv.org/pdf/2607.15231v1)

**Abstract**: Distribution shift in medical imaging remains a central bottleneck for the clinical translation of medical AI. Failure to address it can lead to severe performance degradation in unseen environments and exacerbate health inequities. Existing methods for domain adaptation are inherently limited by exhausting predefined possibilities through simulated shifts or pseudo-supervision. Such strategies struggle in the open-ended and unpredictable real world, where distribution shifts are effectively infinite. To address this challenge, we adopt the "Rank Stability of Positive Regions" as a working assumption under distribution shift, and use it to derive robust spatial hints for source-only segmentation. Guided by this assumption, we propose CRISP, a model-agnostic framework that, unlike deployment-time adaptation, requires no test-time parameter updates and no target-domain data--a target-free, plug-in refinement framework that segments with frozen weights. Rather than using ranking to directly output masks, CRISP exploits the stability of probability rankings under distribution shift to derive robust spatial priors. Via latent feature perturbation, perturbation-invariant high-grade regions define a high-precision (HP) core, while voxels that remain potentially foreground under at least one perturbation define a high-recall (HR) support; these dual priors are then recursively refined under perturbation. We then design an iterative training framework that progressively squeezes HP and HR toward the final segmentation. Extensive evaluations on multi-center cardiac MRI and CT-based lung vessel segmentation demonstrate CRISP's superior robustness, significantly outperforming state-of-the-art methods with striking HD95 reductions of up to 0.14 (7.0% improvement), 1.90 (13.1% improvement), and 8.39 (38.9% improvement) pixels across multi-center, demographic, and modality shifts, respectively.


### MAGiSt3R: Multi-Agent Feed-forward 3D Reconstruction from Monocular RGB Videos
**Authors**: Ziren Gong, Xiaohan Li, Fabio Tosi, Ninghui Xu, Stefano Mattoccia, Jianfei Cai, Matteo Poggi

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15211v1](https://arxiv.org/pdf/2607.15211v1)

**Abstract**: This paper presents MAGiSt3R, a multi-agent 3D reconstruction framework performing reconstruction and camera tracking for monocular RGB videos at almost 10 FPS. MAGiSt3R relies on a feed-forward model from the 3R family to process RGB videos and regress local point maps, and on a merging model, MAGMA, that combines local maps at both intra-agent and inter-agent levels to obtain the final global point map. Furthermore, MAGiSt3R performs pose graph optimization to mitigate cumulative camera drift occurring along the feed-forward pipeline. We evaluate MAGiSt3R on both synthetic and real-world datasets, demonstrating its superior reconstruction and camera tracking accuracy compared to state-of-the-art approaches.


### Self-Evolving Human-Centered Framework for Explainable Depression Symptom Annotation
**Authors**: Hoang-Loc Cao, Van Pham, Truong Thanh Hung Nguyen, Phuc Truong Loc Nguyen, Phuc Ho, Veronica Whitford, Hung Cao

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15202v1](https://arxiv.org/pdf/2607.15202v1)

**Abstract**: Annotation quality is a major bottleneck in building reliable and explainable artificial intelligence (XAI) systems for mental health research. In depression-related datasets, labels are often assigned without structured evidence, symptom-level justification, or traceable alignment with the criteria of the Diagnostic and Statistical Manual of Mental Disorders, Fifth Edition, Text Revision (DSM-5-TR), limiting both transparency and downstream model interpretability. We propose a self-evolving, expert-in-the-loop annotation framework for Major Depressive Disorder (MDD) that combines large language model (LLM)-assisted labeling with expert verification. The framework is intended to support the construction of explainable, DSM-5-TR-aligned datasets rather than to perform clinical diagnosis. It operates in three stages: candidate evidence selection from textual records, criterion-level DSM-5-TR analysis, and case-level synthesis that produces label-level diagnostic and severity annotations. A dual-memory architecture, composed of Example Memory and Reflection Memory, is designed to internalize expert feedback and iteratively improve future annotations without retraining. We describe this mechanism and leave its evaluation across multiple feedback cycles to future work. In addition to final labels, the framework exports clinical evidence, reasoning traces, and edit histories, enabling comprehensive auditability. In a pilot study using expert-reviewed samples, the proposed approach improves annotation consistency and explainability while reducing manual revision effort.


## Generation
### Mask-Aware Policy Gradients for Diffusion Language Models
**Authors**: Haran Raajesh, Kulin Shah, Adam Klivans, Philipp Krähenbühl

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15200v1](https://arxiv.org/pdf/2607.15200v1)

**Abstract**: Reinforcement learning has proven effective for improving reasoning in large language models, but extending it to Masked Diffusion Language Models (MDLMs) remains challenging due to the intractability of the log-likelihood estimation. Existing approaches approximate this log-likelihood by modeling only the token predictions, ignoring the order in which positions are unmasked during generation. We observe that MDLM generation involves two decisions at each step: what tokens to place at each masked position and which positions to remask. We formalize this as a two-stage action MDP, showing that the policy gradient naturally decomposes into a token term and a masking term. Combining optimization of both terms leads to state-of-the-art outcomes on mathematical reasoning and coding benchmarks, with scores of 87.1% on GSM8K and 53.4% on MBPP.


### The Industrialization of Research ; On AI-Driven Science and Its Consequences
**Authors**: Emmanuel Jeannot

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15164v1](https://arxiv.org/pdf/2607.15164v1)

**Abstract**: Artificial intelligence is transforming scientific research -- not merely as a more powerful instrument, but as an autonomous participant in the research cycle itself. This transition constitutes, in the most precise sense of the term, the industrialization of research: a shift from a craft model, in which knowledge, method, and judgment are embedded in the researcher, to a pipeline model, in which these steps are decomposed, automated, and supervised. The US Department of Energy's Genesis Mission is the most ambitious current instantiation of this shift, but the fundamental questions it raises extend far beyond any single program. This essay examines seven such questions: the erosion of the intergenerational transmission of scientific competence; the growing opacity of AI-generated theories; the collapse of peer evaluation under a flood of machine-generated output; the unproven capacity of AI for paradigm-shifting discovery; the capture of the scientific agenda by political and industrial actors; the compounding of systematic errors in closed-loop pipelines; and the structural bifurcation of the global research community into incommensurable tiers. These concerns do not constitute an argument against AI-driven science -- whose demonstrated potential is real and significant. They constitute the conditions under which that potential can be responsibly pursued.


### Concept-Guided Spatial Regularization for World Models in Atari Pong
**Authors**: Yukuan Lu, Zaishuo Xia, Weyl Lu, Yubei Chen

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15142v1](https://arxiv.org/pdf/2607.15142v1)

**Abstract**: World models are usually evaluated as components of model-based reinforcement learning (MBRL) systems, while the world models themselves are rarely studied in isolation.
  We examine five representative visual world-model agents in Atari Pong: DreamerV3, DIAMOND, TWISTER, Simulus, and STORM. After reproducing their training pipelines and matching the reported agent performance, we freeze the learned world models and evaluate them with a closed-loop rollout diagnostic: a policy trained separately from the corresponding MBRL agent interacts with each frozen model, and the generated video trajectories are inspected for visual and dynamical errors. Across all five models, the rollouts contain clear failures, including ball disappearance, incorrect ball motion, and invalid ball-paddle interactions.
  Beyond visual trajectories, we further evaluate them with pixel-space zero-shot MBRL, where a new policy is trained entirely inside a frozen world model and then evaluated in the real environment. Across all five models, the resulting policies substantially underperform those produced by the corresponding original MBRL training pipelines. The gap is particularly large for DreamerV3, whose mean return drops from -5.5 to -20.9, near the minimum Pong return of -21.
  We hypothesize that insufficient modeling of task-critical concepts, such as the ball in Pong, may contribute to these failures. We therefore propose Concept-Guided Spatial Regularization (CGSReg), an auxiliary pixel reconstruction loss applied to segmented concept regions. Experiments show that CGSReg improves both closed-loop rollouts and pixel-space zero-shot MBRL in DreamerV3, DIAMOND, and TWISTER. Its effects vary across the remaining models and evaluation metrics, indicating that CGSReg alone does not address all world-model bottlenecks.


### Learning in Infinitesimal Non-Compositional Sketches
**Authors**: Sridhar Mahadevan

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15107v1](https://arxiv.org/pdf/2607.15107v1)

**Abstract**: This paper develops a categorical framework -- Learning in Infinitesimal Non-Compositional Sketches (LINCS) -- as the repair of non-compositionality: failures of diagrams to factor through quotient sketches lifted to the tangent category setting. Machine learning problems are specified as sketches: graphs with commutativity conditions $\mathcal D$, limit cones $\mathcal L$, and colimit cocones $\mathcal K$, generalizing the usual scalarization of loss functions or vector space assumptions. Non-compositionality is defined purely as failure of a universal factorization problem, not as arithmetic error between the desired and actual predictions. Given a learning sketch $\mathbb S=(S,\mathcal D,\mathcal L,\mathcal K)$, whose underlying graph is $S$, and a model $D:J \rightarrow C$, the base defect is the obstruction to factorization $\mbox{Obs}(\mbox{Fact}_{\mathbb S}(D))$. The tangent lift applies the tangent functor $T$ to obtain $TD:J \rightarrow C$, and LINCS is defined as the obstruction $\mbox{Obs}(\mbox{Fact}_{\mathbb S}(TD))$ -- asking whether infinitesimal perturbations preserve the compositionality constraints.The paper also introduces Tangent Learning Sketches, which are sketches equipped with Cockett-Cruttwell tangent structure. The paper defines the INC endofunctor, which iterates the tangent lift, producing a tower $D,TD,T^2D, \cdots$ of factorization problems. ML is thereby formulated as the search for a coalgebraic fixed point where successive tangent unfoldings stabilize ($νT_{\mbox{INC}}$). Using the Aczel--Mendler theorem, we prove existence of a final INC coalgebra whenever $T_{\mbox{INC}}$ admits a set-based class realization that creates its final carrier. A detailed experimental evaluation of LINCS is underway in a number of concrete ML settings, including deep learning, large language models, and reinforcement learning, and is described in companion papers.


### Long-Context Fine-Tuning with Limited VRAM
**Authors**: Vladimir Fedosov, Aleksandr Sazhin, Artemiy Grinenko, Frank Woernle

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15105v1](https://arxiv.org/pdf/2607.15105v1)

**Abstract**: Parameter-efficient fine-tuning reduces model and optimizer memory, but dense attention still makes long training sequences expensive. We combine Hierarchical Global Attention (HGA) with segment-wise backpropagation and tiered KV storage. Only the active segment remains differentiable in VRAM; older KV is detached into RAM or NVMe, and HGA loads a bounded set of exact historical tokens for each query block. On Qwen3-8B with 4-bit QLoRA and PG19, dense training on a 16 GB Quadro RTX 5000 fits 2,048 tokens but fails at 4,096, whereas HGA reaches 16,384 tokens with 15.28 GB peak VRAM. Under evaluation the same adapter runs through 131,072 tokens on this card; VRAM is not constant but grows gently with the resident chunk summaries, so RAM and NVMe capacity set the practical limit beyond these lengths. At the shared 2K training length, HGA-trained and dense-trained adapters obtain 2.7405 and 2.7383 nat under the same dense-attention readout, while the stock model obtains 2.9541. At this boundary HGA training is already marginally faster (217.75 vs. 207.02 tokens/s), and the HGA-to-dense throughput ratio improves from 1K to 2K; because HGA keeps the attended historical set per token approximately constant while dense work per token grows, we expect this lead to widen as context grows. Dense attention is used for the main quality and retrieval comparisons so that they measure the learned weights and remain compatible with standard generation frameworks. HGA can also be used for retrieval and generation; an optimized production-grade serving implementation is under development.


### Digital Pantheon: Simulating and Auditing Coalition Formation with LLM Agents
**Authors**: Dylan Van Mulders, Matthias Bogaert, Dirk Van den Poel

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15095v1](https://arxiv.org/pdf/2607.15095v1)

**Abstract**: The formation of political coalitions is a complex negotiation driven by both concrete policy objectives and deep-seated ideological convictions. While Large Language Models (LLMs) open new avenues for computational political science, the neutrality and helpfulness biases instilled by Reinforcement Learning from Human Feedback (RLHF) prevent them from sustaining steadfast partisan behaviour. We present a multi-agent framework that reconciles factual grounding with ideological alignment by combining Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and Retrieval-Augmented Generation (RAG): DPO instils aggressive party-specific personas, while a per-party RAG pipeline keeps each agent bounded to its official manifesto. We operationalize the framework on the 2019 Flemish election, deploying the partisan agents in a hub-and-spoke negotiation arbitrated by a formateur. To make the emergent negotiation interpretable, we introduce a Multi-Layered Information Lineage Topology (MILT) that traces every clause in the final agreement back to its manifesto origin and classifies it into five provenance states, a Coalition Influence Score (CIS) that aggregates these traceable contributions to identify which party shaped the agreement, and a real-world grounding pass that benchmarks each simulated provision against the historically adopted coalition agreement. Across three independent simulations the framework yields a stable winner and ranking (N-VA ahead of CD\&V and Open Vld), and manifesto-anchored lineage reliably predicts real-world materialization whereas hallucinated content does not. The result is a transparent, scalable testbed for the ex-ante exploration of party compatibility and formateur-mediated compromise.


## VLA
### ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory
**Authors**: Jiayi Tian, Shiao Liu, Yuting Xu, Jia Lu, Zihao Guan, Honglin Han, Di Yang, Minqi Gu, Yifei Qian, Tianlin Zhang, Yanqing Zhu, Zeqian Ye, Menglin Yang, Fei Wang, Xu Hu, Xiuxian Li, Wei Zhang, Shihui Su, Yiyan Ji, Jingbo Wang, Ziteng Feng, Jiaheng Liu, Zhaoxiang Zhang, Xiaolong Wu, Zixiao Tang, Zhining Gu, Yang Cai, Linbo Zheng, Jingjing Ma, Mingyang Yin, Zedong Chu, Ziqiao Li, Mu Xu

**Published Date**: 2026-07-11

**Updated Date**: 2026-07-15

**PDF Url**: [2607.10350v2](https://arxiv.org/pdf/2607.10350v2)

**Abstract**: Recent VLM and VLA systems have improved robotic perception and action prediction, yet long-horizon embodied agents still require a general runtime layer for reasoning, memory, tool use, verification, and cross-embodiment execution. We present ABot-AgentOS, a general robotic Agent Operating System that sits above low-level controllers and provides a deliberative agent layer for scene-conditioned planning, context-isolated skill execution, multi-stage verification, multi-modal memory, and edge-cloud collaboration. To evaluate such systems, we introduce EmbodiedWorldBench, an executable benchmark with 16 indoor, outdoor, and hybrid scenes, four difficulty levels, and over 200 tasks involving navigation, object search, NPC dialogue, dynamic events, and trace-grounded scoring. ABot-AgentOS further introduces Universal Multi-modal Graph Memory, a persistent source-grounded substrate that converts dialogue, visual observations, spatial context, temporal relations, and task traces into typed nodes and edges. A failure-driven self-evolution loop converts diagnosed memory failures into gated runtime evo-assets that are promoted only to later evaluation splits, preventing current-split ground-truth leakage while enabling continual improvement. On an initial EmbodiedWorldBench subset, ABot-AgentOS improves over a single-controller baseline in both task success and goal completion. Across memory benchmarks, ABot-AgentOS Static achieves 87.5 on LoCoMo, 59.9 on OpenEQA EM-EQA, 88.6 on Mem-Gallery, and 76.5 Acc@All on NExT-QA; self-evolution further improves LoCoMo to 88.7, OpenEQA to 60.4, and Mem-Gallery to 89.0. These results suggest that a general Agent OS layer can improve long-horizon embodied execution while providing persistent, auditable memory for continual interaction.


### ActiveFly-Bench: Aligning Embodied Question Answering with Vision-Language-Action for Aerial Embodied Perception
**Authors**: Weichen Zhang, Shiquan Yu, Yinan Zhu, Peizhi Tang, Shilong Ji, Zhiyuan Deng, Tianyi Lyu, Haoyang Wang, Xin Zeng, Chen Gao, Yong Li, Xinlei Chen

**Published Date**: 2026-07-11

**Updated Date**: 2026-07-11

**PDF Url**: [2607.10180v1](https://arxiv.org/pdf/2607.10180v1)

**Abstract**: We introduce ActiveFly-Bench, the first benchmark to bridge cyberspace reasoning and physical-world interaction for UAV embodied perception. The benchmark decomposes active perception into three hierarchical tasks: Aerial Embodied Question Answering (Air-EQA), Observation Behavior Planning (OBP), and Fine-grained Language-guided UAV Control (FLUC), explicitly connecting high-level task understanding, behavior planning, and low-level control. The datasets are collected from both real-world and simulated outdoor environments for training and evaluation. We further develop ActiveFly, a closed-loop UAV agent that integrates visual-language reasoning with fine-grained control, and deploy it on a physical UAV platform. Experiments with representative VLMs and VLA models show that current UAV agents still struggle with behavior planning, viewpoint adjustment, and robust task completion in active perception. These results establish ActiveFly-Bench as a new testbed for embodied aerial intelligence.


### On the Efficiency of LoRA Fine-Tuning for Vision-Language-Action Models in Industrial Robotic Manipulation
**Authors**: Finn Ferchau, Daniel Pommer, Cristian Axenie

**Published Date**: 2026-07-11

**Updated Date**: 2026-07-11

**PDF Url**: [2607.10172v1](https://arxiv.org/pdf/2607.10172v1)

**Abstract**: Deploying billion-parameter Vision-Language-Action (VLA) models on industrial hardware requires fine-tuning to bridge the embodiment gap. Full Fine-Tuning (FFT) provides maximal plasticity but requires data centre-grade GPUs. We present a systematic study of Low-Rank Adaptation (LoRA) for $π_0$, a flow-matching VLA, evaluated on four precision assembly tasks with a UR5e robotic manipulator. Across a sweep of LoRA ranks (r=8 to 256), allocation strategies, and component-freezing ablations, we find no statistically significant advantage of FFT over certain LoRA configurations. Performance saturates at r=32, and uniform allocation across the Vision-Language-Model (VLM) backbone and action expert proves sufficient. Freezing the VLM or restricting the vision encoder to LoRA significantly degrades performance, indicating that embodiment adaptation requires both semantic and visual plasticity. These results suggest that LoRA at r=32 with full vision encoder fine-tuning is a practical approach, reducing static peak VRAM from 36.2 to 10.8 GiB (parameters and optimizer states, activation memory excluded) without detectable performance loss.


### TS-Mask VLA: 2D Temporal-Spatial Masking for Vision-Language-Action Model with Effective Bridging
**Authors**: Shengzhuo Yang, Ronghao Yu, Chuanjie Lv, Linpeng Peng, Hang Yu, Jie Ren, Jiajun Lv, Yong Liu

**Published Date**: 2026-07-10

**Updated Date**: 2026-07-10

**PDF Url**: [2607.09818v1](https://arxiv.org/pdf/2607.09818v1)

**Abstract**: Vision-language-action (VLA) models aim to understand natural-language instructions and visual observations, and to generate and execute corresponding actions as embodied agents. Recently, autoregressive token-based action generation has driven the development of many representative VLA models. However, this paradigm often reduces action generation to next-token prediction, thereby lacking explicit modeling of the spatiotemporal structure of action sequences and the disentanglement between vision-language representations and actions, which can limit performance in long-horizon and complex scenarios. In this paper, we propose TS-Mask VLA, a vision-language-action framework for robot manipulation. TS-Mask VLA is built upon two key designs: (1) a Discrete Diffusion Action Expert equipped with a Bridge Attention conditioning bridge, which enables multi-layer conditioning from the VLM and facilitates more accurate and stable action generation; and (2) a temporal-spatial 2D masking strategy for discrete action tokens that strengthens the model's understanding of cross-time dependencies and inter-dimensional coupling, leading to more structurally consistent action sequences. We conduct extensive experiments on simulation benchmarks and real-world tasks. On LIBERO, TS-Mask VLA achieves a 95.7 percent average success rate with only 0.5B parameters, outperforming significantly larger models. On CALVIN, it attains the best average sequence length of 4.19 and strong long-horizon performance. Comprehensive analyses and ablations further validate the effectiveness of our design.


### HELP: Human-Efficient Large-Scale Robot Post-Training with Rollout Segmentation
**Authors**: Shaopeng Zhai, Qi Zhang, Tianyi Zhang, Haoran Zhang, Fuxian Huang, Zhanhui Lin, Zijun Xu, Weinan Zhang

**Published Date**: 2026-07-08

**Updated Date**: 2026-07-15

**PDF Url**: [2607.09776v2](https://arxiv.org/pdf/2607.09776v2)

**Abstract**: When adapting Vision Language Action (VLA) models to downstream tasks, multiple rounds of post-training are often required to progressively address policy weaknesses. In this report, we focus on maximizing human efficiency during this iterative process, measured by policy improvement and task throughput per unit of human labor and time.
  We propose HELP, a Human-Efficient Large-scale robot Post-training pipeline in which two specialized operators supervise twelve robots concurrently. A trained Teleoperator provides high-value remote interventions and recovery demonstrations, while a Floor Operator monitors the robot fleet, triggers takeovers, and performs physical resets. This role specialization improves human efficiency by reducing task switching, lowering operator training costs, and expanding robot interaction coverage. Beyond increasing rollout volume, concurrent supervision also broadens the range of policy behaviors observed by the human team, making recurring failure modes easier to identify and enabling more targeted takeovers, resets, and recovery demonstrations. To efficiently utilize the large and mixed-quality rollout data, HELP incorporates \vlac, an automatic rollout segmentation critic specifically designed for this setting. It separates autonomous trajectories into progress-making, idle, failure-inducing, and recovery segments. Useful rollout segments are retained and combined with Human-in-the-Loop data for the next post-training round.
  Across four real-world manipulation tasks, HELP achieves 80\%--95\% success rates and improves task throughput by 1.7$\times$--4.2$\times$ over the base model. Under matched HITL recovery budgets, VLAC-CUT further amplifies throughput gains by 1.20$\times$--3.43$\times$ and success-rate gains by 1.50$\times$--3.00$\times$ over HITL-only updates.


## Agent
### BrainPilot: Automating Brain Discovery with Agentic Research
**Authors**: Haoxuan Li, Tianci Gao, Jianhe Li, Yang Fan, Runze Shi, Weiran Wang, Tianxiang Zhao, Zezhao Wu, Xiaoyang Jiang, Qihui Zhang, Jia Li, Xiao Xiao, Kai Du, Xiaoxuan Jia, Chao Xie, Lu Mi

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15079v1](https://arxiv.org/pdf/2607.15079v1)

**Abstract**: Understanding the brain increasingly depends on integrating evidence across scales, modalities, and disciplines. Addressing a single research question therefore requires a coordinated sequence of operations, from surveying prior work to executing analyses and interpreting results in light of domain knowledge. AI agents promise to accelerate this process, but current agents lack domain expertise in brain science, may fabricate claims, drift during multi-step reasoning, and offer few defined points for expert intervention. These failures are especially costly in brain science, where conclusions feed into downstream scientific claims and depend on laboratory-specific expertise and careful human judgment. We present \textbf{BrainPilot} a \textbf{fully open-source} multi-agent system that accelerates brain science research with traceable logs and agent-verified results. A principal investigator (PI) agent coordinates specialist agents grounded in curated domain knowledge: a unified brain science knowledge base containing 7{,}233 indexed items and a skill library of 72 reusable methodology units across seven research domains. Every major step is recorded in the Graph of Trace, an auditable record that links subgoals, tool use, evidence, and claims and allows researchers to follow and inspect the workflow. An Auditor agent further integrates fabrication checking into the workflow. For evaluation, we run three brain science tasks from Agents' Last Exam, introduce our own benchmark, \textbf{BrainPilotBench-v0}, and present additional end-to-end case studies. Across these evaluations, BrainPilot with an open-source backbone model attains performance comparable to state-of-the-art agent framework with less costs.


### ANet Patu-1: The Value of Connection in the Agent Network
**Authors**: Mu Yuan, Jinke Song, Zhaomeng Zhou, Lan Zhang

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15053v1](https://arxiv.org/pdf/2607.15053v1)

**Abstract**: The Internet taught us that the value of a network depends on \emph{how} its nodes connect: broadcast stars scale as $V\!\propto\!N$ (Sarnoff), fully-connected meshes as $N^2$ (Metcalfe), and group-forming networks as $2^{N}$ (Reed). We ask the analogous question for networks of AI agents. We model the net value of connection as a function of coordination-group size, derive from it the properties an optimal collaboration protocol must have, and introduce ANet Patu-1 -- a self-organizing consensus protocol in which the network continuously re-forms its own coalitions, adaptively riding the upper envelope of all three regimes at $O(1)$ parallel consensus rounds. To measure value without opinion-grading, we score an emergent protocol by formally specifying it and deriving its complexity, the way distributed algorithms are analyzed. Two results follow. (i)~Emergence -- a crowd of the \emph{cheapest} model, when heterogeneous, starts weak but its collective value compounds with $N$ and \emph{overtakes} a crowd of a far \emph{stronger} model that is homogeneous: a crossover that marks a scaling law for collaboration rather than for scale. (ii)~Reflexivity -- a heterogeneous network, given only its own problem and no design hints, converges on ANet Patu-1 itself, reconstructing the high-dimensional law that governs its own connective value.


### LQCDMaster: Agentic Scientific Computing for Lattice Quantum Chromodynamics Research
**Authors**: Haofei Gao, Tingjia Miao, Wenkai Jin, Muhua Zhang, Hanzhang Wang, Jie Ran, Jinxin Tan, Zhentao Zhang, Bo Tang, Leiyi Li, Jun Hua, Xiangyu Jiang, Qi-An Zhang, Siheng Chen, Wei Wang

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15001v1](https://arxiv.org/pdf/2607.15001v1)

**Abstract**: Lattice quantum chromodynamics (LQCD) provides a first-principles framework for computing hadronic observables, but its practical use remains limited by the substantial expertise required to turn research motivation into reliable computing workflows. Here we present \textsc{LQCDMaster}, a tool-augmented, skill-guided and domain-specialized scientific computing agent that converts natural-language LQCD research tasks into executable PyQUDA computing workflows, including measurement scripts, job-submission artifacts, execution logs and numerical outputs. The system combines agentic planning, expert-annotated LQCD skills and a deterministic Wick-contraction tool to constrain the algebraically fragile components of code generation. We evaluate \textsc{LQCDMaster} on a benchmark at the forefront of scientific research, comprising 70 LQCD computing tasks, with observables covering local and nonlocal two-point functions, Wilson loops, meson and baryon three-point functions. The generated workflows exactly reproduce expert-written implementations in 63 of 70 tasks at machine precision, with three additional discrepancies attributable to convention mismatches. Across representative observables, the agent reduces implementation time from hours to minutes while preserving end-to-end numerical validation. Further, we present a typical case of \textsc{LQCDMaster}-driven exploration: a lattice computation of light-cone distribution amplitudes with diagonal Wilson-line, a quantity accessible with standard methods but never before computed, and computation of the spectrum of proton, deuteron, triton, hyperon, hyperdeuteron and hypertriton. This work pioneers the paradigm of agentic scientific computing by automating the end-to-end scientific computing workflows in lattice QCD research, lowering its barrier and facilitating the exploration and verification of non-standard scientific ideas.


### OmniaBench: Benchmarking General AI Agents Across Diverse Scenarios
**Authors**: Chengyu Shen, Yujie Fu, Gangtao Xin, Yanheng Hou, Wenlong Fei, Guojie Zhu, Jiawei Li, Hongcheng Gao, Runming He, Zhen Hao Wong, Meiyi Qiang, Hao Liang, Zhao Cao, Hao Jiang, Chong Chen, Wentao Zhang

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.14989v1](https://arxiv.org/pdf/2607.14989v1)

**Abstract**: Large language models are increasingly evolving from text generators into general agents capable of understanding user requests, invoking external tools, and completing complex tasks through interaction. However, existing agent benchmarks often focus on limited scenarios, tool ecosystems, or interaction formats, making it difficult to systematically characterize model capabilities across heterogeneous application settings. We introduce OmniaBench, a benchmark for evaluating general agents across diverse scenarios with explicit state spaces. We derive application-oriented scenario knowledge from app stores, product documents, industry resources, Web retrieval, and human refinement, forming a hierarchical taxonomy that spans ToC, ToB and ToE with 90 level-1 and 354 level-2 domains. Based on this taxonomy, we construct executable environments and synthesize single-turn and multi-turn tasks through four complementary routes: DAG, DAG-S, Solver, and Program. OmniaBench further introduces a ten-dimensional capability taxonomy and eight compositional atomic difficulty factors to support fine-grained evaluation and analysis. The resulting dataset contains 1,431 tasks, together with a challenging subset of 644 tasks designed to reduce evaluation cost and mitigate potential contamination of the full set after public release. The bench presents substantial challenges to current frontier models, with even Claude-Sonnet-5 and GPT-5.6-Sol achieving Overall Pass@1 scores of only 58.54 and 57.14, respectively. Further analyses reveal clear differences across domains and capabilities, as well as persistent limitations in planning, constraint maintenance, and adaptive correction. OmniaBench provides a broad and diagnostic benchmark for characterizing the capability boundaries of general agents.


### LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget
**Authors**: Changhai Zhou, Kieran Liu, Yuhua Zhou, Qian Qiao, Jun Gao, Harry Zhang, Irvine Lu, Nolan Ho, Lucian Li, Andrew Lei, Cleon Cheng, Steven Chiang, Yihang Zeng, Di Zhang, Rio Yang, Kaijie Chen, Andrew Chen, Pony Ma, Weizhong Zhang, Cheng Jin

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.14952v1](https://arxiv.org/pdf/2607.14952v1)

**Abstract**: A growing gap separates inference context lengths from RL post-training: inference systems are approaching million-token contexts, while post-training workloads often remain at 256K tokens or below and rely on length generalization at deployment. The gap is especially important for AI agents, whose observations, tool outputs, documents, and prior decisions accumulate over long trajectories. LongStraw is an architecture-aware execution stack for million-token RL post-training under a fixed GPU budget, instantiated with Group Relative Policy Optimization (GRPO). It evaluates the shared prompt without autograd, retains only model-specific state needed by later tokens, and replays short response branches one at a time, reducing the live training graph at the cost of additional replay time. We implement it for the hybrid recurrent and full-attention Qwen3.6-27B and the compressed-attention mixture-of-experts GLM-5.2. On eight H20 GPUs, LongStraw completes grouped Qwen scoring and response backward at 2.1M positions for groups of 2 and 8; increasing the group size adds only 0.21 GB of peak allocated memory, while a separate stress test reaches 4.46M positions. On 32 H20 GPUs, we validate the end-to-end LongStraw execution path for a 2.1M-token prompt across all 78 layers of GLM-5.2. These experiments establish execution capacity rather than complete training correctness because the captured prompt state is detached and some distributed forward and gradient composition paths remain incomplete.


### StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural Engineering Workflows
**Authors**: Sizhong Qin, Yi Gu, Yao Jiang, Ao Cai, Changjian Zhou, Shaoxuan Shuai, Jiachang Wang, Tianhao Shen, Yueqiang Li, Xinhao Li, Li Zeng, Yueshi Chen, Dachen Gao, Genrong Xu, Wenjie Liao, Xinzheng Lu

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.14896v1](https://arxiv.org/pdf/2607.14896v1)

**Abstract**: Addressing a structural-engineering request requires more than a single answer; it requires a chain of interdependent artifacts: interpreted requirements, a computable model, validation records, solver outputs, code-check records, and a final report. Evaluations centered on question answering or script generation rarely verify this complete evidence chain and may therefore reward fluent outputs even when the underlying engineering workflow is incomplete, internally inconsistent, or non-executable. To address this limitation, we present StructureClaw, an artifact-centered workbench in which LLM agents operate through governed engineering skills, typed tools, shared artifact state, and local analysis backends. We also introduce StructureClaw-Bench, an executable benchmark of 150 controlled scenarios spanning standard workflow execution, interactive robustness, and multimodal structural-model reconstruction. A scenario succeeds only when all required artifact- and execution-level assertions pass in a single run. Across ten agent-model configurations, each evaluated on the same 50 standard cases, the average Success Rate rises from 56.8% with the generic-skill baseline to 88.6% with the full automatic workflow. The interactive and multimodal evaluations identify two prominent remaining challenges: safe handling of invalid numerical inputs and fixture-consistent reconstruction of structural models. These findings show that artifact-centered evaluation can expose workflow-level failures that are difficult to identify from final responses alone, providing a more rigorous basis for evaluating and improving structural-engineering agents. The code and benchmark are available at https://github.com/structureclaw/structureclaw.


