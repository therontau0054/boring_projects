# Abstracts of Papers

## World Model
### Lumos-Nexus: Efficient Frequency Bridging with Homogeneous Latent Space for Video Unified Models
**Authors**: Jiazheng Xing, Hangjie Yuan, Lingling Cai, Xinyu Liu, Yujie Wei, Fei Du, Hai Ci, Tao Feng, Jiasheng Tang, Weihua Chen, Fan Wang, Yong Liu

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31603v1](https://arxiv.org/pdf/2605.31603v1)

**Abstract**: Connector-based video unified models have demonstrated strong capability in instruction-grounded video synthesis, but integrating a large high-fidelity generator into the unified training loop is computationally prohibitive, limiting achievable visual quality. We therefore propose Lumos-Nexus, a training-efficient unified video generation framework that facilitates the development of strong reasoning-driven generation capabilities while significantly enhancing visual fidelity. Lumos-Nexus adopts a two-stage design: 1) During training, only a lightweight generator is aligned with the understanding block to learn to take in reasoning-driven semantic control. 2) During inference, we introduce Unified Progressive Frequency Bridging (UPFB) to progressively hand off generation to a high-capacity pretrained generator in the shared latent space, enabling coarse-to-fine refinement and producing high-fidelity videos without compromising reasoning quality. To fill the gap in reasoning-driven video generation benchmarks, we introduce VR-Bench, which assesses a model's capability to translate inferred intent into coherent and semantically aligned video content. Extensive experiments demonstrate that Lumos-Nexus achieves substantial gains in visual realism and temporal coherence on VBench, while exhibiting strong reasoning-based generative performance on VR-Bench. Code and models are available at https://jiazheng-xing.github.io/nexus-lumos-home/.


