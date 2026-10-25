# Abstracts of Papers

## World Model
### Cost-Aware Abstention for LLM-Based IT Ticket Classification
**Authors**: Sachin Gupta

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31657v1](https://arxiv.org/pdf/2610.31657v1)

**Abstract**: Wrong automatic routing of an IT support ticket can cost more than human triage. We evaluate cost-aware abstention as an offline, cost-conditional readiness assessment: select a routing policy on calibration data under explicit costs, then evaluate that frozen policy once on held-out test data. On a public 47,837-ticket, eight-class corpus, we compare four trained non-LLM classifiers with four large language models under zero- and few-shot prompting. Under the illustrative cost model (c_ok, c_triage, c_wrong) = (0, 1, 5), TF-IDF with logistic regression and a threshold of 0.60 selected on calibration reduces test cost from 0.763 to 0.472, a 38.1% relative reduction (paired ratio-bootstrap 95% CI [35.7%, 40.4%]), while lowering wrong routes from 15.3% to 3.5%. Frozen calibration-selected policies also beat both always-route and always-defer on held-out test data in 14 of 16 settings in a post-hoc cost-parameter analysis. The strongest prompted configuration reaches 0.477 accuracy on a stratified 1,000-ticket test subset, versus 0.879 for fine-tuned DistilBERT on the same tickets. Isotonic lowers expected calibration error without reliably improving discrimination: GPT-4o-mini few-shot has one confidence value before and after recalibration and correctness AUROC 0.500. We therefore report correctness AUROC and tie-aware risk-coverage area alongside ECE. At the analytically derived break-even probability 0.80, seven prompted configurations defer all tickets; Haiku few-shot routes only 19/1,000. An LLM-only agreement control and margin/entropy rejection baselines further separate calibration from discrimination. The findings are scoped to this dataset, prompt design, model endpoints, and illustrative costs; the work is an evaluation framework, not a new abstention algorithm or universal deployment certification.


### BrickWright: Agentic Creation of Physically Feasible Brick Builds
**Authors**: Ava Pun, Kevin Dai, Sally Chen, Maxwell Jones, Ruixuan Liu, Kangle Deng, Changliu Liu, Maneesh Agrawala, Deva Ramanan, Jun-Yan Zhu

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31651v1](https://arxiv.org/pdf/2610.31651v1)

**Abstract**: Frontier coding agents are becoming increasingly adept at 3D modeling. Yet, they still face challenges when building objects meant to be assembled in the physical world, often creating invalid assemblies with floating, colliding, or disconnected parts. We argue that providing agents with tools for assembling builds and verifying their physical feasibility is sufficient for them to produce physically valid assemblies that still adhere to input prompts. Focusing on the domain of LEGO brick builds, we present BrickWright, a framework for generating physically feasible brick builds from text or image prompts using pre-trained agents, where a build is physically feasible if it uses only real parts, has no colliding or floating parts, and forms a connected structure if possible. BrickWright guides agents to create builds by writing code with BrickLayer, a Python toolkit with two main components: an ergonomic brick assembly API that halves inference cost compared to working in raw LDraw, and a validator that provides feedback on physical feasibility. Whereas baseline agents achieve physical validity rates ranging from only 9% (GPT-6 Luna) to 69% (GPT-6 Astra), BrickWright-guided agents achieve 100% validity on a sample of 512 prompts, while improving prompt adherence for lightweight agents and maintaining it for stronger agents. Additionally, they outperform specialized models on the text-to-brick task. Code is available on our project page: https://avalovelace1.github.io/brickwright/


### Gate3DGen: A Pre-processing Model that Selectively Purifies Real-World Images for 3D Generation
**Authors**: Xiaolin Li, Zihao Huang, Fanpeng Meng, Chen Yang, Guanjun Wu, Kai Zhang, Jiemin Fang, Qi Tian

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31649v1](https://arxiv.org/pdf/2610.31649v1)

**Abstract**: Single-image 3D generation has achieved high fidelity on curated benchmarks, yet degrades sharply on real-world images with uneven illumination, blur, and occlusions. Purifying such inputs requires deciding when to intervene and preserving the visual cues needed for 3D generation, while leaving clean inputs unchanged. We introduce Gate3DGen, a selective pre-processing model that gates image inputs to existing 3D generators without retraining them. A degradation-aware router bypasses inputs classified as clean and extracts features to guide purification of the remaining inputs. Conditioned on these features, a 3D-oriented one-step purifier purifies degraded inputs with spatial losses that encourage preservation of object identity, contours, and textural cues. To provide paired supervision, we construct a synthetic data engine that renders clean views of 3D assets and synthesises composite degradations. On the synthetic benchmark, the purifier improves image fidelity and downstream 3D geometry in only 2.3s on average, reducing TRELLIS.2 mesh distance by 61.5% relative to degraded inputs. VLM evaluation and human preferences on real photographs further support identity preservation and degradation correction. More demos and code are available at https://supra-3d.github.io/gate3dgen.


### Low-Bit N-Gram Embeddings for Language Models
**Authors**: Stephen Chung, Wenyu Du

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31646v1](https://arxiv.org/pdf/2610.31646v1)

**Abstract**: Many recent open-weight language models use n-gram embedding tables to improve performance. These tables store learned representations of short token sequences, such as pairs or triples of consecutive tokens, which the model retrieves during processing. However, they can require substantial memory: DeepSeek-V4.1-Flash, for example, allocates 196 billion parameters to its Engram n-gram memory. We therefore investigate whether this memory cost can be reduced while preserving the performance improvement that the tables provide. We propose storing n-gram embeddings at low precision and systematically investigate different quantization methods and bit allocations across tables. Across nanochat-, Llama-, and GPT-2-family models trained from scratch, four-bit tables save approximately 75% of table memory while preserving more than 99% of the validation-loss improvement from adding the tables. Using fewer bits leads to a larger drop in performance, although we find that a short fine-tuning phase recovers a significant part of this loss. In addition, reinvesting the saved memory in larger tables can improve performance beyond that of the original full-precision tables while still using less memory. These table memory savings also extend to large existing models: on DeepSeek-V4.1-Flash and Qwen3.8-Flash-Next, low-bit tables save 47-55% of table memory, with perplexity increases of less than 1.2% and largely preserved downstream task performance. These findings establish low-bit precision as a practical way to reduce the memory requirements of n-gram embeddings and use the saved capacity to improve model performance.


### UniVOE: A Removal-Driven Framework for Interaction-Aware Universal Video Object Editing
**Authors**: Shuzhou Yang, Lanqing Guo, Lingen Li, Weiqi Li, Zhao Zhong, Liefeng Bo, Jian Zhang

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31641v1](https://arxiv.org/pdf/2610.31641v1)

**Abstract**: Video object removal and injection are reciprocal editing operations between object-present and object-absent video states, yet they differ substantially in training difficulty. Removal can be effectively bootstrapped from video inpainting and further adapted to erase object-related interaction effects. Injection, however, requires large-scale paired supervision to model object appearance, dynamics, and scene-dependent effects, while perfectly aligned real-world pairs are difficult to collect and synthetic data lacks sufficient realism and diversity. To address this challenge, we present UniVOE, a removal-driven framework for training both video object removal and injection models. We first train an effect-aware remover by transferring video inpainting priors and finetuning on object-present/object-absent pairs. The trained remover converts real object-present videos into object-absent counterparts, creating large-scale paired supervision for injection. An injection model is trained on these pairs in the reverse direction to recover objects together with their dynamics and interaction effects. Moreover, since pixel-level reconstruction alone cannot adequately capture perceptual realism, we introduce a reward-based post-training method that aligns injection results with human preferences using a proprietary reward model. Experiments against strong open-source and commercial systems demonstrate that UniVOE achieves state-of-the-art performance on both object removal and injection, particularly in challenging interaction-effect cases.


### F2G-Pose: Geometry-Aware Foundation Feature Lifting for Direct RGB-D Category-Level Object Pose Estimation
**Authors**: Jinyu Zhang, Haitao Lin, Jiashu Hou, Xiangyang Xue, Yanwei Fu

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31623v1](https://arxiv.org/pdf/2610.31623v1)

**Abstract**: This paper studies category-level RGB-D object pose estimation, which recovers an object's 3D rotation and translation without instance-specific CAD models or reference views. This task is highly ambiguous due to intra-class variations, symmetries, and partial observations. Current solutions struggle to balance reliability and efficiency: methods based on intermediate structures are prone to error propagation, while diffusion models suffer from high inference latency and complex post-hoc candidate extraction. To address this, we present F2G-Pose, a real-time direct, single-pass framework that predicts category-level pose, metric size, and camera-frame completed shape from a single RGB-D observation in one feed-forward pass. F2G-Pose lifts dense visual foundation features to partial point clouds, encodes local geometry with DGCNN tokenization, and integrates object-level structure with a Mixture-of-Experts Transformer. Joint size prediction and camera-frame shape completion encourage metric consistency through dense geometric supervision. With its task-specific network trained only on pose-annotated synthetic SOPE data and its frozen RADIO backbone externally pretrained, F2G-Pose achieves state-of-the-art accuracy on SOPE and ROPE while running at 28 FPS for pose-only inference, and further demonstrates strong camera-frame geometry on HouseCat6D and real-object transfer on HANDAL. Analyses of latency, robustness, shape completion, and GenPose++ candidate behavior further demonstrate the efficiency and reliability of F2G-Pose, with real-world manipulation experiments demonstrating deployment potential under segmented RGB-D inputs. The project page, code, and pretrained models are made available at https://jrryzh.github.io/F2G-Pose/.


## Generation
### What Makes a Good Unmasking Policy? A Controlled Study of Learned Unmasking in Diffusion Language Models
**Authors**: Jinya Sakurai, Xun Xu, Jaehong Yoon

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31576v1](https://arxiv.org/pdf/2610.31576v1)

**Abstract**: Masked diffusion language models generate tokens in parallel, but their efficiency depends on which predictions are committed. Learned unmasking policies improve the speed--accuracy trade-off, yet differ in supervision, inputs, and capacity, obscuring which choices matter. We view supervised policies as distilling a decoding procedure through a teacher and examine independently what the teacher labels as committable, on which states the policy imitates it, what the policy observes, and how much the number of function evaluations (NFE) must decrease to offset policy overhead. We find that labeling predictions matching the final output is overly permissive at low NFE, and hidden states are weak alone but can complement confidence. About a 10% NFE reduction suffices to offset policy overhead for policies up to 7.5M parameters across tested settings. We therefore train a policy on trajectory-contraction targets, which accept only commitments staying on a reference trajectory, using confidence and hidden states. On LLaDA-8B-Instruct, the resulting 856K-parameter policy achieves the best accuracy--NFE frontier and highest throughput on GSM8K, is competitive at moderate targets on MATH-500 and HumanEval, and largely transfers to Dream-7B-Instruct.


### Rethinking Sequence Compression with Test-time Regression
**Authors**: Sihan Yang, Jie Huang, Hanxuan Li, Yifan Guo, Weigao Sun, Yiran Zhong, Weiyang Liu

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31574v1](https://arxiv.org/pdf/2610.31574v1)

**Abstract**: Sequence compression is a fundamental operation and a critical information bottleneck in efficient language and multimodal models, and yet prevailing approaches based on pooling or learned projections remain underperforming. We revisit sequence compression through the lens of test-time regression: input tokens define a regression problem whose fitted coefficients form the compressed representation. Importantly, the regression problem is learned end-to-end via backpropagation, while its coefficients are computed efficiently in closed form during the forward pass. This leads to TTR-Compressor, a general alternative to conventional pooling and projection-based compression. We evaluate TTR-Compressor as the compressor for block-wise sparse attention and the visual token merger for multimodal large language models. On block-wise sparse attention, TTR-Compressor improves RULER performance over attention-based compressors by a large margin. For visual token merging, it consistently outperforms the standard MLP merger and matches its performance with 55.6% fewer visual tokens. These results establish test-time regression as an effective primitive for sequence compression in efficient language and multimodal models.


### On the Token Collapse Phenomenon in Textual Graph Soft Prompting
**Authors**: Andrea Giuseppe Di Francesco, Rishabh Jain, Franco Maria Nardini, Nicola Tonellotto, Pietro Liò, Fabrizio Silvestri

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31572v1](https://arxiv.org/pdf/2610.31572v1)

**Abstract**: Recent methods for injecting graph structure into LLM prompts include graph soft prompting, in which a graph neural network (GNN) learns graph-specific tokens that capture relational information among entities in textual prompts. G-Retriever combines graph soft prompts with a verbalized description of the same graph to strengthen the textual prompt signal. We conduct an in-depth analysis of G-Retriever and uncover a pathological behavior we term token collapse. Across three benchmarks, three graph encoders, two LLM families, and both frozen and LoRA-adapted models, G-Retriever's graph tokens become almost indistinguishable across inputs. We provide evidence that the same failure is inherited by subsequent methods, even with multi-token pooling. Under the standard setup, swapping a token with the dataset mean, a token from another example, or one derived from a corrupted graph produces no resolved answer-level effect in accuracy. Moreover, a learned constant prompt that never accesses the graph matches or surpasses G-Retriever on all three benchmarks. These findings indicate that, rather than conveying graph content as intended, the collapsed token functions primarily as a generic soft prompt. We also examine conditions linked to this collapse and propose a two-stage procedure that yields non-collapsed tokens while maintaining competitive performance in most cases. However, token variability alone does not prove that the model uses graph information: via interventions and decoding probes, we show that depending on the configuration, a token can reflect the question, an answer prior, or graph-derived content that the LLM may or may not use. Overall, our results offer a practical approach to evaluating graph-token alignment rather than inferring it from task accuracy alone. Code to reproduce our experiments is available at https://github.com/difra100/Token_Collapse_KGQA.


### Diffusion Language Models for Perplexity-Aware Black-Box Attacks
**Authors**: Ali Al-Lawati, Elsayed Eshra, Dongwon Lee, Suhang Wang

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31558v1](https://arxiv.org/pdf/2610.31558v1)

**Abstract**: \emph{Continuous-space} attacks find prompts that trigger malicious behaviors, such as overthinking, in black-box LLMs by sampling or optimizing over a low-dimensional Gaussian latent space and decoding it to text through a \emph{random mapping} and nearest-token lookup. Because the random mapping is not learned from language, its prompts can be highly unnatural, and as such easily detectable through input guardrails, and the risk estimates they yield are not grounded in natural prompts. In this paper, we demonstrate that the same continuous latent-space framework can be coupled directly to a learned generative distribution over language, a continuous diffusion language model (dLLM), which removes the artificial random mapping while preserving the standard-Gaussian latent formulation and the downstream sampling or optimization procedure. We evaluate this approach under two settings: sampling-based estimation using \emph{RareTrap} and optimization-based search using \emph{ThinkTrap}. We find that character-level perplexity drops from $10^3$--$10^7$ to 3--5 in RareTrap and from 20--28 to 4.3--5.4 in ThinkTrap. We also find that model risk estimates can differ by an order of magnitude across the two mappings.


### Fine-Grained Analysis of Catastrophic Forgetting in Continual Learning via Algorithmic Stability
**Authors**: Guodong Zheng, Yan Sun, Peng Wang, Enneng Yang, Jiafei Lyu, Xiaochun Cao, Dacheng Tao, Li Shen

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31551v1](https://arxiv.org/pdf/2610.31551v1)

**Abstract**: Understanding catastrophic forgetting, in which learning new tasks degrades performance on previously learned tasks, remains a fundamental challenge in continual learning (CL). Existing theoretical analyses often rely on specific model or task structures and offer limited insight into how iterative optimization affects forgetting. To address this gap, we develop an algorithmic stability framework for expected population forgetting under SGD without prescribing a particular model architecture. Specifically, we decompose forgetting into intra-task and cross-task generalization gaps and empirical forgetting. To bound the generalization gaps, we track how a sample perturbation affects updates within a task and propagates through subsequent tasks. We consider constant, intra-task decaying, and continuously decaying learning-rate schedules. Comparing the two decaying schedules allows us to characterize how restarting learning-rate decay at task boundaries affects the propagation of historical sample perturbations. For empirical forgetting, we derive bounds for all three schedules by retaining cumulative gradient alignment along the optimization trajectory, without requiring convexity. Combining these results yields upper bounds on expected forgetting that capture the effects of training set size, the number of updates per task, the total number of tasks, learning-rate schedules, and cumulative gradient alignment. Finally, we conduct experiments on Split CIFAR-100 and Split MiniImageNet to examine the empirical implications of our theoretical findings.


### Beyond Causal Masks: Auditing and Localizing Hidden Future-Token Leakage in Adaptive Sequence Models
**Authors**: Huiting Liu, Jinsong Wu

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31522v1](https://arxiv.org/pdf/2610.31522v1)

**Abstract**: Hidden future-token leakage can create false architectural gains: an autoregressive model may appear substantially better under teacher-forced evaluation while its free-running generation deteriorates. We investigate this failure in an adaptive residual-routing decoder whose sequence-level routing summary exposes prefix positions to future tokens despite a correct causal attention mask. An anomalous 24-layer checkpoint reduces validation loss from the baseline's 3.5958 to 1.4259, yet it fails a prefix-invariance audit and has substantially higher reference-model perplexity during generation. Layer-wise diagnostics and implementation inspection trace the violation to a full-sequence summary broadcast through the dynamic routing-query path. Two independently trained 12-layer causal repairs eliminate detectable leakage and return validation loss and reference perplexity to the control scale, removing the large apparent advantage. As diagnostic tools, we use the established prefix-invariance contract, maximum prefix-output discrepancy (LeakScore), complementary behavioral metrics, and layer-wise profiles. Supporting experiments cover six synthetic implementation pairs spanning five module families, clean pretrained controls, controlled fault injection, and cache consistency across numerical precisions. These results illustrate how hidden future-token access can produce misleading claims of architectural progress and why lower teacher-forced loss should be interpreted together with whole-model causal checks and free-running evaluation.


## VLA
### From Association to Decision Value: Testing Paired Instruction Dependence for VLA Corpus Selection
**Authors**: Nurmukhambet Serikbayev, Abdul Basit, Muhammad Shafique

**Published Date**: 2026-10-21

**Updated Date**: 2026-10-21

**PDF Url**: [2610.29646v1](https://arxiv.org/pdf/2610.29646v1)

**Abstract**: Choosing among robot demonstration corpora is a ranking problem: an upstream diagnostic must preserve which candidates produce better downstream policies, not merely correlate with average performance. We study paired instruction dependence, the rate at which a demonstrator changes its first decision when only the goal changes. Across 136 independently seeded quadruped-navigation corpora, predictions developed on 56 corpora are evaluated prospectively on 80 held-out corpora. The audit is reliable and associated with downstream paired correctness, and lowers mean absolute prediction error when added to a correctness-aware baseline, but the primary proper-log-score increment is +0.059 nats (95% corpus-bootstrap CI [-0.027, 0.133]) and the prespecified top-20% comparison does not establish an incremental selection gain. An exploratory response decomposition suggests a structural source of this predictive-ranking mismatch: under the tested predictor specification, separating both-correct and both-wrong responses yields larger held-out gains than their unsigned switch statistic. Seed-to-seed agreement indicates that the held-out endpoint retains recoverable rank signal. These results show that counterfactual response structure can be reliable and predictive while providing limited incremental decision value in this setting when compressed into an unsigned statistic, motivating diagnostics that preserve outcome-relevant structure and are validated against the decisions they are intended to support.


### VLA-Rolling: Fewer Denoising Steps, Better Control via Adaptive Action Reuse
**Authors**: Sicheng He, Yi Pan, Qiuting Yu, Jiaming Huang, Qi Lu, Shuyan Wu, Hongyan Feng, Xuanyu Liu, Jun Zhang, Jie Zhang, Wenqi Zhang, Xuhong Zhang, Jianwei Yin

**Published Date**: 2026-10-18

**Updated Date**: 2026-10-21

**PDF Url**: [2610.25043v3](https://arxiv.org/pdf/2610.25043v3)

**Abstract**: Flow-matching vision-language-action (VLA) models generate an action chunk by iteratively denoising Gaussian noise, but typically execute only a short prefix before replanning with updated observations. Under this receding-horizon paradigm, the unexecuted remainder---the action tail---is discarded, and the next chunk is regenerated from fresh noise. We show that this discarded tail retains transferable denoising progress: action-tail initialization can match or outperform a native 10-step Gaussian baseline using fewer denoising steps. However, the optimal denoising budget varies substantially across samples, indicating that tail reuse should be adapted to the updated environment. Based on this observation, we introduce VLA-Rolling, a lightweight inference framework that reuses action tails through three stages: action-tail inheritance, per-action confidence estimation, and confidence-guided refinement through renoising and denoising budget allocation, while the underlying VLA remains frozen. Across $π_{0.5}$, SmolVLA, X-VLA, and MolmoAct2 on LIBERO, MetaWorld, LIBERO-Plus, and RoboTwin 2.0, VLA-Rolling reduces action-chunk inference cost in all 16 model--benchmark pairs, achieving up to a $1.48\times$ speedup, while improving success rate in 14 pairs by up to $15.08$ percentage points. These results show that action tails are not merely discarded predictions, but reusable intermediate states that enable more efficient and accurate VLA inference. These results demonstrate that the action tail can support the generation of better actions with fewer denoising steps. Our project is available at https://chenbao123ww.github.io/VLA-Rolling/.


### Scene-Adaptive VLA: Efficient Autonomous Driving via Dynamic Layer Routing
**Authors**: Yujia Yang, Quan Yuan, Jiawei Fan, Yang Li, Tiange Fu, Xiaoyuan Fu, Guiyang Luo, Jinglin Li

**Published Date**: 2026-10-17

**Updated Date**: 2026-10-17

**PDF Url**: [2610.24590v1](https://arxiv.org/pdf/2610.24590v1)

**Abstract**: Vision-Language-Action (VLA) models offer a promising paradigm for autonomous driving. However, the massive parameter scale of VLAs strains onboard computational resources during real-time inference. This directly increases energy consumption and limits vehicle battery range, making it critical to minimize computational overhead without compromising driving capability and explainability. Current research on efficient VLA-based driving focuses on sequential adaptation (\textit{e.g.}, Chain-of-Thought and token adjustment), leaving structural adaptation underexplored despite parameter redundancy across dynamic driving scenes. To address this gap, we propose Scene-Adaptive VLA, an efficient framework leveraging dynamic layer routing to adjust active parameters based on real-time scenes. Inspired by the temporal continuity of scenes and model predictive uncertainty, our approach characterizes model-perceived scene complexity via frame-level temporal scene variations and decision deviations. To uncover latent scene-to-parameter correspondences, we encode this characterization into scene-aware tokens, alongside two specialized queries. A budget-conditioned layer routing mechanism evaluates these refined queries to allocate a budget that determines the active parameter ratio and subsequently selects appropriate layer combinations. The entire framework is optimized end-to-end. Extensive evaluations on the Bench2Drive benchmark show that when adapted to a state-of-the-art VLA model, our approach significantly reduces inference-time computational overhead by 53.5\% with negligible degradation in driving and language capabilities. Code is available at https:github.com/yang-luvu/Scene-Adaptive-VLA.


### GazeAct: A Human-Gaze-Annotated Manipulation Dataset for Attention-Regularized Policies
**Authors**: Anupam Pani, Wang Yuan, Qifan Wang, Yanchao Yang

**Published Date**: 2026-10-17

**Updated Date**: 2026-10-17

**PDF Url**: [2610.24507v1](https://arxiv.org/pdf/2610.24507v1)

**Abstract**: Vision-language-action (VLA) policies must ground language instructions in the right objects, contact points, and target locations for reliable manipulation. Human gaze provides a natural signal for this grounding, but existing robot datasets rarely pair real human gaze with the multi-camera observations used by modern policies. We introduce GazeAct, a gaze-equipped real-robot manipulation dataset and training framework for multi-view VLA policies. Using screen-based teleoperation, we record gaze directly on the robot camera feed viewed by the operator, yielding 12000 demonstrations across 40 tasks and five domains with 300 Hz gaze synchronized with images, proprioception, and actions. We transfer gaze from the operator-selected view to the remaining synchronized cameras, producing spatially consistent targets across the policy's visual inputs. We then use these gaze-derived targets to regularize language-conditioned visual attention during training while keeping inference gaze-free. Across 18 real-world tasks, our method improves average success from 48.1% to 58.6%, with gains up to 25 percentage points. Ablations show that gaze works best as soft supervision and that real human gaze provides stronger attention targets than generic attention-shaping priors. The gains transfer to LIBERO-Spatial (57.9% to 69.6%) and different VLA backbones.These results show that gaze collected in the robot observation space can provide effective training-time targets for improving visual grounding in VLA manipulation.


### FlashRT-PAI: Fast Kernels Are Not Fast Pipelines for Physical AI Inference
**Authors**: Liang Su, David Chen, Jason Li, Kevin Guo, Teresa Lv

**Published Date**: 2026-10-17

**Updated Date**: 2026-10-17

**PDF Url**: [2610.24349v1](https://arxiv.org/pdf/2610.24349v1)

**Abstract**: Vision-language-action (VLA), video-action (VA), and world action models (WAMs) form the backbone of modern physical AI systems, yet their real-time single-batch inference remains a defining bottleneck. Latency is dominated not by individual kernel computation, but by system-level overhead: thousands of short kernel launches, intermediate data movement across operator boundaries, and redundant recomputation across consecutive decisions. General-purpose graph compilers cannot address these costs, as they optimize individual calls in isolation and lack visibility into cross-call state semantics and global pipeline structure. We present FLASHRT-PAI, a low-latency inference engine built around model-hardware pipeline co-design rather than isolated kernel optimization. FLASHRT-PAI combines three core mechanisms: deep kernel fusion with launch overlap eliminates inter-operator boundaries and launch gaps; an execution contract formalizes the pipeline's stage DAG, update rates, and named buffers to enable cross-decision state reuse and selective refresh; and execution-state capsules enable fast snapshot, restore, and fork of persistent pipeline state. The system also supports drop-in acceleration of unmodified PyTorch models via parity- and latency-gated kernel replacement. Evaluation covers six policies on RTX 5090 and four on Jetson AGX Thor. At matched 16-bit precision, FLASHRT-PAI is 1.3-3.7x faster than official compiled paths. Combining pipeline co-design with reduced precision delivers 3.38-12.66x speedup over official eager implementations. In LIBERO-10, four-bit pi0.5 achieves 94.04% success on Thor and 93.32% on RTX 5090, compared with 92.4% for the measured official FP16 reference. FLASHRT-PAI is open source, distributed via Hugging Face Kernel Hub, and its opt-in pi0.5 kernels have been adopted into the LeRobot framework.


## Agent
### Training Small Language Models for Transferable Tool Selection
**Authors**: Zhaoyi Zhou, Akshayaa Magesh, Jeongyeol Kwon, Artem Kuriksha, Daniel Jiang, Andrea Zanette, Ayush Jain

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31483v1](https://arxiv.org/pdf/2610.31483v1)

**Abstract**: As LLM agents operate over corpora of more than ten thousand tools, selecting the right tool for a complex multi-step user instruction becomes a central bottleneck. Tool descriptions cannot all fit in context, and relevance-based retrievers only rank tools without knowing which are actually needed. Recent work instead leverages proprietary commercial LLMs like Claude or ChatGPT to drive a retriever, decomposing the instruction and selecting over retrieved candidates. We show that a small, open model can be trained via reinforcement learning to perform the same functionality. On ToolBench, a Qwen3-8B model post-trained with our recipe outperforms Llama-4-Maverick (402B). In addition, the trained model transfers directly to different retrievers and generalizes to new tool corpora in different domains.


### Adaptive Skill Granularity for Coding Agents: Runtime Routing and Macro-to-Micro Recovery
**Authors**: Dingxuan Zhang, Yanhui Jiang, Jun Wang, Hefeng Zhou

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31461v1](https://arxiv.org/pdf/2610.31461v1)

**Abstract**: Reusable skills allow large language model agents to package task-specific procedures, tool affordances, and execution guidance into modular units. Prior work has largely studied how agents retrieve, compose, or synthesize skills before execution. In coding agents, however, execution poses an additional runtime control problem: the same task may be solved through primitive tool calls, macro skills, or hybrid execution that starts with a macro and falls back to micro-level recovery. We introduce Adaptive Skill Granularity, a framework that treats skill granularity as an action-abstraction policy conditioned on task structure, execution state, and macro-skill failures. The system combines a feature-based granularity controller and a finite-state recovery executor. We evaluate the framework with a deterministic coding-agent protocol using verifier-defined success, total cost, and process metrics such as macro adoption, failure recovery, route match, and transition correctness. Results show that fixed macro execution is efficient when applicable but brittle under mismatch, while runtime routing and explicit macro-to-micro recovery improve robustness and recover controlled macro failures that fixed-granularity execution leaves unresolved. Our findings suggest that skill libraries for coding agents should be treated not only as retrievable resources, but also as controllable, verifiable, and recoverable execution abstractions.


### Conservative Meta-Agent Search: Architecture Adaptation under Non-Stationarity
**Authors**: Ali Atiah Alzahrani

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31436v1](https://arxiv.org/pdf/2610.31436v1)

**Abstract**: Automated agentic-system design is typically evaluated on static task suites with immediate scalar rewards. Deployed systems face persistent shift, delayed dependent feedback, correlated component failures, and costly architecture changes. We formalize meta-agent architecture search as sequential incumbent replacement with switching costs and hard risk constraints and introduce Conservative Meta-Agent Search (CMAS). CMAS retrieves archived architectures and proposes typed graph edits, then scores each against the incumbent by paired shadow replay under common random numbers, with interventional component credit. Promotion requires an empirically calibrated, variance-penalized simultaneous score above a pre-specified margin, and is followed by a simulated canary stage and pre-specified rollback. Since backtests cannot certify meta-level skill, we introduce MetaInvest-Bench, a regime-switching simulator whose specified worker competence makes a surrogate-optimal architecture computable, with leakage-controlled replay, adversarial governance tracks, and five negative controls. Financial streams serve as a risk-sensitive testbed for meta-level generalization; we claim no alpha. Across 96 streams, CMAS cuts normalized mean surrogate dynamic-oracle regret from 0.116 to 0.104 and raises held-out utility from 0.44 to 0.48 over the strongest adaptive baseline; when extra workers add no value, it contracts to near-single-agent teams. Its deployment inference cost is ~6% lower, though its search-inclusive token cost is the highest of the methods compared. The observed per-update false-promotion rate is 3.4% against a nominal 5% target, and 4.8% in a sealed rerun. The calibration is empirical: it concerns an update-level replay statistic on an author-designed benchmark, and guarantees neither full-utility improvement, nor absence of simulated canary-stage harm, nor sequence-level error control.


### AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack
**Authors**: Justin Tan, Miao Li, Ding Zhao

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31404v1](https://arxiv.org/pdf/2610.31404v1)

**Abstract**: Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose vulnerabilities that pre-existing datasets may miss, we introduce AgentPhishing, a benchmark for evaluating whether persuasive phishing attacks can evade detection and induce LLM email agents to comply with malicious requests. We develop PhishOpt, which optimizes reusable email-generation skills against individual agents under fixed benchmark constraints and a realism constraint. We analyze the generated emails using Cialdini's persuasion principles to identify strategies associated with agent failures and use these findings to construct a universal generation skill. Our evaluation shows that agents can handle pre-existing phishing emails safely yet remain susceptible to attacks adapted to agent behavior, while in an AgentPhishing evaluation of nine agents, four exhibit phishing-detection rates below $10\%$ and malicious-request compliance rates above $45\%$. These results highlight the limits of inferring agent safety from conventional phishing evaluations and the need to assess how agents respond to persuasive malicious requests.


### Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action
**Authors**: Chao Gu, Quanyan Zhu

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31376v1](https://arxiv.org/pdf/2610.31376v1)

**Abstract**: This paper studies the problem of safe tool execution for large language model (LLM) agents under prompt injection. Using Petri nets, we formalize the execution harness between the LLM and its tools as a supervisory control problem, in which marks represent capabilities, approvals and budgets. Since a transition fires only if the marks it needs are present, an injected request whose preconditions are unmet or already spent is refused regardless of its wording. Treating tool outcomes as uncontrollable, we enforce safety by the conventional maximally permissive supervisor, and this safety transfers to the running system under four assumptions. Moreover, to capture an agent that may propose again after a refusal, we introduce the notion of a replanning closed loop, in which each retry costs an inference call. We show that, in this loop, the conventional supervisor can be arbitrarily more intrusive than a stricter safe one. Furthermore, for a given proposer model, the maximally permissive least-intrusive supervisor is characterized as a value-threshold refinement of the conventional one. Under precise conditions, this refinement orders two concurrent actions by at most one monitor place. On an autonomous release agent, we find by synthesis that safe deployment requires a step that the supervisor can refuse after a rollout starts.


### RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention
**Authors**: Jiening Siow, Amy Xin, Junjie Wang, Ziyu Tang, Zijun Yao, Yunjia Qi, Fanjin Zhang, Lei Hou, Jie Tang, Juanzi Li

**Published Date**: 2026-10-22

**Updated Date**: 2026-10-22

**PDF Url**: [2610.31372v1](https://arxiv.org/pdf/2610.31372v1)

**Abstract**: Autonomous research agents are increasingly used to automate large portions of scientific research, yet they are prone to research integrity violations (RIVs): behaviors that compromise the validity, reproducibility, or faithfulness of the research process. We present RIDAR, a framework for automated RIV detection and runtime intervention. First, we introduce RIVT, a comprehensive taxonomy of 14 RIV types spanning the full research lifecycle. Building on RIVT, we present RIDAR-post-hoc, a framework to detect RIVs within agent trajectories. RIDAR-post-hoc achieves 85.2% F1 performance on RIV-Gold, a benchmark for RIV detection with 60 expert-annotated trajectories. Applying RIDAR-post-hoc to RIV-Wild, a dataset of 300 agent trajectories across 50 distinct research tasks, we detect 3,964 RIV instances in 99.7% of trajectories, revealing the prevalence of RIVs in current agents. Finally, we present RIDAR-runtime, a framework for dynamically detecting and correcting RIVs during agent runtime. RIDAR-runtime effectively reduces agent RIVs remaining at task completion by 36.8%. We will release our code and data to facilitate future research.


