# Abstracts of Papers

## World Model
### From Natural Language to Exact Cover: A Neuro-Symbolic Approach to Zebra Puzzles
**Authors**: Paulius Skaisgiris, Thomas Pammer, Veronika Semmelrock, Mykyta Ielanskyi, Maximilian Heisinger, Erich Kobler

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03641v1](https://arxiv.org/pdf/2611.03641v1)

**Abstract**: Chain-of-Thought (CoT) generation has substantially improved the performance of Large Language Models (LLMs) on complex reasoning tasks, including code generation, data analysis, and exam-style question answering. Despite these advances, purely neural LLMs continue to struggle with elementary logical reasoning problems and lack the determinism, soundness, and reliability characteristic of symbolic reasoning systems. Conversely, classical symbolic methods such as SAT solving and exact cover guarantee correctness and completeness, but require problems to be expressed in highly specialized formal encodings, limiting their applicability to natural language inputs. In this work, we present a synergistic neuro-symbolic framework that bridges this gap by combining neural semantic parsing with deterministic exact cover reasoning. Given a Zebra-style logic puzzle in natural language, an LLM translates entities and constraints into structured tool calls that construct an exact cover instance. A symbolic solver then computes the solution and provides feedback to iteratively refine invalid, under- or overconstrained encodings, exploiting the uniqueness property of Zebra puzzles. We conduct a comprehensive empirical evaluation across multiple parameter scales, post-training paradigms, and LLM families. The results demonstrate that our hybrid approach consistently outperforms strong plain neural baselines, including CoT prompting, as well as recent neuro-symbolic methods.


### WebHarbor: Docking Real Websites for Evolving GUI Agent Environments
**Authors**: Zhaoyang Wang, Qianhui Wu, Boyu Gou, Demi Wang, Jiacheng Zhang, Peichun Hua, Qize Li, Shi Qiu, Yifan Jiang, Yifan Zhang, Zexu Jin, Baolin Peng, Bolin Shen, Chetan Bansal, Dehan Kong, Deren Lei, Dongshen Peng, Fengqing Jiang, Hao Cheng, Haoqing Wang, Jiaming Shan, Jicheng Wang, Jingguang Zhou, Jixuan He, Kaide Zeng, Kangyu Zhu, Lama Moukheiber, Mufan Qiu, Peng Xia, Qihan Sun, Qingwei Lin, Qiushi Sun, Ruichen Zhang, Shuqing Luo, Si Qin, Sicheng Fan, Tao Xiong, Wenlin Yao, Xinyu Zhang, Xinyue Zeng, Xuanrui Li, Xuchao Zhang, Yian Wang, Yichao Liu, Yiming Liang, Yiyang Zhou, Yizhu Jiao, Yuetai Li, Yurun Chen, Yuxuan Zhang, Zheyuan Yang, Zhiyuan Yao, Zhongyang Li, Zihao Li, Zili Wang, Jianfeng Gao, Huaxiu Yao

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03634v1](https://arxiv.org/pdf/2611.03634v1)

**Abstract**: GUI web agents require realistic and interactive environments that remain stable during both evaluation and training. Live website evaluation suffers from changing content, access restrictions, and limited coverage of authenticated workflows, while existing synthetic environments for training often lack functional depth and visual fidelity. We propose WebHarbor, a suite of 153 executable and dockerized website environments that faithfully reconstruct the visual interfaces, content, and functional workflows of real-world web services under deterministic control. We build WebHarbor through task-driven human-agent collaboration, where environments evolve as new tasks expand their functional scope, coding agents implement the required changes, and human contributors audit visual fidelity, functional correctness, and task validity. The resulting suite comprises 3,518 tasks spanning multi-step and post-authentication workflows, where existing works often fail to cover. Beyond reliable evaluation, WebHarbor provides high-fidelity synthetic web environments for cost-efficient reinforcement learning (RL). We demonstrate that a Qwen 4B-level GUI agent trained with RL in WebHarbor generalizes to unseen tasks and performs competitively with leading open-source GUI web agents across four benchmarks. The code and data are publicly available at https://github.com/aiming-lab/WebHarbor.


### Pretraining Data Scale Reverses the Muon-AdamW Fine-Tuning Gap
**Authors**: Catherine Li, Jingchu Gai, Andrej Risteski, Jacob Mitchell Springer, Aditi Raghunathan

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03633v1](https://arxiv.org/pdf/2611.03633v1)

**Abstract**: Muon has recently emerged as a promising optimizer for pretraining large language models, offering a speedup over AdamW in minimizing pretraining loss. However, it remains unclear whether Muon's advantage persists after fine-tuning. In this paper, we study the downstream behavior of Muon and AdamW and uncover a surprising trend: beyond a sufficiently large pretraining data budget, AdamW outperforms Muon after fine-tuning. Moreover, as model size increases, AdamW overtakes Muon at progressively smaller pretraining token-parameter ratios. To explain this reversal, we view fine-tuning as a perturbation of the outputs and introduce the margin-to-spread ratio, which measures how far the correct logit lies above the wrong ones relative to how widely the wrong logits are spread. In language models, Muon has the larger margin-to-spread ratio at small data budgets and AdamW at large ones, mirroring the fine-tuning trend. In a linear associative memory, we prove that after one update the margin-to-spread ratio of gradient descent gains on that of Muon as the data budget grows, and simulations show that this trend persists after extended training.


### Not All Reasoning Generalizes: A Case Study on Learning Generalizable Reasoning Strategies in RLVR
**Authors**: Ziqi Pang, Yu-Xiong Wang

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03627v1](https://arxiv.org/pdf/2611.03627v1)

**Abstract**: Reinforcement learning with verifiable rewards (RLVR) can enable generalizable improvement for large language model (LLM) reasoning. This paper studies how to incentivize such generalization via reasoning strategies. We study this question with a controllable equation-solving framework: finding multiple inputs x for equations f(x)=y, where f is a non-bijective string function. This setting makes reasoning strategies observable while supporting a clear definition of easy-to-hard out-of-distribution (OOD) shifts, e.g., more solutions, longer y, etc. We uncover a subtle RLVR failure: it teaches the model to solve in-distribution tasks with high accuracy and structured step-by-step derivation, yet under OOD shifts, the same model abandons derivation and collapses to ineffective brute-force enumeration, causing sharp accuracy drops. This observation reveals the deeper challenges of RLVR generalization as it is neither incapable base model nor reward hacking, since the model succeeds in-distribution with the correct reasoning strategy. The key to mitigating this failure is an indirect intervention that surprisingly helps: co-training with bijective inversion tasks. Although these bijective tasks are actually not uniformly harder and even further from the non-bijective OOD evaluation, they make derivation more certain and substantially restore the correct strategy and accuracy under OOD shifts. This effect further motivates our theoretical analysis: outcome-only RLVR can shape reasoning processes through implicitly crediting the effective reasoning strategies more, even without process supervision. To conclude, our analysis framework and findings systematically reveal the crucial role and incentivization of reasoning strategies in RLVR generalization under OOD shifts. Code is available at https://github.com/ziqipang/rl_meta_thinking.


### Isekai3D SDG: A Platform for Diverse Synthetic Gameplay Visual Data
**Authors**: Rafal Karp, Gene Liu, Shih-Hsin Li, Eric Courtemanche, Shengze Wang, Josef Spjut, David Pankratz, Mischa Kolbe, Michael Stengel, Sven Elflein, Adam Grygielski, Liwen Wu, Anjul Patney

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03626v1](https://arxiv.org/pdf/2611.03626v1)

**Abstract**: We present Isekai3D Synthetic Data Generation (SDG), a platform for simulating and capturing synthetic 3D gameplay for research in vision and world models, neural graphics, gameplay agents, and other applications. The platform combines reusable environment and character assets with Unreal Engine plugins in a two-stage workflow. First, world simulation generates gameplay while recording the world state, character movements, actions, and camera tracks needed for replay. Second, the recorded simulation is replayed to capture selected outputs, such as rendered video, images, and depth maps, at a specified resolution and frame rate under selected rendering and camera configurations. Separating simulation from capture allows the same recorded gameplay to produce multiple output variants without repeating the original simulation. Visual outputs are accompanied by frame-aligned camera, character, and action metadata. The platform uploads generated data directly in a training-friendly format, reducing intermediate storage, preparation time, and manual processing. This report describes the design of our overall system, including the platform's assets, plugins, and their functionality, explaining how they work together to generate diverse synthetic gameplay data.


### FADE: Factored Ability--Difficulty Filtering for Online RLVR Scheduling
**Authors**: Tomas Duncun, Jonah Ellison, Mateo Ruiz, Hanae Fujita, Ingrid Solberg

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03625v1](https://arxiv.org/pdf/2611.03625v1)

**Abstract**: Group-based reinforcement learning with verifiable rewards (RLVR) learns only from prompts whose sampled completions disagree: all-pass and all-fail groups produce zero relative advantage and burn generation budget without moving the policy. Adaptive schedulers try to steer rollouts toward informative prompts, yet they rely on per-prompt pass-rate trackers that entangle two quantities evolving at very different speeds---the policy's shifting competence across reasoning skills and each prompt's intrinsic difficulty. When a single exponential average or Beta counter tracks both at once, short memory scrambles the relative ordering of prompts whereas long memory reports stale pass rates. We introduce FADE (Factored Ability--Difficulty Estimation), a bilinear state-space filter that separates the two timescales. FADE represents each prompt's success logit as the inner product of a whitened $K$-dimensional skill loading with a fast-drifting policy ability vector, minus a slow-shrinking scalar item intercept. Using Pólya--Gamma augmentation, each minibatch of binary rollout outcomes updates the $K$-dimensional ability posterior in closed form via a rank-$K$ Woodbury step, instantly transferring competence shifts to all unobserved prompts that share those skills while leaving item intercepts stable. From the resulting posterior mean and variance we derive a closed-form utility for the probability of drawing a non-degenerate rollout group. Across five reasoning benchmarks, two base models, and four scheduling paradigms under a matched rollout budget, FADE consistently improves downstream accuracy and calibration while adding less than $0.6$\,ms per step.


## Generation
### Pixel-UMI: Learning Environment-Aware Whole-Body Manipulation from Sensorized Human Demonstrations
**Authors**: Jason Jingzhou Liu, Tony Tao, Deepak Pathak, Ruslan Salakhutdinov

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03647v1](https://arxiv.org/pdf/2611.03647v1)

**Abstract**: Sensorized human demonstrations offer scalable data for mobile manipulation, but embodiment differences complicate policy learning. We present Pixel-UMI, a pipeline for learning environment-aware whole-body policies from human data. We first introduce Environment-Aware Retargeting (EAR), which combines reconstructed scene geometry with demonstrated head and gripper trajectories to determine robot posture and generate collision-aware joint and base targets. Delay-calibrated action assignment converts these trajectories into actions. However, kinematic differences can leave residual pose errors, creating viewpoint mismatches between human demonstrations and robot observations. We therefore introduce Retargeting-Error-Aware Masking (REAM), which uses these errors during training to reduce reliance on mismatched views at deployment. Finally, because estimated actions cannot fully capture contact-rich interactions, we collect on-policy human corrections through DAgger to improve performance. We evaluate Pixel-UMI on five challenging tasks spanning articulated-object manipulation, deformable-object handling, constrained-space reaching, whole-body collision avoidance, and contact-rich bimanual coordination, achieving 87.0% average task progress. Video results are available at https://pixel-robot.com/pixel-umi


### Pixel: A Co-Designed Full-Stack Robot System for Learning General-Purpose Mobile Manipulation
**Authors**: Tony Tao, Jason Jingzhou Liu, Ruslan Salakhutdinov, Deepak Pathak

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03648v1](https://arxiv.org/pdf/2611.03648v1)

**Abstract**: General-purpose mobile manipulation requires a combination of capable robot hardware, scalable demonstration collection, expressive whole-body control, and effective policy learning. Yet these components are often developed independently, creating mismatches that limit the capabilities of the complete system. We present Pixel, a co-designed full-stack system for learning general-purpose mobile manipulation. Pixel combines a low-cost wheeled humanoid with human-aligned kinematics and compliant grippers, multiple teleoperation and robot-free human data-collection interfaces, a unified whole-body controller, and a common policy learning pipeline across human and robot demonstrations. A hierarchical learning stack further enables language-conditioned visuomotor control and long-horizon task execution. We evaluate the system across hardware, data collection, and policy learning, and demonstrate mobile-manipulation behaviors requiring dexterity, active perception, navigation, and whole-body coordination. We hope that Pixel provides an integrated and extensible foundation for studying how robot hardware, data, control, and learning can be designed together for robot learning. More results at https://pixel-robot.com/pixel


### Thought-deciphering via hierarchical EEG-to-text alignment
**Authors**: Xiaopeng Mao, Morten Mørup, Xin Xu, Sang Wan Lee, Sadasivan Puthusserypady

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03623v1](https://arxiv.org/pdf/2611.03623v1)

**Abstract**: Communication is important for our well-being, but it can be impaired by disabilities, such as locked-in syndrome (LIS), cerebral palsy (CP), and dysarthria. Non-invasive brain-to-text brain-computer interfaces (BCIs) offer a promising solution by providing an alternative communication pathway for people with communication disabilities. However, most recent breakthroughs have relied on large, cumbersome, and costly neuroimaging modalities, such as functional magnetic resonance imaging (fMRI) and magnetoencephalography (MEG). Numerous studies have attempted decoding using the lighter and cheaper electroencephalography (EEG), but the results remain inferior compared to the other modalities. More importantly, we do not understand how these modalities are related to text at the letter, word, sentence, and higher semantic levels. Many prior studies have focused on decoding below the sentence level because it is considerably easier to design an experiment around phonemes, letters, and words. However, during communication, sentences play a much more important role than words and letters. This is because sentences carry information at such a high level that they can be understood even if some words and letters are missing. However, within sentence-level decoding, sentence classification is not as well investigated as sentence generation, making it difficult to decide whether a sentence should be retrieved or generated in the context of EEG-to-text decoding. This paper strives to investigate sentence-level EEG-to-text classification via a novel hierarchical alignment framework, where the main goal is to retrieve a read sentence using its context and EEG as inputs.


### D&A: Decoupling Description and Assessment Enables VLMs as Zero-Shot Robotic Reward Models
**Authors**: Marius Memmel, Shawn Yin, Urvi Rutia, Angad Wadhwa, Eldon Li, Gavin Angeloff, Ankit Goyal, Jesse Zhang, Dieter Fox, Fabio Ramos, Anqi Li, Abhishek Gupta

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03622v1](https://arxiv.org/pdf/2611.03622v1)

**Abstract**: Vision-Language Models (VLMs) hold promise for zero-shot video task-progress estimation in robot learning, yet existing frameworks frequently suffer from confirmation bias, hallucinating progress in failed executions due to implicit success assumptions or relative temporal ranking designs. Naive prompting of frontier models collapses into a binary success detector that fails to capture nuanced, non-linear progress and failures. While post-training approaches can mitigate this through explicit training, they demand expensive real-world robotics data and require computationally intensive post-training for every individual base model. To resolve these limitations, we introduce D&A (Describe & Assess): our approach decouples progress estimation into an objective, task-grounded textual description of scene dynamics followed by an assessment phase using explicit rubrics. By compelling the VLM to synthesize an explicit, text-based definition of absolute success before scoring, the framework anchors evaluations to an external, global criterion rather than the video's internal timeline. Empirical results demonstrate that our method calibrates zero-shot estimates and mitigates confirmation bias, providing fine-grained, partial progress metrics that accurately penalize failed executions while correctly interpolating successful runs. Being purely prompt-based, D&A generalizes across tasks, embodiments, and benchmarks---matching or surpassing post-trained reward models---and its reward estimates enable efficient downstream reinforcement learning.


### Benchmark Prediction with Sparse and Unpaired Cached Responses
**Authors**: Hayden Helm, Avijit Ghosh, Ben Johnson, Carey Priebe

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03614v1](https://arxiv.org/pdf/2611.03614v1)

**Abstract**: Evaluating a generative model on all queries from all available benchmark tasks is prohibitively expensive. As such, models are often evaluated on different subsets of tasks and/or different subsets of queries from a given task. The resulting collection of responses and the corresponding (model, task) score matrix are sparse and unpaired. In this paper, we introduce the Product Kernel Perspective Space (PKPS), a collection of low-dimensional representations of models based on their embedded responses. PKPS generalizes existing methods for representing black-box generative models by comparing responses to similar -- rather than just identical -- queries and is therefore able to utilize sparse and unpaired information. Theoretically, we show that benchmark prediction using PKPS is query-efficient relative to methods that only use information from dense and paired portions of the evaluation data. Empirically, we show that PKPS-based methods outperform baselines on benchmark prediction across two large benchmark suites.


### Structured Visual Landscape: Generating Preferred Representations in Biological and Artificial Neural Networks
**Authors**: Yusong Zhao, Edgar Y. Walker, Hao Wang, Mi Lu

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03597v1](https://arxiv.org/pdf/2611.03597v1)

**Abstract**: Understanding how neurons respond to visual stimulus is an important question in both deep learning and neuroscience. It has significant implications for enhancing the interpretability of black-box artificial neural networks and for understanding the visual representation in the human brain. We propose a structured visual representations landscape and design an activation-based prior that allows us to effectively regularize the landscape with activations from brain regions or neural network units. Our model Vis-Lens integrates a variational autoencoder and a diffusion model into an image generation framework. It enables the generation of natural, realistic preferred images by directly modifying the activation-regularized latent codes without per-image iterative optimization. We demonstrate the effectiveness of our framework on both artificial neural networks and human visual cortex using functional magnetic resonance imaging (fMRI) data. Our framework improves activation modulation and image realism compared with a recent state-of-the-art method for generating preferred visual representations of these neural targets.


## VLA
### RoboColosseum: Evaluating Physical Intelligence at Scale In-The-Wild
**Authors**: Tan Sang Nguyen, Yi Ru Wang, Shailesh Shailesh, Gang Yang, Jiamo Hu, Jianuo Jiang, Haoquan Fang, Zhongzheng Ren, Zhongyi Luo, Ian Chong, Aaron Tung, Santiago Pravisani, Minghui Lin, Yao Mo, Ishneet Singh, Benjamin Tee, Harold Soh, Siddhartha Srinivasa, Dieter Fox, David Hsu, Haoming Song, Maxime Ellerbach, Thomas Wolf, Pepijn Kooijmans, Ruijie He, Michael Cho, Jiafei Duan

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.02497v1](https://arxiv.org/pdf/2611.02497v1)

**Abstract**: General-purpose robot policies must work across robots, tasks, and environments, yet the variation that makes physical trials informative also makes them difficult to reproduce. We introduce RoboColosseum, a distributed evaluation framework that combines unified policy serving and standardized protocols across a network of locally operated robots in diverse environments. Our initial study evaluates five vision-language-action (VLA) policies and three frontier AI agents across four embodiments (SO-101, Franka, Bimanual-YAM, and G1 Humanoid). The Open Track compares models without task-specific adaptation in blinded, pairwise trials under matched local conditions. The Fine-tune Track measures how well VLA policies adapt to 20 tasks across all four embodiments when each policy receives the same 100 demonstrations per task. Across 5,699 pairwise Open Track comparisons at 124 sites, frontier agents rival specialized VLA policies, while all systems struggle to complete open-world tasks reliably. After fine-tuning, GR00T N1.7 leads on SO-101 and pi0.5 leads on Franka and Bimanual-YAM. Policy rankings show weak agreement across embodiment-specific task suites (Kendall W = 0.24). Open Track rankings poorly predict relative performance after fine-tuning, with substantial rank reversals on all three embodiments shared between tracks. Measuring partial progress reveals differences that task success alone misses. On the G1 Humanoid, no policy completes any of the five tasks, yet average progress ranges from 13.3% to 23.2% across policies. Open Track rankings stabilize as trials accumulate, and active matchmaking achieves comparable ranking agreement with substantially fewer physical trials than uniform sampling. These results show how distributed physical evaluation can reveal where robot policies generalize, how well they adapt to new tasks, and how far they progress on tasks they fail to complete.


### Scene-Adaptive Readout and Decoding in Diffusion Driving VLAs
**Authors**: Seungjun Yu, Jiho Choi, Inha Kang, Hojun Choi, Seungwook Kim, Hyunjung Shim

**Published Date**: 2026-11-01

**Updated Date**: 2026-11-01

**PDF Url**: [2611.02076v1](https://arxiv.org/pdf/2611.02076v1)

**Abstract**: Diffusion driving vision-language-action models repeatedly execute the backbone at every denoising stage, incurring substantial inference cost, while it remains unclear whether all scenes require the same decoding computation. To distinguish when a trajectory becomes readable from how much further refinement it requires, we analyze trajectory readout across network depth and decoding progress. We identify a depth-decoding dissociation in which late-layer representations already support useful trajectory readout after the first forward sweep, whereas early-layer representations benefit more from continued decoding. We further find that both the preferred readout layer and decoding depth vary across scenes. Based on these observations, we propose a scene-adaptive readout and decoding framework. A scene-conditioned readout MoE adaptively weights and combines trajectory predictions from layer-specific late-layer representations after a single backbone sweep, while an adaptive decoding policy applies additional native refinement only when required by the scene. We evaluate our framework on two diffusion driving VLAs across the Waymo E2E and nuScenes benchmarks. Our method improves validation RFS by up to 0.56 while also improving test performance, and achieves an end-to-end speedup of up to $6.0\times$ on Waymo E2E, while consistently reducing trajectory error on nuScenes. These results demonstrate that scene-level readout and decoding allocation improves planning quality while avoiding unnecessary decoding. Our code is available at https://github.com/sjyu001/SARD


### Route-Guided CBF-QP Repair for Safe Vision-Language-Action Models
**Authors**: Chan Park, Sunwoo Hong, Kirak Kim, Yoonjeong Park, Alexander W. Olson, Ali Pesaranghader

**Published Date**: 2026-11-01

**Updated Date**: 2026-11-01

**PDF Url**: [2611.01713v1](https://arxiv.org/pdf/2611.01713v1)

**Abstract**: Vision-language-action (VLA) models can generate task-oriented robot actions, but they do not guarantee safe execution in obstacle-rich manipulation scenes. Although CBF-QP safety filters can locally project unsafe actions into a safe set, such correction may push the robot away from the learned task trajectory and leave the VLA policy without a reliable recovery direction. We propose Route-Guided CBF-QP Repair, a post-hoc repair module that uses the short-horizon action chunk predicted by the VLA to detect blocked nominal trajectories and generate entry-exit-rejoin guidance around obstacles. The selected route is added to the CBF-QP objective as a soft guidance term, while the CBF safety constraint remains hard. On SafeLIBERO, our method improves collision avoidance, task success, and SafeSuccess compared with AEGIS. Our project page is available at GitHub.


### SCOUT: Planning under Occlusion via Object-Centric World Model Rollouts
**Authors**: Amir Hossain Raj, Xuesu Xiao

**Published Date**: 2026-11-01

**Updated Date**: 2026-11-01

**PDF Url**: [2611.01600v1](https://arxiv.org/pdf/2611.01600v1)

**Abstract**: Robots manipulating in cluttered spaces must often plan from partial views where foreground objects occlude the target, surrounding geometry, and usable free space. Reactive policies often miss these hidden constraints, while exhaustive search becomes computationally prohibitive in dense clutter. We present SCOUT, an occlusion-aware planning framework that bridges high-level deliberation with grounded physical rollouts. SCOUT leverages an object-centric scene representation to reconstruct hidden geometry and derive a relational planning state capturing blocker hierarchies and accessibility corridors. To navigate the vast action space in clutter, an LLM proposes structured action candidates which are then rigorously evaluated via Monte Carlo Tree Search (MCTS) using a learned action-conditioned world model. Evaluations on 'Reveal' and 'Placement' tasks show that SCOUT outperforms Vision-Language-Action (VLA) policies, embodied agents, and 3D world models, with significant gains in long-horizon tasks requiring reasoning over occluded geometry. We further validate the framework's robustness through real-world robotic manipulation in a cluttered shelf environment.


### Same Path, Less Time: Training-Free Fast Execution of Vision-Language-Action Models under Inference Latency
**Authors**: Fuyi Chen

**Published Date**: 2026-11-01

**Updated Date**: 2026-11-01

**PDF Url**: [2611.01390v1](https://arxiv.org/pdf/2611.01390v1)

**Abstract**: Vision-language-action (VLA) models predict chunks of future actions, yet deployed robots waste time in two ways that are independent of model capability: they halt while the next chunk is inferred, and they move at the speed of slow, cautious demonstrations. Existing remedies remove one loss each, and stacking them fails, because asynchrony and speed-up each change the correspondence between planned progress and executed motion. We present Path-preserving Time Scaling (PTS), a training-free execution layer for frozen action-chunking policies built on one principle: the robot's motion is a time reparameterization of a reference path, and the path changes only in response to new observations. A path layer decodes every replan deterministically in one step and enters it at the progress consumed during inference. A time layer sums the planned increments, keeps the arm at 1x while the gripper moves, and caps the rate by the actuator's linear range and by chunk feasibility under latency. We show that misaligned entry and stochastic sampling add a bias and a variance to the continuation error, and derive a break-even success rate that states when speeding up pays off. On LIBERO with two frozen VLAs under injected inference latency, PTS raises task throughput over the strongest deployable baseline by 33% for pi0.5 and 104% for SmolVLA while matching or improving the success rate, is best on all six model-suite combinations, and exceeds zero-latency 1x execution. Against asynchronous 1x execution with the same one-step decoder, the time layer alone adds 28% and 38%. On LIBERO-Dynamic it improves on stop-and-wait execution by 38% and is comparable to asynchronous 1x execution.


### Vision-Language Models Are Joint Denoisers in Robotic Action Generation
**Authors**: Xicheng Gong, Wenxuan Song, Chengze Liu, Qiwei Li, Qize Yu, Jiaolong Yang, Haoang Li, Yadong Mu

**Published Date**: 2026-10-31

**Updated Date**: 2026-10-31

**PDF Url**: [2611.01215v1](https://arxiv.org/pdf/2611.01215v1)

**Abstract**: Diffusion-based vision-language-action (VLA) models cascade pretrained vision-language models (VLMs) with diffusion action experts, but typically restrict the VLM to providing static conditioning. This separation limits how much pretrained perception and reasoning can guide action generation, especially in out-of-distribution settings. We introduce JADE, a Joint Action DEnoiser that enables the VLM and action expert to jointly refine actions. Our key insight is that structured action latents allow the VLM to read the current noisy action together with visual observations and language instructions. At every denoising step, the VLM contextualizes the noisy action and guides the action expert through gated cross-attention, so that its guidance evolves with the action being generated. We further supervise the VLM to recover clean action latents from noisy ones, which gives it a direct action-learning signal and couples perception with control. Additionally, joint denoising enables JADE to generate actions with fewer sampling steps, helping offset the additional cost of VLM participation. An adaptive step-size schedule further balances task performance and inference latency. On RoboDojo, JADE achieves an average success rate of 12.67%, the highest among the evaluated $π_{0.5}$-based methods, and is competitive with recent VLA and WAM foundation models pretrained at scale. It also improves performance on RoboTwin 2.0 and raises the average success rate across four real-world bimanual tasks by 20.8 percentage points compared with $π_{0.5}$.


## Agent
### Strategist: Evolving Reasoning with Agents
**Authors**: Taiming Lu, Qi Xu, Zhigang Hua, Zhuang Liu

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03618v1](https://arxiv.org/pdf/2611.03618v1)

**Abstract**: A model is only half of an AI agent system. The other half is the inference strategy: the reasoning procedure that turns model calls into a response. Today that second half is written by hand, and the experience of building one strategy never carries to the next. We introduce Strategist, a meta-agent that evolves inference strategies across tasks. Each strategy is written as a blueprint,executable code that other strategies can reuse, and together the blueprints form a library. Given a task and a small development set, Strategist retrieves related blueprints, writes candidate strategies, tests them on real samples, and revises them from the results. Every candidate then enters the library, so later tasks build on earlier discoveries. On 30 benchmarks, Strategist beats the strongest baseline on 24 and matches its average accuracy (74.7% vs.74.0%) at 39% lower inference cost. Its strategies also transfer to unseen tasks and other models without further search. The part of an AI system that is not improved on its own now does.


### DiabAgent: Toward Agentic Physiological Control
**Authors**: Chengxi Li, Shaoxuan Li, Deyao Hong, Qingle Liu, Yi Huang, Puheng Bian, Minzhi Xu, Lanyue Zhang, Mingze Sun, Xin Li, Calvin Xiao, Shengyuan Wang, Huan-ang Gao, Jiazheng Xu, Kaisen Yang, Hongning Wang

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03601v1](https://arxiv.org/pdf/2611.03601v1)

**Abstract**: As pretraining scales, medical language models have advanced rapidly in clinical question answering. Their ability to achieve effective physiological control through sustained intervention still lacks systematic quantitative evaluation. Type 1 diabetes provides a concrete setting: impaired insulin secretion creates dependence on exogenous insulin, with dosing continually adjusted using information about meals, exercise, illness, and glucose measurements. We introduce DiabAgent, a research suite for agentic physiological control comprising the Agentic Physiological Control (APC) framework, the DiabetSim simulator, and the SweetBench benchmark. APC controls glucose through medical-device tools, using ongoing observations to infer individual states, accumulate personal experience, and choose treatment actions. We build DiabetSim to simulate different patients, events, and device conditions for scalable virtual testing and training. Using DiabetSim, we construct SweetBench by instantiating 32 scenario designs as 212 glucose-control tasks. With Claude Opus 5.5 and a fixed decision interval of one hour, APC achieves a COGI of 73.5, compared with 71.2 for the open-source closed-loop baseline OpenAPS. Ablations further show that individual adaptation and contextual information improve glucose control. Combining high-frequency rule-based control with lower-frequency agent decisions shows potential for balancing control performance and computational cost. Our work provides a framework, simulator, and evaluation foundation for agents to participate in human physiological control.


### Four Bridges: Measuring Deception Propensity in a Multi-Agent Game
**Authors**: Raphael Casey, Michael Simeone, Alberto Tosato, Florian Ernst, Kemal El Moujahid, James Tamplin, Tommaso Tosato

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03600v1](https://arxiv.org/pdf/2611.03600v1)

**Abstract**: AI agents are increasingly deployed in settings where they interact and coordinate with other agents, yet honesty is mostly measured in single-turn, single-agent benchmarks that pressure the model to deceive. We study deception that emerges in multi-agent interaction without any instruction to deceive. We introduce Kradle, a platform for evaluating AI models, and Four Bridges, an information asymmetry game in which four agents distribute across four rooms: one is the death room, the others hold food worth more if not shared. One agent, the informed agent, knows which room is the death room and can withhold or disclose that information. We evaluate eight frontier models as the informed agent. Deceptive behavior appears in every model and in 73% of all runs (6% to 100% per model), and does not decrease with capability tier within a model family. When the informed agent does disclose, the warning is often challenged, and agents that challenge it enter the death room twice as often as those that do not. Telling all agents that one of them knows the death room collapses deception in six of eight models; telling the informed agent that the room is permanently fatal moves only one. On an open-weight model, an honesty steering vector reduces deception to 0% and adversarial honesty training to 6%. The platform and game provide a testbed for measuring deceptive behavior and comparing interventions.


### Should We Combine Our Data? Algorithms and Limits for Privately Assessing Data Sharing
**Authors**: Mahdi Haghifam, Kumar Kshitij Patel, Avrim Blum, Giulia Fanti, Juba Ziani

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03599v1](https://arxiv.org/pdf/2611.03599v1)

**Abstract**: In this paper, we study when two parties should pool their data to train a machine learning model. Two agents, Alice and Bob, each hold a sensitive labeled dataset and want to train a classifier from a given hypothesis class $\mathcal{H}$. Even when each party's dataset can be perfectly classified on its own, the two parties may follow conflicting labeling standards or have selection biases that affect their features and label sets, such that no single classifier in $\mathcal{H}$ fits their combined data. Before committing to data sharing, Alice and Bob therefore want to test whether a single classifier in $\mathcal{H}$ can jointly fit both datasets---without revealing their individual data points to one another.
  We formalize this problem from a learning-theoretic viewpoint via $\operatorname{opt}_\mathcal{H}$, the minimum \emph{number of mistakes} made by any hypothesis in $\mathcal{H}$ on their pooled data. Through interactive communication, the agents must distinguish $\operatorname{opt}_\mathcal{H}=0$ (compatible datasets) from $\operatorname{opt}_\mathcal{H}\geq t$ (conflicting datasets) under pure $\varepsilon$-two-party differential privacy. A trusted curator could do this with $t=O(1/\varepsilon)$, and we ask how small $t$ can be without one. For thresholds on the real line over a domain of size $m$, we show that the optimal $t$ is $\tildeΘ(\log\log m/\varepsilon)$, exponentially smaller than the $Θ(\log m/\varepsilon)$ samples needed to privately learn thresholds, even with a curator. For halfspaces in $\mathbb{R}^d$, the dependence on $m$ jumps to $\log(m)$: we give a protocol with $t=\tilde{O}(d^3\log m/\varepsilon)$ and show that some domains require $t=Ω(d\log(m/d)/\varepsilon)$.


### Spacetime Emergence in the Memory of a Learning Agent
**Authors**: Philip A. LeMaitre, T. Rick Perche

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03596v1](https://arxiv.org/pdf/2611.03596v1)

**Abstract**: We show that the causal structure of spacetime can emerge within the memory of a learning agent performing a quantum information task. We train a model-based reinforcement-learning agent to maximize the quantum mutual information between localized quantum probes interacting with a quantum field in Minkowski spacetime, without directly providing it with information regarding the spacetime metric or causal structure. In learning to accomplish this task, the reinforcement-learning agent constructs an internal predictive model whose planner develops the characteristic null structure of spacetime, allowing us to reconstruct the causal structure of the Minkowski metric with high accuracy. Within this task, spacetime geometry is obtained from an agent's successful predictions and actions, providing a first step toward showing that spacetime concepts emerge from operational quantum experience.


### FedReady: Bounded Agents for Federation Formation
**Authors**: Ziyue Xu, Holger R. Roth, Chester Chen, Peter Cnudde

**Published Date**: 2026-11-02

**Updated Date**: 2026-11-02

**PDF Url**: [2611.03586v1](https://arxiv.org/pdf/2611.03586v1)

**Abstract**: Federated learning (FL) runtimes standardize aggregation and deployment, but each new study still requires federation formation: selecting task-eligible sites and preparing their local data and task code for federated training or analysis. This preparation recurs when the target changes, while raw records and site-private mappings are excluded from cross-site FL messages. We present FedReady, a system that performs federation formation with bounded LLM agents. Agents propose shared contracts, local adapters, and task code; the runtime owns workflow state and accepts artifacts only after checks tied to their digests. Candidate site discovery prioritizes recall; local eligibility verification checks task support before site admission. Once participating sites and artifacts are fixed, conventional federated training or analysis proceeds without readiness agents. Across 39 simulated retinal sites and four tasks, discovery reaches recall 1.00 at precision 0.65; local eligibility verification removes all 17 false positives without losing an eligible site-task pair. The participating sites supply 45,575 task-record instances and complete four 100-round jobs, including one with a runtime-generated contract. Across ten patient cohorts, preparation supports seven patient populations and holds endpoints at three sources as unsupported. Comparison with manually prepared reference populations and analysis (the manual reference) gives a maximum survival-curve difference of 0.001133. We also analyze 19 development failures, targeted classification ablations, and standalone and heterogeneous agent configurations. These results establish the feasibility of task-specific data preparation before ordinary FL training or analysis.


