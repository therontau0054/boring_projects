# Abstracts of Papers

## World Model
### Medical Image Segmentation: Foundation Model Adaptation versus Task-Specific Training
**Authors**: Emre Kutlusan, Yongmin Li

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14519v1](https://arxiv.org/pdf/2611.14519v1)

**Abstract**: Foundation models pretrained on large natural-image collections are increasingly adapted for medical image segmentation, in the expectation that they will replace models trained for each task. Most comparisons, however, use data from the training distribution and a single task-specific baseline whose configuration is rarely justified, and therefore provide limited evidence of performance at new clinical sites. It also remains unclear how much of a foundation model must be adapted, and what determines this. We adapted a foundation model, DINOv2, with strategies ranging from tuning only its bias terms to full fine-tuning, and compared it with U-Nets and ResU-Nets trained from scratch. Experiments covered colonoscopy, breast ultrasound and dermoscopy, with testing on held-out data from the training source and on independent datasets from other institutions. The adapted foundation model generalised better on every external dataset. Within the training distribution, the task-specific models remained competitive when training data were abundant, and delineated boundaries more precisely, while the foundation model more often missed small lesions. Only a small fraction of the foundation model required adaptation, and the capacity needed was determined by the imaging domain rather than by the adaptation method. A widely used polyp test set was also found to duplicate images from another benchmark. Foundation-model adaptation is therefore warranted where models must work across sites, with capacity selected on the target domain.


### Toward Foundation Detection Models via Example-Based Grounding in EM-DETR
**Authors**: Sheethal Bhat, Bogdan Georgescu, Awais Mansoor, Florin C. Ghesu, Sasa Grbic, Andreas Maier

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14518v1](https://arxiv.org/pdf/2611.14518v1)

**Abstract**: DeepLearning (DL)-based Computer-Aided Diagnostic (CAD) systems have shown great promise in supporting clinicians, but their performance heavily depends on the availability of large, well-annotated datasets. In medical lesion detection, the scarcity of comprehensive, stan dardized annotations and the heterogeneity of existing datasets limit the development of robust foundation models. In this work, we introduce a novel approach to building a multi-domain foundation model for le sion detection by integrating diverse medical image datasets annotated for both anatomical structures and abnormalities. We first propose a student-teacher training strategy to effectively combine datasets with heterogeneous label spaces, mitigating catastrophic forgetting, and im proving feature learning. In addition, building on our previously pro posed example-based EM-DETR framework, we adapt it to jointly learn from multiple domain-specific datasets, enabling fine-grained, example driven detection across modalities. Our model achieves state-of-the-art (SOTA) results, with image-level AUC scores exceeding previous SOTA by 1% point on four key findings in CXRs. We achieve a leading mAP50 in CXRs and mammography, surpassing EM-DETR trained on a single dataset by 2-3% points. This approach paves the way for scalable foundation models in medical imaging that leverage heterogeneous data while maintaining robust and generalizable performance.


### TorchCurves: Differentiable Parametric Curves
**Authors**: Alex Shtoff

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14516v1](https://arxiv.org/pdf/2611.14516v1)

**Abstract**: We present TorchCurves, a PyTorch library that treats vector-valued parametric curves as learnable primitives. Its central operation maps batches of scalar inputs to points on curves represented in B-spline or Legendre polynomial bases, with differentiation through both inputs and coefficients. Curve coefficients can be optimized jointly with the surrounding model or produced by another network. The library provides trainable modules, reusable basis modules, and a functional interface, supporting applications ranging from continuous feature embeddings to Kolmogorov-Arnold networks and functional regression. Its implementation combines classical evaluation algorithms with vectorized PyTorch operations, emphasizing readability and maintainability without custom hardware kernels. Timing experiments compare curve evaluation against NumPy and SciPy and KAN training against EfficientKAN across a range of problem sizes. The results illustrate where this generality remains computationally practical and where overhead is substantial. Library is available on GitHub at https://github.com/alexshtf/torchcurves.


### AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models
**Authors**: Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14515v1](https://arxiv.org/pdf/2611.14515v1)

**Abstract**: Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turns a student's training experience into adaptive scaffolds, with minimal domain-specific information and no human intervention during training. A frozen teacher periodically examines this experience, diagnoses bottlenecks, and designs scaffolds in two forms: (i) strategies shared across a class of tasks and (ii) hints for individual hard tasks, adjusting the content and amount of support as the student learns. The scaffolds are removed at evaluation. We apply the same framework to ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation. When evaluated without scaffolds, students trained with AutoScaffold outperform those trained with the corresponding RL baselines in all four domains, with gains of 7.2 points in ALFWorld success and 4.0 points in average QA exact match. On GPU kernel generation, AutoScaffold increases the fraction of tasks with a correct kernel that runs faster than the PyTorch reference by up to 5.0 points. On math, our student surpasses QuestA's reported accuracy using approximately one-third as many student training steps. Analyses show that the teacher identifies a different failure in each task class and shifts its scaffolds from step-by-step workflows to targeted fixes as the student improves, and that its revised scaffolds help the student learn more than keeping the previous scaffold or using no scaffold.


### Pyrite: Building and Benchmarking Protein-Ligand Pose Ranking Agents
**Authors**: Megha Srivastava, Michael H. Lim, Allison M. Keys, Pranav Murugan, Nate Gruver

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14511v1](https://arxiv.org/pdf/2611.14511v1)

**Abstract**: Predicting how a ligand binds to its target is central to small-molecule drug discovery. Modern cofolding models can generate diverse candidate poses, but reliably ranking these candidates remains challenging. We introduce Pyrite, a pairwise pose-ranking benchmark comprising 1,500 pose pairs across diverse protein-ligand complexes. Expert chemists equipped with 3D visualization tools and physics-based scores perform near chance, highlighting the difficulty of interpreting available chemical signals. To investigate automated ranking, we introduce PyriteRep, a structured representation of molecular geometry, protein-ligand interactions, and physicochemical scores, and develop two LLM-based agents: PyriteReasoner, which directly compares poses through text-based reasoning, and PyriteFeaturizer, which generates executable code to construct features for logistic regression, optionally incorporating features derived from LLM subcalls. These agents achieve up to 67% and 74% accuracy, respectively, exceeding observed expert performance. LLM-guided feature discovery generally outperforms direct reasoning, while Group Relative Policy Optimization (GRPO) improves open-weight models, enabling them to match or surpass closed-source frontier models in our evaluations. These results establish Pyrite as a challenging test of pose-ranking ability and highlight LLM-guided feature discovery as a promising approach to interpret and combine the outputs of computational chemistry tools.


### When Does the Real Wiring Win? Testing connectome structure-function claims against unmeasured physiology
**Authors**: Yeyuan Liu

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14508v1](https://arxiv.org/pdf/2611.14508v1)

**Abstract**: Connectome-constrained models are often used to argue that a measured wiring diagram outperforms shuffled or rewired wiring, and hence that structure shapes function. Such comparisons can confound wiring with how the models are tuned: a connectome fixes who connects to whom, not the excitability, gains or plasticity rates the model also needs, and modellers often tune these until the real-wiring model works. We separate three estimands: physiology tuned on the real wiring and transferred to nulls (P1), each wiring tuned on its own (P2), and P2 restricted to physiology consistent with independent data (P3). The biases involved are known in machine learning (under-tuned baselines, inherited weights, winner's curse); we measure what they do to biological conclusions, using synthetic ground truth, placebo nulls and three Drosophila circuit models. Some claims survive every protocol we test: segregated reward and punishment dopamine improves learning, and head-direction topography is required for a persistent bump. Others do not. In the mushroom body, the real Kenyon-cell output wiring beats a cross-subtype identity shuffle by 0.09 under P1 and P2 but loses to it by 0.09 under P3 (95% CIs exclude zero; held-out runs confirm). The verdict is set by the share of alpha'beta' cells among active Kenyon cells, which P1 selects low; at the share implied by imaging (about 44%) the real-wiring model fails to learn, exposing a model inadequacy rather than a deficit of the fly's wiring. In flyvis, P1 penalises a mirrored connectome, which has a constructed solution within 0.07 (median) of the real error, more than a spatially shuffled one in 50 of 50 members; the ranking survives ten-fold longer retraining but depends on the checkpoint at fifty-fold. A credible structural claim needs matched optimisation, data-constrained physiology and a model that still works there.


## Generation
### Continual-ARC: Measuring Skill Acquisition over a Working Lifetime
**Authors**: Daniel Lenton

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14505v1](https://arxiv.org/pdf/2611.14505v1)

**Abstract**: Agent harnesses have emerged as a promising mechanism for continual learning, alongside test-time parametric learning. However, the current benchmarks have several limitations: they generally focus on a single applied domain, serve each instance only once, and assume a single family of learner, so memory-based and weight-based systems are rarely compared on the same scale. We propose Continual-ARC, a lifelong stream built from the three ARC-AGI editions, whose tasks need no domain knowledge. The same tasks return after dormant gaps with fresh instances, while new tasks keep arriving. On each instance, the learner may pay for demonstrations, submit answers, or act inside the harness, with retries permitted on incorrect submissions, which are paid for. Each instance is scored based on the share of this feedback budget consumed. Since a learner may keep anything between instances, memory-based and weight-based systems are scored on the same scale. After the stream, the learner is frozen and tested on fresh instances of the tasks it met, which measures memorization, and on unseen tasks, which measures generalization. We run an agent harness with frozen weights, with and without persistence, on Qwen3.5-9B and GLM-5.3 Flash, comparing them with two prompting floors, a program-induction method and Qwen3.5-9B's weights trained to imitate GLM-5.3 Flash. Persistence in the harness generally does not improve memorization unless provided with explicit expert guidance. Most harness-based methods still learn less than a floor that simply caches each task's demonstrations, across all models we tested. No harness-based method gains on unseen tasks, whereas weight-based learning shows substantial gains. This opens the door to future weight-based continual learning that could teach models to drive harnesses in new domains.


### Emergent Biological Capabilities in a Foundation Model for Molecular Interactions
**Authors**: Adi Mashiach

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14504v1](https://arxiv.org/pdf/2611.14504v1)

**Abstract**: Foundation models trained on large unlabeled corpora develop emergent capabilities, tasks that go beyond the training objective. We extend this paradigm to multimodal biology with Bonbon, a foundation model for molecular interactions trained on approximately 3.2 trillion tokens of paired protein-ligand sequences. From a single representation space, Bonbon exhibits three zero-shot emergent capabilities at hierarchical levels of resolution: functional (mechanism of action), residue (binding site localization, including orthosteric/allosteric discrimination), and bond (covalent versus non-covalent engagement). All three capabilities generalize to out-of-distribution complexes. Bonbon was trained on protein-ligand sequences alone, without any task-specific supervision and without structural coordinates. We conducted controlled scaling experiments across six model scales from 42M to 1.6B parameters; every capability evaluated shows a sharp jump at the largest scale on continuous metrics, even as pretraining loss decreases smoothly. This demonstrates that loss-based scaling laws alone are insufficient to predict when zero-shot emergent capabilities become available. The capabilities reported here emerge after training at a 1:2,000 parameter-to-token ratio to accommodate the sparsity of paired biological interaction data. The same frozen representations achieve state-of-the-art binding and affinity prediction at five orders of magnitude greater speed than co-folding methods. In prospective wet-lab validation across nine disease targets spanning seven protein families, Bonbon achieves a 61.5% dose-response hit rate on de novo compounds, yielding structurally novel molecules not previously reported to inhibit these proteins, including for out-of-distribution targets.


### Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents
**Authors**: Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14493v1](https://arxiv.org/pdf/2611.14493v1)

**Abstract**: Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies evaluation harness stability through repeated measurements, finding that 97% of configurations meet the stability threshold and that stability patterns are agent-independent. Phase 2 measures known risk detection on 72 ground-truth test cases, where the trace-based framework achieves the best precision-recall balance (F1=0.90) while text-only evaluation matches on recall but generates 5x more false alarms. Phase 3 evaluates unknown risk discovery, uncovering 24 novel failures with zero overlap between functional testing and security red-teaming. Our results demonstrate that (1) the information available to the evaluation harness determines evaluation quality, (2) functional and security evaluation are complementary, and (3) LLM-based evaluation harnesses surface subtle errors that human reviewers miss. We recommend a two-framework strategy: trace-based evaluation for functional assessment and adversarial red-teaming for security validation.


### ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows
**Authors**: Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14492v1](https://arxiv.org/pdf/2611.14492v1)

**Abstract**: Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often states why it took an action; the tool calls alone do not. ReTrace extracts the condition behind each step, merges these conditions across runs into a compact rule document, and generates an executable workflow from it. Only this last stage depends on the platform, so rule documents can be compiled for different orchestration platforms. On $79$ procedures from our production platform, ReTrace workflows reach $93.8\%$ completion, against $96.8\%$ for the agent, at $24\%$ lower cost per task. On $τ^2$-Bench, they reach $75.8\%$ task success (agent: $80.6\%$) and run in $1.3$s instead of $170$s; three rounds of repair on training failures lift $k{=}2$ workflows from $66.7\%$ to $81.2\%$. On eight SOP-Bench procedures, ReTrace without repair trails few-shot generation ($80.6\%$ vs. $83.6\%$), but repair from labeled training failures lifts it to $87.8\%$ at $0.40$s per task, compared to $85.5\%$ in $46.6$s for the agent.


### TimeSeek: Multi-Task and Multi-Domain Pretraining for Generalized Time Series Analytics
**Authors**: Peng Chen, Yihang Wang, Zhongwen Rao, Yang Shu, Yuying Qiu, Yuxuan Chen, Lujia Pan, Bin Yang, Chenjuan Guo

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14491v1](https://arxiv.org/pdf/2611.14491v1)

**Abstract**: Time series analytics has been widely applied across various domains. While existing time series foundation models (TSFMs) have demonstrated promising results, they still face two major challenges: 1) Most TSFMs mainly rely on stacking Transformer layers to increase parameter size, lacking the ability to adaptively model complex time series patterns from multi-domain data. 2) Current TSFMs are primarily pre-trained for specific tasks, e.g., forecasting or anomaly detection, and a few models support multiple tasks, but they fail to fully leverage task specificity and commonality, resulting in suboptimal performance. To address these challenges, we propose TimeSeek, a novel generalized time series analytics model that adaptively models time series patterns from multi-domain data and unifies multiple tasks in pre-training. Conceptually, TimeSeek is guided by selective information sharing under domain and task heterogeneity. From the perspective of multi-domain data, we propose a Multi-Domain Feature Extractor that adaptively captures temporal dependencies and channel correlations based on domain-specific characteristics, including progressive multi-scale modeling and adaptive slot channel modeling. From the perspective of the diversity of tasks, we propose multi-task collaborative training, which leverages task specificity and task commonality through task customization and cross-task training, effectively unifying multiple tasks in pre-training and better adapting to diverse downstream scenarios. After pre-training on large-scale time series data, TimeSeek achieves state-of-the-art performance in forecasting, anomaly detection, and classification tasks across both few-shot learning and zero-shot situations, together with favorable inference efficiency.


### Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game
**Authors**: Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi, Kuan-Hao Huang

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14487v1](https://arxiv.org/pdf/2611.14487v1)

**Abstract**: Research ideation is iterative: researchers refine their ideas step by step based on feedback. Yet existing evaluations obscure this search process, making it difficult to understand how LLMs explore the space of research ideas and what limits their progress. We introduce Re-Search, which adapts the format of Twenty Questions to research ideation: given only the research problem of a published paper, a model must rediscover the paper's core idea by asking yes-or-no questions. Built from 200 ICML 2026 papers, Re-Search tracks how a model's idea evolves as it asks questions and receives binary oracle feedback, isolating ideation from execution. Across six recent LLMs, nearly all progress happens within the first 30 of 100 questions, which largely decide how the game ends; after that, most models plateau. Through controlled interventions on the candidate questions and the hypothesis space, we find that the bottleneck is generation, not judgment: models recognize a good idea or a good question when one is offered, but often cannot produce it on their own. We further analyze the ideation traces and find that models fail by either over-exploiting one direction or over-exploring too many. These findings point to concrete design principles for autoresearch systems: since models can judge candidates they cannot produce, enriching the search with externally sourced ideas and questions may be more effective than improving any single model's generation ability.


## VLA
### One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge
**Authors**: Ilia Larchenko, Gleb Zarin, Atindra Nair, Keerti Manney, Vitaly Kleban, Mirko Kiefer, Anjana Yodaiken

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14432v1](https://arxiv.org/pdf/2611.14432v1)

**Abstract**: We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion from 2025 was that the model was undertrained, so most of the 2026 work went into training the model for longer, optimizing some training parameters, making each training step slightly faster and reducing the gradient noise: a migration from 50 to 100 tasks (semantic stages built from the demonstrations' skill annotations, task and stage embeddings of new tasks warm-started from similar old ones, and a 21-dimensional action space matching the teleoperation controls); variance-reduced multi-sample flow matching with a simple noise-vs-compute model that picks the number of action-expert samples per observation without ablations; and a 200k-step training run, about one pass over the 211M frames of the demonstrations. A cloud evaluation infrastructure keeps a shared record with provenance, episode diagnostics and restorable simulator states, and runs six simulators on one GPU together faster than real time. On top of the learned policy, 14 tasks are routed to a GPT-6 Astra coding agent that controls the robot through observation and motion tools, starting every episode from a frozen copy of its own practice session on training instances. Across these 14 tasks, Astra's mean Q is 0.639, against 0.108 for the learned policy. The public submission included only part of the Astra results and scored 0.446 Q with 27.3% full-task success.


### How Much of Your VLA Is kNN
**Authors**: Denis Grachev, Damien LaRocque, Omar Moured

**Published Date**: 2026-11-09

**Updated Date**: 2026-11-09

**PDF Url**: [2611.13160v1](https://arxiv.org/pdf/2611.13160v1)

**Abstract**: Vision-language-action (VLA) models now exceed 95% success on the LIBERO simulation benchmark, yet it remains unclear how much of this performance requires generalization beyond the training demonstrations. In this work, we show that retrieving nearby demonstrations and reusing their action chunks achieves a success rate of 91.7 % on LIBERO without policy training. Under LIBERO-Plus perturbations, retrieval shows the smallest drop of all evaluated policies. Across nine publicly available VLAs, fine-tuning mostly makes the vision-language backbone a better retrieval key, and the actions of the VLAs remain close to the demonstrations. In addition, we introduce Local Action Consistency (LAC), an offline metric that measures whether nearby observations in representation space are also associated with similar future actions. We show that LAC tracks the success rate of retrieval and can guide the training of a retrieval key. Our evaluation and source code are available at https://github.com/sereact/lerobot_knn.


### VLA Adaptation with Real and Simulated Data: A Case Study on Robotic Chess
**Authors**: Matěj Kripner, Milan Straka

**Published Date**: 2026-11-09

**Updated Date**: 2026-11-09

**PDF Url**: [2611.12676v1](https://arxiv.org/pdf/2611.12676v1)

**Abstract**: Vision-language-action (VLA) models are trained as general-purpose foundation models for robot learning, and require fine-tuning for each downstream task and robot. This raises practical questions such as how much data and training updates are needed, how checkpoints should be selected, and whether simulation can be leveraged to alleviate the cost of real data collection. We study these questions on a task that requires both precise manipulation and spatial understanding of the scene. In this task, an SO-101 arm moves a chess king between two squares that are given only by their names, such as e4 and a5. We fine-tune $π_{0.5}$ with various dataset sizes and update budgets, using teleoperated demonstrations as well as simulated demonstrations from a randomized scripted expert that imitates the variability of human demonstrations. In simulation, the success rate scales with both data and updates. Importantly, we find that a short learning-rate cool-down adds up to 31 points and is necessary for comparing checkpoints, and that validation loss and action error are unreliable for model selection. On the real arm, we fine-tune on up to 256 teleoperated demonstrations and evaluate ten policies in 25 trials each. Partial results indicate that pretraining on the simulated demonstrations helps substantially, most clearly when real data is scarce. We also present a negative result, in which training on the policy's own rollouts with filtered behavior cloning, RECAP-style advantage conditioning, corrections from an automatic coach, or residual reinforcement learning did not yield a measurable improvement over plain behavior cloning in our setting. We release the simulator, the expert and the real demonstrations.


### Be My Eye: Learning to See Beyond a Robot's Own Perspective
**Authors**: Baifu Huang, Shilin Fang, Jianan Wang

**Published Date**: 2026-11-09

**Updated Date**: 2026-11-09

**PDF Url**: [2611.12295v1](https://arxiv.org/pdf/2611.12295v1)

**Abstract**: Robots operating in the real world are inherently subject to partial observability, particularly in multi-robot collaboration, where individual observations may be insufficient for effective task execution. A key challenge is leveraging complementary observations from partner robots to support collaborative decision-making. We argue that information sharing should go beyond passively transmitting raw observations or generic visual features. Instead, robots should selectively encode task-relevant information according to task objectives and execution progress. To this end, we propose a task-oriented active context sharing framework that transforms robot observations into compact representations, preserving critical information under constrained communication budgets. The framework adopts a two-stage training paradigm. In the first stage, onboard observations and task instructions are jointly encoded into compact context representations. Task-oriented future prediction and soft task-progress correspondence learning guide this collaboration-agnostic compression, preserving information about task objectives and execution progress. In the second stage, the learned representations are integrated into a pretrained Vision-Language-Action (VLA) policy, enabling bidirectional context exchange. Each robot combines complementary partner information with local observations to guide action generation. Action supervision jointly refines the context representations and policy, aligning information sharing with collaborative decision-making. Controlled experiments demonstrate substantial performance gains under constrained communication budgets, while three real-world experiments validate the framework in complex dual-robot tasks. These results highlight a shift from passive visual transmission toward active, task-oriented context sharing that directly supports collaborative decision-making.


### APS-VLA: Action-Guided and Future-Aware Token Pruning for Efficient Vision-Language-Action Models
**Authors**: Xiaoyang Xing, Chun-Mei Feng, Anthony Cohn, Xiaoliang Gong, Asoke Nandi

**Published Date**: 2026-11-09

**Updated Date**: 2026-11-09

**PDF Url**: [2611.13030v1](https://arxiv.org/pdf/2611.13030v1)

**Abstract**: Vision-language-action (VLA) policies have demonstrated strong generalization in robotic manipulation, yet processing dense visual tokens often incurs high inference latency. Visual token pruning offers a practical way to reduce this cost, but identifying a compact set of tokens that preserves reliable action generation remains challenging. Existing methods largely rely on static or immediate heuristic cues to estimate token importance. We introduce APS-VLA, a framework that learns visual token selection from robot demonstrations while keeping the pretrained VLA backbone frozen. A lightweight Decision Influence Estimator scores tokens conditioned on current visual observations, language instructions, and robot proprioception. Its training combines two complementary signals: action supervision matches both the full-input policy predictions and demonstrated actions, while an auxiliary visual transition objective uses demonstrated actions to predict subsequent visual features from the selected representation. At deployment, the estimator performs a single hard selection and packing step before the policy's native action-generation procedure; the auxiliary predictor is removed. Experiments with OpenVLA-OFT on LIBERO and with $π_{0.5}$ and XR-1 on RoboCasa365 demonstrate inference acceleration with modest changes in task success. Across five real-world tasks on two dual-arm platforms, APS-VLA reduces mean policy inference latency from 137.25 to 93.25 ms, achieving a $1.47\times$ speedup with an average success rate of 61%, compared with 60% for the unpruned baseline. Together, these results support APS-VLA as a modular, plug-in framework for efficient robotic control across VLA architectures, preserving the underlying policy parameters and native action-generation procedure.


### Thermo-VLA: A Thermal-Aware Vision-Language-Action Model with Gated Residual Modulation for Robotic Manipulation
**Authors**: Jingxuan Chen, Junshi Luo, Chencheng Dong, Xiaojian Nie, Tongge Huang, Qiang Huang

**Published Date**: 2026-11-09

**Updated Date**: 2026-11-09

**PDF Url**: [2611.11981v1](https://arxiv.org/pdf/2611.11981v1)

**Abstract**: Recent Vision-Language-Action (VLA) models have begun incorporating thermal sensing, but existing approaches typically treat thermal images as ordinary visual inputs, providing limited support for temperature-aware relational reasoning in manipulation. To address this limitation, we propose Thermo-VLA with a ThermoRes Encoder, which decomposes thermal images into cold and hot attribute representations and injects them into the RGB token through language-conditioned residual modulation, enabling temperature-driven target selection and continuous manipulation. We further construct six real-world robotic tasks on a dual-arm Unitree G1 platform, spanning basic grounding to relational reasoning. Experiments show that Thermo-VLA achieves an average success rate of 0.86 across four thermal-dependent tasks, outperforming a pi_0.5 baseline that directly incorporates RGB-thermal observations by 18 percentage points. Under unseen-object and scene variations, Thermo-VLA maintains an average success rate of 0.78, achieving the best generalisation performance among the compared methods. Beyond thermal sensing, we transfer the same residual modulation mechanism to colour attributes and observe consistent improvements in both simulation and real-robot experiments, indicating its potential to generalise beyond thermal attributes. Project website: https://j-x-chen.github.io/Thermo-VLA-web/


## Agent
### Contrastive Discovery: Open-Ended Scientific Discovery over Competing Explanations
**Authors**: Ziang Liu, James J. Kim, Yijia Dai, Jennifer J. Sun

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14514v1](https://arxiv.org/pdf/2611.14514v1)

**Abstract**: LLM agents are increasingly used for open-ended, data-driven scientific discovery, yet most of them evaluate hypotheses pointwise, testing an empirical claim $h$ only against its complement $\neg h$. When evidence rejects $h$, the agent learns that one explanation is unlikely but not which alternative the evidence supports. To recover that alternative, we introduce Contrastive Discovery, which replaces the single hypothesis with a contrast set, a scientific question paired with mutually exclusive and collectively exhaustive competing explanations. Each experiment is scored by how its evidence redistributes belief across the set, and the question is resolved when belief concentrates on one explanation. Because contrast sets change only the unit an agent proposes and scores, an existing agent can use them to re-evaluate evidence it has already collected or to guide its search. Across six domains, $89\%$ of the pointwise candidates with the largest belief shifts are rejections. On the same evidence, contrast sets resolve $73\%$ of these candidates to a specific alternative. When contrast sets guide search, the agent resolves $67\%$ more questions than pointwise surprisal under the same experiment budget. In a blinded study, $38$ human experts chose the same explanation on $78\%$ of resolved questions and on $82\%$ of questions where the pointwise agent rejected its hypothesis and stopped. Together, these results support explicit competing explanations as a way for discovery agents to resolve more scientific questions from the same evidence and validation budget.


### Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning
**Authors**: Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14419v1](https://arxiv.org/pdf/2611.14419v1)

**Abstract**: Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting model faithfully represents the intended decision problem. We introduce a benchmark of 44 scenarios spanning game, situational, and cultural settings and evaluate generated world models along three dimensions: mechanical validity, reference-relative structural agreement, and semantic criteria. Across three empirical tracks, we analyze 410 first-pass generations. In the reference-backed game track, 134/135 generated world models pass a strict mechanical audit, yet mean permutation-invariant structural F1 is only 0.366, with just 28/134 mechanically valid models exactly matching the authored reference. In the cultural track, explicitly naming the country changes the generated structural representation for most LLMs while producing only small changes in automated semantic scores. These results show that executability is a necessary but insufficient criterion for LLM-generated world models: models that are mechanically valid can still differ substantially in the structure used by downstream neuro-symbolic reasoning and planning.


### EngineAgent: Agentizing On-Device LLM Inference Engines with Inference Stack Hierarchy Awareness and Hardware Abilities
**Authors**: Zhengxiang Huang, Yujie Sun, Shengheng Chen, Zhaode Wang, Chaoyue Niu, Zeyu Zhao, Chengfei Lv, Fan Wu, Guihai Chen

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14356v1](https://arxiv.org/pdf/2611.14356v1)

**Abstract**: Rapidly evolving LLM architectures and heterogeneous mobile hardware make supporting new models in on-device inference engines a recurring and costly system challenge. Each model may require coordinated changes across conversion, graph construction, operators, and hardware backends. Existing coding agents often miss these cross-layer dependencies and struggle to diagnose failures across host--device execution paths. We present EngineAgent, an agentic system for automating on-device LLM model enablement. Its key insight is to separate reusable engine and hardware knowledge from model-specific implementation. Before enablement, EngineAgent constructs a hierarchy-aware engine index that captures engine abstraction layers and cross-layer dependencies, and pre-validates backend-specific build, execution, and debugging workflows using already supported models. For each new model, a builder uses this knowledge to coordinate cross-layer changes, while an auditor checks implementation completeness and drives iterative debugging through device-side validation. Across 12 tasks spanning three mobile LLMs and four engine--backend pairs on CPUs, GPUs, and NPUs, EngineAgent achieves 75% end-to-end success with either of two underlying LLMs, versus 33.3% for the strongest coding-agent baseline. Success requires compilation, on-device execution, and output-logit agreement with reference implementations. EngineAgent also reduces average per-task time and model-API cost relative to baselines using the same underlying LLMs.


### When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents
**Authors**: Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, Zecheng Sheng, Liwei Hou

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14326v1](https://arxiv.org/pdf/2611.14326v1)

**Abstract**: LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that represents each candidate lesson as a structured hypothesis with an explicit precondition, behavior change, expected effect, and verifier. FGSE applies the hypothesis only in a temporary state, tests it on target-transfer, falsification, and archived-regression probes, and then commits, refines, or rejects it according to measured gain and risk. Across web, app, tool-use, and long-term memory benchmarks, FGSE achieves strong task performance, including 39.8 WebArena success rate, 78.8 AppWorld average completion, and 0.724/0.487 Pass$^1$ on $τ$-Retail/$τ$-Airline, while reducing falsification failures to 5.0%, regression damage to 1.3%, and harmful committed updates to 3.6%. These results suggest that testing memory updates as hypotheses supports more reliable long-term adaptation.


### Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents
**Authors**: Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14320v1](https://arxiv.org/pdf/2611.14320v1)

**Abstract**: External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled only with task success or failure, yet are typically provided without the trajectories they came from, leaving the agent no way to check them. To address this, we introduce WikiTrace, an evidence-linked memory system designed to let agents check each lesson against its original trajectory. Specifically, motivated by the finding that a trajectory often still holds the evidence needed to catch an erroneous lesson, WikiTrace stores each lesson as a concise insight linked to a summary of why its trajectory succeeded or failed and to the raw trajectory itself. Then, on a new task, the agent starts from all insights and, whenever one lacks details needed to act, conflicts with another, or comes from a failed task, descends through its links with terminal tools to fill in missing details or correct the insight before acting. We validate WikiTrace on five agentic benchmarks, showing that it consistently outperforms existing memory approaches and a baseline given the same insights alone, while also reducing memory-induced degradation. Our code is available at https://github.com/yukyeongleee/wikitrace


### MMDM: Measuring Massive Multitask Decision Making
**Authors**: Junhao Shen, Qing Zong, Yue Guo, Zhanqiu Zhang, Yiwen Guo, Hong Cheng

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14309v1](https://arxiv.org/pdf/2611.14309v1)

**Abstract**: System-1 Decision Models directly make structured probabilistic decisions over query-specified options given a state in a single forward pass, without autoregressively generating reasoning trajectories or textual responses. Recent evaluations cover diverse tasks but often rely on existing benchmarks, where prior exposure to test material can obscure generalization. Moreover, real-world decision making often involves long contexts, large option spaces, and complex logical dependencies, challenges that existing benchmarks do not adequately capture together. Thus, we introduce MMDM (Massive Multitask Decision Making), a benchmark of 5,448 high-quality questions across 16 task categories, combining newly constructed tasks with source-grounded recompositions and rewrites for single-select, multi-select, and soft-label decision making in fresh contexts. It covers realistic scenarios such as agent state tracking, tool and skill selection, preference judgments, and rubric scoring, with option spaces ranging from 2 to 1,024 and inputs extending to 64,817 tokens. With MMDM, we conduct a comprehensive quantitative evaluation of 28 decision models, showing that many perform well on common knowledge yet struggle with interdependent options, constrained decisions, and multi-select tasks. For example, Perplexity Decider-V1.2 reaches 78.75% Hard Single-select Accuracy on world knowledge, but only 53.95% on option logic and 47.95% on constraint planning, while the best Hard Multi-select Accuracy across all models is 36.81%. These results highlight joint reasoning, constraint-aware selection, and complete multi-select recovery as key priorities for decision model development, with MMDM providing a testbed for measuring this progress.


