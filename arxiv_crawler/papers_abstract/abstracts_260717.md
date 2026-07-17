# Abstracts of Papers

## World Model
### Hierarchical Denoising For Multi-Step Visual Reasoning
**Authors**: Zezhong Qian, Xiaowei Chi, Chak-Wing Mak, Tianze Zhou, Ruibin Yuan, Yuhan Rui, Hengzhe Sun, Zhuoqun Wu, Yuming Li, Siyuan Qian, Sirui Han, Shanghang Zhang

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15278v1](https://arxiv.org/pdf/2607.15278v1)

**Abstract**: Video models are evolving into vision foundation models, yet they still lack human-like multi-step reasoning. Streaming autoregressive diffusion models are efficient but limited in reasoning, while bidirectional diffusion enables global revision with high inference costs due to dense frame-level denoising. Both paradigms struggle to achieve logical consistency and low-latency streaming for complex reasoning tasks. We propose HDR (Hierarchical Denoising for Visual Reasoning), a unified framework that integrates hierarchical latents into causal video generation for multi-step reasoning. HDR organizes video latents into a tree-structured hierarchy, enabling coarse-to-fine reasoning before streaming output. Coarse denoising layers preserve uncertain hypotheses for global planning, while finer layers progressively refine them into concrete visual states. A sparse hierarchical attention pattern (SHAP) further reduces temporal attention costs. We introduce a level-stratified multi-step video reasoning benchmark with out-of-distribution cases, covering six tasks: maze navigation, Tower of Hanoi, one-line drawing, sliding puzzle, Sokoban, and water pouring. Compared with streaming autoregressive diffusion baselines, HDR improves success from 34.22 to 60.29 (76.2% relative gain) and increases average progress from 76.00 to 89.56, demonstrating more consistent reasoning trajectories. HDR maintains low-latency streaming at 0.70 seconds per latent, achieving 54.2 times faster inference than bidirectional diffusion. It also retains 82.9% of full-data performance with only 2% training data, compared with 52.0% for bidirectional diffusion. Real-world robot experiments further demonstrate HDR's potential for physical interaction and world modeling. Project demo: https://hierarchical-diffusion-reasoning.github.io/.


### RoboTTT: Context Scaling for Robot Policies
**Authors**: Yunfan Jiang, Yevgen Chebotar, Ruijie Zheng, Fengyuan Hu, Yunhao Ge, Jimmy Wu, Tianyuan Dai, Scott Reed, Li Fei-Fei, Yuke Zhu, Linxi "Jim" Fan

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15275v1](https://arxiv.org/pdf/2607.15275v1)

**Abstract**: Recent robot foundation models operate with single-step or short-history visuomotor context. We introduce Test-Time-Training Robot Policies (RoboTTT), a robot model and training recipe that scale visuomotor context to 8K timesteps, three orders of magnitude beyond state-of-the-art policies, without growing inference latency. At this context length, we unlock new robot capabilities: one-shot in-context imitation from human video demonstrations, on-the-fly policy improvement, robustness to perturbations, and stronger performance on multi-stage, long-horizon tasks. We also observe, for the first time, steady gains in closed-loop performance as pretraining context length scales. At its core, RoboTTT integrates Test-Time Training into robot foundation models such as Vision-Language-Action policies, yielding a sequence model whose recurrent state consists of fast weights, parameters updated by gradient descent during both training and inference, compressing histories into weight space and retrieving contextual information for long-context conditioning. To scale training context length, the recipe combines sequence action forcing with truncated backpropagation through time. On challenging real-robot manipulation tasks, RoboTTT improves overall performance by 87% over the single-step context baseline and fully completes a five-minute, ten-stage assembly task, which no baseline ever does. RoboTTT trained with 8K-timestep context outperforms the same model pretrained with 1K timesteps by 62%, suggesting context length as a new scaling axis for robot foundation models. Videos are available at https://research.nvidia.com/labs/gear/robottt/


### MeanFlowNFT: Bringing Forward-Process RL to Average-Velocity Generators
**Authors**: Yushi Huang, Xiangxin Zhou, Jun Zhang, Liefeng Bo, Tianyu Pang

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15273v1](https://arxiv.org/pdf/2607.15273v1)

**Abstract**: MeanFlow generators achieve fast few-step sampling by predicting average velocities over time intervals, making them attractive for efficient generation. Reinforcement learning (RL) has become a powerful way to align diffusion and flow models with human preferences and task-specific objectives. In particular, DiffusionNFT offers an efficient forward-process RL framework that does not require reverse-process trajectories or likelihood estimation. However, applying such RL methods to MeanFlow remains underexplored. DiffusionNFT optimizes instantaneous velocities, whereas MeanFlow samples with average velocities. To bridge this gap, we introduce MeanFlowNFT. Inspired by the MeanFlow identity, which bridges average and instantaneous velocities, we construct an induced instantaneous-velocity predictor. We apply the DiffusionNFT objective to this predictor, making reward optimization well-defined for MeanFlow. Sampling remains based on the average velocity, preserving MeanFlow's fast few-step generation. We further prove that MeanFlowNFT inherits DiffusionNFT's strict policy-improvement guarantee. Experiments on image and video generation show that MeanFlowNFT consistently improves baselines. Moreover, it outperforms prior state-of-the-art RL-tuned few-step generators on most metrics ($6$ of $8$ on SD3.5-M), and can even surpass multi-step RL-tuned diffusion while using only a few sampling steps. For instance, on Wan 2.1, $4$-step MeanFlowNFT reaches a VBench score of $84.33$, surpassing $50$-step LongCat-Video RL ($82.57$).


### Online Neural Space Time Memory for Dynamic Novel View Synthesis
**Authors**: Baback Elmieh, Lynn Tsai, Zeman Li, Srinivas Kaza, Tiancheng Sun, Gabor Csapo, Ali Behrouz, Yuan Deng, Stephen Lombardi, Steven M. Seitz, Xuan Luo

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15271v1](https://arxiv.org/pdf/2607.15271v1)

**Abstract**: Online novel view synthesis from multi-view streaming videos faces a fundamental trade-off: maintaining a persistent, long-horizon memory to reconstruct temporarily occluded regions while operating under strict real-time constraints. While Test-Time Training (TTT) offers a powerful memory mechanism, standard models mandate gradient-based memory updates at every frame to adapt to the changing motion in dynamic scenes. The computational cost of heavy memory updates precludes real-time application and can lead to instability over long contexts. Given that memory updates are more demanding than memory application and video content is largely redundant, we propose to decouple the frequencies of these two processes. Our approach performs periodic memory updates while applying the memory on a per-frame basis, using cross-view attention to manage deformations between the prior memory state and the current frame. To lock in the historical context, we introduce two critical mechanisms: an auxiliary Memory Loss that forces persistent internalization of the scene, and a Memory Caching strategy that regularizes active weights against catastrophic drift. Our method demonstrates real-time, state-of-the-art performance on scenes with dynamic human motion as well as minute-scale online memorization.


### Pretraining Data Can Be Poisoned through Computational Propaganda
**Authors**: Victoria Graf, Hannaneh Hajishirzi, Noah A. Smith, David Kohlbrenner, Kyle Lo

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15267v1](https://arxiv.org/pdf/2607.15267v1)

**Abstract**: Poisoning pretraining data can introduce harmful behaviors to LMs that are difficult to detect and mitigate. Prior work on poisoning pretraining data has largely exploited established data sources such as Wikipedia, which do not represent the large scale and heterogeneity typical of pretraining corpora, and has ignored the interaction between poisoned data and data curation pipelines. We demonstrate that poisoning attacks on pretraining data are feasible beyond this limited setting through an existing web-scale content injection mechanism: public discussion interfaces. Additionally, to measure whether malicious content is included after web crawling and data curation, we introduce HalfLife, a novel analysis for estimating adversarial content inclusion in web-crawl based LM training data. We use HalfLife to explore the feasibility of poisoning pretraining corpora at web scale through open discussion interfaces. Our analysis demonstrates the importance of estimating whether poison injections are included in pretraining data, and establishes third-party webpage content as a possible vector for attacking language model pretraining.


### SceneBind: Binding What and Where Across Vision, Audio and Language
**Authors**: Mingfei Chen, Zijun Cui, Ruoke Zhang, Hyeonggon Ryu, Eli Shlizerman

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15265v1](https://arxiv.org/pdf/2607.15265v1)

**Abstract**: We present SceneBind, an omni-modal representation of realistic scenes with joint semantic and 3D spatial understanding across vision, audio and language. Existing omni-modal encoders excel at instance-level semantics (i.e., what is present), but often lack explicit spatial structure (i.e., where it is). SceneBind addresses this gap by representing each scene as a semantic-spatial entity, combining a global semantic embedding with object-centric semantic-spatial slots. This representation explicitly captures object-level semantics, spatial attributes, and uncertainty. We further propose SceneBind Matching, a semantic-spatial matching scheme that integrates global scene similarity with object alignment, supporting cross-modal scene retrieval and object grounding. To train and evaluate SceneBind, we curate a novel real-world binaural audio-visual dataset with structured semantic and spatial annotations, and propose a training protocol for aligning semantic and spatial signals across modalities. SceneBind is compatible with large-scale pretrained semantic encoders, adds lightweight spatial modeling with only a few additional tokens. It achieves state-of-the-art scene and spatial retrieval while enabling strong zero-shot transfer to downstream tasks such as audio-visual localization.


## Generation
### Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents
**Authors**: Paul Kassianik, Blaine Nelson, Yaron Singer

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15263v1](https://arxiv.org/pdf/2607.15263v1)

**Abstract**: Security-agent evaluations commonly measure peak offensive capability under generous inference budgets, emphasizing vulnerability discovery, exploit development, penetration testing, and CTF completion. Such measurements are useful but incomplete: in operational security, every reasoning step, tool call, telemetry query, and enrichment request consumes budget. We evaluate language-model security agents through this cost-success lens on offensive Cybench challenges and defensive Splunk BOTS v1 investigation challenges. Instead of reporting only best-case success, we compare models at fixed cost levels and decompose performance by inference spend and tool spend. Our results show distinct scalingregimes for red- and blue-team tasks. Offensive CTF performance improves with additional test-time compute, and scaled open-weight models can approach frontier proprietary systems while remaining cost-competitive. Defensive SOC investigation does not scale in the same way: success depends more heavily on disciplined tool use, telemetry navigation, and selective enrichment than on raw reasoning budget alone. We argue that security-agent benchmarks should measure economic efficiency and operational fit alongside task success. Cost-aware, SOC-native evaluations provide a clearer picture of which models are practically useful today and where defensive agents still need to improve. We present an interactive website with our results https://evals.frontier.security.


### teLLMe Why (Ain't Nothing but a Jam): Exploratory Causal Analysis of Urban Driving Data
**Authors**: Qiwei Li, Jorge Ortiz

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15254v1](https://arxiv.org/pdf/2607.15254v1)

**Abstract**: Traffic agencies now have access to large volumes of video-derived data for studying safety and congestion. Most of these data are observational and collected without interventions, which makes causal questions such as "How would rain change traffic density?" difficult to answer. We present teLLMe, a system for exploratory causal analysis of urban driving datasets. The system starts from a structured event table built from dashcam annotations and combines causal structure learning with the PC algorithm, bootstrap-based stability checks, and query-specific effect estimation using linear regression and DoWhy. Natural-language questions are mapped to structured causal queries through a schema-aware LLM, enabling users to specify treatments, outcomes, and subpopulations. teLLMe returns a "Causal Card" that summarizes effect estimates, adjustment sets, DAG support, and assumptions, followed by a short natural-language explanation. Case studies on BDD-derived traffic events show that the system can surface plausible relationships involving weather, peak hours, and traffic density, while making uncertainty and modeling choices explicit. The system is designed as a tool for hypothesis generation and expert reasoning rather than a source of definitive causal claims.


### NeuronSoup: Evolving Asynchronous, Shared-Neuron Temporal Graphs without Backpropagation
**Authors**: Subodh Kalia

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15217v1](https://arxiv.org/pdf/2607.15217v1)

**Abstract**: We present NeuronSoup, a neural computation architecture that replaces synchronous layer-by-layer processing with asynchronous, delay-mediated signal propagation through a pool of shared neurons. Each path in the network routes a continuous-valued signal from one input neuron to one output neuron through a variable number of intermediate hidden neurons. Hidden neurons are physically shared across paths: when two paths pass through the same neuron, the second arrival encounters the accumulated state left by the first, producing constructive or destructive interference that depends on signal polarity and arrival timing. The entire architecture -- topology, weights, delays, and connectivity -- is co-evolved by a genetic algorithm operating on a flat real-valued genome of 14,602 genes. On 10-class MNIST digit classification using frozen ResNet18 features as input, the system evolves a network of 204 active paths through 266 hidden neurons (156 shared across multiple paths, with one neuron participating in 11 distinct paths) and achieves 85.9\% test accuracy after 10,000 generations. The trained model occupies 115 KB. We argue that this architecture addresses fundamental limitations of current deep learning: it requires no differentiable computation graph, adapts its computation depth per-sample, and discovers lateral interactions between processing pathways that current architectures must engineer explicitly. We discuss why genetic algorithms are the correct optimization tool for this problem class, why CMA-ES fails at this scale, and how the architecture generalizes to arbitrary domains by substituting the encoder and output structure.


### Symbal: Detecting Systematic Misalignments in Model-Generated Captions
**Authors**: Maya Varma, Jean-Benoit Delbrouck, Sophie Ostmeier, Akshay Chaudhari, Curtis Langlotz

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15216v1](https://arxiv.org/pdf/2607.15216v1)

**Abstract**: Multimodal large language models (MLLMs) often introduce errors when generating image captions, resulting in misaligned image-text pairs. Our work focuses on a class of captioning errors that we refer to as systematic misalignments, where a recurring error in MLLM-generated captions is closely associated with the presence of a specific visual feature in the paired image. Given a vision-language dataset with MLLM-generated captions, our aim in this work is to detect such errors, a task we refer to as systematic misalignment detection. As our first key contribution, we present Symbal, which utilizes a structured, dual-stage setup with off-the-shelf foundation models to identify systematic misalignments and summarize results in natural language. As our second key contribution, we introduce SymbalBench, a benchmark designed to evaluate automated methods on our proposed task. SymbalBench consists of 1.7 million image-text pairs from two domains (natural and medical images), organized into 420 vision-language datasets with annotated systematic misalignments. Symbal exhibits strong performance on this benchmark, correctly identifying systematic misalignments in 63.8% of datasets, a nearly 4x improvement over the closest baseline. We supplement our evaluations on SymbalBench with real-world evaluations, showing that (1) Symbal can accurately surface systematic misalignments in captions generated by four MLLMs and (2) Symbal is a powerful tool for auditing off-the-shelf image-caption datasets. Ultimately, our novel task, method, and benchmark can aid users with auditing MLLM-generated captions and identifying critical errors, without requiring access to the underlying MLLM. Code is available at https://github.com/Stanford-AIMI/Symbal.


### BadWAM: When World-Action Models Dream Right but Act Wrong
**Authors**: Qi Li, Xingyi Yang, Xinchao Wang

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15207v1](https://arxiv.org/pdf/2607.15207v1)

**Abstract**: World-action models (WAMs) are emerging as a promising foundation for embodied control: rather than predicting actions alone, they learn representations that couple action generation with future world prediction. This coupling is often viewed as a source of robustness, interpretability, and safety, as a robot's action can in principle be checked against its imagined future. In this paper, we show that this assumption is fragile. We introduce BadWAM, a unified framework for modeling and evaluating World-Action Drift Attacks: a new class of WAM-specific adversarial attacks that use small visual perturbations to break the alignment between what a WAM imagines and what it executes. BadWAM characterizes this attack surface along two natural criteria: attack strength and stealthiness. When the adversary prioritizes disruption, BadWAM instantiates an action-only adversarial attack, which directly drives the model toward task-failing actions. When the adversary additionally prioritizes stealth, BadWAM instantiates an imagination-preserving adversarial attack, which seeks to induce harmful action shifts while keeping the model's predicted future close to its clean imagination. Together, these two attacks capture a spectrum of WAM-specific failures: from overt action hijacking to stealthier cases where the model appears to imagine a plausible future but executes a desynchronized action. We evaluate BadWAM across different variants of WAMs. Results show that our attacks substantially reduce task success rates under closed-loop execution. For example, our action-only attack reduces the model performance from 96.5% to 43.1% success. The results of our imagination-preserving attack further exposes a WAM-specific vulnerability: moderate future-preserving regularization can maintain strong attack performance while reducing future imagination drift.


### MM-IssueLoc: A Controlled Benchmark for Evaluating Visual Evidence in Multimodal Repository-Level Issue Localization
**Authors**: Shaoxiong Zhan, Shi Hu, Boyu Feng, Hai Lin, Andrew Gong, Zhengda Zhou, Jiaying Zhou, Yunyun Hou, Hao Su, Hai-Tao Zheng

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15205v1](https://arxiv.org/pdf/2607.15205v1)

**Abstract**: Real repository issues routinely include visual evidence such as screenshots, error dialogs, rendered UI states, and logs, yet repository-level issue localization is evaluated mostly as a text-only task. Existing multimodal SE benchmarks evaluate end-to-end repair, entangling localization with patch synthesis and obscuring whether visual input helped, hurt, or was ignored. We introduce \textbf{MM-IssueLoc}, a controlled benchmark and evaluation protocol for repository-level localization with visual evidence. MM-IssueLoc contains 652 issue-PR instances across 23 languages, with annotations for 7 image categories and 4 relevance levels. It provides file-level and function-level gold labels, paired text-only and with-image evaluation, and VCE-based diagnostics that convert images into structured textual evidence. We evaluate LLM-based and retrieval-based systems, including MM-IssueLoc-VL-Emb as a controlled multimodal retriever. Results show that existing systems remain far from reliable multimodal repository localization: the strongest agent reaches 38.96 file Acc@5 and 22.45 function Acc@10, while the strongest retriever reaches 33.86 function Acc@10. Cross-benchmark comparisons show that high localization scores on text-dominant SWE benchmarks do not transfer cleanly to multimodal issue localization. MM-IssueLoc turns visual evidence into an explicit evaluation variable, enabling future work to test whether systems improve by using visual evidence for localization, rather than by relying on text-only cues or downstream patch-generation effects.


## VLA
### FoMoVLA: Bridging Visual Foresight and Motion Guidance for Vision-Language-Action Models
**Authors**: Wei Li, Peijin Jia, Yuan Ma, Xuefeng Jiang, Titong Jiang, Sheng Sun, Yujian Li, Xin Wen, Han Hong, Zhikang Liu, Bailin Li, Kun Zhan

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.14739v1](https://arxiv.org/pdf/2607.14739v1)

**Abstract**: Vision-Language-Action (VLA) models have achieved impressive results in visuomotor policy learning, yet remain fundamentally reactive, mapping current observations and language to actions without explicit forward prediction of world dynamics. Existing visual foresight methods predict future visual states but lack explicit motion guidance: they show where to go but not how to get there. We argue that future feature prediction and sparse point tracking are naturally complementary: the former provides the goal state, while the latter captures the continuous motion path toward it. We propose FoMoVLA, a framework that augments VLA representations with explicit spatio-temporal supervision by jointly learning future feature foresight and sparse 2D point tracking, enhancing the continuous action policy. FoMoVLA introduces compact foresight tokens to decode future feature states, decodes sparse temporal 2D point trajectories to model compact geometric motion, and couples both through a lightweight future-conditioned cross-attention module that enables consistent reasoning between anticipated states and point dynamics. Extensive experiments on LIBERO, RoboCasa GR-1 Tabletop, and LIBERO-Plus demonstrate state-of-the-art performance and strong zero-shot generalization. Project page is available at https://liauto-research.github.io/FoMoVLA.


### Action QFormer: Structured Representation Shaping under Action Supervision in Vision-Language-Action Models
**Authors**: Yufeng Ji, Wenhao Tang, Haoyi Niu, Koushil Sreenath, Yi Wu, Zhongyu Li

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.14635v1](https://arxiv.org/pdf/2607.14635v1)

**Abstract**: Action supervision in vision-language-action (VLA) models is often treated as a downstream objective for learning action prediction. In this paper, we study it instead as a force that shapes inherited multimodal representations. We show that this shaping has a dual effect: it is necessary for forming action-compatible representations, but when action supervision is applied too directly to the inherited multimodal pathway, it can also destabilize representations that support language-side processing and object grounding. To address this tension, we introduce Action QFormer, a query-based action-facing interface that uses instruction-conditioned queries to reorganize inherited multimodal information into action-facing representations before downstream action generation. In zero-shot sim-to-real navigation, Action QFormer improves average closed-loop task success from 18.8% to 56.3%, raises fixed-instruction action-generation correctness from 22.5% to 75.5%, and nearly eliminates out-of-distribution instruction generations. Further analyses show that Action QFormer changes how action supervision shapes inherited multimodal representations, reducing broad upstream rewriting while preserving targeted and sometimes constructive action-supervised adaptation. These results suggest that improving VLA performance requires not only stronger pretrained backbones, but also better ways of selecting and organizing inherited multimodal information while controlling how it is shaped under action supervision.


### DiMaS: Distribution Matching for Steering Vision-Language-Action Models
**Authors**: Pegah Khayatan, Sara Meziane, Jayneel Parekh, Matthieu Cord

**Published Date**: 2026-07-15

**Updated Date**: 2026-07-15

**PDF Url**: [2607.14280v1](https://arxiv.org/pdf/2607.14280v1)

**Abstract**: Flow-matching-based vision-language-action (VLA) models have emerged as powerful policies for robotic manipulation, yet a critical capability remains underexplored: fine-grained behavioral control, the ability to govern how a robot performs a task by intervening on its internal representations. Representation steering is a well-established interpretability tool for language and vision-language models, where behavioral features are typically encoded as linear directions, but we show that these classic methods fall short in VLAs. We propose DiMaS, a Distribution-Matching Steering strategy tailored to flow-matching VLAs, which transports between representation distributions rather than shifting along a fixed direction, and show that it effectively controls behavior across two state-of-the-art VLAs. We further examine the generalizability of this strategy as the tasks it is learned from and evaluated on grow increasingly dissimilar, characterizing where behavioral control transfers and where it weakens. Finally, through an analysis of the representation structure of the action expert, we explain why classical linear steering falls short in the visuomotor setting: behavioral features are linearly decodable but not linearly steerable, which motivates the distribution-matching design of DiMaS. Our code is publicly available at https://github.com/pegah-kh/dimas, with additional results and videos at https://pegah-kh.github.io/dimas/


### Never Too Late for Force: Accelerating VLA Post-Training with Reactive Force Injection
**Authors**: Yi Wang, Wendi Chen, Zimo Wen, Han Xue, Xueqi Li, Wenye Yu, Zhijie Chen, Hao Yang, Jun Lv, Chuan Wen, Cewu Lu

**Published Date**: 2026-07-15

**Updated Date**: 2026-07-15

**PDF Url**: [2607.14236v1](https://arxiv.org/pdf/2607.14236v1)

**Abstract**: Pretrained vision-language-action (VLA) policies provide strong language-conditioned manipulation knowledge, but they remain largely vision-driven and can struggle once manipulation enters contact states where the scene is occluded, depth is ambiguous, or small force errors push execution off the offline demonstration distribution. We present LIFT (Late Reactive Injection of Force for VLA Post-Training), a force-aware post-training framework that adds contact reactivity to a pretrained VLA policy while preserving its general manipulation knowledge. LIFT grafts a reactive action expert beside the original action expert, initializes it from pretrained action weights, and injects recent 6D end-effector force through causal force memory and zero-initialized cross attention, enabling actions to be refreshed during execution. To address the policy-dependent distribution shift of contact feedback, LIFT further couples reactive force injection with an online DAgger loop that trains on a mixture of offline task-alignment data and human-corrected online rollouts. Across towel folding, book insertion, and Hanoi ring placement, LIFT learns faster and reaches higher performance than vision-only post-training, while ablations show that reactive force memory and online corrective data are both important for robust contact-rich manipulation. Our code and data will be publicly available.


### UESF-Bench: Benchmarking and Probing for Unified Embodied Seeking and Following
**Authors**: Kun Yu, Jianhua Yang, Yixiang Chen, Changwei Wang, Hongyuan Yu, Yan Huang, Fushuo Huo, Ya Jing, Zhumin Chen, Keji He

**Published Date**: 2026-07-15

**Updated Date**: 2026-07-15

**PDF Url**: [2607.13621v1](https://arxiv.org/pdf/2607.13621v1)

**Abstract**: Language-guided human following is an important capability for embodied agents, but existing benchmarks typically assume that the target person is visible at the start of an episode. This setting simplifies the problem and overlooks a more realistic requirement: an agent often needs to first find a language-described target and then persistently follow that target in a dynamic environment. While recent work has started to study human search, existing settings are typically evaluated in task-specific scenarios and often rely on stronger prior knowledge of the environment. Moreover, they usually treat searching and following as separate tasks and still lack a unified benchmark for systematic evaluation. To address these limitations, we introduce the Unified Embodied Seeking and Following Benchmark (UESF-Bench), a large-scale and diverse benchmark for embodied human seeking and following. The benchmark requires agents to handle semantic-guided exploration, reliable behavior switching and recovery, and delayed identity grounding. To this end, we propose SeekFollow-VLA, a vision-language-action framework with a task-driven routing mechanism for latent phase inference and transition modeling between seeking and following. Experimental results show that SeekFollow-VLA achieves clear improvements over both single-head and dual-head baselines across single-person and multi-person environments, establishing a baseline for unified embodied seek-and-follow.


### Semantic Anchoring for Robotic Action Representations
**Authors**: Yuan Xu, Youheng Shi, Chengyang Li, Wentao Zhu, Yizhou Wang

**Published Date**: 2026-07-15

**Updated Date**: 2026-07-15

**PDF Url**: [2607.13597v1](https://arxiv.org/pdf/2607.13597v1)

**Abstract**: Vision-Language-Action (VLA) models inherit rich semantic representations from pretrained Vision-Language Models, yet fine-tuning on limited robot demonstrations degrades this structure and undermines generalization. A fundamental question therefore arises: what constitutes a good action representation? Inspired by the mirror neuron theory's insight that observation and execution share an intention-level encoding, we examine whether a robot's action representations preserve the semantic structure captured by pretrained encoders. Systematic probing confirms that this structure erodes during finetuning, and that its quality synchronizes with both task success and out-of-distribution generalization. We further introduce a plug-and-play method that anchors action representations to a semantic manifold while decomposing representations into a shared semantic channel and a private channel, all discarded at inference, leaving the deployed model unchanged. Validated on different VLA backbones across simulation and real-world benchmarks, our method yields up to +18.7% on real-world in-distribution tasks and +21.5% on out-of-distribution generalization.


## Agent
### SciDiagramEdit: Learning to Edit Scientific Diagrams from Paper Revisions
**Authors**: Yasheng Sun, Zezi Zeng, Yifan Yang, Chong Luo, Wenyi Wang, Ziwei Liu, Jürgen Schmidhuber

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15272v1](https://arxiv.org/pdf/2607.15272v1)

**Abstract**: Editing the figures in a research paper is a routine and time-consuming part of everyday research practice: authors relabel components, rearrange panels, and restyle visuals as they revise their manuscripts. Automating this editing workflow under a natural-language instruction, however, is challenging, because a scientific figure is a dense infographic in which heterogeneous visual elements such as schematics, plots, photos, captions, and arrows are composed under a tight visual grammar to advance a specific argument. To address this, we present SciDiagramEdit, a benchmark and skill-evolution framework that learns from natural paper revisions and operates on the figure's editable vector source, where users can inspect and co-edit individual primitives alongside the agent. Our benchmark mines before/after figure pairs from arXiv version histories, each grounded in the authors' own revision intent. To accommodate the diversity of editing instructions, we adopt agentic learning via skill evolution: an agentic proposer continually refines the agent's skill specification from execution traces over multiple epochs. The resulting skill progressively lifts edit accuracy on a held-out validation set, providing evidence that natural paper revisions are an effective training signal for instruction-driven figure editing.


### SearchOS-V1: Towards Robust Open-Domain Information-Seeking Agent Collaboration
**Authors**: Yuyao Zhang, Junjie Gao, Zhengxian Wu, Jiaming Fan, Jin Zhang, Shihan Ma, Yao Yao, Weiran Qi, Chuyan Jin, Guiyu Ma, Xingzhong Xu, Kai Yang, Ji-Rong Wen, Zhicheng Dou

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15257v1](https://arxiv.org/pdf/2607.15257v1)

**Abstract**: Recent advances in Tool-Integrated Large Language Models have made web search a core capability of information-seeking agents. However, as interaction histories grow, agents increasingly struggle to track task progress. When search attempts fail to yield useful evidence, current single- and multi-agent systems can become trapped in repetitive loops, wasting search budgets and ultimately compromising the quality and completeness of the final output. We introduce SearchOS, a system-level multi-agent framework that turns fragile, implicit search progress into explicit, persistent, and shared state. First, we formulate open-domain information seeking as relational schema completion with grounded citations, where agents discover entities, populate attributes across linked tables, and anchor each value to source evidence. Then we design Search-Oriented Context Management (SOCM), which externalizes the evolving state into Frontier Task, an Evidence Graph, a Coverage Map, and Failure Memory. Built on SOCM, SearchOS applies a pipeline-parallel scheduling mechanism that overlaps the execution of sub-agents and continuously refills freed slots with tasks targeting unresolved coverage gaps to improve utilization and throughput. To schedule and control the execution of search agents, SearchOS introduces a Search Tool Middleware Harness that intercepts model and tool interactions to record grounded evidence and react to stalls or budget exhaustion, and provides a reusable hierarchical skill system comprising strategy and access skills to augment the agents' search process and avoid repeating failed search patterns across runs. On WideSearch and GISA, SearchOS leads all metrics among the evaluated single- and multi-agent baselines, paving the way toward robust information-seeking collaboration.


### AutoSynthesis: An agentic system for automated meta-analysis
**Authors**: Moein Taherinezhad, Sebastian Maier, Gerardo Vitagliano, Francesco Pierri, Stefan Feuerriegel

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15247v1](https://arxiv.org/pdf/2607.15247v1)

**Abstract**: Evidence synthesis is crucial for turning primary research into reliable knowledge for science, medicine, education, and policy. Yet, quantitative evidence synthesis remains largely manual and difficult to scale. Here, we introduce AutoSynthesis, an end-to-end multi-agent system for automated meta-analysis. Given a research question in natural language, AutoSynthesis formulates a search strategy, retrieves scientific literature, screens candidate studies, assesses full-text eligibility, extracts quantitative statistics, computes standardized effect sizes, and finally performs random-effects meta-analysis. AutoSynthesis further supports heterogeneity analysis to examine how effect sizes vary across moderators, as well as risk-of-bias assessment. As output, AutoSynthesis produces a transparent report aligned with PRISMA guidelines. In our application, AutoSynthesis screened over 28 studies and extracted more than 20 quantitative claims. The pooled effect estimates produced by AutoSynthesis are similar to Hedges' $g$ of expert-conducted meta-analyses, indicating close agreement with manual evidence synthesis. Together, these results show that AutoSynthesis can make quantitative evidence synthesis more scalable, thereby supporting evidence-based decision-making across disciplines.


### When Words Are Safe But Actions Kill: Probing Physical Danger Beyond Text Safety in Hidden-State Risk Space
**Authors**: Weimeng Wang, Ziqiang Wang, Zihang Zhan, Chuanpu Fu, Qi Li, Ke Xu

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15218v1](https://arxiv.org/pdf/2607.15218v1)

**Abstract**: Large language models (LLMs) increasingly serve as high-level planners for embodied agents, where linguistically benign instructions can become unsafe once grounded in the physical world. We study whether this physically grounded danger is the same safety problem as ordinary text-level content danger. Through hidden-state direction analysis and random-split null tests, we show that content danger (CD) and physical danger (PD) form separable signals in LLM representations across Qwen2.5-3B/7B/14B/32B, Phi-3.5 and SmolLM2. Building on the CD/PD separability, we propose PRISM, a single-layer L2-regularized logistic probe over full hidden states. PRISM achieves 86.2--87.7\% accuracy on SafeAgentBench with 11.7--13.7\% FPR, while same-scale LLM judges over-block safe tasks at 24.7--39.0\% FPR. We further introduce PhysicalSafetyBench-1K (PSB-1K), a contrastive benchmark of 1{,}000 physical-risk pairs without direct harm keywords, to test whether methods detect physically grounded danger rather than explicit unsafe wording. On PSB-1K, PRISM reaches 99.6\% accuracy and 0.7\% FPR, whereas a Qwen2.5-3B judge rejects 67.8\% of safe tasks. PRISM also replicates on SafeText and EARBench, supporting hidden-state probing as a representation-level method for physical safety beyond text moderation.


### Plover: Steering GUI Agents through Plan-Centric Interaction
**Authors**: Madhumitha Venkatesan, Shicheng Wen, Jiajing Guo, Jorge Piazentin Ono, Liu Ren, Dongyu Liu

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15193v1](https://arxiv.org/pdf/2607.15193v1)

**Abstract**: Graphical user interface (GUI) automation remains challenging in real-world environments, where dynamic layouts, unexpected dialogs, and evolving interface states can cause autonomous agents to drift from user intent. Recent vision-based multimodal agents improve flexibility by operating directly over screenshots and natural language instructions, but planning and adaptation often remain internal, limiting users' ability to inspect, supervise, or correct system behavior. We present Plover, a plan-centric vision-based GUI automation system that externalizes task plans and replanning as persistent, inspectable, and revisable artifacts. Through a planner--executor architecture, Plover supports explicit supervision of evolving execution, localized correction through editable plans, natural-language guidance, and screenshot-grounded interventions, while preserving prior progress during repair. A formative study with six participants informed the interaction design. We then evaluate Plover through benchmark failure-case repair and scenario-based workflow analyses. Our results show that many autonomous GUI-agent failures are structurally repairable when plans remain visible and interventions are localized, and that explicit replanning helps make GUI automation more transparent, controllable, and adaptable.


### Scaling Behavior Foundation Model for Humanoid Robots
**Authors**: Weishuai Zeng, Kangning Yin, Xiaojie Niu, Shunlin Lu, Weixiang Zhong, Jiahe Chen, Feiyu Jia, Xiao Chen, Zirui Wang, Furui Xu, Ming Zhou, Kailin Li, Weinan Zhang, He Wang, Li Yi, Dahua Lin, Jiangmiao Pang, Jingbo Wang

**Published Date**: 2026-07-16

**Updated Date**: 2026-07-16

**PDF Url**: [2607.15163v1](https://arxiv.org/pdf/2607.15163v1)

**Abstract**: Humanoid control requires natural whole-body coordination, precise real-time responses to control signals, and robust generalization across diverse environmental contexts, making it a cornerstone for generalist embodied agents. Behavior Foundation Models (BFMs) have recently emerged as a promising solution to address these challenges by leveraging large-scale behavioral data to achieve superior expressiveness, versatility and generalization. However, despite growing interest in scaling BFMs to further improve their capabilities, it remains unclear how key factors, including the learning paradigm, behavioral data and model architecture should be coordinated to enable effective scaling. In this work, we revisit the scaling recipe for BFMs and demonstrate that substantial performance gains can be achieved through the coordination of three core components: 1) the learning paradigm of motion tracking that reformulates diverse humanoid control problems as the reproduction of integrated whole-body behaviors in the global frame; 2) the strategic synergy between on-policy rollout quantity and reference motion diversity; and 3) the expressive and scalable model architecture termed Humanoid Transformer that facilitates the natural emergence of structured behavioral representations. Through extensive experiments in both simulation and real-world deployment, we demonstrate that our approach yields significant improvements in control fidelity and task generalization, reducing Mean Per-Keypoint Position Error (MPKPE) on the test set by over 10% in local mode and 82% in global mode compared with existing humanoid controllers. These results establish BFM as a principled and effective foundation for scalable and general-purpose humanoid control.


