# Abstracts of Papers

## World Model
### LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models
**Authors**: Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08770v1](https://arxiv.org/pdf/2607.08770v1)

**Abstract**: Recovering high-quality video from sparse event streams is a challenging task. Regression methods often blur textures, while existing generative models struggle with long-term stability. We propose LongE2V, a novel approach that leverages pre-trained video diffusion priors to jointly handle event-based video reconstruction, prediction, and frame interpolation. By fine-tuning a foundational video model, our approach achieves high data efficiency and superior perceptual quality. We introduce Autoregressive Unrolling and Adaptive Context Switching to mitigate temporal drift in extremely long sequences. We also propose Reencoding Alignment with Cross Residual Correction to ensure precise bidirectional consistency during frame interpolation. Furthermore, Event Voxel Density Augmentation ensures robustness across varying sensor resolutions. Extensive experiments on real-world benchmarks demonstrate that LongE2V outperforms state-of-the-art methods across all three tasks, exhibiting exceptional temporal coherence and zero-shot generalization. Project page: https://cdfan0627.github.io/LongE2V-page/


### UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks
**Authors**: Zhekai Chen, Chengqi Duan, Kaiyue Sun, Bohao Li, Yuqing Wang, Manyuan Zhang, Xihui Liu

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08768v1](https://arxiv.org/pdf/2607.08768v1)

**Abstract**: The rapid development of large language models and multimodal large language models has accelerated the emergence of proactive agents capable of operating everyday tools and assisting users in real-world environments. However, existing benchmarks struggle to evaluate such agents effectively, as they often rely on sandboxed environments and single-turn evaluation paradigms. Moreover, their scenario-based task taxonomies mix multiple model capabilities within the same task category, making it difficult to identify the root causes of agent failures. To address these limitations, we introduce UniClawBench, the first capability-driven benchmark designed to evaluate proactive agents in dynamic, real-world settings. UniClawBench is built around five foundational model capabilities: Skill Usage, Exploration, Long-Context Reasoning, Multimodal Understanding, and Cross-Platform Coordination. Based on these capabilities, we design 400 bilingual real-world tasks. Unlike previous benchmarks that rely on static, pre-recorded answers, our benchmark evaluates agents in live Docker containers using fine-grained, step-by-step completion checkpoints. Furthermore, we design a closed-loop evaluation strategy comprising an executor agent, a hidden supervisor agent, and a user agent to simulate realistic multi-turn human feedback without leaking grading criteria. To disentangle base model capabilities from framework-level design choices, we evaluate state-of-the-art models under multiple agent frameworks. Through comprehensive comparisons across both models and frameworks, we show how base model capabilities and agent framework designs jointly shape performance in real-world environments. To facilitate future research, we make our benchmark and code publicly available at https://github.com/HKU-MMLab/UniClawBench.


### OpenCoF: Learning to Reason Through Video Generation
**Authors**: Xinyan Chen, Ziyu Guo, Renrui Zhang, Dongzhi Jiang, Hongsheng Li

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08763v1](https://arxiv.org/pdf/2607.08763v1)

**Abstract**: Reasoning has become a core capability for large models, especially when reliable decisions require understanding logical consequences. Recent video generation models offer a reasoning path distinct from previous Chain-of-Thought (CoT): reasoning can unfold through temporally connected frames, known as Chain-of-Frame (CoF) reasoning. However, existing video generators are primarily trained on general video corpora, still lacking diverse supervision and dedicated designs for CoF reasoning. To address this gap, we introduce OpenCoF, a framework comprising the OpenCoF-17K dataset, a reasoning video dataset spanning 11 task families, and Wan-CoF, a fine-tuned video model for studying whether diverse temporal supervision improves CoF behavior. Across four video reasoning benchmarks, Wan-CoF achieves considerable gains over the Wan2.2-I2V-A14B baseline. Building on this, we empirically explore more advanced designs for CoF capabilities, i.e., equipping the model with visual and textual reasoning tokens. This mechanism respectively captures low-level visual cues and high-level semantic priors for spatial and temporal reasoning. Through performance comparisons and attention analysis, we examine how these tokens contribute across model depth, denoising steps, space, and time. Our results suggest that stronger video reasoning requires both broad temporal supervision and explicit mechanisms for organizing intermediate reasoning state. We open-source the dataset, model, and code to facilitate future research on reasoning-oriented video generation.


### Typicality of Steering for Two-qubit States
**Authors**: Gerard Anglès Munné, Paweł Cieśliński, Tamás Vértesi, Wiesław Laskowski

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08762v1](https://arxiv.org/pdf/2607.08762v1)

**Abstract**: Phenomena that slip beyond the grasp of our classical intuition reveal uniquely quantum effects that deepen our understanding of the physical world and enable advances in information processing, particularly in quantum communication and computation. One such phenomenon is quantum steering, whereby measurements performed by one party influence the conditional states of another when the two share an entangled quantum system. If the observed correlations cannot be explained by a local hidden state model, the state is said to be steerable. In this work, we investigate the typicality of this behavior: given a generic two-qubit state and $m$ Haar-random projective measurements, what is the probability of observing steering? We derive analytical expressions for the steering probability $\mathcal{P}_S$ of Werner states in two- and three-setting scenarios, the latter restricted to coplanar projective measurements on the Bloch sphere. For larger numbers of settings and various random states ensembles, we perform numerical analyses showing that $\mathcal{P}_S$ increases systematically with the number of measurements and substantially exceeds the corresponding probabilities associated with Bell nonlocality. Our results demonstrate that random states with minimal environmental coupling exhibit a high probability of steering for finite $m$ and approach genuine typicality, $\mathcal{P}_S=100\%$, as the number of settings increases. We provide a detailed characterization of $\mathcal{P}_S$ across different state ensembles and specific families, including Bell-diagonal and Werner states, identifying those with the greatest non-classical potential and highlighting their relevance for protocols in which steering serves as a key resource.


### MulTTiPop: A Multitrack Transcription Dataset for Pop Music
**Authors**: Nathan Pruyne, Benjamin Stoler, William Chen, Chien-yu Huang, Shinji Watanabe, Chris Donahue

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08756v1](https://arxiv.org/pdf/2607.08756v1)

**Abstract**: We present MulTTiPop, a dataset of pop music segments and their associated multitrack MIDI recordings for the evaluation of automatic music transcription models. MulTTiPop contains 572 segments of popular music totaling 3.5 hours of audio, and contains songs from diverse genres and decades from the 1930s to 2000s. To collect this dataset, we perform metadata-based matching on song segments from the Lakh MIDI and TheoryTab datasets, manually identify an anchor beat between the audio and MIDI, then use beat tracking on the audio and warp the MIDI to match its tempo and timing. We evaluate state-of-the-art automatic music transcription models on MulTTiPop and find substantial room for improvement, with the best model achieving 38% Onset F1. More details and sound examples of MulTTiPop are available at https://gclef-cmu.org/multtipop.


### SLORR: Simple and Efficient In-Training Low-Rank Regularization
**Authors**: David González-Martínez, Shiwei Liu

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08754v1](https://arxiv.org/pdf/2607.08754v1)

**Abstract**: Low-rank factorization is widely used to compress neural networks, but modern models are often not naturally amenable to aggressive factorization without significant accuracy loss. Existing training-time low-rank regularizers can improve compressibility, but they often require SVDs of large weight matrices, modify the model architecture (introducing additional trainable parameters), or rely on stateful cached quantities. To address these limitations, we introduce SLORR, a simple, stateless, and architecture-preserving framework for in-training low-rank regularization, instantiated with two main variants based on the Hoyer sparsity metric and the nuclear norm. SLORR directly regularizes the original weight matrices using GPU-friendly approximations for the forward and backward passes of the regularizers, for which we provide approximation guarantees. We first evaluate SLORR on ImageNet-1K across short-horizon continued training of ResNet-50, ViT-B/16, and ViT-L/16, and pretraining of ResNet-18, where SLORR induces compressibility while introducing less than 8% training overhead. We further evaluate SLORR-Hoyer in LLM pretraining at 135M and 560M scales: SLORR-trained compressed models preserve performance substantially better than unregularized models while adding less than 1% average training overhead.


## Generation
### Ideas Have Genomes: Benchmarking Scientific Lineage Reasoning and Lineage-Grounded Idea Generation
**Authors**: Yifan Zhou, Qihao Yang, Yan Li, Donggang Li, Xiru Hu, Hokin Deng, Ziyang Gong, Xuanyi Zhou, Huacan Wang, Xiangchao Yan, Wanghan Xu, Wenlong Zhang, Shaofeng Zhang, Yue Zhou, Yifan Yang, Zhihang Zhong, Xue Yang

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08758v1](https://arxiv.org/pdf/2607.08758v1)

**Abstract**: Scientific ideas rarely start from a blank page. They inherit mechanisms, repair known limitations, and recombine pieces of earlier work, much like biological genomes. Current benchmarks still say little about whether AI systems can follow this inheritance structure. We present IdeaGene-Bench (IG-Bench), a benchmark for scientific lineage reasoning and lineage-grounded idea generation. IG-Bench is organized around the IdeaGene framework: each paper or proposal is represented as a set of minimal, typed, evidence-grounded Idea Genome objects, and a GenomeDiff aligns these objects to record inheritance, mutation, loss, external import, and novel insertion under six operational evolutionary dynamics. The benchmark contains 1,961 golden lineage traces, 1,085 curated Idea Genome objects, and 920 pairwise GenomeDiff records across 10 scientific domains. It supports two evaluations. IG-Exam (42 task types, 1,029 instances) tests closed-form lineage reasoning across Idea Genome abstraction, inheritance tracing, evolutionary reasoning, and lineage verification. IG-Arena evaluates generation with a lineage-conditioned Population-Evolution Score(PES), asking whether a proposal can be inserted as a coherent descendant of a given lineage population: it should inherit the right Idea Genome objects, vary meaningfully from nearby work, and offer selection value for future research. Experiments on 14 LLM-based scientists expose a compositional bottleneck. The strongest system reaches only 27.3% exact accuracy on lineage reasoning, and structured lineage context reshuffles system rankings rather than helping every participant uniformly.


### ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation
**Authors**: Kaifeng Zhao, Mathis Petrovich, Haotian Zhang, Tingwu Wang, Siyu Tang, Davis Rempe

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08741v1](https://arxiv.org/pdf/2607.08741v1)

**Abstract**: Generating realistic 3D human motions in real-time within interactive applications is key for animation, simulation, and humanoid robotics. While recent offline motion generation approaches offer precise control via text and kinematic constraints, they lack the inference speed required for interactive settings. Conversely, existing online methods enable real-time synthesis but often sacrifice controllability or struggle with complex text semantics and long-horizon goals due to limited context windows. In this work, we introduce ARDY, a streaming generation framework that bridges this gap by enabling high-fidelity motion generation controllable via online text prompts and flexible kinematic constraints. ARDY employs a hybrid representation that combines explicit root features with a latent body embedding, balancing precise trajectory control with efficient generative learning. We propose a two-stage autoregressive transformer denoiser that features variable history context and supports conditioning on flexible, long-horizon kinematic constraints. By training on a large-scale motion capture dataset and being directly conditioned on text labels and kinematic constraints sampled from ground truth poses, ARDY natively learns controllable generation that supports online prompting and flexible long-horizon goals. Extensive evaluations on the HumanML3D benchmark and the large-scale, high-fidelity Bones Rigplay dataset demonstrate ARDY's high motion quality and constraint adherence, validating the efficacy of our key architectural decisions. Finally, we demonstrate the method's practical versatility through an interactive demo featuring dynamic text control, diverse keyframe pose constraints, path following, and interactive locomotion control via mouse and keyboard. Supplementary video results, code, and model releases can be found at https://research.nvidia.com/labs/sil/projects/ardy/.


### Deep Learning for Joint Narrowband Interference Cancellation and Soft Demodulation in OFDM Systems
**Authors**: Emmanouil Kavvousanos, Francky Catthoor, Vassilis Paliouras

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08717v1](https://arxiv.org/pdf/2607.08717v1)

**Abstract**: Narrowband interference (NBI) severely degrades orthogonal frequency-division multiplexing (OFDM) systems by corrupting subcarriers and rendering classical soft demodulation ineffective. Conventional compressed-sensing (CS) mitigation exhibits high sequential latency and leaves structured, non-Gaussian residuals that cause log-likelihood ratio (LLR) unreliability, decoder saturation, and severe error floors when employing classical Gaussian demappers. We resolve this pipeline mismatch using a unified deep learning framework for joint NBI cancellation and robust soft demodulation. First, NBI-CNet employs a physics-informed convolutional architecture to estimate NBI parameters and remove multi-tone interference in a single forward pass. Without requiring prior knowledge of the active interferer count, NBI-CNet reduces computational complexity by up to 60% ($N{=}2048, Q{=}64$) compared to the state-of-the-art EOMP-IDS algorithm. Second, LLR-CNet acts as a structural whitener by mapping non-Gaussian post-mitigation residuals onto well-calibrated soft metrics. Simulations demonstrate that this joint framework eliminates the error floors inherent to traditional baselines across dense grids. Under severe interference ($\text{SIR}{=}{-}10$ dB), the pipeline operates within a $0.2$ to $0.5$ dB SNR margin of the optimal iterative baseline at a target block error rate (BLER) of $10^{-4}$. Under mild interference ($\text{SIR}{=}10$ dB) with heavy spectral overlap ($Q{=}12$), where classical greedy algorithms erroneously subtract valid data components and corrupt the payload, NBI-CNet avoids signal-peak confusion to deliver a coding gain exceeding $3$ dB. Finally, the architecture circumvents the $2{\times}10^{-4}$ error floor triggered by interferer-estimation errors, while its scale-invariant design enables robust generalization across arbitrary FFT sizes without retraining.


### Remember When It Matters: Proactive Memory Agent for Long-Horizon Agents
**Authors**: Yifan Wu, Lizhu Zhang, Yuhang Zhou, Mingyi Wang, Bo Peng, Serena Li, Xiangjun Fan, Zhuokai Zhao

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08716v1](https://arxiv.org/pdf/2607.08716v1)

**Abstract**: In long-horizon tasks, decision-relevant state is often scattered across an expanding trajectory, while the action agent must surface it and act. As trajectories grow, task requirements, environment facts, prior attempts, diagnoses, and open subgoals can be buried in the context window or pushed beyond it, failing to influence decisions when needed. We call this failure mode "behavioral state decay". We study memory as an active intervention mechanism rather than passive retrieval. A separate memory agent runs alongside an unmodified action agent, updating a structured memory bank from the recent trajectory and deciding whether to inject a memory-grounded reminder or remain silent. The module is plug-and-play with frontier action agents and existing agent harnesses. Across Terminal-Bench 2.0 and $τ^2$-Bench, it improves pass@1 for both weaker and stronger action agents, with gains of +8.3 pp on Terminal-Bench and +6.8 pp on $τ^2$-Bench. Ablations show that selective intervention outperforms passive bank exposure, always-on injection, advisor-only guidance, and general retrieval. As an early step toward open-weight memory policies, we train Qwen3.5-27B on SETA using SFT and GRPO, improving validation reward and achieving partial transfer to Terminal-Bench.


### LTM: Large-scale Terrain Model for Wildfire-prone Landscapes
**Authors**: Xiao Fu, Yue Hu, Meida Chen, Peter Anthony Beerel, Barath Raghavan

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08711v1](https://arxiv.org/pdf/2607.08711v1)

**Abstract**: Accurate 3D terrain maps are essential for emergency response when assessing wildfire hazards. However, wildfire-prone regions often span vast areas where conventional reconstruction methods underperform. Airborne LiDAR systems provide high-resolution terrain data, but they are expensive and infrequently updated. Image-based methods offer a lower-cost alternative, but struggle due to sparse visual features and limited image overlap. We propose a multi-modal reconstruction framework leveraging outdated Digital Elevation Models (DEMs) as geometric priors for image-based 3D reconstruction. Our key innovation is physics-based pixel-pixel alignment between images and DEM data, dramatically reducing computational complexity by eliminating expensive feature matching procedures. To validate our approach, we developed a large-terrain simulator based on a real wildfire-prone area, generating realistic images enabling a comprehensive evaluation. Given posed images and legacy DEMs, our method produces high-fidelity depth maps while maintaining real-time performance. We find significant improvements in reconstruction accuracy and computational efficiency over existing techniques, offering a scalable solution for wildfire response.


### ProjAgent: Procedural Similarity Retrieval for Repository-Level Code Generation
**Authors**: QiHong Chen, Aaron Imani, Iftekhar Ahmed

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08691v1](https://arxiv.org/pdf/2607.08691v1)

**Abstract**: Repository-level code generation requires implementing target functions while accounting for complex cross-file dependencies and project-specific conventions. Existing retrieval methods predominantly rely on lexical, structural, or semantic similarity, often overlooking repository functions that implement similar procedural logic despite differing in identifiers or application domains. We propose ProjAgent, a repository-level code generation system that introduces procedural similarity as an explicit retrieval signal. ProjAgent decomposes the target function into intermediate reasoning steps and employs an agentic workflow to retrieve repository functions that exhibit similar procedural behavior at each step. The retrieved procedural context is integrated with conventional semantic retrieval to construct a richer repository context for code generation. ProjAgent further incorporates a conservative static-analysis feedback loop that iteratively repairs generated code using compiler and static-analysis feedback. Evaluated on REPOCOD, ProjAgent achieves 41.14% Pass@1, outperforming existing retrieval-based baselines. These results demonstrate that procedural similarity is an effective and previously unexplored retrieval dimension for repository-level code generation.


## VLA
### WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving
**Authors**: Xuerun Yan, Zhexi Lian, Nuoheng Zhang, Shiyu Fang, Haoran Wang, Chen Lv, Jia Hu, Binyang Song

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08375v1](https://arxiv.org/pdf/2607.08375v1)

**Abstract**: Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving. However, existing methods either lack comprehensive world cognition or suffer from fragmented world foresight, inherently confining these models to reactive driving. To address this limitation, we propose WCog-VLA, a novel dual-level World-Cognitive VLA framework that successfully bridges semantic world forecasting with generative world evolution to achieve proactive autonomous driving. At the semantic level, WCog-VLA unifies world cognition and reasoning by incorporating 3D spatial perception and injecting agent tokens to capture the world dynamics, while concurrently enabling Game-theoretic Chain-of-Thought (Game-CoT) reasoning. At the generative level, we introduce the Aligned Decoupled Diffusion Transformer (ADDT) as a powerful generative world model that synthesizes physically-plausible joint multi-agent trajectories. Through scene representation alignment, ADDT reduces the number of denoising steps required and thus significantly accelerates inference. To facilitate strategic reasoning, we further construct a large-scale dataset featuring 85k Game-CoT annotations. Extensive experiments on the NAVSIM benchmark demonstrate that WCog-VLA achieves a State-Of-The-Art (SOTA) PDMS score of 92.9.


### LEEVLA: Seeing What Matters in Latent Environment Evolution for Vision-Language-Action
**Authors**: Qi Lyu, Baicheng Liu, Xudong Wang, Jiahua Dong, Lianqing Liu, Zhi Han

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08182v1](https://arxiv.org/pdf/2607.08182v1)

**Abstract**: Vision-language-action (VLA) models aim to map multimodal inputs to robot actions. However, most existing approaches struggle to cover complex dynamic scenarios due to treating all visual tokens uniformly and reasoning with human-selected factors, which lack mechanisms to emphasize task-critical evidence and ignore underlying factors. To address this issue, we propose LEEVLA, a VLA architecture for seeing what matters in Latent Environment Evolution that explicitly guides the model toward informative regions while preserving the structured evolution of latent world representations. To identify salient and instruction-relevant regions, we introduce drift-guided dynamic prioritization (DGDP), which combines dynamic position prioritization (DPP) with semantic drift guidance (SDG) to guide the VLA agent where to attend during training. On top of this, we introduce structured feature flow generation (SFFG), which models how these prioritized features should evolve in latent space via prototype-to-periphery (P2P) prediction, and a mutual-neighborhood contrastive (MC) loss to maintain topological consistency among neighborhoods. Together, DGDP and SFFG form a task-aware "where-how" training framework. Extensive experiments on VLA benchmarks show that LEEVLA consistently outperforms prior methods, confirming that explicit task-evidence guidance and structured latent reasoning are both crucial for scalable VLA. Our code is available at https://github.com/LyuQi127/LEEVLA.


## Agent
### MPFlow: Learning Budgeted Max-Flow Optimization on the Lightning Network with Deep Graph Reinforcement Learning
**Authors**: Harrison Rush, Vincent Davis, Simone Antonelli, Vikash Singh, Jesse Shrader, Emanuele Rossi

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08703v1](https://arxiv.org/pdf/2607.08703v1)

**Abstract**: We address liquidity placement in the Bitcoin Lightning Network (LN): given a fixed budget, which channels should a node open to maximize its routing capacity? We cast this as a budget-constrained combinatorial optimization problem on graphs, selecting $k$ edge additions that maximize $s$--$t$ max-flow, a theory-grounded measure of routing capacity, and solve it with graph reinforcement learning. Our lightweight agent combines a message-passing policy network with proximal policy optimization (PPO) and action masking, and is trained under a hub-exclusion curriculum: the network's top hubs are removed from training subgraphs, forcing the policy to learn capacity-aware placement rather than hub attachment. In extensive experiments on real Lightning Network snapshots, our method consistently outperforms strong heuristic baselines on the max-flow objective across multiple seeds and unseen graphs. The agent has been deployed in production for peer recommendations, executing 4640 channel-open decisions that cumulatively allocate 267.3 BTC over $16 million across 30 managed nodes.


### SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets
**Authors**: Shilin Ou, Yifan Xu, Luyao Zhang

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08681v1](https://arxiv.org/pdf/2607.08681v1)

**Abstract**: As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trustworthiness. In decentralized energy markets, autonomous agents may improve market utility, but may also exploit invalid physical data, create artificial liquidity, and produce unstable governance decisions. Therefore, we propose SolarChain-Eval, a physics-constrained benchmark for evaluating trustworthy economic agents. It formulates market governance as a Gymnasium-compatible Markov Decision Process, where agents make hourly decisions. SolarChain-Eval evaluates each policy across multiple dimensions, including market utility, physical safety, slippage, action smoothness, spatial fairness, and auditability. To support agentic evaluation, SolarChain-Eval incorporates an LLM-based Planner/Auditor layer. The Planner defines episode-level action bounds and audit rules, while the Auditor reviews and revises high-risk actions. All interventions are recorded through structured logs, including trigger signals, proposed actions, revised actions, and audit rationales. Experiments with static, random, myopic, RL, and RL+LLM policies reveal a clear utility-safety trade-off. RL agents improve market utility but can still produce unsafe behavior. When the physics penalty is removed, reward-maximizing agents exploit invalid generation and increase artificial liquidity. The LLM Planner/Auditor improves auditability and mitigates selected risks, but it cannot fully compensate for a misspecified reward function. These results indicate that trustworthy agentic AI evaluation requires both physical constraints and transparent intervention traces. We release data and code as open access on GitHub for replicability.


### WebSwarm: Recursive Multi-Agent Orchestration for Deep-and-Wide Web Search
**Authors**: Xiaoshuai Song, Liancheng Zhang, Kangzhi Zhao, Yutao Zhu, Zhongyuan Wang, Guanting Dong, Jinghan Yang, Han Li, Kun Gai, Ji-Rong Wen, Zhicheng Dou

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08662v1](https://arxiv.org/pdf/2607.08662v1)

**Abstract**: Large language model (LLM)-based web search agents are transforming information seeking from simple factoid question answering into complex, deep-and-wide search and research-oriented tasks. A single ReAct-style agent is constrained by one long trajectory and limited context, making it difficult to handle depth and coverage simultaneously. Existing multi-agent systems improve search coverage through parallel execution and aggregation, but still exhibit clear limitations in recursive depth, collaboration adaptability, and evidence-grounded expansion. We propose WebSwarm, a progressive recursive delegation framework that jointly constructs task decomposition, recursive expansion, and agent collaboration during inference. WebSwarm dynamically instantiates agentic search nodes, each coupling a local objective with a search mode that specifies how the node should organize search and collaboration. Each node can either solve its objective itself or further delegate child nodes; after solving, it returns evidence and results upward, enabling parent nodes to further expand, revise, or aggregate the search process. To guide this process, WebSwarm first probes how task-relevant information is organized on the web to ground subsequent node expansion, and reuses process-level experience across homogeneous sibling nodes. Experiments on BrowseComp-Plus, WideSearch, DeepWideSearch, and GISA show that WebSwarm consistently outperforms single-agent and multi-agent baselines on deep, wide, and interleaved deep-and-wide tasks. Further analyses of ablation, task difficulty, web tool efficiency, and model generalization explain WebSwarm's effectiveness and provide insights for multi-agent search systems.


### Formal Mechanisms for Market Stability in Self-Interested Agent Societies: A Marketplace Simulation Study
**Authors**: Eugene Ng Yi Sheng, Bingquan Shen

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08652v1](https://arxiv.org/pdf/2607.08652v1)

**Abstract**: Self-interested agents, left unconstrained, tend toward defection in repeated social dilemmas, causing cooperative gains from trade to collapse. This paper investigates what formal mechanisms, layered on top of unrestricted communication, are sufficient for a society of such agents to maintain market stability, and how resilient those mechanisms are to adversarial attack. We instantiate the research question as a multi-agent marketplace simulation where 18 LLM agents (DeepSeek-V3) with complementary production specialties must trade within a constrained social network to obtain utility. We conduct two experimental phases: (1) a mechanism comparison across eight conditions under progressive troll injection over 200 rounds, identifying Mediation as the top-performing mechanism; and (2) adversarial red-teaming of Mediation using iteratively prompt-optimised LLM-driven trolls, finding that the best attack (v6) reduces honest-agent utility by 13.3% but cannot collapse the market. Mediation enables recovery even under sustained adversarial pressure. We define adversarial robustness as a mechanism's ability to sustain positive honest-agent utility under optimised attack, and find that Mediation is robust: it can be bent but not broken.


### Multi-Modal, Multi-Environment Machine Teaching for Robust Reward Learning
**Authors**: Ali Larian, Qian Lin, Chang Zong Wu, Daniel S. Brown

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08647v1](https://arxiv.org/pdf/2607.08647v1)

**Abstract**: As autonomous agents are increasingly deployed across diverse operational contexts, aligning their behavior with human intent demands reward functions that remain robust to such changes rather than overfitting to any single environment. Inverse reinforcement learning (IRL) provides a principled way to infer such objectives from human feedback. However, existing analyses of optimal teaching approaches for IRL focus on single-environment, demonstration-only settings, leaving underexplored how heterogeneous feedback modalities and environment dynamics jointly constrain reward functions that generalize across multiple environments. Because demonstrations in one MDP entangle reward information with that environments specific structure, the resulting rewards frequently fail to generalize when the agent is deployed in a new setting. We first analyze how different feedback modalities constrain rewards, showing that, in the unlimited-data regime, comparisons impose strictly stronger global constraints than other modalities. Beyond this theoretical analysis, we introduce a hierarchical machine teaching algorithm for reward learning that operates across multiple MDPs. The algorithm first greedily selects informative environments that expose complementary reward constraints, then strategically queries low-cost feedback within those environments. Empirically, our method achieves substantially lower regret and stronger generalization to held-out environments than uniform teaching baselines under identical feedback budgets, demonstrating the importance of multi-environment, multi-modal teaching for learning dynamics-robust reward functions.


### SMetric: Rethink LLM Scheduling for Serving Agents with Balanced Session-centric Scheduling
**Authors**: Jiahao Wang, Kaizhan Lin, Kaixi Zhang, Jinbo Han, Xingda Wei, Sijie Shen, Chenguang Fang, Wenyuan Yu, Rong Chen, Haibo Chen

**Published Date**: 2026-07-09

**Updated Date**: 2026-07-09

**PDF Url**: [2607.08565v1](https://arxiv.org/pdf/2607.08565v1)

**Abstract**: LLM scheduling is critical to serving, yet it remains unclear how well existing designs fit agentic serving--with LLM requests issued by agents instead of humans. This shifts the workload in two ways: (1) agents act only on complete responses, making the cluster's tokens per second (TPS) the primary goal and relaxing--not eliminating--per-token latency requirements; and (2) requests share much of their KV\$-reuse exceeds 80% of request tokens in a production trace from BAILIAN, versus 54-62% in chat.
  This paper first contributes a systematic study of request scheduling for agents on two real-world traces. We find that to increase KV\$ reuse, existing schedulers overly prioritize routing requests to instances caching their KV\$, overloading a few while leaving the rest idle, capping TPS. We thus present two key insights: (1) load balance need not sacrifice all KV\$ reuse, thanks to the global-tier KV\$ store and (2) by utilizing the workload's intra-session locality, balancing a small fraction of requests--the first request in each agent session--suffices to balance the cluster without sacrificing most KV\$ reuse on local instances.
  SMETRIC realizes these insights with balanced session-centric scheduling: it routes each session's first request purely for load balance and its follow-up requests in a cache-aware manner, preserving load balance and local reuse while keeping demand on the global tier low. Using the session turn information as the scheduling metric is deliberate: it is derived efficiently and accurately from the user inputs alone, so the scheduler stays clean and stateless. SMETRIC improves cluster TPS by 10-16% under prefill-decode colocation with a global store and prefill TPS by 2-34% under disaggregation over state-of-the-art schedulers, also with a better per-token latency.


