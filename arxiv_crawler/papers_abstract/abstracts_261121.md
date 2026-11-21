# Abstracts of Papers

## World Model
### RL Post-Training in Diffusion Transformers Is Activation Steering
**Authors**: Tuna Han Salih Meral, Kaan Oktay, Alec Helbling, Atakan Kara, Duen Horng Chau, Pinar Yanardag

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26627v1](https://arxiv.org/pdf/2611.26627v1)

**Abstract**: Reinforcement learning (RL) post-training substantially improves the visual quality, text rendering, and compositional accuracy of diffusion transformers. Because capabilities such as rendering requested text or composing multiple objects are inherently prompt-dependent, a natural hypothesis is that improving them requires learning complex, input-dependent transformations. To isolate how much of these gains an input-independent shift explains, we probe each RL-tuned model with a deliberately simple parameterization: a fixed set of steering vectors added to the block outputs of the frozen base model. On SD3.5-M, these vectors hold 65x fewer parameters than the RL-tuned LoRA (0.29M against 18.8M). We fit them to match the velocity predictions of public RL-tuned checkpoints, with no reward in the objective. Although the vectors are identical for every prompt, token, and sampling seed, they recover 90.0-96.3% of the reward gains of six RL-tuned image models, and 89.8% and 111.9% on two RL-tuned video models. Initialized at zero and trained with online RL, the vectors alone exceed the reward gains of weight-based RL on text rendering (OCR) and human preference (PickScore) on SD3.5-M. A constant shift thus suffices for most of the gain of policy-gradient RL post-training: without new input-dependent transformations, it steers the pretrained generator toward what it can already compute.


### TideCache: Efficient Hybrid LLM Serving with Transparent Cache Management and Layer-Wise Streaming
**Authors**: Jinbin Luo, Xiaozhe Yao, Shang Yang, Zhijian Liu, Song Han, Qinghao Hu

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26619v1](https://arxiv.org/pdf/2611.26619v1)

**Abstract**: Hybrid architectures have become mainstream among open-weight language models. Their global-attention and bounded-state layers maintain heterogeneous caches whose demands vary with context length and concurrency. We present TideCache, a serving system on CPU--GPU superchips with three components for allocating GPU memory among caches and managing their residency across GPU and host memory. The Transparent Cache Pool redistributes physical pages among cache components behind fixed virtual addresses, preserving cache layouts and backend interfaces. The Cache Streamer uses computation intervals provided by bounded-state layers to prefetch the next global-attention layer's prefix into GPU slots shared across global-attention layers, reducing GPU residency while overlapping layer-wise transfers with computation. Generated KV remains resident. The Request Scheduler selects resident or streamed execution and triggers capacity adjustments according to request size and queue state. Together, they let HBM released by streaming accommodate other cache components and additional requests. Implemented in SGLang and evaluated on GB300 and GH200 across seven model/platform configurations, TideCache completes up to 2.04x as many agent turns, reduces overall P50 per-token latency by 20--59%, and improves agent P50 TTFT by 1.40--3.05x compared with SGLang with HiCache.


### One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning
**Authors**: Yuxin Jiang, Wenqiang Sun, Jiaqi Li, Yuchao Gu, Lvmin Zhang, Ivor Tsang, Mike Zheng Shou

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26617v1](https://arxiv.org/pdf/2611.26617v1)

**Abstract**: Videos reveal how the world changes, but rarely the actions that cause those changes. Latent action learning recovers such supervision from visual transitions, yet often learns the underlying dynamics largely from scratch. We ask whether a pretrained video generator can instead provide the prior for both inverse and forward dynamics. We introduce O$^{2}$LaF, built on a simple principle: one prior, two dynamics. We initialize both models from the same pretrained video DiT and adapt them to their distinct roles: a feed-forward transition encoder with learnable action queries for inverse dynamics, and a causal, action-conditioned video generator for forward dynamics. By controlling information access and optimizing both dynamics end-to-end through a compact bottleneck, O$^{2}$LaF learns transferable actions from unlabeled videos. Across navigation and robotic manipulation, O$^{2}$LaF sets a new state of the art in few-shot action probing and enables stronger zero-shot action transfer across visual contexts and embodiments. Beyond generative video priors, we further extend our framework to predictive representation priors such as V-JEPA2, achieving competitive performance. Our findings suggest a broader paradigm for latent-action learning: repurposing pretrained video models to discover transferable actions and predict their consequences.


### ScaleWorld: High-Resolution World Generation through Shared Prediction and Refinement
**Authors**: Yansong Qu, Wesker Zheng, Quanjian Song, Zhiyuan Zhang, Xiao Cao, Shengchuan Zhang, Liujuan Cao

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26615v1](https://arxiv.org/pdf/2611.26615v1)

**Abstract**: High-resolution generation enables video world models to render fine-grained scene structures and textures, but directly generating high-resolution video incurs substantial computational and memory costs. We present ScaleWorld, a causal video model that unifies low-resolution world prediction and high-resolution refinement within a single shared backbone. By refining its own predictions, ScaleWorld produces high-resolution world videos without requiring a separate refinement model. For each video chunk, the shared backbone first completes a low-resolution prediction and then performs one-step high-resolution refinement conditioned on that prediction. To support efficient streaming generation, we maintain separate causal states with a long low-resolution history for prediction and a short high-resolution history for refinement. To address task interference during distillation, we separate specialist optimization from capability consolidation and introduce task-asymmetric on-policy distillation (TA-OPD). This procedure transfers prediction and refinement behaviors from specialized teachers into a shared student through local velocity matching under their respective sampling and history policies. {Extensive experiments demonstrate that ScaleWorld achieves high-quality world generation with improved computational and memory efficiency.


### Bio-PM-Guided Synthetic IMU Generation
**Authors**: Deepali Singh, Deepesh Parpani, Aviral Gupta

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26607v1](https://arxiv.org/pdf/2611.26607v1)

**Abstract**: Collecting and labeling inertial measurement unit (IMU) data for human activity recognition (HAR) is expensive, and models trained on one group of subjects often fail to generalize to unseen individuals. Even with balanced data, classifiers struggle to distinguish dynamically similar activity classes and benefit from targeted augmentation. We explore whether synthetic IMU data generated in the representation space of a pretrained biosignal encoder, Bio-PM \cite{b1}, can serve as a practical augmentation source. Rather than synthesizing raw signals, we leverage Bio-PM's frozen encoder to convert 10-second IMU windows into token embedding sequences and train class-conditional decoders in this space: (1) an autoregressive transformer decoder that predicts tokens sequentially, and (2) a diffusion decoder that learns the token distribution through a denoising objective. We analyze generation realism through distributional metrics and embedding-space visualizations, evaluate downstream utility through leave-one-subject-out HAR classification, and present a PatchDecoder for approximate raw waveform reconstruction. Our diffusion decoder achieves a Train-on-Synthetic-Test-on-Real (TSTR) macro-F1 of 0.68, demonstrating that generated tokens are realistic enough to train a classifier that transfers to real data. Combining synthetic-token augmentation with a 320-dimensional gravity-aware feature representation raises LOSO macro-F1 from 0.729 to 0.809 over a real-only baseline across 51 subjects on the WISDM benchmark, with statistically significant gains concentrated in the most challenging activity classes. These results demonstrate that high-fidelity generation in a pretrained encoder's representation space is achievable and practically useful for cross-subject HAR augmentation.


### Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth
**Authors**: Peiyun Hu, Marko Mihajlovic, Lyndon Duong, Lahav Lipson, Wei Dong, Amaël Delaunoy, Stephan R. Richter, Vladlen Koltun

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26603v1](https://arxiv.org/pdf/2611.26603v1)

**Abstract**: We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that processes both images and video and predicts depth maps at native resolution. Depth Pro 2 produces depth maps that are metrically accurate, sharp, and temporally consistent all at once, outperforming prior work in all of these dimensions. We release a family of models that define a new Pareto frontier in terms of metric accuracy, sharpness, temporal consistency, and runtime. We release code and weights at https://apple-aiml-research.github.io/ml-depth-pro-2/


## Generation
### PlayCraft: Designing Engaging Games from Agent Play Experience
**Authors**: Weihao Cheng

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26624v1](https://arxiv.org/pdf/2611.26624v1)

**Abstract**: Recent AI agents can generate playable games, but these games are not necessarily engaging. Mastery is a key source of engagement, yet designing for it requires extensive human play and tuning. We propose PlayCraft, an automated framework that uses a vision-based agent to play games and draws on its detailed play experience to revise them for mastery. Starting from an initial game, PlayCraft alternates between playing and crafting. In the playing stage, a player agent watches the game screen, uses the controls, and pursues the game objective over repeated episodes while retaining memory. After each episode, it reports its progress, outcomes, decisions, and reflections. In the crafting stage, a crafter agent uses these reports to revise the game. It estimates player abilities, predicts performance at different proficiency levels, and compares those predictions with a target learning progression. It diagnoses the game and addresses the gaps by giving players meaningful opportunities to improve through better decisions and execution. We evaluate games in fresh runs with player agents across three intelligence settings, measuring learning gain and learning slope. Compared with the initial games, PlayCraft yields larger learning gains and steeper learning slopes in most games. It also outperforms the baselines on the macro-average of each metric at every intelligence setting.


### ProtoDiffusion: Token-per-Layer Generative Modeling of Multi-Layer Images
**Authors**: Adrià Ciurana Lanau, Harleen Hanspal, Lusine Abrahamyan, Emilio Tylson Baixauli, Yu Cao, Danai Triantafyllidou, Stefano Zorzi, Gustavo Zanoni Felipe, Peter Griger, Stefan Sietzen, Petru-Daniel Tudosiu

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26586v1](https://arxiv.org/pdf/2611.26586v1)

**Abstract**: Graphic designs are ordered compositions of RGBA layers whose separation enables selection, movement, and reuse. Existing layered models represent each layer with a full-canvas or region-sized spatial latent grid, so representation size grows with the cumulative spatial extent of the layers. We present ProtoDiffusion, a latent-diffusion framework built on ProtoVAE, a multi-layer variational autoencoder that encodes a design into one shared spatial prototype and one candidate vector per layer. Each candidate conditions a shared decoder to reconstruct its corresponding RGBA layer. For $N$ layers, the representation contains $HW+N$ tokens before backbone-specific packing, compared with $NHW$ for full-grid-per-layer representations. ProtoDiffusion jointly denoises the prototype and a fixed set of candidate slots, conditioned on an image or text, with bounding boxes as optional layout guidance. The model leaves unneeded slots empty and determines the number of layers and, in absence of boxes, their layout, requiring neither as input. The same architecture supports both image-to-design and text-to-design. ProtoVAE achieves high-fidelity reconstruction from its compact shared latent representation, reaching 40.43 dB PSNR on layer crops. On the LayerD evaluation split, image-to-design achieves RGB L1 scores of 0.040 with bounding boxes and 0.057 without, with box-guided alpha soft IoU (0.850) comparable to the strongest fine-tuned baseline (0.871). On merged images, text-to-design reaches 66.41 FID versus 86.84 for FLUX.2 [klein], achieves a 0.860 text-accuracy score, and runs $19.1\times$ faster than the same-backbone generation-then-decomposition cascade.


### Text-Aware, Vision-Blind: How Multimodal Image Editing Systems Handle Unsafe Inputs
**Authors**: Ziqing Yang, Yixin Wu, Michael Backes, Yang Zhang

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26569v1](https://arxiv.org/pdf/2611.26569v1)

**Abstract**: Multimodal image generation systems have made rapid progress and increasingly emphasize content safety. However, their safety mechanisms tend to rely on a single modality and lack joint consideration of both visual content and text prompts, particularly in instruction-guided image editing, where the uploaded image may itself carry risk. We thus introduce EditSafetyBench, a benchmark that measures system-level safety awareness of advanced image editing systems, containing 5,940 image-instruction pairs, covering safe and unsafe images across 11 risk categories and three edit intents. We then probe the benchmark dataset on four systems, including Gemini, GPT, Qwen API, and Qwen Local. Based on our evaluation, we observe a systematic text-vision safety mismatch: Gemini and GPT refuse 87.1\% and 81.6\% cases containing unsafe-intent editing prompts, while only refusing 24.2\% and 22.4\% cases with both unsafe images and neutral instructions. At the category level, most risks are considered inconsistently by different systems, e.g., GPT allows 70.4\% editing attempts of unsafe political content while Gemini only allows 34.8\%. Notably, sexual content shows the strongest visual sensitivity, likely benefiting from mature NSFW identification works. Our findings highlight the need for safety guardrails that jointly reason over both visual and textual modalities in image editing systems.


### GEOHunter: Mapping a Generative Engine Optimization Network in the Wild
**Authors**: Sean Tang, Peiran Wang, Ying Li, Esha Shivakumar, Tao Meng, Yuan Tian

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26564v1](https://arxiv.org/pdf/2611.26564v1)

**Abstract**: Generative engines synthesize retrieved web pages into answers, recommendations, and rankings. Generative engine optimization (GEO) services sell visibility in these answers by publishing promotional articles on user-generated-content (UGC) platforms for paying clients. Such promotion raises concerns in medical and financial domains, where misleading advice can cause harm. To study the severity of this problem, we measure one such paid-content operation across three major Chinese UGC platforms, uncovering 1,985 accounts associated with the network comprising 466,357 inferred promotional placements. We find that the network promotes products across diverse categories through a growing pool of accounts, conducting coordinated campaigns spanning months across multiple platforms while evolving its listicle content over time. Across nine generative engines from both the US and China, we find that 4.5% to 20% of retrievable cited pages are attributable to the network, depending on how strictly attribution is drawn. On eight of these engines, its clients are named in 52% of answers, against 68% for category leaders. Our work demonstrates the effectiveness of UGC GEO placement at influencing generative engine outcomes, and reveals content-level defenses as insufficient against coordinated UGC placements, where account-level and platform-level signals are necessary for proper defense.


### AURA: AUdio-dRiven streaming Avatar
**Authors**: Nathaniel Cohen, Nicolas Dufour, Amélie Royer, Alasdair Newson, Patrick Pérez

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26540v1](https://arxiv.org/pdf/2611.26540v1)

**Abstract**: Current audio-driven video diffusion models can synthesize realistic talking-head videos but generally require dozens of diffusion denoising steps over multi-second video chunks, making them unsuitable for streaming applications such as voice assistants and virtual avatars, where low-latency and online causal generation are required properties. AURA generates video chunk by chunk with a rolling KV cache, requiring only the audio of the current chunk to start generating, rather than a multi-second audio look-ahead like bidirectional models. It comes in two sizes: AURA 1.3B streams 576p video in real time on a single GPU (20.7 fps for a 16 Hz playback rate), making it suited to interactive avatar applications, and AURA 5B streams 720p video at 9.7 fps. Our two-stage distillation pipeline first aligns the causal student with the teacher, by training it to match the teacher's trajectories with fewer diffusion steps and a chunk-wise sliding window causal attention mask, then applies Distribution Matching Distillation (DMD) with backward simulation to close the remaining quality gap. On standard talking-head benchmarks, AURA 1.3B runs 23x faster than its own bidirectional teacher and reaches a quality comparable to TalkVerse at a lower resolution, and AURA 5B matches its TalkVerse teacher at 720p while running 17x faster. To support reproducibility and further research on streaming avatar generation, we release the weights of both models along with a dataset of 30K synthetic videos and their precomputed teacher trajectories.


### Cost-Aware Agentic Feature Optimization System for Fleet-Scale Ranking Models
**Authors**: Chang Yang, Yao Xuan, Wendan Yan, Nhat Le, Jiang Liu, Longhao Jin, Zhen Peggy Yao, Alireza Vahdatpour, Djordje Gligorijevic

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26531v1](https://arxiv.org/pdf/2611.26531v1)

**Abstract**: Large Web platforms operate large fleets of ranking models, each selecting features from a shared pool of tens of thousands. We present an end-to-end agentic system that optimizes features across the fleet under resource constraints shared across models and those set per model, such as feature pipeline cost and serving throughput (QPS), respectively. In this system, LLM agents propose hypotheses, and deterministic tools execute experiments and verify them. For each model, an LLM generates and shortlists cross features from a combinatorial candidate space, and all features are then ranked by several importance methods. Feature blending mixes these rankings into a single selection, using Pareto fronts across tasks for multi-task models. An LLM Researcher agent then tunes the feature selection in 10--25 asynchronous trials under resource caps, and a trimming step keeps the pipeline cost within budget. Across production models, the system improves normalized entropy by 0.31% on average within each model's budget, and the trimming step cuts pipeline cost by 2.3% with no regression beyond measurement noise. The optimized models were launched, and in online A/B tests they improved a primary online metric by 0.20%.


## VLA
### PGX: Physically Grounded Execution for Long-Horizon Humanoid Loco-Manipulation
**Authors**: Kai Lu, Chenyang Ma, Ioannis Havoutis

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26596v1](https://arxiv.org/pdf/2611.26596v1)

**Abstract**: Robotic vision-language-action (VLA) models can execute diverse individual manipulation skills, yet they still struggle with long-horizon loco-manipulation tasks, where temporal structure, skills, and precision are tightly coupled within a monolithic model. We propose Physically Grounded Execution (PGX), a framework that offloads temporal and precision control to two classical training-free components, allowing the VLA to focus on stage-specific skill dynamics. PGX decomposes long-horizon loco-manipulation into three layers: (i) a predicate-based state machine governs task progression, using physical predicates to gate phase transitions, trigger recovery, and coordinate navigation and waiting. Shared predicate semantics connect offline demonstration segmentation, online execution, and stage-wise evaluation; (ii) VLA skills operate within active manipulation phases, with flat or stage-trained models concentrating on task-relevant actions; and (iii) world-coordinate locking (WCL) maintains spatial consistency through base station keeping, object-relative positioning, and world-anchored contact targets. We demonstrate the effectiveness of PGX with extensive experiments conducted on three simulated tasks and one real-world task using a Unitree G1 humanoid robot for long-horizon loco-manipulation, showing improvements in stage progression and task success rates. Project page is available at: https://kl-research.github.io/pgx


### Mind2Act World: A Diagnostic Benchmark for Embodied Mind, Physical Action, and Mind-Action Composition in Robotic Manipulation
**Authors**: Yuzhi Huang, Jie Wu, Fanding Huang, Junchao Lin, Weichen Zhang, Ziyi Xiong, Yang Li, Zhengwei Xie, Zhimin Wang, Zhen Liu, Jiazhen Huang, Yuzheng Zhang, Yuche Liu, Hongyi Yang, Chen Tang, Shixiang Tang, Hakan Aktas, Adam Wu, Duo Wu, Kangye Ji, Shuzhao Xie, Huanan Liu, Weijue Bu, Chenxin Li, Xinyuan Wang, Tianyi Bai, Yinan Mao, Jiawei Wang, Minglei Li, Heng Yu, Ehsan Adeli, Minchen Li, Yong-Lu Li, Cengiz Öztireli, Huazhe Xu, Chao Yu, Jing Zhang, Shanghang Zhang, Weitao Zhou, Wenwu Zhu, Cheng Chi, Jingyan Jiang, Zhi Wang

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26444v1](https://arxiv.org/pdf/2611.26444v1)

**Abstract**: Embodied intelligence aims to let robots perform complex physical tasks with human-like adaptability and reliability, which requires three complementary capabilities: history-based cognitive reasoning, precise and timely physical execution, and the composition of reasoning and execution through environmental feedback. Yet existing benchmarks either evaluate reasoning and execution within the same tasks or assess them separately without their composition, so they reveal little about whether a failure comes from reasoning, execution, or their composition. We introduce Mind2Act World, a diagnostic benchmark of 30 simulated manipulation tasks from five real-world application domains. Each task has three difficulty levels and two scene settings (Clean and Random), yielding 180 configurations. The tasks form three views: Mind tests decisions based on past observations, Act tests precise and timely execution, and Mind2Act combines both in closed-loop tasks where action outcomes guide later decisions. Comparing the three views shows whether a system lacks a capability or fails to compose capabilities it already has. A diagnosis harness further attributes the failed episodes of three representative systems to Mind, Act, or their composition and summarizes each system in a profile card. Our evaluation of multimodal agents, vision-language-action models (VLAs), and world-action models (WAMs) shows that competence in a single view does not carry over to Mind2Act tasks. Even the strongest agent succeeds in 52.7% of Mind and 39.0% of Act episodes but in only 12.0% of Mind2Act episodes. The strongest agent retains task state but struggles with sustained contact, whereas end-to-end policies execute practiced motions but retain little task state. These findings point to composing reasoning and execution through environmental feedback as the main open problem.


### FastRoverVLA: Fast Vision-Language-Action Execution for Off-Road Autonomous Driving
**Authors**: Changtao Zhao, Yingxue Guan, Li Wang, Shijie Zhao, Yuhang Zhang, Shengkai Zhang, Qing Wang, Ziying Song

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26242v1](https://arxiv.org/pdf/2611.26242v1)

**Abstract**: Off-road vision-language-action (VLA) models generate scene-conditioned plans, but frequent trajectory updates can repeatedly invoke expensive multimodal inference. Reusing a prediction reduces this demand while leaving its commands exposed to changes in vehicle motion. FastRoverVLA addresses this mismatch by decoupling visual plan generation from motion-conditioned execution. Its training-free interface maintains decoded plans between visual predictions. A speed-curvature action buffer is aligned with measured motion at each update, integrated into a local trajectory, and advanced by consuming the current action. The corrected remainder is written back to the buffer, preserving motion corrections across successive updates. A bounded refresh rule normalizes speed and curvature variations within a newly decoded plan and assigns a short or long reuse budget according to the resulting plan-roughness score. The interface requires neither backbone features nor an additional learned driving policy. Over a 3 s horizon, independent real-request evaluation achieves average displacement error (ADE) and final displacement error (FDE) of 0.328/0.596 m on ORAD-3D and 0.266/0.526 m on RELLIS-3D, reducing FDE by 18.0% and 36.7% at request rates of 6.0% and 4.8%, respectively. These runs retain lower errors across four backbones and both datasets and reduce Qwen3-VL request-processing cost by factors of 16.6 and 20.8 under serial replay, while mechanism and motion-only controls identify persistent state correction as the main source of the observed accuracy benefit. The source code and evaluation materials are publicly available at https://github.com/ADEPT-ORG/FastRoverVLA.


### Full Rank and Stable Sampling of $\tanh$ Networks
**Authors**: Philipp Grohs, Matěj Trödler

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.25867v1](https://arxiv.org/pdf/2611.25867v1)

**Abstract**: We study the recovery of feedforward $\tanh$ networks of fixed architecture with $P$ parameters from finitely many point evaluations. First, we characterize the set of parameters where the differential of the realization map has full rank and show that it coincides with the regular parameters in the sense of Vla{č}i{ć} and B{ö}lcskei (2021). Second, we make use of this characterization to prove that almost every tuple of $2P+1$ sampling points yields uniform-norm Lipschitz stability on compact subsets of this parameter set. Third, we prove that for exact observations, projected gradient descent and projected Gauss--Newton converge locally from sufficiently close feasible initial guesses. The same evaluations also determine the realized function for arbitrary parameters and identify parameters in the characterized set up to permutations and sign changes of hidden neurons. Finally, we develop a general framework for real-analytic networks that highlights the role of full rank in stability and local reconstruction.


### DMT-Attack: Diffusion-Prior Texture Search for Closed-Loop Vision-Language-Action Policies
**Authors**: Jun Xia, Shangwen Wang, Jun Ma, Ruichao Ren, Zhouyang Jia, Xin Zhao, Huijun Liu, Jie Yu

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.25695v1](https://arxiv.org/pdf/2611.25695v1)

**Abstract**: Vision-language-action (VLA) policies rely on visual feedback throughout manipulation, making them vulnerable to persistent texture attacks. However, optimized patterns can stand out from their surroundings, making an attack easier to notice and its carrier more likely to be inspected or removed. To address this limitation, our key insight is to search the structured image distribution of a diffusion model for natural-looking textures while using closed-loop feedback to identify task-disruptive candidates. Based on this idea, we propose DMT-Attack, a gradient-free gray-box attack that generates textures for ordinary scene objects such as tablecloths. A frozen text-conditioned diffusion model defines the search space, and an eight-expert latent proposal network is initialized from evaluated teacher latents and refined using rollout feedback. We evaluate DMT-Attack against pi_0.5 and OpenVLA-OFT across four LIBERO suites. DMT-Attack achieves a macro clean-conditioned attack success rate (cASR) of 57.9%, compared with 44.7% for UPA-RFAS and 19.7% for random natural textures. It also attains higher scene similarity and a lower clean-calibrated detector flag rate (45% versus 97.5-100% for optimized patch baselines). These results demonstrate that natural-looking textures can disrupt VLA visual feedback and closed-loop decision-making, motivating defenses that jointly assess visual appearance and task behavior.


### A$^2$-VLA: Adapting Vision-Language-Action Policies to New Tools through Agentic Affordance Discovery
**Authors**: Chenyuan Zhou, Chaoyi Huang, Zibo Wang, Zhiyuan Li, Yong-Lu Li

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.25656v1](https://arxiv.org/pdf/2611.25656v1)

**Abstract**: Tools with different shapes can have similar functions, but transferring manipulation skills across tools requires understanding how tool geometry relates to the specific task and adjusting the manipulation strategy accordingly. The key challenge is to discover the common affordances that contribute to task completion across different tools and verify whether they support new tools in performing similar work. We present A$^2$-VLA, a tool-adaptation framework that combines an embodied agent with a VLA policy. It treats tool affordances as hypotheses the agent can construct, test, and revise. Given teleoperated demonstrations with a few source tools, the agent reconstructs the scenes in simulation and autonomously determines task-relevant affordance features: functional regions and their key geometric properties. It develops affordance-extraction skills and refines both the features and skills through autonomous experiments in the reconstructed scenes. Validated extraction skills accumulate in a reusable skill library for unseen tools. Finally, A$^2$-VLA uses encoded functional-region features as conditioning inputs to a $π_{0.5}$ backbone during training and inference. Evaluation examines affordance reliability in reconstructed scenes and real-robot task success on unseen tools. Our method achieves 86.1% success in simulated cross-tool trajectory retargeting based on affordances. On three real-robot tool-use tasks, A$^2$-VLA improves task success by 30.7 percentage points over $π_{0.5}$.


## Agent
### SoK: Assessing the Evolution of LLM Capability in Software Vulnerability Research
**Authors**: Amine Lbath, Manan Suri, Aurelien Delaitre, Vadim Okun, Massih-Reza Amini, Dinesh Manocha

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26601v1](https://arxiv.org/pdf/2611.26601v1)

**Abstract**: LLM-based agents are becoming increasingly capable at discovering, validating and patching vulnerabilities in real software, and vendors and researchers report that this is already changing how vulnerabilities are found and fixed. These claims, however, are scattered across papers, vendor reports and disclosures and are rarely comparable. We introduce a framework that rates these capabilities on an autonomy scale modeled on the levels of driving automation, and qualifies each claim by its correctness, its availability and the strength of its evidence. We use this framework to systematize the published evidence on LLM capability in vulnerability research. We find that agents discovered, validated, and patched vulnerabilities in real-world software without human intervention before the restricted frontier models of 2026, and that open-weight models subsequently attained comparable autonomy for discovery and validation. We then measure the consequences of evolving LLM security capabilities in a decade of public vulnerability records, advisories and exploitation data. In 2026 the number of disclosed vulnerabilities more than doubled, with an increasing share rated critical or high, and severe bugs that had survived a decade or more in widely used code were reported several times more often than before. Yet the time between the stages of a vulnerability's life, from report to fix and from disclosure to attack, has not shifted noticeably so far. We grade the mitigations proposed in the literature with an explicit rubric and draw guidance for each group of stakeholders from the best-supported ones.


### Replication of Agentic Security Events: Audit and Investigation (ROGUE-AI)
**Authors**: Mengxiao Wang, Mahbub Alam, Kalyan Nakka, Nitesh Saxena

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26553v1](https://arxiv.org/pdf/2611.26553v1)

**Abstract**: Agents based on large language models (LLMs) can now delete files and send payments on behalf of their users. News media reports routinely describe failures of these agents (e.g., Replit's coding agent deleting a production database), but a report often only says what went wrong and rarely (in)validates the incident or finds its root cause. Incident catalogs collect these reports, and benchmarks record whether agents fail, but neither replicates an incident nor tests the cause its report might identify. In this paper, we present ROGUE-AI (Replication of Agentic Security Events: Audit and Investigation), a multi-agent framework that closes the above gap and rebuilds each reported incident offline together with a matched control that lacks only the blamed cause, and runs agents on both. Our results suggest that ROGUE-AI is able to reproduce the reported harm in 89% of its 108 attempted replications. Agents built on five current GPT, Claude, Gemini and DeepSeek models made the reported mistake in 18% to 33% of runs, against at most 1% without the blamed cause. Of the 72 incidents with real-world harm, 62 had no underlying attacker, and in these, agents did what their task asked for but missed an ordinary hazard, such as a database shared with the live site. Replications without an attacker caused more harm than replications of prompt injection for all five models. Defenses against prompt injection look for injected instructions, but these replications contain none. Further, a warning after each tool output that names the hazard and its consequence lowered harm for all five models, whereas a note of the same length that does not mention the hazard left most of the harm in place. Built from real incidents, the ROGUE-AI replications form a reusable audit framework that vendors can rerun before each new release.


### Backtracking Agent Applications Security Incidents
**Authors**: Yicheng Cai, Taegyu Kim, Peng Liu

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26525v1](https://arxiv.org/pdf/2611.26525v1)

**Abstract**: Agent applications are increasingly deployed, yet agent-specific attacks pose real threats to them. Upon a security incident, organizations backtrack to identify the CEP (compromise entry point), remediate the damage, and prevent its recurrence. The main artifacts available for backtracking are trajectory logs, which record agent functionalities, and source code; app(lication)-specific function call logs are often fairly limited. However, trajectory logs are at the agent functionality abstraction layer, while the CEP candidates are function calls at the app code execution layer. Due to this semantic gap, the analyst needs to manually inspect the relevant code for each CEP candidate to infer its corresponding agent functionality. In this work, we present Origin, a backtracking tool for the analyst to submit a small number of queries to identify CEPs that existing tools cannot provide. Our approach poses two challenges: (1) define the intermediate abstraction that captures the mapping relationships between the two semantic layers; (2) determine the region-to-variable mapping for constructing the cross-layer graph defined in the intermediate abstraction. Each region is a specific group of agent functionalities. Origin addresses the challenges by (1) the cross-layer dependency graph (CLDG) that connects region-inferred functions at the semantic level to the variables in the low-level taint propagation subgraph, plus the associated query language, and (2) the region inference algorithm. Case studies on five popular agent applications across eight attack incidents show that an analyst using Origin correctly identifies all the CEPs.


### Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning
**Authors**: Élodie Côté-Gauthier, Doina Precup, Isabeau Prémont-Schwarz

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26504v1](https://arxiv.org/pdf/2611.26504v1)

**Abstract**: Continual reinforcement learning requires agents to adapt when the task changes while reusing what they know about the environment. Successor features separate dynamics from task-specific reward, but their effectiveness depends on the choice of base features. Taking the identification of entorhinal grid cells with eigenvectors of the successor representation as a design principle, we build this basis from eigenvectors of the transition matrix of a fixed reference policy. With such a basis, the successor features at a state-action pair are a linear combination of the base features at that same pair, which is not true in general, and the coefficients are known in closed form: each successor feature is its base feature multiplied by $θ_i = 1/(1-γλ_i)$, where $λ_i$ is its eigenvalue. The long-term return is thus predicted from the same features as the immediate reward, no successor-feature network or replay buffer is needed, and adapting to a new task reduces to a linear regression on the reward. The agent acts greedily on the action values of the reference policy, which is one step of policy improvement over it and suffices to reach a single goal. In a two-goal gridworld, with the uniform random walk as reference policy, whose eigenvectors are the low-frequency Laplacian eigenvectors, agents built this way maintain near-maximal return across every change of goal, whereas SimpleSF and DQN lose most of their return at each change.


### FLUID: Flexible, Evidence-Grounded Situated Task Guidance
**Authors**: Yunqi Zhao, Run Peng, Ze Dong, Ryan Lu, Yinpei Dai, Joyce Chai

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26491v1](https://arxiv.org/pdf/2611.26491v1)

**Abstract**: Real-time task guidance is inherently flexible: when an agent guides a user through a task, multiple responses and timings can be appropriate, and sometimes the best action is to remain silent. Existing benchmarks often miss this flexibility by treating synthesized dialogues as fixed targets for what to say and when to say it. We introduce FLUID (Flexible, Evidence-Grounded Situated Task Guidance), a unified framework for modeling, evaluating, and enabling flexible interaction in multimodal task guidance. Using naturally occurring human-human guidance from WTaG and HoloAssist, FLUID grounds interventions in their supporting evidence, necessity, and timing flexibility, and uses this representation both to evaluate flexible guidance and to build a real-time agent for task guidance. Our agent achieves the strongest overall balance of response correctness, intervention precision, timely guidance, and response latency among evaluated systems, while still leaving room for improvement in avoiding speech overlap. Together, FLUID moves situated task guidance beyond rigid reference matching toward more natural and adaptive human-AI interaction. Project page: https://fluid-guidance.github.io.


### Seer: Guiding Small Deep-Research Agents with Shared Decision Models
**Authors**: Yuhao Zhou, Yang Zhou, Yuanxi Li, Jindi Lv, Dan Si, Qing Ye, Jiancheng Lv

**Published Date**: 2026-11-19

**Updated Date**: 2026-11-19

**PDF Url**: [2611.26423v1](https://arxiv.org/pdf/2611.26423v1)

**Abstract**: Deep-research agents repeatedly decide what to search, read, and verify, often using large cloud-hosted language models for action proposal. However, privacy and local control motivate running agents on users' devices, where limited memory and compute favor smaller models and complicate on-device training. Yet inference-time guidance faces three obstacles: exploring alternatives through real execution adds tool calls, prompted self-evaluation is bounded by the agent's judgment, and model-specific guidance risks repeated adaptation costs. We introduce Seer, an inference-time framework providing local guidance that separates the agent's action proposal from learned consequence prediction and value estimation. From a shared corpus of real research trajectories, we train two models: a tool-response simulator on observed call--response pairs and a value estimator on histories labeled with discounted terminal correctness. The simulator and estimator are trained offline and reused across agents without further training. Moreover, Seer executes only the selected action and adds only real tool responses to the committed history, avoiding tool calls on discarded candidates at additional inference cost. Across multiple deep-research benchmarks, Seer substantially improves agent performance for different language models. For instance, GAIA accuracy rises from 13.6% to 41.7% for Qwen3.5-4B and from 22.3% to 50.5% for Qwen3.5-9B. Furthermore, our analyses suggest that broader candidate coverage can compensate for imperfect simulation, while prediction and scoring errors limit the benefits of wider imagined search. These findings highlight the potential of reusable models for prediction and evaluation to strengthen small research agents through extra local computation without the real execution of the discarded candidates.


