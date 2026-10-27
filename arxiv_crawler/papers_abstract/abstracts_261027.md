# Abstracts of Papers

## World Model
### Retriever-Free Retrieval: Navigating Documents with Decision Models
**Authors**: Chao Wan, Paul Jünger, Beixi Du, Bodong Liu, Navaneetha Krishnan, Kilian Q. Weinberger

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35868v1](https://arxiv.org/pdf/2610.35868v1)

**Abstract**: While language models have become dramatically more capable, retrieval still largely relies on lexical matching or similarity in fixed embedding spaces. This creates a capability asymmetry: what the retriever fails to find, even the strongest generator cannot recover. We propose DecisionRAG, which brings the capabilities of pretrained language models to retrieval using decision models that jointly evaluate candidate branches in a single forward pass, without generating any tokens, and show that judging candidates in a shared context makes their relevance estimates comparable. Like a person browsing a library, DecisionRAG navigates the corpus's inherent structure from broad topics down to individual passages, deciding at each level which branches are worth exploring. Without task-specific training or a first-stage retriever, DecisionRAG outperforms dense retrieval with an 8B reranker by 13.8 R@1 points on MultiDoc2Dial and 17.4 Hit@1 points on Natural Questions. Across four benchmarks, including a corpus of 2.68 million Wikipedia paragraphs, retrieval takes just 0.7-1.8 seconds per query.


### Center-of-Mass Interpretation of Evolution Strategies
**Authors**: Akshat Gupta

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35865v1](https://arxiv.org/pdf/2610.35865v1)

**Abstract**: Evolution strategies (ES) update a model by sampling a population of perturbed copies, scoring each one, and moving in the reward-weighted direction of the perturbations. This update is usually presented as an estimate of a smoothed gradient. We present a geometrical interpretation of this update instead. Treat each perturbed model as a particle and its reward as the particle's mass. Before scoring, every particle has the same mass and the population balances at its centroid. Once rewards are assigned, it balances at its reward-weighted center of mass instead. We show that the mean-subtracted ES update is exactly this displacement, scaled by a scalar factor that depends on the mean reward, for any finite population. The physical reading needs nonnegative rewards, which can always be arranged by adding a constant to every reward without changing the update. In the limit of a large population or under antithetic sampling, the centroid sits on the model itself, so ES has an even simpler geometric interpretation: from its current location, the model moves towards the reward-weighted center of mass of its own population. The same picture explains what subtracting the mean reward does: it changes the point from which the displacement is measured, from the model to the sampled centroid. Our contribution is an intuitive, geometric way to visualize an ES update, exact for any finite population.


### Auto-Research Arena: Benchmarking and Advancing Auto-Research in Language Modeling
**Authors**: Xi Chen, Chongjian Ge, Yiran Xu, Yiqun Mei, Henrik I. Christensen, Hao Tan, Ziwen Chen, Hanwen Jiang

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35866v1](https://arxiv.org/pdf/2610.35866v1)

**Abstract**: As autonomous research systems become more capable, benchmarks must both evaluate their performance and support meaningful research progress. We introduce Auto-Research Arena, a multi-target benchmark for evaluating autonomous research systems and discovering ideas in language modeling. Arena supports diverse research objectives within a shared experimental environment by separating admissibility from improvement: model quality and resource constraints determine whether a result qualifies, while the selected target measures progress among admissible results. We instantiate Arena in language model pretraining with nine targets spanning model, data, training, and inference efficiency, and evaluate seven research harnesses using two foundation models. Arena clearly differentiates existing harnesses across research objectives, with several sophisticated methods outperformed by our simple sequential search baseline, indicating substantial headroom in current auto-research systems. Beyond evaluation, Arena reveals a substantially broader frontier of model and system ideas aligned with active research directions. Reusing these discoveries in a new quality-driven search yields lower training loss under matched data and FLOPs and lower held-out BPB at the same model size. Together, Arena provides a common framework for benchmarking autonomous research and expanding its scope in language modeling. The code is available at https://github.com/Auto-Research-Arena/auto-research-arena


### On the stability of learning
**Authors**: John J. Vastola

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35856v1](https://arxiv.org/pdf/2610.35856v1)

**Abstract**: Learning algorithms are usually analyzed under the assumption that informative gradients are continuously available. But this is not always true---learning signals in biological neural networks, for example, may be sparse, local, and only intermittently available at any given synapse. In this work, we show that if gradient information is noisy and only intermittently available, learning may be unstable. In particular, even if average learning dynamics converge to the correct optimum, variance in learning may be asymptotically infinite. We explore this point in a number of analytically tractable settings, including single-layer and multi-layer linear networks, and derive explicit conditions under which learning is stable. These conditions complement, but are conceptually distinct from, existing conditions related to the stability of stochastic gradient descent. Our work demonstrates that unbiased credit assignment is not enough for reliable learning; sufficiently frequent and informative feedback is also required, which yields an additional constraint on models of biologically plausible learning.


### FL4N: Feed-forward Latent Model for 4D Novel View Synthesis
**Authors**: Eunbeen Hong, Hyeonseo Yu, Honggyu An, Jooho Son, Hyunah Ko, Soowon Son, Chaehyun Kim, Jahyeok Koo, Jisoo Kim, Junhwa Hur, Seungryong Kim

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35854v1](https://arxiv.org/pdf/2610.35854v1)

**Abstract**: 4D novel view synthesis (NVS) aims to render dynamic scenes across viewpoints and timestamps, which requires jointly inferring 3D structure and temporal dynamics. Existing monocular feed-forward methods often rely on explicit 4D Gaussian representations, which are prone to temporal inconsistency and severe rendering artifacts. We present FL4N, the first feed-forward latent 4D NVS model. Instead of relying on explicit 4D primitives, FL4N encodes a 4D scene prior into a unified latent representation across space and time. Our core insight is that learning temporal dynamics as residuals on top of a pretrained static latent prior enables effective 4D modeling with limited dynamic training data. To this end, we introduce a lightweight dynamic encoder that leverages static scene features to disentangle object motion from camera-induced parallax. Trained solely with an image synthesis objective, FL4N achieves state-of-the-art 4D NVS quality while rendering in real time. Its learned latent representation generalizes to real-world videos and disentangles viewpoint from time.


### OSWAM: An Effective World Action Model with One-Step Action Generation
**Authors**: Guowen Zhang, Liyi Chen, Xu Hu, Pengfei Wang, Jingfan Chen, Chenhang He, Lei Zhang

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35850v1](https://arxiv.org/pdf/2610.35850v1)

**Abstract**: Direct-policy World Action Models (WAM) have demonstrated the benefits of decoupling action generation from explicit future visual prediction for efficient inference in autonomous driving and embodied control. However, they still require tens of denoising steps to achieve competitive action quality, incurring substantial latency and hindering real-time deployment. Simply reducing the number of denoising steps will collapse the nonlinear multi-step denoising trajectory into coarse updates, substantially degrading action quality. To reduce the denoising steps while enabling real-time action generation, we present an effective world action model with one-step action generation, namely OSWAM, for autonomous driving and embodied control. We argue that it is the absence of structured action priors in random noise initialization that forces direct-policy WAMs to recover coherent action sequences through iterative denoising. Hence, we construct imagination tokens to initialize the diffusion process, providing physical priors and action-conditioned representations. We further introduce privileged information distillation with future conditioning to enhance future-aware action generation. As a result, OSWAM can efficiently and effectively generate high quality actions in just one diffusion step. Our experiments demonstrate that OSWAM achieves comparable or even better results in both autonomous driving and embodied control than direct-policy WAM and Joint-WAM that require tens of steps. It obtains approximately $3\times$ speedup over direct-policy WAM baselines and supports real-time compiled inference with latency as low as 40ms on an NVIDIA RTX 5090 GPU. The project page is available at https://gwenzhang.github.io/OSWAM/


## Generation
### Patient-specific rubric-based evaluation of large language models across longitudinal cancer care
**Authors**: Wei-Wei Zhang, Pengkai Wang, Yan Li, Zhijie Sang, Guan-Qun Zhou, Jun-Yan Li, Shu-Han Zhou, Pei-Wen Liu, Ting-Xi Tang, Min Tang, Zhitian Hou, Jianmin Wu, Jian Guan, i Lin, Hongxia Yang, Ying Sun

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35847v1](https://arxiv.org/pdf/2610.35847v1)

**Abstract**: Large language models (LLMs) show promise in specialty medicine, yet existing evaluations largely focus on isolated clinical encounters rather than tracking how clinical responsibilities evolve across a longitudinal care pathway. Here we introduce NPC-RubricBench, a phase-aware benchmark for evaluating multistage clinical reasoning across the cancer care continuum, using nasopharyngeal carcinoma as a defined disease context. Curated from longitudinal records of 405 patients across two cancer centers, the benchmark comprises 941 patient-phase units across six sequential care phases and 17,688 patient-specific atomic criteria spanning five evaluation dimensions, with each assessment strictly restricted to decision-time clinical evidence. Evaluating 30 general-purpose and medical LLMs revealed that strong diagnostic performance does not carry over to downstream care. We evaluated 30 general-purpose and medical LLMs, showing that high diagnostic performance did not translate into improved downstream care. Instead, the dominant failure modes reversed across phases. Explicit decision errors dominated anatomical staging at 48.2%, whereas decision omissions dominated initial work-up and post-treatment follow-up at 33.4% and 30.4%, respectively. In the evaluated model set, medically adapted models showed higher omission rates than general-purpose models. Moreover, varying query granularity exposes a critical specification trade-off: broad open-ended requests degrade Decision Quality across all 30 models, while more detailed, checklist-like prompts raise Decision Quality but reduce Evidence Faithfulness and Safety Adherence. Furthermore, NPC-RubricBench demonstrates that static diagnostic benchmarks are insufficient to ensure consistent clinical reliability over time, highlighting the importance of phase-adaptive safeguards in multistage medical AI.


### Work Agents: Systems, Capabilities, and Optimization
**Authors**: Zishan Xu, Enjun Du, Mingqi Gao, Cheng Yang, Junhao Shen, Zirong Chen, Zhiyuan Yao, Yifu Guo, Yuquan Lu, Jinyang Huang, Zhengxi Lu, Siyi Liu, Ziyu Zheng, Yongqi Zhang, Difan Zou, Weiwen Liu

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35845v1](https://arxiv.org/pdf/2610.35845v1)

**Abstract**: As foundation models evolve from information generation to digital work execution, agents are increasingly capable of completing complex tasks across tools, applications, and workflows. However, existing research lacks a unified perspective on how agents reliably accomplish delegated work. To address this gap, we present a work-centric, system-level perspective that views work agents as systems combining foundation models and runtime harnesses to execute tasks in stateful workspaces and deliver verifiable outcomes. We introduce two complementary dimensions, work persistence and work openness, to characterize working conditions, and classify digital work into five forms according to task scope and organization. Building on this framework, we identify five core capability families required for reliable work execution and examine approaches to model optimization, harness optimization, and their joint optimization. We further analyze existing evaluation methods and metrics from the perspective of work outcomes. Finally, we discuss future research directions, including sustained work delegation, adaptation to open environments, and the interaction between work execution and capability improvement. This paper provides a unified framework for understanding, optimizing, and evaluating work agents, supporting the development of systems capable of delivering reliable, verifiable, and practically valuable work outcomes.


### Information-Theoretic Secure Aggregation With Heterogeneous Client Quantization
**Authors**: Shreya Meel, Sennur Ulukus, Itzhak Tamo

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35833v1](https://arxiv.org/pdf/2610.35833v1)

**Abstract**: In federated learning (FL), secure aggregation enables a server to compute the sum of local model updates of $N$ clients, without revealing any information on the individual model updates to the server, beyond their sum. Different clients may be subject to heterogeneous bandwidth constraints, and consequently may choose different numbers of quantization levels to represent the information they send. Most secure aggregation works require the clients to project the values of their update parameters to a common finite group (or field), which does not directly accommodate heterogeneous precision constraints on their transmitted masked updates. Existing approaches of secure aggregation with heterogeneous quantization levels reveal partial aggregates of model-updates, and can reveal segments of individual model updates, under certain dropout and client-server collusion patterns. To prevent this privacy breach, we propose an information-theoretic secure aggregation scheme that tolerates client drop-outs, and up to $T$ semi-honest clients that collude with each other and with the server, under heterogeneous quantization at clients. Our protocol utilizes the $(T+1, N)$ threshold black-box secret sharing construction, where secret shares of the client updates, despite belonging to distinct algebraic groups owing to different quantization, are generated from identical linear integer systems.


### Profiling a Frontier Agent with EBench: From Direct Control to Harness with Policy
**Authors**: Yifei Yao, Yude Zou, Guanbo Jiao, Xing Gao, Ning Gao, Yukai Wang, Jiantong Chen, Zihou Zhu, Xinyu Li, Ningyu Yan, Shuai Wang, Jianming Ma, Haoyu Guo, Weinan Zhang, Chunhua Shen

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35832v1](https://arxiv.org/pdf/2610.35832v1)

**Abstract**: Frontier multimodal large language models (MLLMs) can control robots without robot-specific training, but how their capabilities compare and interact with post-trained vision-language-action (VLA) and world action model (WAM) policies across manipulation demands remains to be thoroughly evaluated. In this report, we evaluate GPT-6-Astra on EBench as the core of an agent that controls a robot through an agent harness under the same visual and proprioceptive observation protocol as post-trained policies. We study two agent configurations: direct control, in which the agent generates waypoint commands directly, and harness with policy, in which it can also invoke a post-trained VLA or WAM policy for action execution. Under direct control, the agent achieves competitive overall performance relative to post-trained policies. It leads on short-horizon tasks and exhibits the least performance variation across generalization dimensions, whereas it underperforms post-trained policies on long-horizon tasks, tabletop manipulation, and high-precision contact-rich tasks. In the harness with policy, invoking a post-trained VLA or WAM combines the complementary strengths of both components, raising overall task success to the level of the strongest compared post-trained policies while substantially reducing token cost. However, performance remains below the per-task upper bound of the standalone components due to suboptimal policy invocation, fixed-instruction execution without subgoals, and grasp disruption when the agent resumes control. Overall, our study characterizes the capability boundary of a frontier MLLM agent and suggests directions for improving future agent harness design. Project page: https://internrobotics.github.io/EBench-Astra-Tech-Report/


### Reva: Real-Time Vulnerability Detection through Contextual Probing of Large Language Models
**Authors**: Amine Lbath, Massih-Reza Amini

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35829v1](https://arxiv.org/pdf/2610.35829v1)

**Abstract**: A vulnerability costs more to fix the later it is discovered. As coding agents generate code faster than developers can review it, software needs a first line of defense screening each new function in real time. LLM agents have recently become capable of finding real-world vulnerabilities by working as a security expert would: they run analysis tools, explore the surrounding code, test hypotheses and weigh the evidence before forming their own judgement. This reasoning, however, spans many model calls, so that each verdict takes minutes of compute, far too long for real-time screening. Faster detectors, which fine-tune deep learning models or prompt an LLM for a direct verdict, are less accurate: they judge a function without the context an agent gathers, and an LLM's generated verdict is unreliable even when given some of it.
  We present REVA (REal-time Vulnerability Analysis), an AI vulnerability detector that brings the security context and code understanding components behind agentic detectors into a single forward pass of an LLM. For each new function, REVA gives the LLM a pre-computed threat model of its module, lightweight static analysis findings and call-graph information. REVA leverages a trained probe to read the LLM's internal representations of the new function in this context. On PrimeVul's held-out test set, REVA on GLM-5.3-Flash reaches 60.0% accuracy in about one second per function. This matches VulTriage (59.2%), the state-of-the-art agentic detector, run on the same LLM, while being over 250 times faster and less than a tenth as costly. On the same prompt, the probe is 14% to 17% more accurate than the LLM's own direct verdict. Across three open LLMs, REVA is at least as accurate as VulTriage, and about 10% more accurate on two of them. An LLM's internal representations thus encode much of what agentic detectors obtain through reasoning.


### Pretraining Knows What, Simulation Teaches How: Compositional Generalization in a Sim-Trained Robot Agent
**Authors**: Benjamin Pikus, Daniel Saunders, Mircea Mironenco, Salman Mohammadi, Mathew Mathew, Sirou Zhu, Divya Makkar, Xuhua Huang, Qinbo Li, Supreeth Narasimhaswamy, Siyuan Cen, Thomas Neff, Dejia Xu, Shyamal Buch

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35817v1](https://arxiv.org/pdf/2610.35817v1)

**Abstract**: A robot policy needs to understand what a task is asking for in a scene, and how to move the robot to accomplish that task. To achieve these two skills, we introduce Zero-real Agent Policy (ZAP), a recipe that teaches a small off-the-shelf vision-language model to control a robot via a simple tool harness. We use a pretrained 27B parameter model to bootstrap world understanding and reasoning, followed by supervised fine-tuning and GRPO on simple simulated tasks to teach it how to move the robot. Without any real-world robot data during training, ZAP reaches 96.7% success on real-world tasks, matching GPT-6 Astra in our harness and outperforming the MolmoAct2 VLA (33.3%), while running 3x faster and 17x cheaper than GPT-6 Astra. We demonstrate that ZAP also generalizes to completely new objects, goals, strategies, and language by seating a test tube in a rack (and choosing a different hole in the rack when prompted), handing a test tube between arms mid-air, drawing an X on a tic-tac-toe board, and playing chess. These goals and types of manipulation don't appear in our training data. Furthermore, ZAP also transfers to an unseen embodiment. On a single-arm Franka, ZAP reaches 55.9% on RoboLab-120, 4.9 percentage points ahead of the leading VLA/WAM baseline.


## VLA
### VLA-HWBench: Where the Time Goes When VLA Models Run on Edge Hardware
**Authors**: Borui Xu, Hongshi Tan, Wenqi Jiang, Bingsheng He, Ming Wu, Jason Zeng, Michael Heinrich

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.34717v1](https://arxiv.org/pdf/2610.34717v1)

**Abstract**: Vision--language--action (VLA) models increasingly run on edge devices aboard robots, where inference latency constrains closed-loop robot control. However, it remains unclear how to design VLA models, their inference software and edge hardware so that robots can run VLA inference in real time. Most VLA models report only task success, while prior studies cover limited action-generation strategies, divide inference into at most three stages, and lack comparisons of inference optimizations on the same models.benchmarking 18 open VLA models across released and alternative backends on NVIDIA Jetson AGX Thor and AMD Ryzen AI Max+ PRO 395, with a seven-stage inference breakdown. Our study reveals three insights. First, action-generation strategy matters more than model size. It dominates 14 of 19 Jetson configurations, latency varies by $82\times$ on Jetson and $157\times$ on AMD, and parameter count explains at most 15% of latency variance. Models that generate long action chunks in a few flow-matching steps keep up with control, whereas token-by-token decoding does not. Second, kernel fusion with 4-bit weights helps most, running $π_{0.5}$ and GR00T N1.7 2.6--2.9$\times$ faster than PyTorch with \texttt{torch.compile}, but it exists for only these two models and only on the Jetson. Optimization also moves the time to the stages it shortens least, as CPU preprocessing grows from 12\% to 39\% of the GR00T N1.7 call. Third, after optimization, memory bandwidth limits only the stages that process few tokens on the Jetson, such as the denoising steps, whereas software limits all other stages, from unfused kernels to serial preprocessing on the host CPU. Overall, low-latency edge VLAs should use few action-generation iterations, inference software should extend kernel fusion and low-bit weights to more models and platforms, and edge hardware needs high memory bandwidth and a fast host CPU.


### Benchmarking Obstacle-Conditioned Safety in Household Robot Navigation
**Authors**: Hyunwoong Bae, Jisu Han, Jiyeon Choi, Dohoon Kim, Taesup Moon

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.34674v1](https://arxiv.org/pdf/2610.34674v1)

**Abstract**: Safe household navigation requires robots to regulate clearance and speed according to what an obstacle is and how close it is, without unnecessary conservatism. Yet existing evaluations do not test whether semantic safety distinctions are reflected in continuous motion. To that end, we introduce OSMA-Bench, an Obstacle-Conditioned Safe Motion Adaptation Benchmark built on spatially matched scenario sets that differ only in obstacle type. We also propose the \emph{Semantic Sensitivity Index} (SSI), which measures whether clearance and distance-dependent speed and smoothness follow the caution ordering of obstacles. Evaluating VLM-based and vision-language-action (VLA) policies on the benchmark, we find that neither consistently adapts its motion to obstacle safety, even with explicit safety prompts. Our analysis shows that the policies can correctly distinguish obstacles by safety relevance but fail to reflect this distinction in the motion parameters or actions they produce. For VLM-based policies, which recognize the obstacle and then generate a navigation program, adding an explicit parameter-inference step between these two stages improves adaptation. These findings expose a gap in \emph{semantic-to-motion grounding}, highlighting the need to translate semantic caution into appropriately safe motion.


### RobotAgentBench: Towards Open-world Robot Autonomy
**Authors**: Lingjun Mao, Jinglin Cao, Lukun He, Wenpeng Xu, Yuchen Yan, Hengyu Jin, Zijun Zhang, Jinzhou Tang, Songyao Jin, Ziche Liu, Yifei Shao, Junbo Huang, Fang Nan, Ruobing Han, Ziqiao Xi, Ziming Xu, Shuang Liang, Sibo Zhu, Wenyi Wu, Xinyue Wang, Yiming Huang, Xinkai Zou, Gao Zhu, Kun Zhou, Biwei Huang

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.34649v1](https://arxiv.org/pdf/2610.34649v1)

**Abstract**: Recent advances in vision-language-action (VLA) and world-action models (WAMs) have significantly improved robotic manipulation, yet deploying robots in the open world demands a higher level of autonomy beyond executing predefined tasks. Robot agents offer a promising paradigm for this transition, integrating task discovery, contextual reasoning, physical execution, and adaptive recovery into a closed interaction loop. However, existing benchmarks largely evaluate isolated capabilities, failing to capture the complexity of open-world robot autonomy. We introduce RobotAgentBench (RAB), a comprehensive benchmark for evaluating robot agents in realistic, open-world household environments. Through an agent-assisted, human-in-the-loop real-to-sim pipeline, RAB constructs 50 diverse household layouts with interactive objects and physically grounded tasks, encompassing 90 atomic tasks, 18 short-horizon tasks, 8 long-horizon tasks, and 4 open-ended scenarios. RAB provides a multi-level evaluation of robot agent capabilities: (1) task-level assessments systematically examine five complementary dimensions: task discovery, context reasoning, manipulation, failure recovery, and robustness; (2) scenario-level evaluation assesses how agents integrate these capabilities to autonomously fulfill high-level user needs. Furthermore, RAB enables systematic comparisons of standalone VLA/WAM models and diverse robot agent architectures under a unified planning-execution-verification framework. Extensive experiments reveal substantial gaps between manipulation and autonomy, demonstrate the advantages of agentic architectures and recursive self-improvement, and highlight the remaining challenges toward open-world robot autonomy.


### TRIAGE: Efficient Vision-Language-Action Inference Needs Both Reuse and Pruning
**Authors**: Sooyoung Kwon, Carlee Joe-Wong, Kyunghan Lee

**Published Date**: 2026-10-25

**Updated Date**: 2026-10-25

**PDF Url**: [2610.34519v1](https://arxiv.org/pdf/2610.34519v1)

**Abstract**: Vision-language-action (VLA) models are increasingly used for robot manipulation because they map camera images and a language instruction directly to actions. Robots that cannot be tethered to a workstation, such as mobile manipulators and humanoids, must run them on onboard embedded boards, where the prefill latency of the language backbone grows with the hundreds of visual tokens processed at every control step. To meet real-time limits, training-free accelerators recompute only a subset of the visual tokens and skip the rest, either by pruning them or by reusing their cached key-value (KV) states. The two options save nearly the same computation, yet existing methods apply only one of them to every skipped token. Through a token-level diagnostic, we show that which option keeps the action closer to full recomputation depends on the token's drift, the change in its shallow-layer value since its cache was computed. On both backbones tested, reusing tokens below a drift threshold was no worse than pruning them, whereas beyond it, reuse yields up to 4.4x the action error of pruning; the same diagnostic calibrates this threshold per backbone. Building on this finding, we propose TRIAGE, which deems a cache valid when its drift is below this threshold and it is not too old. TRIAGE recomputes a fixed budget of tokens, prioritizing important tokens with invalid caches, reuses every other token with a valid cache, and prunes the rest; prune-only and reuse-only methods are the two extremes of this partition. Because the budget fixes the number of recomputed tokens, it directly sets the prefill latency. On LIBERO and SimplerEnv, TRIAGE stays within 3 pp of full recomputation in average success rate while cutting prefill latency on a Jetson AGX Orin by up to 48%, and with only 7% of visual tokens recomputed, it beats the strongest baseline by 24.4 pp on LIBERO-Object.


### Variational Cognitive Memory Abstraction for Long-Horizon Vision-Language-Action Models
**Authors**: Xinyu Liu, Daiying Tian, Chenwei Tang, Ruyang Han, Chengyang Zhang, Qingyu Zeng, Wei Ju, Liangli Zhen, Jiancheng Lv

**Published Date**: 2026-10-25

**Updated Date**: 2026-10-25

**PDF Url**: [2610.34251v1](https://arxiv.org/pdf/2610.34251v1)

**Abstract**: Vision-Language-Action (VLA) models have shown remarkable success in robotic manipulation, yet their ability to execute long-horizon tasks remains limited by insufficient long- term memory modeling. Existing methods either rely on implicit temporal representations within policy networks, where historical information can be gradually diluted, or maintain explicit memory buffers that suffer from redundancy, noise accumulation, and inefficient retrieval. In this paper, we propose CogMemory, a novel variational cognitive memory framework that enables VLA systems to selectively preserve and reuse task-relevant historical information. Our approach encodes multimodal trajectories into compact latent memory representations through a selective state- space memory encoder, multi-slot temporal abstraction, and variational information compression. During action generation, dynamic cross-attention retrieval with gated fusion adaptively incorporates relevant memories into policy prediction. With merely 3.45M additional parameters, CogMemory stays lightweight and seamlessly fits both early- and intermediate-fusion VLA backbones. Extensive experiments on long-horizon robotic manipulation benchmarks demonstrate consistent improvements across diverse VLA backbones.


### One Scan is Enough: Demonstration-Free Adaptation for Language-Guided Navigation
**Authors**: Zhuoyuan Yu, Yuxing Long, Du Wang, Junyang Wang, Hongwei Fan, Hao Dong

**Published Date**: 2026-10-24

**Updated Date**: 2026-10-24

**PDF Url**: [2610.33794v1](https://arxiv.org/pdf/2610.33794v1)

**Abstract**: Deploying a language-guided navigation policy in a new building usually means watching it fail. Public-benchmark VLAs degrade scene by scene as layout, appearance, and language drift, and the standard fix of teleoperating fresh trajectories on site does not scale. We replace human demonstration with a single brief iPhone scan. Scan2Instruction compiles that scan into a complete training environment, automatically synthesizing executable navigation episodes with grounded instructions. PRPT-KS then adapts the policy through a closed-form Pareto utility read directly off the reconstructed scene, with no learned critic and no human labels. Across five real environments, the two designs together drive our RealNav to an 85% real-robot success rate, compared with 49% for a RealNav baseline post-trained on human demonstrations, and still achieve 82% in unscanned regions of the same buildings, compared with 41% for the same baseline. Our work turns demonstration-free scene adaptation for language-guided navigation from an aspiration into a working reality.


## Agent
### I-HITL: Inalienable Human-in-the-Loop
**Authors**: Samuel Breckenridge, Dani Vilardell, Wenhao Wang, Fan Zhang, Ari Juels

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35835v1](https://arxiv.org/pdf/2610.35835v1)

**Abstract**: Human oversight is a pillar of AI safety. It is often exercised by a human in the loop (HITL) who approves critical actions taken by an AI agent. AI agents' increasing ability to bypass guardrails, though, raises the question of how to enforce HITL robustly.
  We introduce the concept of inalienable human-in-the-loop (I-HITL). An I-HITL protocol ensures that an agent can initiate an action only with explicit human approval, even when the human interacts with a system (e.g., a local agentic harness) compromised by the agent. A strong I-HITL protocol additionally ensures such approval even when an adversarial human attempts to delegate approvals to an agent.
  To motivate I-HITL, we report on experiments with a popular agentic wallet platform in which raising an agent's spending cap requires HITL approval via emailed one-time passcodes (OTPs). Given access to the user's email and a task blocked by the cap, we find that ten different frontier models will often autonomously raise the cap, harvesting OTPs to bypass a HITL guardrail and surfacing other vulnerabilities.
  We formally define I-HITL using the concept of communication topologies and prove necessary and sufficient conditions for its realization. We show that an I-HITL protocol requires a trusted entity - a trusted computing device (or equivalent) - and characterize which such devices can and cannot realize an I-HITL protocol. We present a prototype I-HITL system called Countersign that can plug into and strengthen existing HITL systems using off-the-shelf consumer mobile devices.


### FOCUS: Active Critic Learning for Long-Horizon Language Model Agents
**Authors**: Zhengping Jiang, William Jurayj, Liaoyaqi Wang, Chunsheng Zuo, Anqi Liu, Benjamin Van Durme

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35801v1](https://arxiv.org/pdf/2610.35801v1)

**Abstract**: Sparse outcome rewards make it difficult for long-horizon language-model agents to assign credit to earlier actions. Learned critics provide value estimates for intermediate states, but these estimates can be inaccurate, while estimating intermediate values with repetitive continuation samples from points within a trajectory incurs substantial costs. To mitigate these issues, we introduce FOCUS, an RL method that uses selective branching to help the critic network learn its value estimator. The rollout controller facilitates active learning for the critic by sampling continuations from states that are expected to most reduce the critic's estimation error. These refined value estimates then score the segment between consecutive states with a TD($λ$) advantage, while the sampled evidence supplies training targets for the critic. FOCUS supports long-horizon agentic reinforcement learning through a modular context-management interface that decouples context management from rollout allocation. Our experiments show that using compaction-induced segment boundaries for value estimation and credit assignment, FOCUS outperforms GRPO and VinePPO with matched per-step generation budgets on legal reasoning, deep search, and code localization benchmarks, improving held-out accuracy at Qwen3.5-9B scale by 7.2 points over the strongest baseline on BrowseComp-Plus (55.4 vs. 48.2) and by 4.1 points on DeonticBench (56.5 vs. 52.4).


### A Unified Arena for LLM Agents across Diverse Eurogame
**Authors**: Fengrui Zhang, Xiang Li, Ruomeng Ding, Jiayi Yuan, Yuchen Huang, Zhaoyang Han, Xiaoliang Wang, Daoyuan Chen, Yaliang Li

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35773v1](https://arxiv.org/pdf/2610.35773v1)

**Abstract**: Interactive environments offer a practical way to evaluate large language model (LLM) agents, and competitive games extend this evaluation to decisions shaped by competing goals and other agents' choices. Yet existing evaluations confined to individual games or execution frameworks leave unclear which competitive advantages persist across settings. We introduce DECE (Diverse Eurogame Competitive Environments), a unified arena spanning ten Eurogames with shared interfaces and evaluation protocols. These games combine lasting strategic commitments, competition over shared resources, and multiple routes to victory. Our primary study evaluates 12 model-harness configurations, spanning nine models and four execution harnesses, in 480 three-player matches across ten games. The main and supplementary studies comprise 1,032 completed matches in total. These comparisons reveal broad cross-game ranking agreement alongside game-specific strengths. Matched studies show that the same model can perform differently across execution harnesses, adding another source of variation to these profiles. These performance advantages do not consistently translate into better token or cost efficiency, making resource use an additional consideration when comparing configurations. Together, the findings support evaluating complete agent configurations by both their competitive performance across games and the resources needed to achieve it.


### Free to Look, Free to Reason: Simple LLM Harnesses Outdiagnose Hand-Crafted Root Cause Analysis Agents
**Authors**: Tingzhu Bi, Xun Zhang, Jinglin Li, Ping Wang, Meng Ma

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35767v1](https://arxiv.org/pdf/2610.35767v1)

**Abstract**: Root cause analysis (RCA) of microservice failures has attracted many LLM agents whose investigation is hand-crafted, through standard operating procedures, fixed stages and role agents. Each is evaluated on its own data against few baselines, so it is unknown whether this design beats letting a capable model investigate on its own. We compare three simple harnesses that prescribe none of the model's calls (one call over an evidence package, a SQL agent and the Codex coding agent) with five published LLM RCA agents and with statistical and causal methods on RCAtlas, 90 validated cases from eight public datasets, across six models and three reasoning efforts. The simple harnesses are the most accurate (PR@1 65-77% on three mid-tier models), ahead of the published agents (16-53%) and the non-LLM methods (6-39%), on every model on which both families were run. The published agents fix from a tenth to all of their model calls in the program, and a case study shows how these prescriptions skip the decisive evidence. A stronger model mainly improves reliability, a multi-turn harness mainly improves aptitude, and more reasoning effort changes accuracy by a few points at most while multiplying the time by up to seven. Among runs more accurate than the best non-LLM method, every Pareto-optimal run in cost or time uses a simple harness.


### Preference-Guided Cooperation in Multi-Objective Multi-Agent Reinforcement Learning
**Authors**: Qiyue Xia, J. Michael Herrmann

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35736v1](https://arxiv.org/pdf/2610.35736v1)

**Abstract**: Multi-objective multi-agent reinforcement learning (MOMARL) addresses agent coordination and objective trade-offs simultaneously while optimising overall system performance. Existing work tends to treat multi-agent cooperation and multi-objective optimisation as largely independent components of a learning problem, which amounts to an exorbitant complexity except in trivial cases. We study here whether the structure provided by multiple objectives can itself be exploited to facilitate cooperation, rather than being treated as an additional optimisation challenge. We formulate MOMARL at both the team and individual levels and introduce objective-wise counterfactual credit assignment to evaluate each agent's contribution across the team objectives. We propose Meta-Gradient Informed Multi-Objective Multi-Agent Reinforcement Learning (MIRL), with static (MIRL-S) and dynamic (MIRL-D) variants. By incorporating meta-gradient information, MIRL enables agents to learn how to prioritise objectives individually while collectively optimising the system-level objective, allowing the multi-objective structure to directly guide cooperation. Experiments on a multi-objective multiple particle environment show that our methods improve Pareto-front quality over baselines, with the dynamic variant achieving the strongest performance.


### MiRL: Error-Targeted Reinforcement Learning for Correcting Terminal Agent Misbehaviors
**Authors**: Runchu Tian, Zaid Khan, Zun Wang, Justin Chih-Yao Chen, Mohit Bansal

**Published Date**: 2026-10-26

**Updated Date**: 2026-10-26

**PDF Url**: [2610.35697v1](https://arxiv.org/pdf/2610.35697v1)

**Abstract**: Error-targeted learning gives a legible way to improve a model: identify specific weaknesses of the model, train the model to fix these weaknesses, and check whether the weaknesses are fixed. We study how to apply error-targeted learning to terminal agents, which solve long-horizon tasks specified in natural language by interacting with a command shell. Existing error-targeted methods are designed for single-turn tasks, and existing analyses of agent failures are used to evaluate and debug agents rather than to train them. We propose Misbehavior-driven RL (MiRL), which first profiles the errors of a policy to find generalizable misbehaviors: kinds of wrong steps that recur across many environments. MiRL then trains the policy with RL, starting rollouts at the steps where these misbehaviors occur and rewarding a rollout only if it passes the tests and avoids the misbehavior. On Qwen3.5-4B, eight misbehaviors account for 52.1% of wrong steps. After training with MiRL, the policy repeats the measured misbehaviors 43% to 57% less often on average on unseen prefixes. MiRL outperforms TMax-4B on Terminal-Bench Lite (51.8% vs. 47.4%) and matches it on Terminal-Bench 2.1 (21.3% vs. 20.6%), while using 35% of its rollouts. These results show that error-targeted learning can be applied to realistic, long-horizon terminal tasks.


