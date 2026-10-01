# Abstracts of Papers

## World Model
### Ranking-Aware Prompt Optimization for Multimodal Clinical Diagnosis
**Authors**: Tian Xia, Minghao Liu, Yiqing Liang, Laixi Shi, Jiayun Wang

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40361v1](https://arxiv.org/pdf/2609.40361v1)

**Abstract**: Multimodal large language models (MLLMs) are rapidly advancing clinical diagnosis, yet their adaptation pipelines remain anchored to accuracy-based objectives. Clinical data are heavily class-imbalanced: a constant-majority predictor can score above 90% accuracy while being clinically useless. We therefore evaluate and optimize for AUROC, a threshold-free score that ranks positives above negatives and is invariant to class balance. We focus on prompt optimization in MLLMs. Reflective methods such as GEPA use a binary scores matrix with one row per evaluation instance and one column per candidate prompt; cells record per-instance correctness, so the column average is accuracy and drives candidate selection. We introduce pair-level Pareto prompt evolution (Ranking-PE), which replaces each correctness row with a pairwise-ordering row over (positive, negative) instance pairs: the cell is 1 if the candidate scores the positive higher than the paired negative. The column average then equals empirical AUROC (by the Wilcoxon-Mann-Whitney identity). We apply this swap at all three layers the prompt evolution search reads from - the scores matrix that decides Pareto dominance, the per-example feedback to the reflection LM, and final candidate selection - at no extra model calls and with no surrogate loss. Across three diseases on MIMIC, accuracy-based prompt evolution can degrade ranking; Ranking-PE reverses this, beating the accuracy-based recipe by +5.8 AUROC pp on fine-tuned Qwen3-VL-8B and +16.2 pp on MedGemma-4B. Ablations examine each design component and show that a medical-grade visual backbone - via vision-encoder-tuned SFT or medical pretraining - is a prerequisite that prompt search cannot replace - our recipe extends reflective prompt evolution from text-only data to multimodal clinical decision-making.


### Semifactual Credit-Augmented Policy Optimization
**Authors**: Junshu Pan, Zhizhang Fu, Shulin Huang, Yiran Ding, Zifan Cheng, Wenqi Shao, Qiaosheng Zhang, Yue Zhang

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40360v1](https://arxiv.org/pdf/2609.40360v1)

**Abstract**: Reinforcement learning with verifiable rewards (RLVR) has improved the reasoning capabilities of large language models (LLMs), yet their predictions remain sensitive to task-irrelevant prompt features. We investigate this sensitivity through semifactual prompt interventions that preserve the underlying problem and its answer. Our analysis reveals substantial variation in token-level sensitivity and shows that suppressing high-drift token candidates during decoding improves reasoning accuracy without updating model weights. These findings highlight a limitation of Group Relative Policy Optimization (GRPO), which assigns the same outcome-derived advantage to every response token and may reinforce potential spurious dependence alongside useful reasoning. Motivated by this observation, we introduce Semifactual Credit-Augmented Policy Optimization (SCAPO), a causally inspired variant of GRPO that incorporates semifactual stability into token-level credit assignment. SCAPO measures token probability drift for fixed responses under semifactual interventions and uses normalized stability scores to reduce advantages for relatively unstable tokens during early training, while granting no additional credit for stability alone. On Qwen3-4B-Base and Qwen3-1.7B-Base, SCAPO improves AIME 2024-2026 accuracy over GRPO by 5.63 and 4.17 percentage points, respectively. At both model scales, SCAPO achieves the best results on most evaluated mathematics benchmarks and all evaluated out-of-distribution benchmarks among the compared methods. These results suggest that semifactual stability provides an effective training signal for improving reasoning and generalization through finer-grained credit assignment in RLVR. The code is available at https://github.com/DtYXs/SCAPO.


### Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model
**Authors**: Liming Lu, Xianzheng Ma, Wenkun He, Guanqi Zhan, Yilin Zhao, Junyu Chen, Mengyao Xu, Jiaojiao Fan, Wenhang Ge, Yuchao Gu, Yunze Liu, Boyi Li, Zhen Dong, Victor Prisacariu, Ming-Yu Liu, Song Han, Han Cai

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40358v1](https://arxiv.org/pdf/2609.40358v1)

**Abstract**: Video world models are expected to predict how the physical world evolves, yet they often produce visually plausible videos that violate basic physical principles. Existing approaches commonly assume that natural language is insufficient to represent the physical knowledge required for reliable generation, and therefore introduce additional visual, latent, numerical, or planning-based signals. We revisit this assumption and introduce Physis-Lang, a self-evolving framework that treats physical language as a shared and optimizable representation across data curation, model training, and video generation. Physis-Lang represents physical processes through language that describes their relevant entities, causes, interactions, governing principles, temporal evolution, and effects. To improve this representation, we construct PhysCapBench, which decomposes physical processes into atomic assertions and evaluates captions using recall and precision. An agentic loop iteratively analyzes assertion-level errors and refines the instruction used to produce physical captions. Physis-Lang further converts model deficiencies into textual descriptions and uses language-guided retrieval to identify visually diverse videos that cover missing physical processes. Experiments on four widely used physical video benchmarks with Wan and Cosmos backbones demonstrate consistent improvements in physical plausibility. Notably, starting from open-source Cosmos3-Nano backbones, our Physis-Lang-enhanced models surpass the leading proprietary Veo 3.1 model.


### ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing
**Authors**: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40356v1](https://arxiv.org/pdf/2609.40356v1)

**Abstract**: Recent video generation is increasingly realistic and controllable, yet video editing remains less developed, particularly for precise local edits that must preserve the original scene dynamics. Video scene text editing replaces text on scene surfaces, such as storefront signs, whiteboards, and product labels, while preserving the surrounding content, motion, and camera dynamics. Although scene text editing is well studied for images, video scene text editing that achieves high visual quality, temporal consistency, and edit locality remains underexplored. Existing resources offer limited paired real-video data, and general video-editing metrics do not directly measure whether the requested text remains correct over time. We introduce ViTeX-Bench, a benchmark suite comprising ViTeX-Dataset and a three-axis evaluation protocol. The dataset contains 387 real-world 720p videos with text-region masks and editing instructions: 230 provide reviewed, pipeline-generated paired edits for training, and 157 form a frozen evaluation split. The protocol evaluates text correctness, visual and temporal quality, and edit locality through 13 metrics, with one primary metric per axis and a Pareto comparison of their trade-offs. OCR calibration, human evaluation, and annotation-sensitivity analyses support the interpretation of these scores. Across eight baselines from four editing families, accurate text, temporal stability, and scene preservation remain difficult to achieve together. We also release ViTeX-Edit-14B, an open-source reference editor fine-tuned on the paired training split with motion-aligned glyph-video conditioning. It achieves CharAcc 0.688, the highest mean among the evaluated video-native editors, and the lowest comparable text-crop Warp among raw editor outputs. ViTeX-Bench provides a reproducible foundation for studying these trade-offs in video scene text editing.


### Image Classifiers are Efficient Self-Supervised Video Representation Learners
**Authors**: Owais Iqbal, Sudipta Sarkar, Shyam Marjit, Omprakash Chakraborty, Anirban Chakraborty, Abir Das

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40347v1](https://arxiv.org/pdf/2609.40347v1)

**Abstract**: We introduce VideoMSN, a Masked Siamese Network framework for efficient self-supervised spatio-temporal representation learning in videos. Instead of relying on heavy 3D architectures or reconstruction-based autoencoders for learning with unlabeled data, we repurpose standard image Vision Transformers by representing videos as super images which are grids composed of frames sampled from videos. From each super image, we construct two views: one with spatial patch masking and the other with temporal frame masking, ensuring no information leakage across frames. A shared Vision Transformer (ViT) encoder aligns their embeddings using a masked Siamese loss, capturing both motion and appearance cues without reconstruction. Our decoder-free formulation leverages an image foundation model towards efficient video representation learning. Starting from pretrained DINO-v3 and DeiT-v3 image encoders, VideoMSN achieves state-of-the-art performance on Kinetics-400, UCF101, and HMDB51 while requiring up to $32\times$ fewer and $160\times$ fewer video pretraining epochs compared to prior video self-supervised learning methods. Our proposed approach also shows strong performance in low-shot classification, confirming the transferability of the learned representations in a label-scarce scenario. Project Page: https://cvir.github.io/projects/videomsn.


### Ego4WAM: What Matters When Scaling Egocentric Human Data for Robot Learning?
**Authors**: Zhihao Sun, Liu Liu, Xinjiang Wang, Haoyi Jiang, Wei Feng, Huiqiang Zhang, Xiaosong Jia, Zhizhong Su, Zuxuan Wu

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40341v1](https://arxiv.org/pdf/2609.40341v1)

**Abstract**: Egocentric human data provides a scalable source of experience for robot learning, but varies substantially in human-robot alignment, behavioral coverage, and available supervision. Existing work shows favorable scaling with increasing human data, but it remains unclear which data properties drive downstream robot gains and how to use such data throughout the training pipeline. We present a systematic study of egocentric human data with different alignment and supervision under a unified world-action model framework. With the model backbone fixed, we disentangle the effects of human-robot alignment, data duration and task diversity, action supervision, and data usage strategies. We find that aligned human demonstrations substantially improve out-of-distribution generalization and reduce target-task robot data requirements; data duration and task diversity affect downstream capabilities differently; and video-only supervision remains effective without action labels, providing a strong foundation for subsequent video-action training. We validate these findings through closed-loop policy evaluation on both real robots and RoboDojo. Rather than treating data duration as the sole scaling axis, Ego4WAM shows how alignment, task diversity, available supervision, and usage strategy jointly shape the value of egocentric human data for robot learning.


## Generation
### Removing Timing Shortcuts Improves Non-Invasive Brain-to-Text
**Authors**: Dulhan Jayalath, Oiwi Parker Jones

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40359v1](https://arxiv.org/pdf/2609.40359v1)

**Abstract**: We find that major reported improvements in decoding words from non-invasive brain recordings are largely reproducible without any brain data. In the influential work of d'Ascoli et al. (2025), time series of brain activity from subjects perceiving continuous speech are segmented into fixed-length windows starting at each word. A neural network then generates predictions for all of the words in a sentence together. Neighbouring windows partially overlap, implicitly revealing the interval between words. Since these intervals indicate the duration of the words spoken, and different words tend to have different durations - for example, "the" is much shorter than "supercalifragilisticexpialidocious" - the neural network can improve its predictions of words without relying on the underlying brain activity. Consistent with this, the method reaches 22.0% balanced accuracy on synthetic signals containing no brain information, compared with 22.3% on real brain recordings. To prevent the network from learning this shortcut, we make a single, simple change. Instead of jointly encoding all windows in a sentence, we process each independently. As a result, the neural network achieves better performance by learning underlying word-specific information from brain recordings. This makes two existing strategies become much more effective than before. Both aggregating predictions from distinct neural responses to the same word and using a pretrained LLM as a linguistic prior now substantially improve results. On our perceived speech benchmark, this simple recipe (SimpleB2T) achieves a word error rate of 36.6% with five observations per word, approaching past invasive speech decoding performance, albeit under different conditions. The results in this work expose an important shortcut in brain-to-text decoding and show that removing it leads to a simple and considerably more effective strategy.


### Turbo Harness: Instance-Adaptive Harness Optimization
**Authors**: Tunyu Zhang, Hao Wang, Kai Xu, Dimitris N. Metaxas

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40330v1](https://arxiv.org/pdf/2609.40330v1)

**Abstract**: Automating the search for effective harnesses is an important step toward enabling agents to recursively self-improve. Existing harness optimizations typically produce a single global harness that is applied uniformly across task instances. However, a harness that works well on average may not be optimal for every instance. We introduce Turbo Harness, a framework that can adapt a globally optimized harness to each instance by reusing information generated during the original optimization process. Specifically, Turbo Harness recycles artifacts produced during a completed global harness optimization run, and summarizes them into a structured playbook. We train a harness editor to leverage this prior optimization experience to generate instance-specific patches to the global harness. At inference time, the editor uses the instance and the playbook to construct a tailored harness in which the execution model operates. Through numerical experiments, we show that Turbo Harness consistently outperforms existing harness optimization baselines across seven benchmarks spanning interactive agent tasks, software engineering, and long-horizon terminal tasks.


### Cogentic: Multi-Agent Orchestration for Automated Proof Discovery
**Authors**: Yang Cai, Vineet Gupta, Yanchen Jiang, Christopher Liaw, Aranyak Mehta, Grigoris Velegkas, Di Wang

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40324v1](https://arxiv.org/pdf/2609.40324v1)

**Abstract**: We present Cogentic, a multi-agent harness for automated proof discovery on open research problems. While frontier language models can generate strong mathematical ideas in a single shot, single-shot generation is often insufficient for open problems that require exploring multiple competing conjectures, overcoming subtle technical obstructions, and retaining intermediate progress over a long horizon. Cogentic addresses these challenges through an iterative prove--verify loop in which an orchestrator allocates a population of independent provers across distinct proof directions, subjects their output to adversarial verification by several specialized components, and promotes confirmed intermediate results into a persistent verified ledger that later rounds build on. The harness is designed to be able to solve research-level math and theoretical computer science problems. Using Gemini as the base model, Cogentic produced novel results on five open problems across online learning, auction theory, and mechanism design. Each result was independently verified by domain experts and is developed in full in companion papers. We list these results, and new ones as they are verified, at https://sites.google.com/view/cogentic .


### MatLoom: Layered Text-to-Material Generation in a Compact Program Space
**Authors**: Anson Y. Lam, Shuqing Li, Michael R. Lyu

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40322v1](https://arxiv.org/pdf/2609.40322v1)

**Abstract**: Material generation should produce not only an appearance, but also the rules that construct it. We introduce MatLoom, a compact, layer-oriented language for text-to-material generation with pretrained language models. Each program composes alpha-masked layers whose shared spatial expressions define coverage and physically based rendering (PBR) channels, making dependencies between patterns, color, and relief explicit. A standalone interpreter evaluates the program into material maps, while the source retains named fields and layer parameters for subsequent authoring. Without task-specific fine-tuning, our pipeline uses parser-guided repair and preview-based critique to revise material designs, then searches noise seeds while keeping each candidate's remaining source fixed. On a curated benchmark of 141 prompts evaluated with six backbones, our best-performing configuration achieves higher mean scores than three diffusion baselines on all four flat-layout prompt-alignment metrics. Its initial programs already exceed all three baselines on mean BLIPScore, before critique or seed search. Retained programs have a median length of 21 lines when pooled across backbones. In a blind four-way comparison involving 30 participants and 20 prompts, our renders receive 59.2% of choices, compared with 19.3% for the most-preferred baseline. Compact executable programs thus offer a way to generate prompt-aligned materials while retaining their construction as part of the asset.


### Compression Footprints as Security Signals for Model-Poisoning Defense in Federated Learning
**Authors**: Sachi Shome, William Eiers

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40312v1](https://arxiv.org/pdf/2609.40312v1)

**Abstract**: Lossy compression is widely used in Federated Learning (FL) but is generally treated as an error source, while conventional poisoning defenses inspect update geometry. In this work, we instead treat the compressor's response as a security signal: the input-dependent distortion and payload behavior induced by lossy compression can expose differences between honest and attack-generated updates. We introduce the concept of a \emph{compression footprint}: the low-dimensional collection of reconstruction, directional, sparsity, and payload statistics induced by a lossy compressor. We characterize sufficient conditions under which compression footprints separate honest and malicious updates, and operationalize our findings in the CRAFT (\emph{Compression-guided Robust Aggregation via Footprint Trust}) server-side robust aggregation method. Crucially, under a strict honest-majority assumption, CRAFT uses server-verifiable footprints, requires no client-side metadata nor knowledge of the number of malicious clients, and adds no communication beyond the compressed FL pipeline. Moreover, while CRAFT assumes a strict honest majority, it does not require the number of malicious clients to be known in advance. We observe that error-bounded lossy compressor (EBLC) footprints provide stronger separation than Top-K footprints and that footprint trust suppresses malicious influence. We evaluate CRAFT under IID client data with 36\% malicious participation across six standard model-poisoning attacks, three datasets, and six robust aggregation baselines, finding that CRAFT consistently achieves the best accuracy in 7 out of 18 settings and within 1.7 percentage points of the best in the others. Our results show that lossy compression can serve as both a communication mechanism and a security signal for robust aggregation in FL.


### Looped Diffusion Transformer
**Authors**: Yong Xien Chng, Tianyi Chen, Wenwen Tong, Haiwen Diao, Zhongang Cai, Lei Yang, Ziwei Liu, Lewei Lu, Dahua Lin, Gao Huang

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40305v1](https://arxiv.org/pdf/2609.40305v1)

**Abstract**: Improving text-to-image models has traditionally relied on increasing model size or the number of denoising steps. In this work, we explore an alternative way to scale computation by repeatedly running shared Transformer blocks within each denoising step, effectively increasing computational depth while keeping the parameter count fixed. This looped computation enables iterative refinement of internal representations without explicit reasoning tokens. However, naive looping fails to consistently improve image quality. We trace this problem to weak supervision across intermediate loops and unregulated attention updates that progressively erode local information. To overcome these challenges, we propose Looped Diffusion Transformer (Looped-DiT), which combines deep supervision across intermediate loops with self-modulating attention to stabilize looped feature updates. Under matched-parameter and matched-compute settings, Looped-DiT consistently outperforms non-looped baselines. Notably, a 260M-parameter looped model can surpass a model 6.5x larger across multiple text-to-image benchmarks while requiring 4.9x lower inference compute. Beyond this performance gain, we find that looped computation can offer a more effective form of iterative computation for diffusion models, with increasing loop depth yielding larger gains than adding more denoising steps under a fixed inference budget. Furthermore, deeper loops can progressively correct mistakes made in earlier loops, exhibiting behaviors suggestive of latent reasoning. Together, these results show that looped computation offers a promising way to scale visual generation models.


## VLA
### WorldAuditBench: Interactive 3D World Auditing with Multimodal Agents
**Authors**: Ziyan Jiang, Jingbo Yang, Jiabao Ji, Yujian Liu, Qiucheng Wu, Tommi Jaakkola, Yang Zhang, Shiyu Chang

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40325v1](https://arxiv.org/pdf/2609.40325v1)

**Abstract**: As interactive 3D worlds are increasingly used to study intelligent behavior, it becomes important to develop efficient pipelines for identifying anomalies in these simulated environments, such as floating objects, traversable walls, or objects inconsistent with the surrounding scene. Multimodal AI systems, including vision-language models (VLMs) and vision-language-action models (VLAs), have shown potential for automating this task. However, 3D world auditing is complex, requiring the close coupling of two distinct capabilities: action, to navigate the 3D world and search for anomalies systematically and efficiently; and visual reasoning, to understand the environment and identify anomalies from multimodal observations. It remains largely unexplored whether multimodal agents can effectively couple these two capabilities, using visual reasoning to identify potential anomalies while taking actions to validate them. In this paper, we introduce WorldAuditBench, a benchmark for 3D world auditing comprising 213 anomaly tasks across 13 environments built with Unreal Engine 5 and Three.js, spanning five anomaly families. We evaluate five frontier models under a fixed exploration budget using two auditing paradigms: VLA-based exploration followed by VLM-based anomaly identification, and an end-to-end VLM agent in which visual reasoning directly guides action selection. Across the evaluated models and two paradigms, success rates range from 6.6% to 42.3%, substantially below human performance (83.4%). Through the task of world auditing, WorldAuditBench provides a testbed for studying how multimodal agents couple action and visual reasoning in interactive 3D environments, while highlighting current limitations in their ability to gather and interpret evidence during exploration.


### DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents
**Authors**: Haoyuan Deng, Jiebin Liu, Tengxiao Zhang, Langning Yan, Hongye Cao, Ziwei Wang

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40306v1](https://arxiv.org/pdf/2609.40306v1)

**Abstract**: Pretrained robot policies provide useful action priors, but long-horizon manipulation still requires coordination between semantic reasoning and physical execution. Semantic reasoning operates at a coarser timescale than physical interaction, while episode-level failures provide limited guidance on which system component should be revised. We propose DynaHarness, a dynamic physical harness that couples semantic reasoning with physical governance through a shared execution contract and turns failure evidence into validated capability revisions. To be more specific, the slow brain proposes capabilities and symbolic arguments, while the fast brain grounds and monitors commands, refuses unresolved actions, substitutes capabilities, and requests replans when needed. The physical execution contract bounds each accepted command and records execution evidence across analytic skills, recovery skills, and the frozen VLA. Failure attribution localizes faults in these records and directs targeted revisions of reusable capabilities or execution mechanisms. Paired regression checks govern admission or rejection, closing the self-evolution loop. On LIBERO-Pro, DynaHarness achieves 75.2% on 800 newly sampled initial states, compared with 17.5% for the frozen policy. With the same capability library, full dynamic execution reaches 74.0% versus 63.9% under nominal one-step replanning. This demonstrates the value of DynaHarness as a dynamic physical harness that governs how existing capabilities are grounded, monitored, and coordinated during execution. Our project page is at https://denghaoyuan123.github.io/Dynaharness_page/.


### PrefPI: Preference-Guided Steering into Out-of-Distribution Behaviors
**Authors**: Seungeun Rho, Wontaek Kim, Danfei Xu, Sehoon Ha

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40165v1](https://arxiv.org/pdf/2609.40165v1)

**Abstract**: We present PrefPI (Preference-Guided Policy Iteration), an iterative framework for steering pretrained generative robot policies using only relative preferences over self-generated trajectories. Unlike prior preference-learning methods that primarily sharpen modes already represented by the policy, we study steering beyond the initial effective support, where desired behaviors are rarely or never observed under the initial policy. Our key idea is to formulate preference learning as preference-conditioned generative modeling: preferred trajectories define a conditional distribution, whose density ratio with the broader behavior prior provides an implicit preference signal amplified by classifier-free guidance (CFG). Repeating this preference-conditioned modeling and guidance step yields a form of preference-guided policy iteration, turning incremental improvements toward previously inaccessible behaviors. Across diffusion policies and the PI0.5 flow- matching VLA in simulation and the real world, PrefPI produces substantial behavioral shifts with limited feedback. In particular, PrefPI increases object transport height from 10.7 cm to 19.8 cm on real hardware with only 150 preference-labeled trajectories.


### Tactile Curiosity Drives Robot Interaction
**Authors**: Klemens Iten, Alexander Proshkin, Bhavya Sukhija, Stelian Coros, Andreas Krause, Pieter Abbeel, Carmelo Sferrazza

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40134v1](https://arxiv.org/pdf/2609.40134v1)

**Abstract**: Mastering robot manipulation skills via reinforcement learning (RL) remains largely sample-inefficient. The most common RL algorithms rely on random action sampling to discover new strategies, resulting in agents that allocate most of their training budget to motions in free space, away from the contacts from which manipulation skills emerge. Existing intrinsic motivation methods based on model disagreement or epistemic uncertainty improve on isotropic noise, but they can also reward uncertainty in functionally irrelevant transitions, such as erratic motions in free space. In this work, we argue that tactile feedback provides a natural signal for exploration, and introduce TacEx, a framework that incorporates touch into epistemic uncertainty-driven exploration by decomposing model uncertainty across sensory modalities and directing curiosity toward the tactile channel. By anchoring curiosity to the sense of touch, TacEx drives the robot to discover complex contact dynamics, learning to manipulate and grasp objects without task rewards or expert demonstrations during exploration. The interaction-dense dataset collected through this tactile-driven curiosity supports offline learning of downstream pick-and-place policies without additional environment interaction. We further use tactile-driven exploration to post-train vision-language-action (VLA) models. Although the VLAs are initially pre-trained without tactile feedback, post-training with TacEx substantially improves downstream performance while remaining highly sample-efficient.


### When Instructions Retrieve Trajectories: Diagnosing and Mitigating Generalization Failures in VLA Models
**Authors**: Hung-Jen Chen, Yu-Hsun Hou, Yan-Hong Chen, Yan-Fu Chen, Binghua Cai, Min Sun, Chun-Yi Lee

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.39971v1](https://arxiv.org/pdf/2609.39971v1)

**Abstract**: Vision-language-action (VLA) models can exceed 90% success on in-distribution tasks and withstand nuisance changes that preserve the required action, yet fail under counterfactual changes that demand a different action. Aggregate robustness scores can therefore conceal a more specific failure, in which a policy responds to both language and vision yet does not combine them to select the action the task requires. We call this failure instruction-action binding. Instructions cue familiar trajectory families, and visual feedback adjusts their execution. Behavioral analyses of fine-tuned $π_{0.5}$ and GR00T-N1.7 policies reveal that failed rollouts often retain the source behavior or switch to another demonstrated task. These switches show that language is not simply ignored. Readouts and interventions connect these choices to task-conditioned internal states. Our analysis of the imitation objective shows how narrow conditional action support can leave grounded and instruction-keyed solutions indistinguishable on the demonstrations. This motivates Equivariant Counterfactual Training (ECT), which acts at two levels. ECT data supply valid demonstrations in which the same instruction requires different actions in distinguishable scenes, while the ECT loss trains each demonstration with its counterpart in the same update. In a controlled LIBERO-PRO comparison, full ECT raises $π_{0.5}$'s mean position-swap success from 36% to 59%. On CALVIN, where counterparts already occur in the original data, the ECT loss improves five-task completion without new demonstrations. On a real UR5e under a fixed demonstration budget, full ECT raises unseen-position success from 8% to 88%.


### Learning from Runtime Feedback through Failure-Bank Self-Evolution for Vision-Language-Action Models
**Authors**: Mingyue Cui, Zheyuan Liu, Yihan Zhu, Zheyuan Zhang, Meng Jiang

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.39820v1](https://arxiv.org/pdf/2609.39820v1)

**Abstract**: Vision-language-action (VLA) models generalize broadly across robotic manipulation tasks, but complex environments require balancing task success with unintended contact. Runtime shields can correct individual actions, but they leave the underlying policy unchanged, so repeated disagreements may create a persistent policy-shield mismatch that blocks task progress. To address this challenge, we introduce FailBank, a four-stage self-evolving framework that converts runtime feedback into persistent policy improvement. During collection, a fixed CBF-based safety module serves as an observe-only teacher, producing counterfactual corrections while the policy remains in control. Outcome-aware admission then converts useful proposals into corrective targets and retains successful uncorrected actions as quiet anchors for guarded LoRA updates. We evaluate FailBank on the VLA-Arena benchmark across two difficulty levels and two VLA backbones. Compared with the base policies, FailBank improves the joint success-cost operating point. Across the two backbones, FailBank improves task success rate by 8.5 and 6.9 percentage points, while reducing policy-induced cumulative cost by 35.6\% and 23.8\%, respectively. Compared with runtime shielding, FailBank raises task success rate by 25.4 and 9.5 percentage points, while maintaining comparable policy-induced cumulative cost. These results show that runtime feedback can serve as persistent policy supervision rather than only as a temporary action constraint.


## Agent
### How Much of a Harness Does a Strong Agent Need for Autonomous ML Engineering?
**Authors**: Kirill Brilliantov, Alejandro Hernández-Cano, Emmanuel Abbé

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40303v1](https://arxiv.org/pdf/2609.40303v1)

**Abstract**: Recent autonomous machine learning engineering (MLE) agents have made significant progress on public leaderboards. Often motivated by progress stagnation over long-horizon cycles and limited Large Language Model (LLM) primitives, modern MLE agents are deployed on top of increasingly elaborate machinery: multi-agent orchestrators, dedicated retrieval subagents, and more. While such harnesses expand, the use of more primitive but improved coding agents - where LLMs have direct access to the execution environment through read, write, and bash primitives - has received little attention in the field. In this paper we find that, under an equal time budget and the same frontier LLM backbone, open-source state-of-the-art harnesses provide no advantages over a single session of a minimal-harness coding agent baseline, pointing to the backbone as the primary driver for performance. Via a series of large-scale systematic ablation studies, we argue that the machinery layers become redundant in the coding agent setting. We conclude that the effort spent elaborating hand-crafted harnesses around strong models yields poor returns for current MLE benchmarks.


### PivotOPD: Learning to Recover from Pivotal Mistakes in Multi-Turn Agents
**Authors**: Yinghui He, Yapei Chang, Khushi Bhardwaj, Daniele Molinari, Tugrul Konuk, Jan Kautz, Ali Hatamizadeh

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40285v1](https://arxiv.org/pdf/2609.40285v1)

**Abstract**: On-policy distillation (OPD) is a promising approach for training language agents, providing dense teacher supervision on student-generated trajectories. However, in multi-turn interaction, an incorrect action changes the states the student encounters later, so errors compound across turns. In preliminary experiments across three Qwen3 models (8B to 235B), we find that more than half of the failed rollouts contain a pivotal mistake, an action that moves the agent farther from completing the task, and this mistake typically occurs early. These pivotal mistakes often remain recoverable: guiding the model for only a few turns after the pivotal turn can restore task success. We therefore propose PivotOPD, an on-policy distillation framework that jointly trains the student to prevent pivotal mistakes and to recover from the states they create. At each pivotal mistake, a teacher model provides a gold action and then names a recovery action at each of the next few turns. Preventive distillation uses the gold action with reverse KL to steer the student away from the pivotal mistake, while recovery distillation uses the recovery actions with forward KL to transfer recovery behaviors that the student rarely samples. Against 13 baselines on ALFWorld, WebShop, and Search-based QA, PivotOPD achieves the strongest average performance for both Qwen3-1.7B and Qwen3-8B students, improving over the strongest baseline on ALFWorld by +5.5% with the 1.7B student. The gains also transfer to another model family on the software engineering domain, where PivotOPD raises the resolve rate of a Nemotron-3.5 student on SWE-Bench Verified by +3.2%. Project page: https://research.nvidia.com/labs/lpr/pivotopd/


### cua-speedrun: Standardized Benchmarking of the Speed of Computer-Use Agents
**Authors**: Pranjal Aggarwal, Lawrence Keunho Jang, Sean Welleck, Daniel Fried, Ruslan Salakhutdinov, Jing Yu Koh

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40284v1](https://arxiv.org/pdf/2609.40284v1)

**Abstract**: Computer use agents (CUAs), which use graphical user interfaces (GUIs) to complete tasks on a computer, have recently surpassed human performance on many standard benchmarks, including difficult long-horizon tasks. Their capabilities are undoubtedly impressive, however, a key barrier to the widespread adoption and deployment of CUAs remains their speed and cost. Progress towards faster yet capable CUAs requires reliable evaluation of their speed, but many CUA benchmarks currently face a reproducibility crisis. Benchmarks are based on complex infrastructure with varying machine and container configurations that confound the evaluation of the execution speed of CUAs. Towards addressing this gap, we propose cua-speedrun, which introduces standardized infrastructure and task sets, with a focus on evaluating the speed and efficiency of CUAs. cua-speedrun uses a uniform virtual machine setup and execution pipeline, along with a common agent interface that enables single-agent implementations to operate seamlessly across different benchmarks. Across four different CUA benchmarks, we evaluate how reasoning effort, agent harnesses, and environment latency affect performance, speed, and cost. We find no single model family is optimal for all three; none of the open-weight models are on the frontier, and also, unintuitively, for some models increasing the reasoning effort can speed up task completion, while faster environment input-output can slow down overall task completion time. We also demonstrate that we can effectively reduce the evaluation task set of most CUA benchmarks without degrading overall statistical power, allowing for more efficient benchmarking and comparison. We believe cua-speedrun will enable structured progress towards fast, efficient CUAs, unlocking new real-world use cases and applications. All code, infrastructure, and analysis are available at https://cuaspeedrun.com.


### Belief-Aware Multi-Agent Path Finding under Map Uncertainty
**Authors**: Viraj Parimi, Shao-Hung Chan, Han Zhang, Jingkai Chen, Brian Williams

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40269v1](https://arxiv.org/pdf/2609.40269v1)

**Abstract**: Multi-Agent Path Finding (MAPF) aims to find collision-free paths for multiple agents in a shared environment. Classical MAPF assumes that all static obstacles are known in advance, but real-world environments can change unexpectedly due to fallen objects, spills, or other local disturbances. When such changes are spatially correlated, an observation can inform traversability estimates beyond the observed location. Prior approaches address uncertainty in traversability through contingent plans or replanning based on direct observations, but do not leverage this spatial dependence to infer the traversability of nearby unobserved locations. As a result, they cannot use one observation to anticipate nearby unobserved obstacles that may cause costly rerouting later. We focus on Belief-Aware MAPF, where map discrepancies are fixed during execution but initially unknown, and observations can be informative beyond the observed location. We propose Multi-Agent Gaussian belief Inference for Coordination (MAGIC), a framework that updates a shared belief about traversability online based on agents' observations. MAGIC uses a Gaussian Markov Random Field and Gaussian Belief Propagation to approximately infer traversability and construct detour-aware costs for standard MAPF planners. Our experiments on MAPF benchmarks show that MAGIC reduces the executed sum of costs compared to existing approaches on 96.3% of instances, across several planner families and teams of up to 800 agents, demonstrating its applicability to large-scale MAPF problems.


### ComputerSD: Online Self-Distillation from Real-Time Feedback for Computer-Use Agents
**Authors**: Yong Du, Tongbo Chen, Zhengxi Lu, Yizhou Liu, Bofan Chen, Tao Jiang, Wenhao Xu, Yongliang Shen

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40253v1](https://arxiv.org/pdf/2609.40253v1)

**Abstract**: Online training enables computer-use agents (CUAs) to improve through interaction with executable environments. However, existing methods primarily rely on sparse outcome rewards, which provide no supervision for intermediate actions. On-policy self-distillation (OPSD) offers token-level learning signals through privileged rescoring, but directly applying it to CUA online training presents two challenges: fixed guidance may become misaligned with the student's current state, and guidance-induced probability shifts may conflict with step-level correctness. We introduce ComputerSD, an online self-distillation method for CUAs that converts real-time feedback from executed GUI transitions into guidance for policy learning. A fine-tuned GUI analyzer produces guidance and a step-level value score after each action; the guidance provides privileged context, while the score regulates the resulting OPSD signals. ComputerSD jointly optimizes token-level OPSD and trajectory-level GRPO in a fully asynchronous training framework. On OSWorld-Verified, ComputerSD outperforms outcome-only GRPO by 1.9 and 4.1 percentage points on the general-purpose Qwen3-VL-8B-Thinking and specialized EvoCUA-8B backbones, respectively. Evaluation in out-of-distribution settings further supports the generalizability of ComputerSD. These results demonstrate the effectiveness of learning from real-time feedback through online self-distillation for CUAs.


### STARS: From Spatiotemporal Dynamics to Social Representations in Human-Robot Interaction
**Authors**: Nathan Tsoi, Michael J. Munje, Tejas Oberoi, Rishab Maheshwari, Pengen Zheng, Tanush Chauhan, Peter Stone, Joydeep Biswas

**Published Date**: 2026-09-30

**Updated Date**: 2026-09-30

**PDF Url**: [2609.40245v1](https://arxiv.org/pdf/2609.40245v1)

**Abstract**: Robot navigation in dynamic, human-centered environments requires socially-compliant decisions grounded in robust scene understanding. Recent Vision-Language Models (VLMs) exhibit promising capabilities such as object recognition, common-sense reasoning, and contextual understanding, capabilities that align with the nuanced requirements of social robot navigation. However, it remains unclear whether VLMs can accurately understand complex social navigation scenes (e.g., inferring the spatial-temporal relations among agents and human intentions), which is essential for safe and socially compliant robot navigation. While some recent works have explored the use of VLMs in social robot navigation, no existing work systematically evaluates their ability to meet these necessary conditions. In this paper, we introduce the Social Navigation Scene Understanding Benchmark (SocialNav-SUB), a Visual Question Answering (VQA) dataset and benchmark designed to evaluate VLMs for scene understanding in real-world social robot navigation scenarios. SocialNav-SUB provides a unified framework for evaluating VLMs against human and rule-based baselines across VQA tasks requiring spatial, spatiotemporal, and social reasoning in social robot navigation. Through experiments with state-of-the-art VLMs, we find that while the best-performing VLM achieves an encouraging probability of agreeing with human answers, it still underperforms simpler rule-based approach and human consensus baselines, indicating critical gaps in social scene understanding of current VLMs. Our benchmark sets the stage for further research on foundation models for social robot navigation, offering a framework to explore how VLMs can be tailored to meet real-world social robot navigation needs. An overview of this paper along with the code and data can be found at https://larg.github.io/socialnav-sub.


