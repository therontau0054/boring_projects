# Abstracts of Papers

## World Model
### Reasoning LLM Improves Speaker Recognition in Long-form TV Dramas
**Authors**: Yuxuan Li, Lingxi Xie, Xinyue Huo, Jihao Qiu, Jiacheng Shao, Pengfei Chen, Jiannan Ge, Kaiwen Duan, Qi Tian

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02504v1](https://arxiv.org/pdf/2607.02504v1)

**Abstract**: Long-form TV dramas present a formidable challenge for comprehensive video understanding, where deciphering complex storyline often relies on \textbf{speaker recognition}, the task of accurately attributing each spoken utterance to its respective character. In this paper, we advance this field through two primary contributions. (1) We introduce \textbf{DramaSR-532K}, a large-scale benchmark comprising 532K annotated dialogue lines across more than 900 unique characters, necessitating the integration of auditory, linguistic, and visual cues for speaker recognition. (2) We propose \textbf{DramaSR-LRM}, a robust approach built upon a large reasoning model (LRM). DramaSR-LRM is designed to autonomously aggregate contextual evidence via multimodal tool-use, synthesizing diverse inputs to achieve high-fidelity attribution. Experimental results demonstrate that DramaSR-LRM significantly outperforms existing baselines, particularly on short utterances where acoustic biometrics are inherently unreliable. \textit{All the data and code will be made publicly available at the project page: https://www.github.com/198808xc/DramaSR-LRM.}


### VT-WAM: Visual-Tactile World Action Model for Contact-Rich Manipulation
**Authors**: Shuai Tian, Yupeng Zheng, Yuhang Zheng, Songen Gu, Yujie Zang, Yuxing Qin, Weize Li, Haoran Li, Wenchao Ding, Dongbin Zhao

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02503v1](https://arxiv.org/pdf/2607.02503v1)

**Abstract**: Contact-rich manipulation requires policies to react to local deformation, pressure, slip, and friction, yet these cues are temporally sparse and often invisible in visual observations. Existing visual-tactile policies usually feed tactile observations directly into action prediction, but rarely model tactile deformation dynamics during action generation. In this paper, we introduce VT-WAM, a Visual-Tactile World Action Model that jointly learns future visual prediction, tactile deformation prediction, and action prediction within a unified flow matching framework. In particular, VT-WAM introduces (1) Asymmetric Mixture-of-Transformers (MoT) attention to bridge a first-frame visual anchor with temporal tactile dynamics, and (2) contact-gated Action-Visual-Tactile Attention Guidance (AVTAG) to encourage action queries to rely on tactile evidence during contact phases. Across six real-world contact-rich manipulation tasks, VT-WAM achieves a 71.67% average success rate, outperforming Fast-WAM by 26.67% and OmniVTLA by 35.84%. Ablations demonstrate that modeling tactile deformation dynamics and guiding contact-phase tactile attention are both important for contact-rich tasks. Project website: https://vt-wam.github.io/.


### Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots
**Authors**: Ling Xu, Chuyu Han, Borui Li, Hao Wu, Shiqi Jiang, Ting Cao, Chuanyou Li, Sheng Zhong, Shuai Wang

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02501v1](https://arxiv.org/pdf/2607.02501v1)

**Abstract**: Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied.cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied.cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied.cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied.cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.


### Learning Agile Intruder Interception using Differentiable Quadrotor Dynamics
**Authors**: Michael Anoruo, Xiaoyu Tian, Abhishek Rathod, Timothy Naudet, Thomas Canchola, Eric Sturzinger, Kshitij Goel, Wennie Tabib

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02472v1](https://arxiv.org/pdf/2607.02472v1)

**Abstract**: This paper presents a methodology for learning a control policy to intercept an intruder using the 3D direction unit vector to the intruder and the interceptor state. Prior deep reinforcement learning approaches assume either relative position or distance to the intruder is available, but this information is not readily accessible in real-world applications that employ passive, monocular camera sensors. Instead, we propose a solution that leverages an analytical policy gradient method using differentiable quadrotor dynamics to learn agile interception at speeds up to 10 m/s. The proposed approach outperforms baseline methods that utilize simplified point mass dynamics by an average of 30%.


### Human Capital, Not Model Benchmarks, Predicts Hybrid Intelligence in Forecasting
**Authors**: Vivienne Ming

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02467v1](https://arxiv.org/pdf/2607.02467v1)

**Abstract**: Whether pairing people with AI helps or hurts is usually reported as a single average effect. Using a real-money prediction market (Polymarket) as an objective, externally resolved benchmark, this pilot shows that the value of human-AI collaboration depends on a specific, measurable form of human capital. Analyzed at the level of the individual forecaster, hybrid performance is trimodal: most people either deferred to the model (matching it) or used it to rubber-stamp a prior guess (performing worse than the model alone), while a minority engaged in genuine complementary reasoning and reached accuracy matching or even exceeding (i.e., lower error than) the market itself. Collaborative traits (perspective-taking, intellectual humility, and curiosity) rather than raw cognitive ability or model benchmarks, distinguished who reached that mode. The results are preliminary but statistically robust, and motivate a pre-registered replication now in preparation.


### Neuron-Aware Data Selection for Annotation-Free LLM Self-Distillation
**Authors**: Zhuowei Chen, Xiang Lorraine Li

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02460v1](https://arxiv.org/pdf/2607.02460v1)

**Abstract**: Post-training large language models (LLMs) without real-world interaction feedback or human-labeled supervision remains challenging, particularly in specialized domains where expert annotations are costly to obtain. Recent annotation-free self-evolution methods address this by using the model's own outputs as supervision signals, constructing a teacher via additional context and aggregating predictions across multiple rollouts through majority voting to produce pseudo-labels. However, these approaches are not without drawbacks: SFT- and GRPO-based variants suffer out-of-domain performance degradation, while reward-based on-policy RL inflates calibration error. In this paper, we propose Neuron On-Policy Self-Distillation (Neuron-OPSD), a data-centric framework for annotation-free self-distillation that leverages internal neuron activations to guide both training-data selection and teacher context construction. The model is then trained via on-policy distillation from the teacher distribution, requiring no ground-truth labels at any stage. Across specialized-domain benchmarks, Neuron-OPSD improves in-domain task performance while preserving cross-domain generalization and mitigating calibration collapse over prior annotation-free baselines. This framework is particularly relevant to settings where online interaction or external supervision is costly or infeasible, and is conceptually distinct from offline RL approaches that rely on logged, reward-labeled trajectories.


## Generation
### WorldSample: Closed-loop Real-robot RL with World Modelling
**Authors**: Yuquan Xue, Le Xu, Zeyi Liu, Zhenyu Wu, Zhengyi Gu, Xinyang Song, Bofang Jia, Ziwei Wang

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02431v1](https://arxiv.org/pdf/2607.02431v1)

**Abstract**: Reinforcement learning (RL) can overcome the demonstration-coverage limitation of imitation learning (IL) by allowing robots to improve through trial-and-error interaction beyond the states observed in demonstrations. However, deploying RL on real robots remains constrained by high interaction costs, since each physical rollout is costly and reflects only one realized action-outcome path. To address this challenge, we propose WorldSample, a physically grounded data augmentation framework for real-robot RL that closes a real-synthetic loop between physical rollouts, world-model generation, and policy improvement. Grounded on real rollouts, WorldSample generates high-fidelity synthetic transitions through a post-trained world model, which greatly lowers the visual hallucination. Specifically, rather than simply using these transitions as real-world experience, WorldSample introduces Policy-Paced Learning (PPL) to regulate the training process through sample selection and scheduling, balancing useful augmentation against value overestimation and mitigating the hallucination-induced noise. Experiments on robot manipulation tasks involving contact-rich and precise tasks show that WorldSample improves policy success rate by 28% while reducing training steps by 59% compared with baselines. Furthermore, WorldSample improves world model visual fidelity by 19.4dB in PSNR and 0.47 in SSIM over demonstration-only post-training, validating the effectiveness of the real-synthetic loop for both policy and world model performance.


### LIME: Learning Intent-aware Camera Motion from Egocentric Video
**Authors**: Boyang Sun, Jiajie Li, Yung-Hsu Yang, Chenyangguang Zhang, Tim Engelbracht, Sunghwan Hong, Cesar Cadena, Marc Pollefeys, Hermann Blum

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02417v1](https://arxiv.org/pdf/2607.02417v1)

**Abstract**: Autonomous robots often need to move their camera before they can act: to inspect an object, reveal an occluded region, or obtain a view that responds to a user's intent. While vision-language navigation translates instructions to base motion and vision-language-action policies map instructions to manipulation actions, language-conditioned camera motion remains comparatively underexplored as a first-class action. We formulate language-conditioned camera motion generation: given a current RGB observation and a free-form natural-language intent, predict a relative target camera pose for the next observation. This task is inherently non-trivial: viewpoint changes are driven by latent perceptual intentions, and a valid motion may operate at different semantic granularity, from entering a room to looking around a corner, inspecting a visible object, or revealing an occluded detail. To model this structure, we mine multi-intention camera-motion supervision from egocentric video, pairing plausible intents and observation-gain descriptions with relative SE(3) target poses. We propose LIME, a vision-language camera-motion generator that combines an auto-regressive observation-gain output with a continuous flow-matching pose head. This design lets the model jointly predict what the next view should reveal while representing multi-hypothesis target views. Across experiments and downstream robotic tasks, we show that LIME can learn to actively choose camera poses from passive human video, turning ordinary egocentric recordings into supervision for intent-aware active perception.


### Text-Driven 3D Indoor Scene Synthesis in Non-Manhattan Environments
**Authors**: Xianhui Meng, Zirui Song, Yuchen Zhang, Li Zhang, Yongxuan Lv, Xiuying Chen, Kun Wang, Yan Luo, Kai Chen, Hangjun Ye, Long Chen, Jun Liu, Xiaoshuai Hao

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02407v1](https://arxiv.org/pdf/2607.02407v1)

**Abstract**: Large Language Models (LLMs) have demonstrated remarkable capabilities in 3D indoor synthesis for Manhattan environments. However, existing methods often fail to capture plausible object layout patterns in non-Manhattan settings, primarily because they struggle to model non-orthogonal spatial relationships, leading to high geometric violations and low physical fidelity. To address this challenge, we propose SPG-Layout, a novel text-driven framework designed to generate physically plausible indoor scenes within complex non-Manhattan environments. Specifically, we first utilize statistical priors of object distributions to guide the training process, enhancing environmental understanding and fidelity. Furthermore, mirroring human design workflows, we adopt a hierarchical layout strategy that prioritizes the placement of large objects, thereby substantially minimizing layout violations. By synergizing these components, SPG-Layout achieves a balanced optimization of semantic realism and physical plausibility. To evaluate performance in these complex settings, we constructed a new benchmark comprising 500 diverse non-Manhattan environments. Extensive experiments demonstrate that SPG-Layout consistently and significantly outperforms existing methods across both Manhattan and non-Manhattan environments. The code will be publicly released.


### WattGPU: Predicting Inference Power and Latency on Unseen GPUs and LLMs
**Authors**: Mauricio Fadel Argerich, Jonathan Fürst, Marta Patiño-Martínez

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02391v1](https://arxiv.org/pdf/2607.02391v1)

**Abstract**: Large Language Model (LLM) inference workloads are a rapidly growing contributor to data center energy consumption. Optimizing these deployments requires matching specific LLMs to the most efficient GPUs, but operators currently lack the tools to do so without exhaustively profiling each combination. While some predictive models exist, they still require profiling data and struggle to generalize to hardware unseen during training. To address this, we introduce \textit{WattGPU}, featuring two predictive models for mean GPU power draw and Inter-Token Latency (ITL). Our approach leverages only publicly available LLM metadata and GPU specifications, eliminating the need for hardware access or profiling while enabling generalization to unseen NVIDIA server-grade GPUs and LLMs. We evaluate our models using rigorous leave-one-GPU-out and leave-one-LLM-out cross-validation on a dataset of 42 open-source LLMs (0.1B--27B parameters) and 8 GPUs under both offline and server scenarios. The mean power draw model achieves a median absolute percentage error of $\leq3.4\%$ for offline and $\leq13.5\%$ for server scenarios on unseen GPUs, while the latency model achieves $\leq8.5\%$ in server mode, both maintaining strong GPU ranking correlations for server scenarios (Kendall $τ\geq0.76$). Compared to standard physically grounded baselines -- Load-Scaled Thermal Design Power (TDP) for power draw and roofline for latency -- our models reduce median absolute percentage error by approximately 4$\times$ on unseen LLM-GPU combinations for server scenarios or approximately 2$\times$ for completely unseen GPUs. WattGPU's data and code are publicly available at https://github.com/maufadel/wattgpu.


### DecompRL: Solving Harder Problems by Learning Modular Code Generation
**Authors**: Juliette Decugis, Fabian Gloeckle, Francis Bach, Taco Cohen, Gabriel Synnaeve

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02390v1](https://arxiv.org/pdf/2607.02390v1)

**Abstract**: How can Large Language Models (LLMs) solve problems they currently cannot? Repeated sampling scales test-time compute but GPU cost grows linearly with attempts, while reinforcement learning (RL) with verifiable rewards improves single-attempt accuracy at the expense of sample diversity. Both strategies ultimately fail when the base policy has near-zero probability of producing a correct solution: no amount of sampling or gradient signal can overcome a search space that is simply too large. We take a different approach: rather than sampling harder, we make the task easier by decomposing problems into smaller, independently solvable sub-functions whose implementations can be recombined. Since off-the-shelf models are not trained for this modular generation, we introduce DecompRL, an RL algorithm that explicitly learns to decompose and implement hierarchical code structures. Recombining $k$ implementations of $n$ modules yields up to $k^{n}$ candidate solutions, shifting the bottleneck from GPU inference to cheap CPU evaluation and cutting GPU token cost by $\sim$50$\times$. On LiveCodeBench and CodeContests (Qwen~2.5~7B, Code World Model~32B), DecompRL outperforms standard and diversity-optimized RL baselines beyond $10^5$ tokens per problem, solving problems that standard generation cannot reach.


### Understanding Agent-Based Patching of Compiler Missed Optimizations
**Authors**: Batu Guan, Zirui Wang, Shaohua Li

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02370v1](https://arxiv.org/pdf/2607.02370v1)

**Abstract**: Compiler missed optimizations refer to cases in which compilers failed to optimize certain code. It takes many compiler developers' efforts to implement or patch such missed optimizations. In this paper, we present a systematic study of how well agents patch compiler missed optimizations. We identify a significant challenge that patching a missed optimization requires more than just fixing the reported case, and instead requires generalizing to similar cases. We construct a benchmark of real-world LLVM missed optimization issues and compare agent-generated patches with patches from developers in terms of optimization scope. Our results show that coding agents often optimize the given examples, but many generated patches either cover only part of the developer-intended scope or partially overlap with it; in some cases, they further generalize beyond the reference patch. We further introduce historical-knowledge augmentation techniques that leverage prior LLVM optimization pull requests through retrieval and distillation, showing that they improve developer-aligned generalization and yield practical benefits when applied to real-world IR.


## VLA
### Fast Enough to Act: Spatio-Temporal Visual Token Merging for Low-Latency Robotic VLMs and VLAs
**Authors**: Junzhou Chen, Jindong Wang, Gang Zhou

**Published Date**: 2026-06-28

**Updated Date**: 2026-06-28

**PDF Url**: [2606.29350v1](https://arxiv.org/pdf/2606.29350v1)

**Abstract**: Vision-language models and vision-language action models endow the robot with unprecedented capabilities. However, the input of video and high-resolution images yields a massive number of visual tokens, leading to extremely high inference latency and severely hindering the robot's real-time control. To break through this computational bottleneck, we propose ST-Merge, a plug-and-play, training-free framework that efficiently fuses redundant tokens directly during the visual encoding phase. By explicitly constructing 3D spatiotemporal coordinates, it employs a multi-queue parallel matching and weighted aggregation mechanism to achieve efficient and geometrically consistent fusion of redundant tokens across frames. In addition, we introduce a post-merge positional correction mechanism that effectively eliminates spatial deviation caused by merging by dynamically re-evaluating the rotational position code of the weighted centroid of the vision token, thereby ensuring the high-precision spatial awareness required for dexterous operation. In the Video Question Answering task on the mainstream VLM, Qwen2.5-VL, ST-Merge achieves a 2$\times$ inference speedup with only a tiny 1\% loss in precision. When deployed on the $π_{0.5}$ VLA policy, ST-Merge achieves an 8.3$\times$ speedup at 1024 $\times$ 1024 resolution and matches the baseline success rate at this high-resolution setting. At lower resolutions, it introduces a small drop in accuracy.


### SurgVLA-Bench: Towards Evaluating Vision-Language-Action Models for Laparoscopic Surgical Robotics
**Authors**: Jiashuo Sun, Yue He, Wenxuan Liu, Tao Mao, Jiazheng Wang, Xiang Chen, Min Liu

**Published Date**: 2026-06-28

**Updated Date**: 2026-06-28

**PDF Url**: [2606.29247v1](https://arxiv.org/pdf/2606.29247v1)

**Abstract**: Vision-Language-Action (VLA) models represent a promising direction for embodied intelligence in surgical robotics. Despite the prevalence of VLA benchmarks for general robotics, standardized evaluation platforms specifically designed for surgical contexts remain absent. To address this limitation, we present SurgVLA-Bench, the first comprehensive benchmark for evaluating VLA models in laparoscopic surgical robotics. Leveraging the SurRoL simulation platform, we construct a hierarchical task taxonomy ranging from atomic actions to complete surgical procedures, complemented by a multi-dimensional evaluation framework assessing action accuracy and semantic consistency. We then systematically evaluate two representative paradigms, including autoregressive models such as OpenVLA, and flow matching models such as $π_{0}$, $π_{0.5}$, and SmolVLA. Our experiments show that autoregressive models tend to excel in semantic understanding, while flow matching models often achieve higher task precision but may face generalization trade-offs. However, even the best-performing models remain far from satisfactory, as the constrained endoscopic field of view, restricted viewing angles, and frequent occlusions persist as fundamental physical bottlenecks. The code and data are available at https://github.com/VCL-HNU/SurgVLA


### Behavior Uncloning: Distilling Mode Redirection into Policy Weights without Inference-Time Steering
**Authors**: Hao Wang, Jiuzhou Lei, Dayou Li, Bangya Liu, Minghui Zheng, Manling Li, Ruohan Zhang, Zhiwen Fan

**Published Date**: 2026-06-28

**Updated Date**: 2026-06-28

**PDF Url**: [2606.29201v1](https://arxiv.org/pdf/2606.29201v1)

**Abstract**: Behavior-cloned policies often learn multiple behavior modes from demonstration datasets, including modes that are unsafe or otherwise undesired at deployment. For example, a policy trained on diverse handover demonstrations may learn to pass a knife blade-first. Standard remedies such as data curation and inference-time steering either require access to the original demonstrations for full retraining or add substantial inference-time overhead. To address this gap, we propose MoRE(Mode Redirection), which redirects policy rollouts toward desired behavior modes through a short "uncloning" step. Specifically, MoRE distills the redirection signal from a temporary mode classifier into the policy weights to steer behavior. A retain loss balances this edit by preserving desired-mode competence, allowing the standalone policy to suppress unwanted modes with zero inference-time overhead. Across eight simulated and real-world tasks, MoRE improves the average deployment success rate (SR) by 44 percentage points over the original mixed-mode policy. Among all compared adaptation and steering baselines, MoRE achieves the strongest SR and approaches the filtered-data retraining reference, while preserving task competence and inference speed. MoRE also generalizes across robot policy backbones, including Diffusion Policy and the Pi0.5 VLA, diverse task categories, and real-world deployments.


### X-Mind: Efficient Visual Chain-of-Thought via Predictive World Model for End-to-End Driving
**Authors**: Bohao Zhao, Chengrui Wei, Guangfeng Jiang, Ruixin Liu, Xuejie Lv, Liu Liang, Sutao Deng, Xiuyang Fan, Pengkun Zheng, Jinyun Zhou, Rui Guo, Hanpeng Liu, Yutong Zheng, Yi Guo, Xinlong Zheng, Qingyu Luo, Zhuangzhuang Ding, Yu Zhang, Hang Zhang, Xianming Liu

**Published Date**: 2026-06-27

**Updated Date**: 2026-06-27

**PDF Url**: [2606.28758v1](https://arxiv.org/pdf/2606.28758v1)

**Abstract**: Predicting future states is essential for autonomous agents, yet current Vision-Language-Action (VLA) models fundamentally lack this capability, relying instead on reactive perception-action mapping. While integrating Predictive World Models (PWMs) addresses this gap, existing approaches either incur prohibitive cascaded latency or act as shallow terminal tasks that fail to deeply embed forward-looking reasoning. To endow VLA models with this reasoning capability, we propose X-Mind. Rather than treating PWMs as an external auxiliary module, this framework internalizes them as the Visual Chain-of-Thought (Visual CoT). By enforcing a world rollout prior to action, the model is constrained to imagine future evolution first, yielding a driving policy that is robustly grounded in environmental dynamics and aware of the future consequences its actions will unfold. The challenge here is efficiency, and we tackle it on two fronts. First, we introduce a compact representation of visual thinking: an abstract sketch that fuses a Bird's-Eye-View (BEV) layout with abstract driving priors (e.g., navigation intents and traffic rules). Rather than rolling out dense future frames, the model reasons over this sketch as a mental canvas; aided by a Deep Compression Autoencoder (DC-AE), a 12-frame future rollout is reduced to merely 96 tokens, alleviating the long-context computational bottleneck. Second, to accelerate generation further, we propose a recurrent block diffusion scheme that unrolls the denoising steps across the layers of the large drive model, folding iterative refinement into the backbone's one forward pass. Trained and validated on large-scale real-world data, X-Mind achieves competitive end-to-end driving performance, which makes it a highly practical, low-latency solution that successfully deploys large-scale cognitive reasoning directly onto resource-constrained vehicle platforms.


### HAT-4D: Lifting Monocular Video for 4D Multi-Object Interactions via Human-Agent Collaboration
**Authors**: Jiaxin Li, Yuxiang Wu, Zhenkai Zhang, Xinrui Shi, Haoyuan Wang, Yichen Zhao, Su Linxiang, Chenyang Yu, Mingyu Zhang, Yifan Ding, Boran Wen, Li Zhang, Ruiyang Liu, Yong-Lu Li

**Published Date**: 2026-06-26

**Updated Date**: 2026-06-26

**PDF Url**: [2606.28215v1](https://arxiv.org/pdf/2606.28215v1)

**Abstract**: Extracting dynamic 4D object interactions from massive, in-the-wild monocular videos offers a highly efficient data collection pathway for scaling Embodied AI and training VLAs. However, existing monocular 4D reconstruction methods primarily focus on isolated objects, often failing under the severe occlusions and complex dynamics inherent in multi-object interactions. To bridge this gap, we propose HAT-4D, the first agentic framework designed to reconstruct the 3D geometry, temporal dynamics, and physical interactions of multiple objects from a single video. By integrating VLMs with a multi-level human-in-the-loop feedback mechanism, HAT-4D efficiently resolves depth ambiguities and interaction-induced occlusions during 3D generation and 4D propagation, yielding physically plausible assets without relying on expensive multicamera rigs. As a scalable data engine, HAT-4D facilitates the creation of MVOIK-4D, an open-world benchmark for monocular 4D interaction reconstruction, accompanied by a novel multi-dimensional evaluation protocol focused on physical plausibility and temporal consistency. Extensive experiments demonstrate that HAT-4D achieves SOTA performance on most evaluation metrics, while maintaining competitive semantic alignment. Ablation studies show that introducing a small amount of human feedback improves interaction reconstruction. Moreover, the data produced by HAT-4D effectively improves baseline performance when used for fine-tuning. Our data and code are available at https://lijiaxin0111.github.io/HAT4D/


### S$^2$-VLA: State-Space Guided Vision-Language-Action Models for Long-Horizon Manipulation
**Authors**: Zhipeng Xie, Zongyi Han, Xiangyi Wei, Shiliang Sun, Yang Li, Jing Zhao

**Published Date**: 2026-06-26

**Updated Date**: 2026-06-26

**PDF Url**: [2606.27872v1](https://arxiv.org/pdf/2606.27872v1)

**Abstract**: Vision-Language-Action (VLA) models have demonstrated strong capabilities in robotic manipulation, but their performance degrades significantly in long-horizon tasks due to cumulative error propagation. This limitation largely arises from static feature fusion mechanisms that rely on fixed weights to combine visual, language, and action representations, preventing the model from adapting to different phases of task execution. To address this limitation, we propose S$^2$-VLA, a framework that introduces a State-Space Guided Adaptive Attention (SSGAA) mechanism. SSGAA maintains a belief state that tracks task progression and generates dynamic gating weights to adaptively fuse information from three complementary sources visual features for spatial perception, task intents for high-level task planning, and temporal action sequences for execution consistency. This adaptive fusion allows the model to shift its focus throughout task execution, aligning with the evolving requirements of different task stages. Despite its compact 2B parameter size, S$^2$-VLA consistently outperforms larger 7B-scale models and achieves state-of-the-art performance on long-horizon manipulation benchmarks, including LIBERO and SimplerEnv. highlighting the importance of adaptive feature fusion for long-horizon robotic manipulation.


## Agent
### Hardware-Enforced Semantic Coordination for Safety-Critical Real-Time Autonomous Systems
**Authors**: Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02376v1](https://arxiv.org/pdf/2607.02376v1)

**Abstract**: Recent advances in agentic AI are producing increasingly complex autonomous systems that integrate large language models, world models, optimization engines, specialized neural architectures, autonomous platforms, and human operators. While much current research focuses on improving reasoning capabilities, safety-critical real-time deployment also requires bounded and verifiable coordination among heterogeneous components operating concurrently under uncertainty. Software-mediated coordination presents fundamental limitations in domains where bounded latency, deterministic coordination, and enforceable safety guarantees are essential.
  Hence, we propose a hardware-enforced semantic coordination architecture in which selected coordination semantics are implemented directly at the hardware level via field-programmable gate arrays (FPGAs). The approach builds on the Topic-Based Communication Space Petri Net (TB-CSPN) framework, which separates semantic reasoning from interaction management.
  In this approach, selected TB-CSPN coordination mechanisms are mapped onto FPGA primitives, creating a hardware-native semantic coordination layer. Focus is not on acceleration, but on enforcing temporal synchronization, semantic gating, authorization constraints, and bounded coordination behavior directly in hardware. Semantic reasoning remains adaptive and software-driven, while embedded coordination semantics become deterministic.


### SkillFuzz: Fuzzing Skill Composition for Implicit Intents Discovery in Open Skill Marketplaces
**Authors**: Jinwei Hu, Yi Dong, Youcheng Sun, Xiaowei Huang

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02345v1](https://arxiv.org/pdf/2607.02345v1)

**Abstract**: Large Language Model (LLM)-based agents increasingly automate software engineering tasks through reusable skills, natural-language instruction documents that guide planning and execution. Open skill marketplaces enable users to assemble agents by co-activating community-contributed skills, but marketplace operators typically audit skills in isolation. As a result, individually benign skills may interact to redirect an agent toward unintended objectives, which we term implicit intents. Detecting such intents is challenging because the effect emerges only through skill composition, execution environments are often unavailable at admission time, and the space of possible co-activations grows exponentially with marketplace size. In this paper, we formulate implicit-intent discovery as a fuzzing problem over skill compositions, where skill compositions are the unit under test, planning artifacts expose agent intent before execution, and deviations from a skill-free baseline serve as a differential oracle. Based on this formulation, we propose skillfuzz, the first execution-free testing approach that extracts structured skill contracts and uses contract-guided Monte Carlo Tree Search to prioritize potentially conflicting compositions. Across representative skill-marketplace workloads, skillfuzz discovers over 1,000 distinct implicit intents under a fixed query budget, confirms more than 80% of the highest-risk flagged compositions during execution-time validation, and identifies substantially more high-severity implicit intents than alternative search strategies while exploring only a fraction of the pairwise interaction space they require.


### Grounded autonomous research: a fault-tolerant LLM pipeline from corpus to manuscript in frontier computational physics
**Authors**: Haonan Huang

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02329v1](https://arxiv.org/pdf/2607.02329v1)

**Abstract**: Autonomous-research agents have demonstrated end-to-end LLM automation in machine-learning sandboxes where execution provides calibration. Frontier physical science differs categorically: physical reasoning underlies every methodology choice, toolchains are often underdocumented, and calibration must come from external literature anchors - which unscaffolded agents cite but do not confront, hallucinating plausible, unverifiable results from internal priors. We present a pipeline that runs end-to-end from a corpus of 11,083 recent condensed-matter physics arXiv papers to a publication-grade manuscript with three substantive physics findings (here on altermagnetic piezomagnetism): the agent autonomously conceives a research direction by mapping the corpus, calibrates methodology by reproducing published references, conducts novel first-principles computations, and writes the manuscript - grounded in literature throughout, across 47 fresh-context sessions in six phases sharing only on-disk state, with 2,162 literature-consultation events. Fault tolerance emerges from redundancy: fresh-context isolation, distributed grounding, and adversarial review catch what any single session misses; pre- and post-pilot stages are fully autonomous, and pilot requires bounded human intervention only at reproduction failures - operational knowledge curation, not scientific direction. Two paired failure modes - a pre-architecture baseline and a no-pilot ablation - isolate structurally enforced numerical confrontation at calibration checkpoints as the operative grounding mechanism. The primitives, characterized failure modes, and quantified intervention pattern lay a foundation for autonomous research in high-stakes scientific domains beyond computational physics.


### AgenticSTS: A Bounded-Memory Testbed for Long-Horizon LLM Agents
**Authors**: Xiangchen Cheng, Yunwei Jiang, Jianwen Sun, Zizhen Li, Chuanhao Li, Xiangcheng Cao, Yihao Liu, Fanrui Zhang, Li Jin, Kaipeng Zhang

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02255v1](https://arxiv.org/pdf/2607.02255v1)

**Abstract**: Memory for a long-horizon LLM agent is a contract about what each future decision is allowed to see. The simplest contract appends past observations, tool calls, and reflections to every prompt, which makes prior context easy to access but also turns it into a jumbled mixture in which the effect of any single memory component is hard to isolate. We introduce and instrument an alternative bounded contract: every decision is made from a fresh user message assembled by typed retrieval, with no raw cross-decision transcript appended. The prompt thus stays bounded across runs of any length, and any single layer can be ablated in isolation. We instantiate the contract in Slay the Spire 2, a closed-rule stochastic deck-building game whose runs require hundreds of tactical and strategic decisions. A public online benchmark of frontier LLMs on the same game reports zero wins at the lowest difficulty across five configurations, and the developer-reported human win rate at the same difficulty is 16%; the task is hard but not saturated. Within our harness, a fixed-A0 ablation shows the largest observed difference when triggered strategic skills are enabled: the no-store baseline wins 3/10 games and adding the skill layer 6/10. At this sample size the comparison is directional rather than statistically decisive (Fisher exact p\approx0.37); a cross-backbone probe and public accumulating-context baselines are reported as operational comparisons rather than controlled tests of the contract variable itself. We release a reproducible testbed: 298 completed trajectories with condition tags, frozen memory/skill snapshots, prompt records, and analysis scripts -- an agent design and a validated, reusable methodology for studying how explicit memory layers shape long-horizon LLM-agent decisions.


### Copewell: A Multi-Agent Swarm Architecture for Equitable Mental Wellness Support
**Authors**: Seren Yenikent, Jack Vinijtrongjit, Katherine Ng

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02245v1](https://arxiv.org/pdf/2607.02245v1)

**Abstract**: Mental health disorders affect nearly one billion people globally, yet 75% of individuals in low- and middle-income countries receive no treatment due to workforce shortages, cost barriers, and stigma. Current AI-powered wellness solutions predominantly rely on single-mode conversational interfaces that suffer high abandonment rates and fail to provide measurable, immediate relief calibrated to users' dynamic emotional states. This paper presents Copewell, a novel multi-agent swarm system designed to expand access to mental wellness support through human-centered AI principles. Our architecture introduces three technical innovations: (1) a multi-source assessment framework integrating self-reported, physiological, and contextual data to mitigate algorithmic bias; (2) valence-arousal emotion mapping using Russell's Circumplex Model of Affect to route users to specialized AI agents; and (3) dual-mode intervention delivery combining conversational support with evidence-based sensory wellness protocols. We examine the sociotechnical design considerations underlying Copewell's development, including a privacy-first architecture, embedded ethical oversight through a dedicated Ethics Supervisor agent, and participatory design informed by mental health practitioners. Early practitioner engagement and beta deployment inform design decisions and identify directions for future empirical evaluation. This work contributes to responsible AI discourse by demonstrating how technical architecture can operationalize equity and safety principles from inception.


### Criticality-Based Guard Rail Validation for AI Agent Decisions in Autonomous Telecom Networks
**Authors**: Ravi Kant Sharma

**Published Date**: 2026-07-02

**Updated Date**: 2026-07-02

**PDF Url**: [2607.02210v1](https://arxiv.org/pdf/2607.02210v1)

**Abstract**: The evolution toward fully autonomous telecommunications networks (Autonomous Network Levels 4-5) requires AI/ML agents to make real-time network decisions without human intervention. However, no standardized runtime mechanism exists to intercept and validate individual inference outputs before they trigger live network state changes, creating risks of erroneous autonomous decisions. This paper proposes the Guard Rail Validation (GRV) framework, a standardizable runtime architecture for intercepting and validating AI-driven decisions before execution. The framework evaluates decisions across multiple weighted dimensions -- including action scope, action type, service criticality, agent autonomy level, reversibility, and temporal behavioural patterns -- to determine a criticality level. Based on this level, graduated validation mechanisms are applied: execute-with-logging, bounds checking, independent agent validation, or multi-agent consensus. The framework additionally provides cross-agent conflict detection with criticality-weighted priority resolution and runtime conformance logging for regulatory compliance (e.g., EU AI Act Article 14). We present the architecture, algorithmic procedures, O-RAN deployment model, and evaluate threat coverage against known AI/ML attacks in telecommunications.


