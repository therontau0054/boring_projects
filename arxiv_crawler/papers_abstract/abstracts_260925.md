# Abstracts of Papers

## World Model
### LLM Agents Can Easily Tamper With Their Own Traces
**Authors**: Jeremy Qin, David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner, Ameya Prabhu, Maksym Andriushchenko

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30266v1](https://arxiv.org/pdf/2609.30266v1)

**Abstract**: Asynchronous monitoring, incident investigations, and compliance audits primarily rely on agent traces to reconstruct what happened. These analyses assume that LLM agents cannot tamper with their own execution traces. We show that local LLM agents such as Claude Code, Codex, Antigravity, Open Code and Grok Build fail to enforce this boundary. All tested harnesses, except Muse Code, allowed agents to delete their traces when asked, without triggering monitor guardrails. We also validate that external attackers can exploit this gap to induce trace deletion. Finally, we show that trace tampering behavior emerges naturally in frontier models, when agents try to improve their rewards. We advise practitioners to ensure trace logging happens through an independent interception mechanism outside of the agent's control, preserving trace integrity even in cases of full host compromise. Overall, our findings identify a concrete failure of trace integrity in agent infrastructure which can be used to conceal misaligned behaviors like scheming or sabotage.


### AD-WM: Action-Discriminative World Models for Counterfactual Model Predictive Control
**Authors**: Jiabin Qiu, Zixuan Chen, Hongye Cao, Jieqi Shi, Jing Huo, Yang Gao

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30264v1](https://arxiv.org/pdf/2609.30264v1)

**Abstract**: Latent world models are typically trained to predict factual transitions, whereas model predictive control (MPC) must compare alternative actions from the same state. A model can therefore achieve low factual prediction error yet poorly distinguish candidate actions. We introduce AD-WM, an action-discriminative joint-embedding world model for counterfactual MPC. AD-WM combines residual latent dynamics with predictor-level action-recovery regularization, using inverse dynamics and a normalized recovery objective motivated by conditional mutual information. Both objectives encourage planning transitions to preserve action information; their auxiliary heads are discarded at test time, leaving MPC unchanged. On OGBench-Cube, AD-WM improves hard-start success from 3.7% to 52.0% over a matched LeWM baseline and improves mean success over the reproduced baseline in four of five simulation environments. Planning diagnostics show that factual prediction error and whole-bank action ranking do not follow the closed-loop success ordering, whereas CEM-aligned elite regret tracks success more closely. With a frozen V-JEPA 2 encoder and matched DROID post-training, AD-WM also improves zero-shot transfer to our Franka setup, increasing basic pick-and-place success from 42.2% to 71.1% without lab-specific adaptation. These results suggest that world models for planning should preserve action-dependent differences needed for counterfactual selection, rather than optimize factual prediction accuracy alone. More videos and code are available at https://ad-wm.github.io/.


### Agentic Detection of Online Conspiracies
**Authors**: Lior Biton, Oren Tsur

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30250v1](https://arxiv.org/pdf/2609.30250v1)

**Abstract**: Conspiratorial discourse on social media is not always expressed through explicit claims or stable lexical markers. The same surface content may express endorsement, legitimate concerns, criticism, satire, or mockery. The main challenge is therefore not only recognizing conspiracy-related claims, but inferring the speaker's intent -- the utterance's illocutionary force. We argue that this can be achieved through the use of relevant social contexts and propose an agentic framework, equipped with a set of tools supporting social queries.
  We demonstrate the benefits of our approach on a unique dataset of Hebrew tweets, covering 80\%--90\% of the public Hebrew tweets published over a four-year span (late 2018-- early 2023), encompassing several election cycles as well as the COVID pandemic years and related vaccination campaigns. This extensive coverage can be used in recovering different social contexts. Evaluating our framework on a manually-annotated adversarial dataset, we find that context-aware workflows consistently outperform text-only classification and that the agentic framework performs significantly better than other frameworks and settings, including a non-agentic model exposed to the same contexts available to the agent. We further provide an analysis of the results, the errors and efficiency (token economy) tradeoffs.
  These findings support viewing the task of conspiracy detection as a socially embedded interpretation task, in which effective classification depends not only on access to contexts, but also on adaptive reasoning in which the agent uses tools on a per-case basis, asking only for evidence relevant to its current reasoning step.


### Rolling-WAM: World Action Models with Rolling Imagination
**Authors**: Yinghua Zhou, Junjie Ye, Yiqi Zhao, Hao Dong, Celina Shiyu Wang, Ruohai Ge, Tingyi Yang, Basile Van Hoorick, Gaurav Sukhatme, Vitor Guizilini, Yue Wang

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30247v1](https://arxiv.org/pdf/2609.30247v1)

**Abstract**: World Action Models (WAMs) couple action generation with future visual prediction for robotic manipulation. However, completing the joint video-action denoising process at each replanning cycle incurs substantial latency, delaying action updates and limiting closed-loop responsiveness. We present Rolling-WAM, a formulation that distributes joint denoising across successive replanning cycles. Our method maintains a sliding window of video-action chunks at staggered noise levels. At each step, a rolling noise schedule fully denoises the imminent action chunk for execution, while partially refining farther-future chunks. As the window advances with new camera observations, the retained future chunks continue their denoising process. This distributes the computational cost over time while carrying an evolving visual-action context across chunk boundaries. Evaluations on LIBERO, RoboTwin, and a real-world Unitree G1 humanoid show that Rolling-WAM achieves competitive manipulation performance. By removing the need to denoise the entire prediction horizon from scratch, it delivers a 4.5x steady-state replanning speedup over standard joint WAMs.


### JevOut: Natural Context Can Flip Decision Models
**Authors**: Zixiang Xu

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30243v1](https://arxiv.org/pdf/2609.30243v1)

**Abstract**: Dedicated decision models such as Jev map unstructured language to probability distributions over finite choices, allowing their outputs to directly route requests, select tools, and trigger actions. Yet real-world inputs rarely arrive in isolation: they come with background details and surrounding context. We find that short additions that fit naturally into this context can nevertheless redirect an otherwise correct decision, even when the correct answer remains unchanged. To study this behavior, we fix a wrong target option for each initially correct item and use the model's option probabilities to refine fluent context additions while preserving the source, question, choices, and gold answer. Within 64 accepted target evaluations, the optimizer identifies contexts that redirect Jev on 312 of 508 initially correct decisions (61.4%); in 229 cases, Jev assigns at least 0.7 probability to the fixed wrong option. Across seven datasets, three additional decision systems show targeted flip rates of 64.9%-73.2% on decisions they initially answer correctly. Taken together, these results expose a pronounced fragility in current decision models: short, ordinary-looking context can shift a correct choice to a high-confidence wrong one. Because these models turn language directly into downstream choices, this sensitivity raises concerns about treating their probability outputs as reliable decision interfaces.


### Coding Agents for Generalized Task and Motion Planning Problems
**Authors**: Matteo Merler, Bowen Li, Josh Roy, Yichao Liang, Qianwei Wang, Yixuan Huang, Tom Silver

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30233v1](https://arxiv.org/pdf/2609.30233v1)

**Abstract**: Task and motion planning (TAMP) problems remain difficult even with full observability and object-centric states because discrete decisions are tightly coupled to geometric, kinematic, and dynamic constraints. Generalized TAMP addresses this difficulty by exploiting regularities across problem instances to reduce planning effort on new instances. However, existing methods require substantial TAMP-specific engineering. We investigate whether coding agents can automate this process by synthesizing programs that generalize across instances. Given a task description and simulator access, each agent chooses how to interact with the environment while developing a program within a fixed synthesis budget. The program is then frozen and evaluated on unseen instances. We evaluate Claude Code (Opus 5) and Codex (GPT-5.6 Sol and GPT-6 Astra) on 28 simulated environments from KinDER and PDDLStream, with object counts beyond those evaluated in the original benchmark. Across all program synthesis methods, we evaluate 980 generated programs on 100 held-out instances each, 98,000 evaluation episodes in total. Overall, we find that coding agents are surprisingly effective at generalized TAMP: all three agent configurations outperform hand-engineered planners, one-shot generation, and an LLM-based generalized planning baseline in mean success (56% to 95% versus 47% for the planners, on the 16 environments where a planner is available). As object counts grow, the agents' programs maintain higher success than the planner, using an order of magnitude less computation per instance on average. Logs show agents using interaction to calibrate physical models, test edge cases, and refine strategies. We release all code, including the full prompts given to the agents. These findings suggest that coding agents are a strong baseline for generalized TAMP.


## Generation
### RAPID: Robot Agentic Programming from Demonstrations
**Authors**: Yuyao Liu, Jiayuan Mao, David Hsu, Leslie Pack Kaelbling, Tomás Lozano-Pérez

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30249v1](https://arxiv.org/pdf/2609.30249v1)

**Abstract**: Coding agents have demonstrated enormous success in solving complex programming problems. To leverage their potential for robot systems, this work introduces Robot Agentic Programming from Demonstrations (RAPID), which automatically generates, verifies, and refines robot programs, given a single visual human demonstration. The iterative agentic loop of code refinement requires several key ingredients: (i) a testable task specification, (ii) action primitives for robot execution, and (iii) an interactive environment for program execution and verification. RAPID infers all three from the demonstration automatically. To make the resulting program reusable beyond the demonstration setting, RAPID uses an object-centric relational program representation that focuses on the underlying structure of the demonstrated strategy rather than the specific motion per se: it expresses the action primitives as trajectory-optimization programs that realize object-level motion effects, while composing them through relational constraints that capture scene-specific geometry at run time. We evaluated RAPID in simulation on eight challenging contact-rich nonprehensile manipulation tasks as well as general prehensile manipulation tasks in the LIBERO-Pro benchmark. We also successfully deployed it on a real Franka arm and evaluated on all eight nonprehensile tasks. In all experiments, RAPID demonstrated strong performance, with generalization over object pose, shape, material, and environment. Website: https://yuyaoliu.me/projects/rapid.


### Requirement-Bound Verified Commissioning: A Frozen Four-Billion-Parameter Local Model as a Candidate Generator under an External Acceptance Layer with Verification and Release Authority
**Authors**: Mehmet Iscan

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30219v1](https://arxiv.org/pdf/2609.30219v1)

**Abstract**: An acceptance protocol is developed for sensor-coordinate and polarity binding in mechatronic commissioning. Candidate generation is separated from release authority. Requirements unsupported by a deterministic parser are routed to a frozen local language model with four billion parameters. Plans are released only when both facts can be derived by an external gate under a sealed grammar. One canonical answer is requested from a gold-standard user when eligible. The protocol was evaluated once under a criterion fixed before benchmark construction, on 144 tasks written by isolated agent contexts without access to the gate, grammar, or experimental plan. Three contributions are established. First, candidate generation and release decisions were measured separately. Fabricated ready plans were committed on 21 of 22 routed unanswerable tasks, and all were rejected. The same 83 releases were reproduced without model calls. Second, no false release was observed among 83 releases. A one-sided 95% Clopper-Pearson upper bound of 0.0354 was obtained as a diagnostic under an independent-and-identically-distributed assumption, below the sealed 5% threshold. However, one false release was subsequently recorded among 146 releases outside the benchmark at seed 0. Third, protection against incorrect user answers was characterized. Both facts were bound from the original text on 13 of 96 answerable tasks. Incorrect answers were released in 169 of 431 pairings on the remaining tasks, including failures involving coordinate exclusion. A deployable questioning policy was not tested because eligibility was determined from the answer key. Gate sensitivity and real user behavior were not measured.


### Minimally Invasive Steering of Language Models
**Authors**: Taha Entesari, Jingyu Zhang, Daniel Khashabi, Mahyar Fazlyab

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30218v1](https://arxiv.org/pdf/2609.30218v1)

**Abstract**: Pre-logit steering adapts a frozen language model to a test-time reward by adding vectors to its final hidden states. Unregularized reward optimization can substantially alter the output distribution and degrade generation quality. We propose Minimally Invasive Steering Vector Optimization (MISVO), which penalizes interventions using the local KL geometry of the induced token distribution. The resulting Fisher quadratic measures distributional sensitivity and admits an analytic gradient computed through matrix--vector products with the frozen language-model head. We derive an exact decomposition of the sequence-level KL gradient into an analytic Fisher term and a suffix score-function term. For a fixed generation horizon, we show that the suffix term is second order in the steering magnitude and that three Fisher surrogates agree with the full KL gradient to first order. MISVO uses the frozen-reference surrogate to optimize position-specific interventions without updating model parameters. Across preference and code-generation tasks on models with approximately 1B--14B parameters, MISVO achieves the highest mean reward in six of seven model--task settings, with diversity and coherence scores close to those of Best-of-N.


### Instrumental Monitor Evasion Emerges Under Ordinary Task Pressure
**Authors**: David Schmotz, Derck Prinzhorn, Luca Beurer-Kellner, Anselm Paulus, Ameya Prabhu, Maksym Andriushchenko

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30217v1](https://arxiv.org/pdf/2609.30217v1)

**Abstract**: A central concern in AI safety is that agents may treat oversight as an obstacle when it conflicts with completing their goals. We study instrumental evasion, the propensity of LLM agents to circumvent runtime monitoring as a means of completing ordinary tasks. We introduce EvasionBench, a benchmark of 50 diverse task-policy pairs in which completing the task requires an operation prohibited by a runtime monitor. Agents know that their tool calls are monitored and are prompted to continue working when they pause. Across our evaluations, best-of-3 evasion attempt rates reach up to 98% and success rates up to 88%, with substantial variance across models. Claude Fable 5.1 succeeds less often, but frequently makes creative attempts to circumvent the monitor. Evasion generally increases with test-time compute, with higher evasion rates at greater reasoning effort and token use. Traces show that agents encode prohibited commands, decompose operations across tool calls, and retry until relevant context leaves the monitor's history. We also find that GPT-6 Astra's low evasion rate comes with overrefusal, as it frequently abandons otherwise solvable tasks under a denial-of-service prompt injection. Our findings show that ordinary task pressure can lead to adaptive attempts to evade runtime monitors without an explicit adversarial objective. Effective oversight must therefore remain robust against repeated attempts, as the persistence that helps agents solve difficult tasks can also drive them to circumvent their guardrails.


### A Living Benchmark for Information Retrieval from Electronic Health Records
**Authors**: Jordan L. Cahoon, Chloe O. Stanwyck, Sulaiman Somani, Philip Chung, Kevin R Keet, Kameron C. Black, Andrea T. Fisher, Sarita Khemani, Jerry Liu, Stephen Ma, Saloni K. Maharaj, Rita M. Pandya, Eduardo Perez-Guerrero, Priyanka Pillai, Lisa Shieh, David J. H. Wu, James Xie, James C. McAvoy, Teresa Nguyen, Jessica Tran, Lucy Yin, Bridget Lin, Alison Callahan, Jason A. Fries, Nigam H. Shah, Emily Alsentzer

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30205v1](https://arxiv.org/pdf/2609.30205v1)

**Abstract**: Large language model (LLM)-based clinical assistants are increasingly being integrated into electronic health record (EHR) systems, transforming how clinicians retrieve and synthesize information from patient records. Their safety and utility depend on rigorous evaluation, yet existing benchmarks are manually curated, costly to update, and rapidly become obsolete with evolving technological advancements. We present a scalable framework that automatically generates question--answer pairs from longitudinal EHR notes. Nineteen clinicians validate the benchmark generator, producing the Benchmark for Retrieving Information in EHRs (BRIE), a continuously maintainable evaluation dataset. Across nine LLMs and five inference strategies, state-of-the-art systems frequently omit clinically important information, particularly for questions requiring synthesis across multiple documents and encounters. Because the generator itself is validated, BRIE supports evaluations that static benchmarks cannot, including the generation of multiple answers that reflect variation in clinician reasoning for robust performance assessment and continuously refreshing benchmark content to guard against leakage. Our results demonstrate that scalable benchmark generation enables rigorous, up-to-date evaluation of clinical LLMs as they are deployed in rapidly evolving healthcare settings.


### Search-Aware Reinforcement Learning for Multi-Component Query Understanding in Roblox Game Search
**Authors**: Nayoung Choi, Shengjian Chen, Xiaokai Wei, Wenzheng Zhang, Daiyao Yi, Rachit Pareek, Vincent Su, Michelle Gong, Jinho D. Choi

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30177v1](https://arxiv.org/pdf/2609.30177v1)

**Abstract**: Query understanding (QU) plays a critical role in production search systems, translating raw user queries into search execution plans that drive downstream retrieval and ranking. While large language models (LLMs) have enabled QU to be framed as a structured multi-task generation problem (e.g., intent classification, query expansion), optimizing such models to produce search-engine-coupled outputs remains challenging: static, label-based supervision fails to capture how each component actually interacts with the underlying search pipeline to affect downstream performance. We present a search-aware reinforcement learning (RL) framework for QU based on a distill-then-RL paradigm. Teacher-student supervised fine-tuning (SFT) first yields a well-formed, schema-compliant policy initialization. The RL stage then optimizes each QU component with rewards derived from live interaction with the search engine, tailored to that component's operational role, rather than a single reward tied to the final search outcome. Experiments on Roblox search show that this component-specific optimization improves both per-component utility and downstream search quality, raising NDCG@20 by 8.9 points over the SFT policy and by 3.5 points over training with a single end-to-end reward.


## VLA
### World Action Agent: Harnessing VLMs for Robot Manipulation via World Action Rehearsal
**Authors**: Yehang Zhang, Haojian Huang, Yifan Chang, Jianchong Su, Bohan Zhou, Yingjie Xu, Wosong Chen, Tianhao Zhou, Chenxu Wang, Tianyi Zhang, Yangkai Wei, Wenqian Li, Shiyuan Deng, Yinchuan Li, Ying-Cong Chen, Zexi Li

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.29964v1](https://arxiv.org/pdf/2609.29964v1)

**Abstract**: General-purpose vision-language models (VLMs) bring broad knowledge and spatial reasoning to robot manipulation, yet existing systems either use them indirectly, to predict constraints or write programs, or give them a view of the scene rather than a world in which to act. We present World Action Agent (WAA), a multi-agent harness through which VLMs pilot robots with basic tools, making every decision within a visual action workspace. The workspace has three properties. Contact views, selected automatically from the scene geometry, present the scene around the current interaction. Action rehearsal turns each action into an editable proposal that the agent, alone or through an Imagination Agent, previews and revises against planning feedback before execution. In-view correction closes the loop between observation, rehearsal, and low-level execution, letting the agent remove residual offsets in the view where it observes them. Through the same workspace, WAA acquires embodied procedural knowledge in two ways: it evolves multimodal skills from expert videos and human teaching under evidence-based review and consults them through a Skill Agent, and its interaction traces train smaller VLMs to pilot the same harness. On LIBERO-Pro, WAA with skills evolved only from LIBERO-90 reaches a state-of-the-art 75.6% average success, outperforming end-to-end VLAs, code-as-policy agents, and a visual-harness baseline with the same backbone; the same skills remain effective on robosuite without further learning. Fine-tuning Qwen3.5-9B on harness traces raises its out-of-domain success from 1.7% to 43.3%.


### Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs
**Authors**: Riccardo Andrea Izzo, Rimvydas Rubavicius, Gianluca Bardaro, Subramanian Ramamoorthy, Matteo Matteucci, Alessandro Suglia

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.29382v1](https://arxiv.org/pdf/2609.29382v1)

**Abstract**: Flow-matching Vision-Language-Action (VLA) models have emerged as a potential solution for generalist robot control, designed by combining a pretrained Vision-Language Model (VLM) backbone with an action expert that generates continuous robot actions. While these models exhibit impressive capabilities, due to their very high number of parameters, their computational requirements are often prohibitive for robotics control. To mitigate these inefficiencies, existing methods predominantly skip VLM backbone layers with early exits or reduce denoising steps, while leaving action expert depth untouched. We propose a framework that exposes backbone depth $V$, action expert depth $A$, and denoising steps $D$ as three jointly configurable compute axes in a VLA. Starting from a pretrained VLA, we attach lightweight Exit Transformers (ET) at intermediate depths in both the backbone and the action expert, trained to distil the last layer of the policy into each exit. Furthermore, we introduce a KV Cache synthesis mechanism that manages the missing keys and values of the skipped backbone layers, allowing the action expert to exit deeper than the backbone. Finally, we show that the optimal compute budget is task-dependent, with different tasks benefiting from different axes and depths. Notably, our method does not require training the original policy from scratch, and for each exit, it increases the number of parameters by only $2.1\%$ for SmolVLA and $4.1\%$ for $π_{0.5}$. We validate our approach across two flow-matching VLAs (SmolVLA, $π_{0.5}$) and two benchmarks (LIBERO, Meta-World), revealing complementary effects: $V$ and $A$ respectively reduce FLOPs and latency, while $D$ improves both. Our joint configurations $(V,A,D)$ reduce latency by $79.2\%$ and computation (FLOPs) by $31.8\%$, while improving mean success rate by $5.6\%$.


### CrossSafe: Towards Cross-Embodiment Latent Safety Filters
**Authors**: Ihab Tabbara, Yuxuan Yang, Hussein Sibai

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.28984v1](https://arxiv.org/pdf/2609.28984v1)

**Abstract**: Cross-embodiment learning has shown that a single model, such as a vision-language-action (VLA) model, can learn state representations and manipulation skills that can be applied across heterogeneous robots to accomplish various tasks. We hypothesize that the same holds for safety enforcement. The reasoning required to satisfy a safety constraint, such as detecting an obstacle, recognizing that it should be avoided, and selecting a safe abstract action, is largely shared across robots. What differs across embodiments is how the abstract safe action is realized: morphology, kinematics, and dynamics determine which actions are safe and feasible. Consequently, the same action can be safe for one robot and unsafe for another. This is especially important for generalist manipulation policies that operate in a common end-effector action space without explicitly capturing how safety depends on the robot's morphology and kinematics. We propose embodiment-conditioned safety filtering, in which a Hamilton-Jacobi reachability-based value function and its corresponding safety-maximizing policy are shared across robots. Using a morphology-aware latent representation of the robot and its environment, we perform Hamilton-Jacobi reachability analysis directly in latent space so that the learned safety concepts can generalize across embodiments while remaining explicitly conditioned on each robot's morphology and kinematics. We evaluate our approach across five bimanual robot embodiments and five manipulation tasks with whole-body collision-avoidance constraints. Our results show that a single policy, jointly trained across five manipulation tasks and four embodiments, exhibits zero-shot generalization to a held-out embodiment, reducing the nominal policy's collision rate. They also show that training using more embodiments improves generalization.


### Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching Vision-Language-Action Policy
**Authors**: Mehmet Turan Yardımcı, Yunus Emre Çoğurcu

**Published Date**: 2026-09-23

**Updated Date**: 2026-09-23

**PDF Url**: [2609.28838v1](https://arxiv.org/pdf/2609.28838v1)

**Abstract**: Online reinforcement learning fine-tuning of pretrained flow-matching vision-language-action (VLA) policies promises robots that keep learning after deployment, but continued updates often destroy competence on individual tasks while the aggregate still looks healthy. We study this failure mode, which we call task collapse, under a matched small-compute budget on LIBERO-10 with a 450M-parameter SmolVLA policy trained by PPO with stochastic (SDE) sampling. Three exploration-noise policies differ in one live variable: a fixed noise scale, a ReinFlow-style learned noise network, and an uncertainty-gated controller that redistributes exploration across task streams from task-agnostic novelty and competence signals, without task labels or episode boundaries. Under the pooled definition, fixed noise collapses tasks in two of three seeds and learned noise in every seed measured to iteration 200, while the controller collapses none in any of its three seeds. Measured parameter displacement shows the controller's action expert keeps changing, while its mean applied noise is close to the fixed scale in the available logs. The matched comparison supports the controller's effect on task preservation; the separate contributions of its adaptation across states and over time are not disentangled. A lower fixed scale slows the decline but does not stop it. No arm improves on the behavior-cloning baseline in this budget. Two properties of that regime are measured beside this result, not offered as its cause: following the reference recipe, training runs in bfloat16 with no fp32 master copy, under which 96.02% of the action expert's elements stay bit-identical across three consecutive iterations, and an fp32 master copy at the reference learning rate collapses both arms in a single-seed observation. We release tools measuring per-task collapse under four definitions, rescoring noise and instrument tares.


### Less Language, More Latents: Annotation-Efficient VLAs for Driving
**Authors**: Alexey Zakharov, Kemal Oksuz, Puneet K. Dokania

**Published Date**: 2026-09-23

**Updated Date**: 2026-09-23

**PDF Url**: [2609.27747v1](https://arxiv.org/pdf/2609.27747v1)

**Abstract**: Vision-language-action models (VLA) promise human-steerable autonomous driving, but their training is bottlenecked by the scarcity of frames paired with natural-language instructions: while camera streams and expert trajectories are logged at scale, language annotations (e.g., turn left at the intersection) remain scarce and expensive to acquire. To address this challenge, we introduce Latent Action Driving Annotations (LADA), a three-stage pipeline that transforms abundant unlabelled observation-trajectory pairs into a substrate for language-conditioned control. First, we train a latent action model with a vector-quantised bottleneck, producing a compact codebook of high-level vehicle intents. Second, a small language-annotated subset is used to train a vision-language translator to map observations and language instructions into this codebook. Third, we train a driving VLA on observation-latent-action pairs over the full unlabelled corpus. Using fewer than 5% of language annotations and without leveraging any auxiliary chain-of-thought reasoning or visual question answering streams, LADA achieves a Driving Score of 87.98 and a Success Rate of 70.46% on the closed-loop Bench2Drive benchmark, matching or surpassing fully supervised baselines.


### InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies
**Authors**: Sai Puneeth Reddy Gottam, Elmar Rueckert, Vedant Dave

**Published Date**: 2026-09-23

**Updated Date**: 2026-09-23

**PDF Url**: [2609.27734v1](https://arxiv.org/pdf/2609.27734v1)

**Abstract**: Vision-Language-Action (VLA) policies often rely strongly on the camera viewpoints seen during training, causing substantial performance degradation when deployed from unseen perspectives. Collecting demonstrations from sufficiently diverse physical viewpoints is expensive and still provides only sparse coverage of the viewpoint space. We introduce InfiNoVA, a data-augmentation framework that converts synchronized multi-camera demonstrations into a dense distribution of geometrically consistent training views. InfiNoVA reconstructs each manipulation trajectory as a time-varying 3D Gaussian representation and renders novel observations from sampled camera poses while preserving the original state-action correspondence. This explicit scene representation improves frame-level fidelity and temporal consistency while reducing task-critical hallucinations observed in generative novel-view synthesis. Across four real-world manipulation tasks, policies trained with InfiNoVA achieve 5.4x higher average success under unseen randomized viewpoints than both VISTA-based augmentation and the unaugmented policy. InfiNoVA further achieves 1.7x higher success than training directly on all five physical camera views. These results show that dense, geometrically grounded viewpoint augmentation provides a practical route toward camera-robust robot policies without modifying the underlying policy architecture.


## Agent
### Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning
**Authors**: Sudip Bhujel, Shanghao Shi, Ruiquan Huang, Ning Zhang, Yang Xiao

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30258v1](https://arxiv.org/pdf/2609.30258v1)

**Abstract**: Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal structure can amplify this leakage beyond single-frame attacks. We introduce Temporal Reconstruction Attack on Consecutive Encodings (TRACE), an amortized temporal gradient-inversion attack that autoregressively reconstructs the sequence of private observation-action trajectories from per-step policy-learning gradients. The attack exploits two structural signals ignored by prior single-frame methods: (i) cross-time correlation between successive embodied gradients, which we formalize via a conditional mutual-information bound, and (ii) closed-form action recovery from policy-head gradient structure, which we prove exact when standard entropy regularization is sufficiently small. On held-out embodied scenes, TRACE reaches $18.8$ dB PSNR with near-perfect action recovery at $3$-$4.5$ ms per reconstructed frame, dominating the learning-based baseline across all reconstruction metrics and exceeding optimization attacks while running orders of magnitude faster. Further evaluation demonstrates TRACE's broader applicability across recurrent, residual, and compact transformer victim architectures, multi-modal inputs, and larger discrete action spaces. Defense experiments suggest that protecting temporal gradient streams may require sequence-aware privacy mechanisms.


### Underwater C3-JEPA: An Object-Centric Cross-View World Model for ROV Salvage
**Authors**: Yuncong Yang, Jinlong Li, Yulong Xue, Feng Wu, Chunwen Zhang, Lei Qiao, Xuyang Wang

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30214v1](https://arxiv.org/pdf/2609.30214v1)

**Abstract**: We present Underwater C$^{3}$-JEPA (cross-view, control-conditioned, context-extended), an object-centric multi-view predictive world model for near-field heavy-load underwater ROV salvage. Without contact sensors, it predicts in latent space how the task-object state evolves through contact interaction and under the hydrodynamic lag of the vehicle, from synchronized multi-view RGB observations and vehicle control signals. C$^{3}$-JEPA encodes multi-camera observations into task-object and context tokens, fuses cross-camera evidence through held-out-view attention, and directly predicts future states conditioned on control. Weak binding anchors the target and gripper at low annotation cost, while SIGReg sharpens the geometric representation. Experiments show that the learned representation transfers substantially more task-relevant information to downstream probes than a reconstruction-free latent baseline, while keeping the predictor lightweight. The resulting predictive interface supports model-predictive-control (MPC) candidate evaluation and imagined-rollout behavior-agent training. Validation on real underwater video shows the same architecture recovering a withheld camera's object state and staying ahead of persistence, so the recipe transfers beyond simulation.


### Jev-Mobile: Jev as an Executor for Mobile GUI Agents
**Authors**: Linghua Zhang

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30186v1](https://arxiv.org/pdf/2609.30186v1)

**Abstract**: Vision-language models (VLMs) have become a common foundation for autonomous mobile GUI agents, but most existing systems rely on the VLM for both planning and action grounding at nearly every interaction step, leading to substantial latency and model-serving cost. We introduce Jev-Mobile, which shifts this paradigm to low-frequency VLM planning and high-frequency lightweight execution: the VLM specifies local goals, the accessibility tree defines a structured executable action space, and Jev, a fast typed decision model, repeatedly selects actions within this space. This design allows multiple GUI actions to be executed under a single VLM decision, reducing expensive VLM inference while preserving adaptive interaction. On the full AndroidWorld task suite, Jev-Mobile achieves 79% task success, compared with 78% for SeeAct-V and 84% for a Step-wise VLM baseline. Among successful trajectories, it reduces mean end-to-end execution time by 32.7% and mean model API cost by 73.4% relative to Step-wise VLM. These results show that decoupling high-level VLM reasoning from low-level action execution can substantially improve mobile GUI agent efficiency while maintaining competitive task performance.


### Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management
**Authors**: Giacomo Arcieri, Gregory Duthé, Christophe Muller, Konstantinos G. Papakonstantinou, Daniel Straub, Eleni Chatzi

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30150v1](https://arxiv.org/pdf/2609.30150v1)

**Abstract**: Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration correlations and economies of scale. While deep reinforcement learning has shown promise in optimizing maintenance policies, scaling to real-world networks remains challenging. Centralized approaches become computationally intractable in large-scale systems, whereas decentralized approaches often fail to capture essential coordination mechanisms. To address these challenges, we propose a graph-based framework that integrates accurate environment modeling with scalable decision support. First, we employ a hierarchical Bayesian model leveraging a Gaussian Process on Graph kernel to infer a realistic, spatially correlated networked environment of railway maintenance planning from real-world data provided by the Swiss Federal Railways. Second, we introduce a topology-aware Multi-Agent Reinforcement Learning (MARL) framework by integrating graph neural networks and graph Transformers to optimize network-level policies. A central contribution of this work is the demonstration of scalability through zero-shot transfer learning: graph-based agents, trained only on small network portions, are successfully deployed in a zero-shot manner on large-scale unseen networks without any retraining. Numerical results indicate that the proposed method significantly outperforms optimized heuristics and standard MARL baselines, reducing computational training time while maintaining superior performance on large-scale networks.


### GRASP: Generating, Revising, and Assessing for Strategic Planning with Agentic AI
**Authors**: Arunabh Srivastava, Mohammad A.,  Khojastepour, Srimat Chakradhar, Sennur Ulukus

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30147v1](https://arxiv.org/pdf/2609.30147v1)

**Abstract**: Large Language Models (LLMs) typically exhibit a performance profile where reliability degrades as task complexity increases. We address the challenge of generating high-quality natural language executable plans for complex tasks by introducing $\textbf{GRASP}$, a strategy-aware, multi-stage planning framework. GRASP decouples the planning pipeline across specialized, context-isolated modules: it pre-compiles global macro-guidelines (GenPlan), explores alternative localized strategies within isolated context windows (RevPlan), and independently evaluates trajectories using a multi-criteria discriminator (VerPlan). Empirical evaluations show that GRASP consistently establishes a new state-of-the-art frontier across diverse datasets, yielding substantial accuracy gains over direct LLM planners on Natural Plan Calendar Scheduling ($\sim$12.4$\%$$\uparrow$), ZebraLogic ($\sim$30.8$\%$$\uparrow$), and SciBench Math. Crucially, under multi-task scaling-where standard planners suffer immediate performance collapse-GRASP completely flattens the multi-task degradation penalty. In interleaved dual-task environments, GRASP achieves an absolute accuracy gain of up to 16.7$\%$ over direct LLM planners. Furthermore, by isolating context and enforcing strict macro-regularization, GRASP outperforms frontier reasoning models (such as GPT-5-mini) by a margin of 14.5$\%$.


### Screen Before You Serve: Simulation for Production Customer Experience AI Agents at 140M Scale
**Authors**: Edesio Alcoba, Kevin Rossell, Aman Gupta, Shao Tang, Jiwoo Hong, Pabel Carrillo-Mendoza, Wanderson Conceição Ferreira, Alvaro Tedeschi, Zayd Simjee, Shreya Rajpal, Bruno Finardi Hime, Christian Sousa, Luis Moneda, Herbert Fei, Daniel Silva, Rohan Ramanath

**Published Date**: 2026-09-24

**Updated Date**: 2026-09-24

**PDF Url**: [2609.30137v1](https://arxiv.org/pdf/2609.30137v1)

**Abstract**: Customer experience (CX) agents use tools and large language models to address customer requests and guide conversational interactions with an organization's products. Improving these agents, especially in regulated industries, is difficult: they must detect intent, follow complex operational policies and use tools reliably. Manual end-to-end testing offers limited coverage, while live experiments expose customers to failures that can erode trust.
  We present a hypothesis-driven simulation workflow for screening candidate CX agents before deployment. Synthetic customers react to agent responses and simulated tool outputs enable multi-step agentic workflows without invoking production backends. We use the Snowglobe simulator on Nubank's Card Delivery agent and its expanded successor, Card Management - Nubank's highest-volume chat-support agent in Brazil. Across 4 deployed versions, simulated and production version-level binary evaluator scores show high correlation. Simulation-guided iteration increased transactional net promoter score (tNPS) by 36.69 points in a live A/B test. We also screened open-weight configurations in over 16,000 simulated conversations. In a subsequent live A/B test, the selected model increased self-service rate (SSR) by 8.82 percentage points to the highest level observed at Nubank, with no statistically significant change in tNPS. Simulation made broad exploration of models, reasoning settings, and prompts feasible without customer exposure, enabling production improvements that would have been impractical to pursue through live experimentation alone.


