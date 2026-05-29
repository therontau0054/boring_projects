# Abstracts of Papers

## World Model
### Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
**Authors**: Nhat-Minh Nguyen

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30353v1](https://arxiv.org/pdf/2605.30353v1)

**Abstract**: Are AI agents tools, co-authors, or researchers? We present a quantified case study ($N=1$): a physicist supervising an AI coding agent (Claude Code, Sonnet and Opus models) over 12 work days and 57 sessions to build CLAX-PT, a differentiable one-loop perturbation theory module in JAX. We documented and classified 15 supervision events by intervention level.
  The agent resolved ten autonomously by iterating against oracle tests. Two more by the physicist's domain knowledge. The three it could not -- all evaded oracle detection -- share a common property: the agent treated symptom reduction as root-cause resolution. It spent 33 of the 57 sessions adjusting coefficients within a code architecture that could not represent the target physics, and could not re-evaluate its CLASS-PT branch choice even when prompted to reconsider; only an injected physics concept (anisotropic BAO damping) triggered the redesign. Separately, the agent committed a calibrated correction that passed all oracle tests but corresponded to no quantity in the theory, predicting wrong values at any other cosmology.
  The fudge factor was caught and replaced within the same session. Three supervision practices proved critical for catching what oracle tests missed: testing at diverse parameter points beyond the fiducial calibration; shared changelogs that surfaced stalled exploration across sessions; and an explicit rule against unphysical numerical patches. In this case, supervision design, not model capability, determined whether the agent's output was trustworthy. Closing the gap would require agents that propose architectural alternatives rather than optimize within a given structure, and distinguish predictive adequacy from explanatory correctness -- capabilities not exhibited here, not obviously addressed by scaling alone. [Abridged.]


### GMOS: Grounding Moving Object Segmentation in 3D Space and Time
**Authors**: Junyu Xie, Tengda Han, Weidi Xie, Andrew Zisserman

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30352v1](https://arxiv.org/pdf/2605.30352v1)

**Abstract**: Moving Object Segmentation (MOS) aims to discover, segment, and track objects that move independently of the camera. Current MOS methods, however, exhibit two fundamental limitations: they rely on pre-computed 2D auxiliary modalities such as optical flow or point trajectories that lack 3D geometric information, and they treat motion as a sequence-level attribute, overlooking the instantaneous motion state of each object. We address both by grounding MOS in 3D space and time, and propose GMOS, a framework that operates directly on RGB video to produce 3D-aware, temporally fine-grained segmentation of multiple moving objects, alongside a foreground--background variant GMOS-S for faster deployment. To support training and evaluation in this regime, we curate GMOS-2K, a dataset of 2,210 real-world videos with per-object temporal motion annotations drawn from five established Video Object Segmentation (VOS) benchmarks, and formalise MOS-I ("I" for instantaneous), a temporally fine-grained evaluation protocol with three complementary metrics. GMOS achieves state-of-the-art results across MOS, MOS-I, and Unsupervised VOS benchmarks, while running significantly faster than prior multi-object MOS methods and supporting online inference for streaming deployment.


### VideoMLA: Low-Rank Latent KV Cache for Minute-Scale Autoregressive Video Diffusion
**Authors**: Hidir Yesiltepe, Jiazhen Hu, Tuna Han Salih Meral, Adil Kaan Akan, Kaan Oktay, Hoda Eldardiry, Pinar Yanardag

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30351v1](https://arxiv.org/pdf/2605.30351v1)

**Abstract**: Long-rollout causal video diffusion has converged on a fixed-size sliding-window KV cache, with recent progress innovating within this layout by changing which tokens occupy the window or how their positions are encoded. The per-head KV layout itself, a dominant contributor to streaming memory and latency, has been mostly left unchanged. In this paper, we present the first study of Multi-Head Latent Attention (MLA) in video diffusion. VideoMLA replaces per-head keys and values with a shared low-rank content latent and a shared decoupled 3D-RoPE positional key, reducing per-token KV memory by 92.7% at every cached layer. We further investigate why MLA succeeds in video diffusion even though the spectral assumption often used to motivate it in language models does not hold: pretrained video attention is not low-rank, with 99%-energy effective rank far above any practical latent dimension. VideoMLA retains quality at compression ratios where direct spectral approximation would predict large reconstruction error. We show that the MLA bottleneck, rather than the pretrained spectrum, determines the effective rank: both spectral and random initialization occupy nearly the full rank budget from initialization, and training preserves this budget while adapting within it. On VBench, VideoMLA matches short-horizon streaming video diffusion baselines, achieves the best overall score at long horizons among evaluated methods, and improves throughput by 1.23x on a single B200.


### DynaFLIP: Rethinking Robotics Perception via Tri-Modal-Dynamics Guided Representation
**Authors**: Jusuk Lee, Seungjae Lee, Jonghun Shin, Hoseong Jung, Sungha Kim, Daesol Cho, H. Jin Kim, Jia-Bin Huang, Furong Huang

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30350v1](https://arxiv.org/pdf/2605.30350v1)

**Abstract**: Robot manipulation critically depends on perception that preserves the action-relevant aspects of a scene. Yet most robot learning pipelines are built upon visual encoders pre-trained for static recognition or vision-language alignment, leaving motion understanding to downstream policies. We introduce DynaFLIP, a dynamics-aware multimodal pre-training framework that pushes motion understanding upstream into perception. We construct image-language-3D flow triplets from heterogeneous human and robot videos, and use these triplets as training-time supervision to shape an image-only encoder. Our key idea is to encourage the three modalities to span a small simplex volume in the shared hyperspherical space -- a smaller simplex volume indicating stronger alignment. To avoid the geometric ambiguity and trivial collapse of naive volume minimization, we combine simplex-volume minimization with a cosine regularizer and a contrastive objective. Our analyses show that DynaFLIP focuses on control-relevant regions critical for manipulation. The resulting dynamics-aware representations serve as reusable visual backbones and consistently outperform baselines across diverse downstream policies, including VLAs. We validate this across diverse simulation and real-world setups, with gains reaching +22.5% under out-of-distribution scenarios. Our results suggest that robot generalization improves when visual representations are trained to encode not just what is present, but how the world changes under action.


### LLMSurgeon: Diagnosing Data Mixture of Large Language Models
**Authors**: Yaxin Luo, Jiacheng Cui, Xiaohan Zhao, Xinyi Shang, Jiacheng Liu, Xinyue Bi, Zhaoyi Li, Zhiqiang Shen

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30348v1](https://arxiv.org/pdf/2605.30348v1)

**Abstract**: The pretraining data mixture of Large Language Models (LLMs) constitutes their "digital DNA", shaping model behaviors, capabilities, and failure modes. Yet this composition is rarely disclosed, making post-hoc auditing of data combination or provenance difficult. In this work, we formalize $\textbf{Data Mixture Surgery (DMS)}$: given only generated text from a target LLM, estimate the domain-level distribution of its pretraining corpus under a predefined taxonomy. We propose $\textbf{LLMSurgeon}$, a strong framework that casts DMS as an inverse problem under the label-shift assumption. Rather than directly aggregating classifier outputs, LLMSurgeon estimates a calibrated $\textit{soft}$ confusion matrix and solves a constrained inverse problem to correct systematic domain confusion and recover the latent mixture prior. To evaluate, we introduce $\textbf{LLMScan}$, a recipe-verifiable evaluation suite built from open-source LLMs with transparent pretraining mixtures. Across LLMScan, LLMSurgeon recovers domain mixtures with high fidelity under fixed protocols. Our work presents a practical, post-hoc approach for auditing the digital DNA of foundation models without access to their training data.


### NeuROK: Generative 4D Neural Object Kinematics
**Authors**: Chen Geng, Guangzhao He, Yue Gao, Yunzhi Zhang, Shangzhe Wu, Jiajun Wu

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30347v1](https://arxiv.org/pdf/2605.30347v1)

**Abstract**: Data-driven approaches have revolutionized 3D vision, enabling transformers to effectively reconstruct and generate static 3D objects. However, generating simulative 4D dynamics -- realistic temporal deformations of static objects under various physical conditions -- remains challenging and often ad hoc, despite its importance in building comprehensive 3D world models. Most existing methods assume a predefined physical model and use system identification to estimate parameters, restricting these methods to specific categories and small-scale datasets. We propose that these restrictions can be overcome by learning a data-driven kinematic state parameterization for object-centric physical systems. Specifically, we learn both a latent space representing all possible states of the object and a decoder that maps any sampled latent to a plausibly deformed shape of the object. We refer to this parameterization as Neural Object Kinematics (NeuROK), and learn a transformer-based encoder-decoder model on a curated large-scale 4D dataset. This formulation and the learned model significantly simplify the generation of simulative dynamics since we only need to consider the dynamics within a low-dimensional latent space from the Lagrangian mechanics' perspective in classical physics. We demonstrate the effectiveness and generality of this neural simulation framework across diverse dynamic object types, showing clear advantages over prior works. Project page: https://chen-geng.com/neurok


## Generation
### SchGen: PCB Schematic Generation with Semantic-Grounded Code Representations
**Authors**: Qinpei Luo, Ruichun Ma, Xinyu Zhang, Lili Qiu

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30345v1](https://arxiv.org/pdf/2605.30345v1)

**Abstract**: Printed circuit board (PCB) schematic design defines nearly all electronic hardware, but it remains manual and expertise-intensive. While generative AI has advanced digital and analog IC design, PCB schematic generation from natural-language intent is largely unexplored. This paper presents SchGen, the first large language model that generates editable PCB schematics from natural-language requests. The key challenge lies in the lack of an LLM-suited representation and a large-scale dataset. Current schematic formats are dominated by verbose, tool-specific syntax and geometry-heavy descriptions, making them difficult to generate reliably. We introduce a semantically grounded code representation that encodes schematic editing primitives with relative placement and pin-name-based wiring, transforming a geometry-driven generation problem into a semantics-driven matching task amenable to LLMs. We further construct a large-scale dataset of PCB schematics paired with user prompts via a human-agent collaborative pipeline that converts open-source hardware designs into our representation. Experiments show that SchGen significantly outperforms alternative representations and even larger general-purpose LLMs on wire connectivity accuracy and functional correctness. Our results highlight the critical role of representation design in enabling generative models for complex hardware design tasks.


### Tiny but Trusted: Efficient Vision-Language Reasoning for Time-Series Anomaly Detection
**Authors**: Xiaona Zhou, Muntasir Wahed, Tianjiao Yu, Constantin Brif, Ismini Lourentzou

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30344v1](https://arxiv.org/pdf/2605.30344v1)

**Abstract**: Recent advances in Vision-Language Models (VLMs) have achieved impressive performance across many tasks, yet prior studies report unsatisfactory performance when applying large language or multimodal models to finding abnormal patterns in sequential data. Public anomaly detection benchmarks typically provide interval annotations but not natural-language rationales, making it difficult to fine-tune VLMs to produce grounded, interpretable decisions. To address this gap, we construct VisAnomBench, a curated benchmark built from public time-series datasets and augmented with high-quality anomaly explanations selected from multiple large VLMs using fine-grained, task-specific rewards. Through fine-tuning on this benchmark, we develop VisAnomReasoner, a parameter-efficient VLM for time-series anomaly detection. Experimental results on VisAnomBench show that VisAnomReasoner achieves more accurate anomaly localization and consistently outperforms all baselines, with improvements of at least 21.23 and 23.87 percentage points in precision and F1, respectively. Additional experiments on the TSB-AD-U benchmark demonstrate strong cross-benchmark generalization, with VisAnomReasoner improving precision and F1 by 9.57 and 13.39 percentage points, respectively.


### Unlocking the Working Memory of Large Language Models for Latent Reasoning
**Authors**: Lukas Aichberger, Sepp Hochreiter

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30343v1](https://arxiv.org/pdf/2605.30343v1)

**Abstract**: To improve the reasoning capabilities of large language models, test-time compute is typically scaled by generating intermediate tokens before the final answer. However, this couples reasoning to autoregressive generation and thereby conflates internal computation with external communication. In contrast, human cognition can use working memory to hold and manipulate information internally without the need to externalize intermediate thoughts. Drawing on this principle, we introduce Reasoning in Memory (RiM), a latent reasoning method that replaces the autoregressive generation of reasoning steps with memory blocks. These memory blocks are fixed sequences of special tokens that unlock the working-memory capacity of large language models. Since they are fixed rather than generated, they can be processed in a single forward pass, enabling compute-efficient latent reasoning. To operationalize these memory blocks, we employ a two-stage curriculum. First, we ground them by predicting explicit reasoning steps after each memory block. Second, we discard this step-level supervision and iteratively refine the final answer after each memory block. Our experiments on reasoning benchmarks show that, across language models of different families and sizes, RiM matches or exceeds existing latent reasoning methods while avoiding the autoregressive generation of thoughts. These results demonstrate that large language models can be trained to use working memory as an effective mechanism for latent reasoning.


### GPIC: A Giant Permissive Image Corpus for Visual Generation
**Authors**: Keshigeyan Chandrasegaran, Kyle Sargent, Suchir Agarwal, Michael Jang, Michael Poli, Juan Carlos Niebles, Justin Johnson, Jiajun Wu, Li Fei-Fei

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30341v1](https://arxiv.org/pdf/2605.30341v1)

**Abstract**: Studying scalable methods for visual generative modeling requires large, accessible, and stable datasets. We introduce GPIC, a Giant Permissive Image Corpus of approximately 28 trillion pixels. GPIC comprises diverse internet images captioned by a state-of-the-art vision-language model, including 100M training, 200K validation, and 1M test examples. Moreover, all GPIC images are permissively licensed for both research and commercial use. GPIC is safety-filtered, deduplicated, and centrally hosted on Hugging Face. We provide a benchmarking protocol for generative modeling on GPIC. Finally, we provide a reference baseline for pixel-space flow matching on GPIC. Our dataset, benchmark, and models are available at https://huggingface.co/datasets/stanford-vision-lab/gpic. Evaluation toolkit and code are available at https://gpic.stanford.edu


### Demystifying Data Organization for Enhanced LLM Training
**Authors**: Yalun Dai, Yangyu Huang, Tongshen Yang, Yonghan Wang, Xin Zhang, Wenshan Wu, Qihao Zhao, Hao Li, Yuanyuan Gao, Kim-Hui Yap, Scarlett Li

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30334v1](https://arxiv.org/pdf/2605.30334v1)

**Abstract**: Large Language Models (LLMs) have revolutionized various fields, yet their training efficiency is heavily reliant on effective data curation. While data selection has been widely studied, the strategic data organization for enhanced training remains an underexplored area, particularly since current LLMs are often trained for only one or a few epochs. This paper systematically explores the influence of data organization on LLM training by reusing pre-computed sample-level scores originally generated for data efficiency, thereby incurring minimal additional computational overhead. We identify and formalize four key guidelines for optimizing data organization: Boundary Sharpening, Cyclic Scheduling, Curriculum Continuity, and Local Diversity. Guided by them, we introduce two novel data ordering methods termed STR and SAW. Extensive experiments across different model scales and data sizes, encompassing both pre-training and SFT stages, validate the effectiveness of our summarized guidelines. They also demonstrate the robustness of our proposed data ordering methods in enhancing the stability and performance of LLM training. Github Link: https://github.com/microsoft/data-efficacy/


### SoundnessBench: Can Your AI Scientist Really Tell Good Research Ideas from Bad Ones?
**Authors**: Sy-Tuyen Ho, Minghui Liu, Huy Nghiem, Furong Huang

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30329v1](https://arxiv.org/pdf/2605.30329v1)

**Abstract**: Autonomous AI research agents aim to accelerate scientific discovery by automating the research pipeline, from hypothesis generation to peer review. However, existing benchmarks rarely test a fundamental bottleneck: whether Large Language Models can judge the methodological viability of a research idea before expending time and computational resources. We introduce SoundnessBench, a curated benchmark of 1,099 machine-learning research proposals reconstructed from ICLR submissions, labeled with reviewer soundness sub-scores, and audited against source papers. SoundnessBench should be interpreted as a benchmark for recoverable proposal-stage soundness rather than exact prediction of full-paper review outcomes. Across 12 frontier LLMs, we find a pervasive optimism bias: under standard prompting, models frequently rate low-soundness proposals as sound, while aggressive prompting largely shifts errors from false positives to false negatives. Additional controls for public-corpus contamination, paper-identifying phrases, surface features, and human audit quality suggest that this behavior is not explained by a single confounder. Our results indicate that current LLMs are not yet reliable as standalone first-gate evaluators for scientific rigor.


## VLA
### RoboWits: Unexpected Challenges for Robotic Creative Problem Solving
**Authors**: Chunru Lin, Hongxin Zhang, Fenghao Yu, Zhehuan Chen, Thomas L. Griffiths, Yejin Choi, David Held, Chuang Gan

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30326v1](https://arxiv.org/pdf/2605.30326v1)

**Abstract**: The ability to reason, adapt, and creatively solve problems under unexpected challenges is essential for robots operating in real-world environments. However, current robotic benchmarks primarily emphasize skill-level execution and provide limited insight into such cognitive reasoning capabilities. We introduce RoboWits, a bi-manual robotic benchmark designed to systematically evaluate cognitive reasoning, creative tool use, and robustness to unexpected conditions. To enable scalable construction of high-quality reasoning-centric unexpected scenarios, we propose an automated task generation pipeline formulated as a multi-agent cooperative framework, comprising agents for seed task generation and verification, metric generation, scene generation, and task mutation. Using the pipeline, we curated 30 diverse seed tasks and 208 tasks with mutations and graded difficulty across geometry, material, and assembly-based reasoning. We benchmark popular robot policies, pre-trained VLAs, and oracle-state planners. Our results reveal a significant performance gap: while pre-trained VLAs exhibit preliminary success on seed tasks after single-task fine-tuning, they struggle to perform on mutated tasks, implying their brittleness in manipulation tasks requiring reasoning, strategy adaptation, and robustness to deceptive or constrained environments. Project page is available at https://umass-embodied-agi.github.io/RoboWits.


### Qwen-VLA: Unifying Vision-Language-Action Modeling across Tasks, Environments, and Robot Embodiments
**Authors**: Qiuyue Wang, Mingsheng Li, Jian Guan, Jinhui Ye, Sicheng Xie, Yitao Liu, Junhao Chen, Zhixuan Liang, Jie Zhang, Xintong Hu, Xuhong Huang, Pei Lin, Junyang Lin, Dayiheng Liu, Shuai Bai, Jingren Zhou, Jiazhao Zhang, Haoqi Yuan, Gengze Zhou, Hang Yin, Ye Wang, Yiyang Huang, Zixing Lei, Wujian Peng, Delin Chen, Yingming Zheng, Jingyang Fan, Xianwei Zhuang, Xin Zhou, Haoyang Li, Anzhe Chen, Tong Zhang, Xuejing Liu, Yuchong Sun, Ruizhe Chen, Zhaohai Li, Chenxu Lü, Zhibo Yang, Tao Yu, Xionghui Chen

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30280v1](https://arxiv.org/pdf/2605.30280v1)

**Abstract**: Embodied intelligence is often studied through specialized models for individual tasks such as manipulation or navigation, resulting in fragmented capabilities and limited generalization across tasks, environments, and robot embodiments. In this work, we study whether heterogeneous embodied decision-making problems can be unified within a single vision-language-action model. We present Qwen-VLA, a unified embodied foundation model that extends Qwen's vision-language modeling stack from perception, understanding, and reasoning to continuous action and trajectory generation through a DiT-based action decoder. Qwen-VLA is trained with a large-scale joint pretraining recipe over diverse data sources, including robotics manipulation trajectories, human egocentric demonstrations, synthetic simulation data, vision-and-language navigation data, trajectory-centric supervision, and auxiliary vision-language data. To support multiple robot platforms, we introduce embodiment-aware prompt conditioning, where robot-specific textual descriptions specify the current embodiment and control convention. We further cast manipulation, navigation, and trajectory prediction into a unified action-and-trajectory prediction framework, enabling transferable visual grounding, spatial reasoning, and continuous action generation across robot morphologies, task families, and environments. Experiments on manipulation, navigation, and trajectory-centric benchmarks show consistent multi-task performance and out-of-distribution generalization under variations in scene layout, background, lighting, object configuration, and robot embodiment. Qwen-VLA-Instruct achieves 97.9% on LIBERO, 73.7% on Simpler-WidowX, 86.1%/87.2% on RoboTwin-Easy/Hard, 69.0% OSR on R2R, 59.6% SR on RxR, 76.9% average OOD success in real-world ALOHA experiments, and 26.6% zero-shot success on DOMINO dynamic manipulation.


### BORA: Bridging Offline Reinforcement Learning and Online Residual Adaptation for Real-World Dexterous VLA Models
**Authors**: Zhongxi Chen, Yifan Han, Yanming Shao, Huanming Liu, Congsheng Xu, Xiaoyu Chen, Yao Mu, Wenzhao Lian

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30226v1](https://arxiv.org/pdf/2605.30226v1)

**Abstract**: Vision-Language-Action (VLA) models have emerged as a promising paradigm for grounding visual-language understanding into real-world robotic manipulation. However, dexterous manipulation remains challenging for VLA policies due to high-dimensional hand control and compounding execution errors, which makes real-world RL post-training essential for bridging the gap between visually grounded action generation and physically reliable dexterous execution. However, high-dimensional dexterous exploration often triggers temporal inconsistency, sample inefficiency and hardware risks in the real world. To address these challenges, we propose BORA, an offline-to-online RL post-training framework designed for real-world dexterous VLA models. In the offline phase, BORA constructs a critic that takes both the VLM's cognition tokens and action chunks as inputs. This design enables action-conditioned value guidance, allowing the critic to evaluate dexterous hand motions beyond visual context alone. During the subsequent online phase, BORA freezes the VLA base and introduces a lightweight, Human-in-the-Loop (HiL) chunk-wise residual adaptation mechanism to mitigate real-world execution errors and further correct the offline-learned intents within the actual physical environment. By inheriting the offline critic and employing intervention-driven rewards, BORA effectively corrects execution discrepancies and adapts to real-world physical variances while preserving the pretrained policy as a stable prior. Extensive evaluations across five complex real-world dexterous tasks demonstrate that BORA significantly outperforms pure imitation learning and traditional decoupled RL baselines, achieving a 33% absolute increase in average success rate under standard settings and up to a 43% improvement in unseen object generalization.


### VLA-Trace: Diagnosing Vision-Language-Action Models through Representation and Behavior Tracing
**Authors**: Haoyuan Shi, Xiancong Ren, Yingji Zhang, Qinfan Zhang, Jiayu Hu, Haozhe Shan, Han Dong, Jinpeng Lu, Yinda Chen, Yi Zhang, Yong Dai, Xiaozhu Ju

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30117v1](https://arxiv.org/pdf/2605.30117v1)

**Abstract**: Understanding how Vision-Language-Action (VLA) models transform multimodal knowledge into embodied control remains an open challenge. We present VLA-Trace, a progressive diagnostic framework that analyzes VLA models through a unified evidence chain from representation dynamics to causal control attribution and behavioral manifestation. It specifically combines cross-modal and checkpoint-drift centered kernel alignment (CKA) to trace representation evolution, attention knockout interventions to identify modality-specific control pathways, and rollout-level behavioral probes to examine grounding, shortcut dependence, and semantic following. Experiments on $π_{0.5}$ and OpenVLA reveal three key findings. First, the two models exhibit distinct modality-specific adaptation dynamics during VLA finetuning. Second, they rely on different multimodal routing strategies and layer-wise dependencies during action decoding. Third, although VLA policies excel at visually grounded trajectory generation, they remain limited in fine-grained semantic following. These findings highlight future directions for representation-preserving adaptation, causal VLA circuits, and compositional semantic control.


### VisualThink-VLA: Visual Intermediate Reasoning for Effective and Low-Latency Vision-Language-Action Policies
**Authors**: Mingjian Gao, Wenqiao Zhang, Yuqian Yuan, Yang Dai, Binhe Yu, Zheqi Lv, Haoyu Zheng, Jiaqi Zhu, Zhiqi Ge, Zixuan Wan, Siliang Tang, Yueting Zhuang

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30011v1](https://arxiv.org/pdf/2605.30011v1)

**Abstract**: Recent work has begun to equip vision-language-action (VLA) policies with explicit intermediate reasoning. In embodied control, however, textual chain-of-thought is a poor fit: irrelevant or weakly textual information can interfere with action prediction, while autoregressive text decoding adds too much latency for real-time closed-loop execution. We present VISUALTHINK-VLA, a visual intermediate-reasoning framework for accurate, low-latency VLA policies. Our bootstrapping philosophy is to guide action with effective visual thinking: VISUALTHINK-VLA bootstraps action prediction through a compact visual-evidence interface that preserves spatial precision while avoiding decoding overhead. Besides, to further improve performance and efficiency, VISUALTHINK-VLA adopts a tailored selective routing mechanism to learn the visual evidence tokens, enabling low-latency inference while preserving high-capacity specialization. We also introduce VisualEvidence-Kit, a supervision-and-audit resource centered on a VisualEvidence-Agent that constructs a 754.7k VLA instructions VisualEvidence-Set for route supervision and counterfactual faithfulness tests. Across multiple benchmarks and real-robot evaluation, VISUALTHINK-VLA achieves the highest success rate on most benchmarks while reducing the multi-second latency of reasoning-augmented baselines to the sub-second regime. For example, on BridgeData V2, it reduces step latency from 8.377,s with ECoT to 0.367,s, achieving a 22.8 times speedup.


### VLA-Pro: Cross-Task Procedural Memory Transfer for Vision-Language-Action Models
**Authors**: Shengyu Si, Yuanzhuo Lu, Ruimeng Yang, Ziyi Ye, Zuxuan Wu, Yu-Gang Jiang

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.29562v1](https://arxiv.org/pdf/2605.29562v1)

**Abstract**: Vision-Language-Action~(VLA) models have shown strong potential for general-purpose robotic manipulation, yet they still struggle to generalize to unseen tasks that necessitate transferring relevant experience across objects, scenes, and action patterns. This paper proposes VLA-Pro, a plug-and-play framework designed to enhance cross-task generalization by storing task-relevant procedural memories at training time and transferring these memories during inference. Specifically, VLA-Pro stores task-specific LoRA adapters as parameterized procedural memories during training. At inference time, VLA-Pro retrieves relevant procedural memories based on the current multi-modal context and dynamically fuses these memories for generating the current action chunk. Experiments on RoboTwin, RLBench, and real-world manipulation tasks show that VLA-Pro consistently improves cross-task generalization across multiple backbones, achieving up to a 207% relative improvement in simulation and increasing real-world success rate from 5.8% to 65.0%. These results suggest that procedural memory retrieval and adaptation provide an effective mechanism for transferring manipulation experience to novel tasks while preserving modularity and execution stability.


## Agent
### Locally Coherent, Globally Incoherent: Bounding Compositional Incoherence in Multi-Component LLM Agents
**Authors**: Anany Kotawala

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30335v1](https://arxiv.org/pdf/2605.30335v1)

**Abstract**: Multi-component LLM agents assemble probabilistic claims from components that each see only part of a joint problem; the composition can violate basic probability axioms even when every component is locally coherent. We formalise this locally coherent, globally incoherent failure via the compositional residual eps*, the L2 distance from the composed quote to the joint coherent polytope, computable at runtime from system output and the declared cross-component coupling constraints. A product-structure dichotomy characterises when local coherence suffices, and a Rayleigh-quotient prediction matches the observed residual within 7% on three of four relation classes. A hierarchical Boyle-Dykstra projection repairs the composition deterministically; an anytime-valid e-process gives sequential coherence monitoring. Across 1,876 ensemble cliques on a four-LLM mid-tier panel (frontier-panel rerun in Section 5.5), eps* > 0 on 33-94% of cliques, translating to +0.115 nats per bet of regret on 1,770 resolved bets under the proportional allocation rule (the gain collapses to +0.006 under bettors that themselves coherentise). Three intuitive LLM-side mitigations(retrieval, partition-aware prompting, aggregator-LLM) each fail or regress.


### Gram: Assessing sabotage propensities via automated alignment auditing
**Authors**: David Lindner, Victoria Krakovna, Sebastian Farquhar

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30322v1](https://arxiv.org/pdf/2605.30322v1)

**Abstract**: We introduce Gram, an automated alignment auditing framework to assess the propensity of AI agents to engage in sabotage. We evaluate Gemini models across 17 simulated agentic deployment scenarios that incentivize sabotage. We find Gemini models misbehave in about 2-3% of our simulated trajectories. Many of these cases are explained by "overeagerness" in Gemini models resulting in both excessive role-playing and goal-seeking behavior. In contrast to other alignment auditing approaches, Gram is designed to specifically evaluate misalignment and intentional sabotage in agentic coding and research agents. We additionally introduce an experimental investigator agent pipeline which enables fine-grained targeted experiments to identify the drivers of misbehavior. We find that increasing realism of environments and removing nudges to misbehave tends to reduce sabotage rates close to zero.


### Loong: A Human-Like Long Document Translation Agent with Observe-and-Act Adaptive Context Selection
**Authors**: Yutong Wang, Xuebo Liu, Derek F. Wong, Zhilin Li, Rongqing Jiang, Min Zhang, Shimin Tao, Daimeng Wei, Min Zhang

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30274v1](https://arxiv.org/pdf/2605.30274v1)

**Abstract**: Document-level translation remains one of the most challenging tasks for large language models, which are constrained by limited context windows that impede global cohesion, while simultaneously suffering from redundant contextual information that degrades translation quality. To address this, we propose a human-like long document translation agent called Loong, which leverages a 3E memory module (Essence-Exemplar-Entity) to store summaries, sentence pairs, and entity records as historical context. Instead of passively attending to all history, Loong performs deep reasoning to adaptively identify the optimal context for translation guidance. Loong optimizes its context policy through reinforcement learning, utilizing preference data derived from its own sampled observe-and-act reasoning trajectories. Empirical evaluations demonstrate that Loong achieves substantial translation quality improvements in English $\Leftrightarrow$ Chinese, German, and French directions, with average gains of up to 13.0 points across the three evaluation metrics. Furthermore, Loong exhibits strong generalization across domains and robustness against contextual noise, while maintaining remarkable stability in ultra-long document translation. Our code is released at https://github.com/YutongWang1216/LoongDocMT.


### PhyGenHOI: Physically-Aware 4D Generation of Dynamic Human-Object Interactions
**Authors**: Omer Benishu, Gal Fiebelman, Sagie Benaim

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30268v1](https://arxiv.org/pdf/2605.30268v1)

**Abstract**: We address the task of generating physically accurate and visually faithful 4D Human-Object Interaction (HOI). Given a static 3D human and target object represented as 3D Gaussian Splats (3DGS), our goal is to synthesize dynamic scenes where the human actively engages with the object through actions, such as punching or kicking, in accordance with a given input text. To this end, we introduce PhyGenHOI, a novel framework that couples generative human motion with an explicit physical object simulation. We model the human as a semantic agent driven by a Motion Diffusion Model (MDM) and the object as a physical agent simulated via the Material Point Method (MPM), utilizing 3D Gaussians as a unified, differentiable representation. We supervise their interaction through three coupled mechanisms: (1) A Windowed Attraction Loss that temporally synchronizes generative motion to intercept the object; (2) A Contact-Driven Re-simulation step that triggers physically consistent momentum transfer upon impact; and (3) A Masked Video-SDS objective that injects video-based priors to enhance contact fidelity. Experiments show PhyGenHOI generates physically consistent 4D HOI across diverse actions, humans, and objects, outperforming baselines. Project page and videos: https://omerbenishu.github.io/PhyGenHOI/


### Unifying Temporal and Structural Credit Assignment in LLM-Based Multi-Agent Prompt Optimization
**Authors**: Wenwu Li, Yuran Song, Mingze Zhao, Bo Jin, Wenhao Li

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30227v1](https://arxiv.org/pdf/2605.30227v1)

**Abstract**: While Multi-Agent Systems (MAS) empower Large Language Models to tackle complex reasoning tasks through collaborative interaction, optimizing their dynamics remains a formidable challenge due to the discrete, non-differentiable nature of the computation graph and the sparsity of global supervisory signals. Existing black-box optimizers struggle to attribute trajectory-level failure to specific local components, resulting in inefficient, high-variance exploration. We argue that tractable MAS optimization needs structural inductive biases to disentangle error signals. We propose temporal and structural credit assignment, which decomposes the objective along two axes: (i) temporal credit, using state-space bottlenecks to identify critical rounds, and (ii) structural credit, using stationary role policies to isolate agent contributions. Leveraging these decomposed signals, we introduce a discrete, verbalized block coordinate descent algorithm for iterative refinement. Rather than indiscriminate global updates, it alternates between optimizing role prompts and aggregation protocols, using LLM-generated "proxy gradients" to target only the identified weak links. Across diverse reasoning benchmarks, our approach substantially reduces query complexity while improving performance, providing a principled and interpretable path toward self-improving MAS.


### Automating Low-Risk Code Review at Meta: RADAR, Risk Calibration, and Review Efficiency
**Authors**: Chris Adams, Arjun Singh Banga, Parveen Bansal, Souvik Bhattacharya, Rujin Cao, Pedro Canahuati, Nate Cook, Brian Ellis, Prabhakar Goyal, Gurinder Grewal, Tianyu He, Matt Labunka, Alex Manners, David Molnar, Ging Cee Ng, Vishal Parekh, Jiefu Pei, Frederic Sagnes, James Saindon, Will Shackleton, Sid Sidhu, Gursharan Singh, Karthik Chengayan Sridhar, Matt Steiner, Pratibha Udmalpet, Sean Xia, Stacey Yan, Audris Mockus, Peter Rigby, Nachiappan Nagappan

**Published Date**: 2026-05-28

**Updated Date**: 2026-05-28

**PDF Url**: [2605.30208v1](https://arxiv.org/pdf/2605.30208v1)

**Abstract**: AI-assisted coding tools have altered software production. At Meta, significant lines of code per human-landed diff grew by 105.9% year over year and per-developer diff volume rose 51%, with agentic AI responsible for over 80% of that growth. Meanwhile, the share of diffs receiving timely review has declined, exposing a widening gap between code supply and reviewer bandwidth. We ask three questions that progress from feasibility through calibration to impact: (1) can risk-stratified automation operate at scale across diverse organizations, (2) how does tuning the risk threshold affect the trade-off between automation yield and safety, and (3) to what extent does automated review reduce end-to-end latency for AI-generated changes? We deployed RADAR (Risk Aware Diff Auto Review), a multi-stage funnel that classifies each diff by authorship and source type, applies eligibility gates, static heuristics, a machine-learned Diff Risk Score, LLM-based Automated Code Review, and deterministic validation before landing qualifying changes. We evaluate RADAR through telemetry covering 535K+ RADAR-reviewed diffs, observational before-after comparisons for policy changes, and difference-in-differences analysis of efficiency outcomes. RADAR has reviewed 535K+ diffs and landed 331K+. Relaxing the Diff Risk Score threshold from the 25th to the 50th percentile increased the approve rate to 60.31%. The revert rate for RADAR-reviewed diffs is 1/3 that of non-RADAR diffs, and the Production Incident rate is 1/50 that of non-RADAR diffs. RADAR reduces median time to close by over 330% and median diff review wall time by 35%. Risk-aware layered automation can materially reduce review bottlenecks created by AI-driven code growth without compromising production safety.