### KLIP: localized distribution shift detection via KL-divergence with diffusion priors in Inverse Problems
**Authors**: Alireza Kheirandish, Jihoon Hong, Sara Fridovich-Keil

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31596v1](https://arxiv.org/pdf/2605.31596v1)

**Abstract**: Diffusion models have shown promising performance as data-driven priors for computational imaging, as well as some capacity to detect out-of-distribution (OOD) images. However, existing approaches to OOD detection often require some knowledge of the shifted distribution, fail to detect subtle or localized distribution shifts, and operate on full images, rather than the indirect measurements available in inverse problems. We propose an OOD detection metric based on the Kullback-Leibler divergence between the diffusion prior and the posterior distribution, that (i) does not require any calibration data or knowledge of the shifted distribution, and (ii) can detect whole images as OOD as well as localize OOD patches within an image. Experimentally, we show that this metric can detect subtle yet semantically meaningful distribution shifts, such as the shift from healthy liver CT scans to those with tumors, and generalizes across different types of diffusion models, datasets, and inverse problems. Our code can be found at https://github.com/voilalab/KLIP.


### Stateful Online Monitoring Catches Distributed Agent Attacks
**Authors**: Davis Brown, Samarth Bhargav, Arav Santhanam, Kasper Hong, Ivan Zhang, Matan Shtepel, Steffi Chern, Alexander Robey, Eric Wong, Hamed Hassani

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31593v1](https://arxiv.org/pdf/2605.31593v1)

**Abstract**: Language models can find thousands of severe software vulnerabilities, and agents are increasingly being misused for cyberattacks. To avoid detection, attackers frequently distribute their misuse, splitting a harmful task across many user accounts so each individual transcript looks benign. Because safety monitors score only one agent context at a time, they are structurally blind to misuse that is only visible in aggregate, across many accounts. We show this gap is real by building, to our knowledge, the first distributed agent attack, a multi-agent scaffold that completes hard cybersecurity tasks while hiding the harmful objective across subagents with limited contexts, evading a standard monitor that catches it only a fifth as often as prior agent attacks. Towards a defense, we develop an online stateful monitor that uses real-time clustering to collect weak suspiciousness signals across many agent transcripts, and escalates only rarely to a language model that flags misuse across user accounts. In evaluations with large-scale simulated datacenter traffic, our monitor Pareto dominates standard monitors, catching distributed attacks 30% earlier and flagging cyber misuse before it reaches the most harmful stages. Crucially, this comes at negligible additional latency for ~99% of user traffic. This detection advantage persists but narrows as the benign background traffic grows very large. After an extensive red-teaming exercise, we improve the defense and surprisingly also find that it catches standard jailbreaks, since adaptive attackers reuse attack variants across accounts. Our results point toward a new class of safety monitors which reason over groups of users rather than isolated transcripts.


### CoFiDA-M: Concept-Aware Feature Modulation for Cross-Domain Adaptation with Image-Only Inference
**Authors**: Nurjahan Sultana, Moi Hoon Yap, Xinqi Fan, Wenqi Lu

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31591v1](https://arxiv.org/pdf/2605.31591v1)

**Abstract**: Models for AI-based skin cancer screening suffer a severe performance drop when shifting from expert dermoscopic (source) images to consumer-grade clinical (target) images, hindering real-world deployment. Existing domain adaptation methods often ignore crucial semantic invariants, such as clinical concepts. While new foundation models like MONET can provide this semantic information as dense, probabilistic scores, this metadata is unavailable at test time, creating a deployment paradox for practical image-only screening tools. We address this gap by proposing CoFiDA-M, a privileged information framework that learns from concepts at training time but deploys as an image-only model. Our method trains a teacher network that uses MONET concept probabilities to guide a FiLM modulator, transforming visual features into a semantically ``edited" feature space. A lightweight, image-only student is then trained to reproduce this edited representation, not just the teacher's final predictions. This distillation ``bakes" the clinical reasoning into the student's weights. On a challenging multi-dataset benchmark, our image-only student significantly outperforms state-of-the-art approaches, especially in melanoma recall. Our work provides a practical and generalizable framework for leveraging noisy, probabilistic metadata as privileged information, demonstrating strong cross-dataset robustness and potential for real-world deployment beyond dermatology. Implementation code is available at: https://github.com/mmu-dermatology-research/CoFiDA.git


### Language Models Learn Constructional Semantics, Not To Mention Syntax: Investigating LM Understanding of Paired-Focus Constructions
**Authors**: Wesley Scivetti, Ethan Wilcox, Nathan Schneider, Kanishka Misra, Leonie Weissweiler

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31586v1](https://arxiv.org/pdf/2605.31586v1)

**Abstract**: Grasping the semantics of rare constructions (form-meaning pairings) has been shown to be a challenging problem that has currently only been solved by the largest LLMs. It remains an open question if open-source models have robust constructional understanding, and if so, what learning dynamics underlie the acquisition of this knowledge. Focusing on a set of rare Paired-Focus constructions in English (e.g. "let alone", "much less"), we construct a novel dataset to test their meanings using both scalar adjectival semantics and general world knowledge. Testing a wide range of models differing in parameter count, architecture, and pretraining dataset size, we find that several modestly sized models are sensitive to both the forms and the meanings of Paired-Focus constructions, though models trained on human-scale data fail at all meaning evaluations. Turning to training dynamics for a set of open-checkpoint models, we find that Paired-Focus understanding emerges later in training than Paired-Focus syntactic knowledge, and that learning of Paired-Focus semantics is correlated with gains in some domains of world knowledge. Overall, our empirical results support the conclusion that modestly sized open-source models can grasp the rare Paired-Focus constructions, and demonstrate a connection between knowledge of Paired-Focus constructions and other meaning domains.


### LongTraceRL: Learning Long-Context Reasoning from Search Agent Trajectories with Rubric Rewards
**Authors**: Nianyi Lin, Jiajie Zhang, Lei Hou, Juanzi Li

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31584v1](https://arxiv.org/pdf/2605.31584v1)

**Abstract**: Long-context reasoning remains a central challenge for large language models, which often fail to locate and integrate key information in extensive distracting content. Reinforcement learning with verifiable rewards (RLVR) has shown promise for this task, yet existing methods are limited by low-confusability distractors and sparse, outcome-only reward signals that cannot supervise intermediate reasoning steps. To address these issues, we introduce \textsc{LongTraceRL}. For data construction, we generate multi-hop questions via knowledge graph random walks and leverage search agent trajectories to build \emph{tiered distractors}: documents the agent read but did not cite (high confusability) and documents that appeared in search results but were never opened (low confusability), producing training contexts that are far more challenging than those built by random sampling or one-shot search. For reward design, we propose a \emph{rubric reward} that uses the gold entities along each reasoning chain as fine-grained, entity-level process supervision. This rubric reward is applied only to responses with correct final answers (positive-only strategy), distinguishing the reasoning quality among correct responses and preventing reward hacking. Experiments on three reasoning LLMs (4B--30B) across five long-context benchmarks demonstrate that \textsc{LongTraceRL} consistently outperforms strong baselines and encourages comprehensive, evidence-grounded reasoning. Codes, datasets and models are available at \href{https://github.com/THU-KEG/LongTraceRL}{https://github.com/THU-KEG/LongTraceRL}.


## Generation
### TunerDiT: Training-free Progressive Steering of Diffusion Transformer for Multi-Event Video Generation
**Authors**: Ruotong Liao, Guowen Huang, Qing Cheng, Guangyao Zhai, Lei Zhang, Xun Xiao, Thomas Seidl, Daniel Cremers, Volker Tresp

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31590v1](https://arxiv.org/pdf/2605.31590v1)

**Abstract**: Text-to-video (T2V) generation faces challenging questions when generating videos with long horizons containing multiple events. Inspired by the intrinsics of the diffusion process, we probe video diffusion transformers (DiTs) and uncover intrinsic turning points in the DiT denoising trajectory where conditioning text affects generation from global layout to fine-grained details. Building on this finding, we present TunerDiT, a simple yet effective progressive steering method that requires no additional training for multi-event generation. TunerDiT comprises two steering handles: (1) Event-Partitioned Masking that enforces event boundaries while allowing cross-event transition bands; (2) Cross-Event Prompt Fusion that injects neighboring event semantics for late-stage refinement. We contribute a self-curated prompt suite for benchmarking multi-event generation, i.e., Meve. TunerDiT achieves state-of-the-art performance across 8 metrics and offers a tunable trade-off between video consistency and event separation, compared with other training-free methods. The improvement in text alignment increases with the event count, indicating a scaling possibility with increasing event count.


### Giving Sensors a Voice: Multimodal JEPA for Semantic Time-Series Embeddings
**Authors**: Utsav Dutta, Gerardo Pastrana, Sina Khoshfetrat Pakazad, Henrik Ohlsson

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31580v1](https://arxiv.org/pdf/2605.31580v1)

**Abstract**: Transformer-based architectures have advanced sequence modeling in language and vision, yet general-purpose representation learning for heterogeneous multivariate time series remains underexplored. We introduce CHARM (Channel-Aware Representation Model), which incorporates channel-level textual descriptions into a Transformer encoder equivariant to channel order. CHARM is trained with a Joint Embedding Predictive Architecture (JEPA) and a novel loss promoting informative, temporally stable embeddings; latent-space prediction encourages robustness to sensor noise while description-aware gating provides interpretability through learned inter-channel relationships. Across anomaly detection, classification, and short- and long-term forecasting, the learned embeddings achieve strong performance using only a linear probe. Performance is driven primarily by the JEPA objective and conditioning architecture, with text descriptions serving as channel identifiers for cross-dataset generalization.


### SPECTRA: Synthetic IR Test Collections with Relevance Oracles and Controlled Distractor Diagnostics
**Authors**: Eric Liang

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31575v1](https://arxiv.org/pdf/2605.31575v1)

**Abstract**: Scalable information retrieval testing needs corpora that are large enough to stress index construction, ranking latency, query routing, and evaluation tooling, yet human-judged test collections remain expensive and may be unavailable when documents are private or still under design. This paper introduces SPECTRA, a reproducible framework for generating synthetic text corpora and retrieval test collections through a separation of latent topical structure, surface text realization, metadata controls, query intent generation, and deterministic relevance oracles. The framework is intended as a diagnostic complement to Cranfield-style and TREC-style evaluation, not as a replacement for human assessment. A single-process Python prototype generated corpora up to 60,000 documents and 9.61 million tokens while preserving controllable long-tail vocabulary growth and producing graded relevance labels for 96 queries. In the local simulation study, generation remained close to linear at roughly 12K to 14K documents per second, estimated Zipf slopes stayed near 0.86 in absolute value, and increasing cross-topic distractor text reduced BM25 nDCG@10 from 1.00 at 2% distractors to 0.43 at 36% distractors. These results show that lightweight synthetic corpora can expose retrieval-system scaling and failure modes before costly collection construction begins.


### What Gets Unmasked First? Trajectory Analysis of Diffusion Models for Graph-to-Text Generation
**Authors**: Qing Wang, Jacob Devasier, Chengkai Li

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31564v1](https://arxiv.org/pdf/2605.31564v1)

**Abstract**: We present the first systematic study of masked diffusion language models (MDLMs) for graph-to-text generation. We analyze MDLM generation trajectories -- the order in which tokens are unmasked during iterative decoding -- and find that, unlike autoregressive LLMs which generate text linearly, MDLMs naturally prioritize entities first, followed by relational and function words, with structural tokens resolved last. We further identify a previously undocumented failure mode of supervised fine-tuning: SFT disrupts this strategy by prematurely anchoring structural sentence-ending tokens early in the decoding trajectory, effectively fixing the output length which can lead to omitted or hallucinated information. To address this, we propose lambda-scaled structural decoding, a training-free inference-time modification that downweights structural token confidence and recovers +9.4 BLEU-4. Finally, we introduce Graph-LLaDA, which integrates a Graph Transformer encoder into LLaDA's decoding process to explicitly incorporate relational graph structure. Cross-dataset evaluation on LAGRANGE reveals that previous baselines overfit to dataset-specific patterns, while LLM- and MDLM-based approaches generalize significantly better.


### Positional versus Symbolic Attention Heads: Learning Dynamics, RoPE Geometry, and Length Generalization
**Authors**: Felipe Urrutia, Juan José Alegría, Cinthia Sanchez Macias, Jorge Salas, Cristian B. Calderon, Cristobal Rojas

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31558v1](https://arxiv.org/pdf/2605.31558v1)

**Abstract**: Transformer-based language models are widespread in today's society. As such, understanding the mechanisms by which they solve structured tasks and predicting how they may behave in novel scenarios is of great importance for safe deployment. We study the learning dynamics of attention heads in a controlled setting by training a decoder-only Transformer (GPT-J) on two structurally equivalent multi-hop reasoning tasks: a number task requiring positional reasoning and a letter task requiring symbolic reasoning. Using a recently introduced metric that classifies attention-head behavior as positional or symbolic for a given prompt, we show that successful learning is associated with the emergence of pure heads, i.e., heads that express themselves as either positional or symbolic. Despite the tasks' structural equivalence, they impose different mechanistic demands: the number task requires both positional and symbolic heads, whereas the letter task requires only symbolic heads. We then identify the computational roles of these heads, characterize the basic functions they implement, and give theoretical constructions showing how single-layer RoPE-based attention can realize these functions through geometrically interpretable query, key, and value operations. This analysis yields a quantitative separation between positional and symbolic mechanisms in their robustness to longer sequences, formalized through a novel notion of discrepancy. We empirically validate the resulting predictions in both controlled and real-world models, showing that symbolic mechanisms extrapolate more reliably to longer sequences while positional mechanisms face sharper limitations.


### Vision-Language Models Suppress Female Representations Under Ambiguous Input
**Authors**: Arnau Marin-Llobet, Simon Henniger, Mahzarin R. Banaji

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31556v1](https://arxiv.org/pdf/2605.31556v1)

**Abstract**: Alignment teaches vision-language models (VLMs) to avoid expressing demographic biases, and when gender is clearly visible they largely succeed. Far less is known about ambiguous inputs (a worker in full gear, a figure seen from behind) cases common in practice yet rarely studied. We find that minimal prompting pressure exposes occupation-gender defaults when prompting ambiguous input images, with models collapsing to male even for strongly female-stereotyped occupations. But do these outputs reflect what models actually encode internally? We introduce LALS (Latent Association Leaning Score), a zero-shot metric that projects visual-token activations into the model's text-embedding space to measure concept associations per token and layer. Across 15 occupations, over 800 gender-ambiguous images, and four VLMs, internal representations and outputs are systematically decoupled: models often encode a female association internally yet output male. Layer-wise analysis reveals an asymmetric filter -- male signal amplifies end-to-end while female signal peaks mid-network and is suppressed before generation -- and a color ablation shows that culturally loaded visual cues such as clothing color further modulate these internal associations.


## VLA
### DeMaVLA: A Vision-Language-Action Foundation Model for Generalizable Deformable Manipulation
**Authors**: Taiyi Su, Jian Zhu, Tianjian Wang, Youzhang He, Zitai Huang, Jianjun Zhang, Chong Ma, Hanyang Wang, Tianjiao Zhang, Munan Yin, Weihao Ding, Yi Xu

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31286v1](https://arxiv.org/pdf/2605.31286v1)

**Abstract**: Real-world household robots require Vision-Language-Action (VLA) foundation models that can acquire reusable manipulation skills across diverse objects, task conditions, and household environments. Deformable-object folding is a representative challenge, requiring robots to handle clothing items from random initial states across varying categories, geometries, materials, and scenes. However, existing VLA systems commonly train separate policies for different object categories, while naively mixed multi-task training often suffers from task interference and degraded performance. To move beyond category-specific folding policies, we introduce DeMaVLA, a VLA foundation model for generalizable Deformable Manipulation. DeMaVLA adopts a VLM backbone with an action expert and formulates continuous action generation using flow matching. To improve efficiency, the action expert is constructed by pruning every other transformer layer while preserving layer-wise alignment with the VLM backbone, reducing training and inference cost. DeMaVLA is first pre-trained on approximately 5,000 hours of selected real-world dual-arm demonstrations to acquire general manipulation priors. It is then post-trained on mixed folding data that aggregates self-collected demonstrations and corrective trajectories from real-robot failures across multiple folding tasks through a human-in-the-loop Data Aggregation~(DAgger) pipeline. Experiments show that DeMaVLA achieves competitive performance on RoboTwin and strong real-world results on our household folding benchmark. These results highlight the value of scalable real-world data, efficient action generation, and corrective learning for general-purpose VLA policies in deformable-object manipulation.


### Does Visual Information Play a Decisive Role in Vision-Language-Action Model Driving Behavior?
**Authors**: Jingtao He, Hongliang Lu, Xiaoyun Qiu, Yixuan Wang, Xinhu Zheng

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31041v1](https://arxiv.org/pdf/2605.31041v1)

**Abstract**: Vision-Language-Action (VLA) models have demonstrated promising capability in autonomous driving, highlighting the potential of unified multimodal architectures for jointly modeling perception and planning. However, how current VLA-based driving behavior is grounded in visual information remains poorly understood. Existing evaluation protocols mainly focus on aggregate performance metrics, lacking structured and practical diagnostics to quantify visual-behavior dependency. In this work, we introduce a structured multi-level visual perturbation framework to analyze visual-behavior dependency in VLA-based driving models systematically. The framework organizes controlled visual perturbations along three complementary dimensions: channellevel degradation, information-level disruption, and structurelevel modification. We apply it to VLA-based driving systems and evaluate behavioral responses under both open-loop trajectory prediction and interactive closed-loop safety evaluation. Experimental results reveal evaluation-dependent dependency patterns and uneven visual grounding across abstraction levels. These findings call for more structured analyses and principled design of VLA driving models to better understand how visual information shapes behavior and develop safer, more robust systems.


### Hide-and-Seek in Trajectories: Discovering Failure Signals for VLA Runtime Monitoring
**Authors**: Seongheon Park, Wendi Li, Changdae Oh, Samuel Yeh, Zsolt Kira, Michael Hagenow, Sharon Li

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.30834v1](https://arxiv.org/pdf/2605.30834v1)

**Abstract**: Vision-Language-Action (VLA) models enable robots to follow natural language instructions and generalize across diverse tasks, but they remain vulnerable to execution failures that compromise reliability in real-world deployment. Detecting such failures during execution is therefore critical for the robust deployment of embodied systems. Existing failure detection methods either rely on expensive action resampling or external models, while alternatives propagate trajectory-level labels uniformly across every timestep, obscuring localized failure signals. In this paper, we propose \textbf{Hide-and-Seek}, a framework that formulates VLA failure detection as a coarsely supervised learning problem. By combining inter-trajectory and intra-trajectory contrastive objectives, Hide-and-Seek localizes failure-indicative actions and induces temporally structured failure signals from trajectory-level supervision alone, without any step-level annotation. We evaluate Hide-and-Seek on LIBERO, VLABench, and a real-world robotic platform across three representative VLA policies: OpenVLA, $π_0$, and $π_{0.5}$.Our method achieves state-of-the-art multi-task failure detection performance with a practical accuracy--timeliness trade-off under conformal prediction, and generalizes well to both seen and unseen tasks.


### BOKBO (Best of K Bad Options): Calibrated Abstention for VLA Policies
**Authors**: Anya Singh, Cabrel Happi, Jai Relan, Varun Nair, Vidyut Baradwaj

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30660v1](https://arxiv.org/pdf/2605.30660v1)

**Abstract**: Test-time scaling for vision-language-action (VLA) policies, methods such as RoboMonkey, SEAL, MG-Select, and V-GPS, samples K candidate action chunks at inference and executes the verifier-best. When all K candidates are unsafe, the system executes a violating action with no warning. We propose BOKBO, the first conformal abstention layer for K-sample VLA inference, providing finite-sample distribution-free guarantees on executed-violation rate. We provide both global and per-task (Mondrian) variants, with the per-task variant closing the conditional gap on the hardest tasks.
  Our analysis exposes a structural failure of policy-internal nonconformity scores under perturbation-based K-sampling: the base-policy confidence proxy and K-sample disagreement correlate at 0.98 with the action-noise hyperparameter $σ$, while correlating at the noise floor with actual safety violations. We test the failure's scope by replicating the analysis under token-level temperature sampling and find the failure is mechanism-specific and partially mitigated under policy-stochasticity-based sampling. A learned violation predictor conditioned on semantic visual features and task identity supports tight calibration: at $ε$ = 0.05 on libero_object_temp_x0.1 with OpenVLA-OFT, the conditional CRC bound holds on 86% of bootstrap splits with 78% coverage and 70% net task success. Mondrian-BOKBO raises the minimum per-task conditional hold fraction from 0.71 to 0.93. Results are stable across 5 training seeds, replicate within bootstrap noise on $π_0$-FAST, hold on libero_spatial_temp_x0.1 as a co-equal benchmark, and survive four within-suite distribution shifts. We additionally identify and correct a methodological pitfall: globally-set force thresholds well below expert-typical manipulation forces conflate unsafe behavior with normal manipulation, inflating violation rates by $5\times$.


## Agent
### A Tight Theory of Error Feedback Algorithms in Distributed Optimization
**Authors**: Daniel Berg Thomsen, Adrien Taylor, Aymeric Dieuleveut

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31594v1](https://arxiv.org/pdf/2605.31594v1)

**Abstract**: Communication costs are a major bottleneck in distributed learning and first-order optimization. A common approach to alleviate this issue is to compress the gradient information exchanged between agents. However, such compression typically degrades the convergence guarantees of gradient-based methods. Error feedback mechanisms provide a simple and computationally cheap remedy for this issue, but numerous variants have been proposed, and their relative performance remains poorly understood. This paper provides tight convergence analyses for two of the main error-feedback algorithms from the literature, the classic Error Feedback method (EF) and Error Feedback 21 (EF21), by identifying optimal step-size choices and constructing optimal Lyapunov functions tailored to each method. The results hold independently of the number of agents and recover the known best guarantees possible in the single-agent regime.


### Choosing the Lens: Strategic Perspective Activation in Context-Dependent Argumentation
**Authors**: Albert Sadowski, Jarosław A. Chudziak

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31581v1](https://arxiv.org/pdf/2605.31581v1)

**Abstract**: The same arguments often need to be evaluated under different external regimes. An agent with influence over the regime has a strategic lever that standard formalisms do not directly capture. We introduce context-dependent argumentation frameworks (CDAFs), an extension of Dung's theory in which a defeat function determines, per context, which attacks succeed. A perspective-labeled specialisation derives the defeat function from a relevance set $ρ$ and a priority $π$. The relevance set is the agent's action space. In a small worked example, the agent's target argument is rejected under every full-relevance injective priority, yet accepted under partial activations, one of which no VAF audience can mirror. We define the corresponding decision problem, ACTIVATION-MANIPULATION, and record baseline complexity bounds. Tight bounds and multi-agent variants are left open.


### If LLMs Have Human-Like Attributes, Then So Does Age of Empires II
**Authors**: Adrian de Wynter

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31514v1](https://arxiv.org/pdf/2605.31514v1)

**Abstract**: Much research has been carried out on large language models (LLMs) and LLM-powered agentic workflows. However, many works within the field state emergence of, ascribe to, or assume, generalised anthropomorphic attributes to them (e.g., morality or understanding of natural language). Our goal is not to argue in favour or against the existence of these attributes, but to point out that these conclusions could be incorrect. For this we build and train a simple neural network on the videogame Age of Empires II, and note that any entity in a sufficiently-powerful substrate, such as LEGO or the Greater Boston Area, could also present such attributes. Hence, the purported anthropomorphic attributes of LLMs are empirically non-unique: although some properties (e.g., responses to prompts) could remain constant, others, such as the interpretation of their perceived behaviour, might change with the substrate. Thus, any empirically-grounded discussion requires explicit measurement criteria; otherwise the interpretation is left to the representation. We then show that assuming that these attributes exist or not in a system, independent of the substrate and in a generalised way, leads to either circular or uninformative conclusions, regardless of the experimenter's viewpoint on the subject. Finally we propose a 'null' assumption, where one assumes LLM non-uniqueness instead of assuming anthropomorphic attributes to set up an experiment, along with examples of it. We also discuss potential objections to our work, briefly survey the field, and prove that \textit{Age of Empires II} is functionally- and Turing-complete.


### Skill Reuse as Compression in Agentic RL
**Authors**: Zhikun Xu, Yu Feng, Jacob Dineen, Taiwei Shi, Jieyu Zhao, Ben Zhou

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31509v1](https://arxiv.org/pdf/2605.31509v1)

**Abstract**: Large language model agents trained with reinforcement learning (RL) often learn brittle, task-specific shortcuts. We hypothesize that agents generalize better when their successful trajectories are structurally compressible, decomposed into a small set of reusable abstract patterns. To formalize this, we introduce ReuseRL, which grounds agentic RL in the Minimum Description Length (MDL) principle. ReuseRL extracts a shared skill dictionary from successful trajectories and augments the RL objective with a segmentation cost, explicitly penalizing idiosyncratic behaviors that encode poorly. We prove a PAC-Bayes generalization bound for this compression penalty. Across ALFWorld, TextWorld-Cooking, and Countdown-Stepwise, ReuseRL improves in- and out-of-distribution success over vanilla GRPO and strong round-length baselines.


### AutoSci: A Memory-Centric Agentic System for the Full Scientific Research Lifecycle
**Authors**: Weitong Qian, Beicheng Xu, Zhongao Xie, Bowen Fan, Guozheng Tang, Jiale Chen, Xinzhe Wu, Mingtian Yang, Chenyang Di, Jiajun Li, Lingching Tung, Peichao Lai, Yifei Xia, Ziyi Guo, Yanwei Xu, Yanzhao Qin, Shaoduo Gan, Xupeng Miao, Bin Cui

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31468v1](https://arxiv.org/pdf/2605.31468v1)

**Abstract**: Scientific research has traditionally been human-intensive, requiring researchers to coordinate literature, ideas, experiments, manuscripts, and review responses across long project cycles. The rise of LLM-based scientific agents creates an opportunity to automate this process. Such a system must support the full research lifecycle, maintain structured persistent memory across projects, and improve its own research procedures over time. However, existing systems either partially satisfy or fail to satisfy these requirements, leaving a gap for a unified automated scientific research system. As a result, we present AutoSci, a memory-centric agentic system for the full scientific research lifecycle. AutoSci is organized around four modules. SciMem provides schema-governed research memory, separating Long-Term Knowledge Memory for reusable scientific knowledge from Active Research Memory for project-level artifacts such as ideas, experiments, manuscripts, and reviews. SciFlow executes a five-stage lifecycle from literature understanding to rebuttal through a harness that controls state, context, verification, feedback, and orchestration. SciDAG augments difficult skills with DAG-shaped multi-agent operators and reusable stage-specific templates. SciEvolve converts feedback signals from users, experiments, reviews, and external environments into versioned updates to SciMem organization, SciFlow skills, and SciDAG templates. Together, these modules make AutoSci a persistent research environment that can execute, remember, and evolve across research projects. The code repository is available at https://github.com/skyllwt/AutoSci.


### GPU Forecasters: Language Models as Selective Surrogates for Kernel Runtime Optimization
**Authors**: Zaid Khan, Justin Chih-Yao Chen, Jaemin Cho, Elias Stengel-Eskin, Mohit Bansal

**Published Date**: 2026-05-29

**Updated Date**: 2026-05-29

**PDF Url**: [2605.31464v1](https://arxiv.org/pdf/2605.31464v1)

**Abstract**: GPU kernels are the workhorse of modern deep learning, and optimizing them (via evolutionary search or coding agents) usually requires repeated measurement on target hardware. While these measurements provide the ground-truth signal necessary for kernel search, they are costly, because each evaluation of a kernel requires compilation and repeated execution on a GPU. As improvements in LLM inference reduce the cost of writing novel kernels and LLM-driven searches scale to large search budgets, on-device evaluation becomes a bottleneck. To address this, we study how LLMs can serve as selective GPU surrogates for kernel evaluation, by forecasting the performance of proposed kernels. A useful surrogate should be accurate, and it should be selective, by knowing when it could be wrong, and deferring to the GPU. To evaluate surrogates, we measure whether their forecasts are accurate, calibrated, and practically useful for recovering fast kernels under limited GPU-measurement budgets. Next, we study whether reinforcement learning can improve forecast accuracy and confidence calibration. Our experiments demonstrate that LLMs can accurately forecast relative kernel performance, that their utility can be improved through reinforcement learning. Used inside a kernel search, the surrogate lets the search consider several times as many candidates under the same GPU evaluation budget, and that leads to finding faster kernels than an equal-budget baseline. These results suggest that LLMs can play a broader role in kernel optimization, by acting as virtual models of a GPU rather than solely as kernel generators for search.


