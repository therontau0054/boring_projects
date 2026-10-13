# Abstracts of Papers

## World Model
### Can Language Models Play the Wikipedia Game?
**Authors**: Alexander Hickey, Joanna Knight, James Bishop

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13948v1](https://arxiv.org/pdf/2610.13948v1)

**Abstract**: Language models increasingly support or automate information retrieval from document collections too large to index. This task is difficult when it requires specialist linguistic or scientific knowledge. We used the Wikipedia Game to test language models on an analogous information retrieval task. In the game, players must reach a target article using only article links. We compared sentence embedding models and LLMs across five Wikipedia languages and five academic-literature datasets. We construct very large local graphs of Wikipedia pages and of paper citations using OpenAlex and provide code to build and navigate them. This allows the study of language models' navigation capabilities without relying on third-party APIs. We compared the models with human and TF-IDF benchmarks. The Wikipedia Game format enables robust comparisons across techniques, languages, and domains. No model significantly outperformed humans, although the best models (GPT-o3 mini, GPT-4o, QwQ:32B, and DeepSeek-R1:70B) achieved comparable success. Performance and rankings varied across languages and topics, with implications for practitioners utilising these techniques.


### Hide and Seek: HIDE Concepts to SEEK explanations for black box models
**Authors**: Bhanu Tokas, Rahul Nair, Rockwell Jackson, Hannah Kerner

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13935v1](https://arxiv.org/pdf/2610.13935v1)

**Abstract**: Interpreting machine learning model predictions is a central challenge, particularly for black-box vision models. Concept-based attribution methods interpret models using human-understandable concepts. Existing concept-based methods can only interpret classification and regression models. They require access to model weights or large concept-annotated datasets, and most methods cannot provide image-level attribution. We propose Hide and Seek (HnS), a new method for concept-level attribution that does not require access to model weights or labeled concept datasets. HnS can interpret a wide range of vision models. Given a concept and image set, HnS retrieves concept-aligned images using a vision-language model, localizes the concept within each image, masks the localized region, and measures attribution from the change in the black-box model's output between the original and masked images. This enables faithful attribution by directly measuring the model's behavior and supporting local attributions. We validated HnS on CelebA and COCO-Stuff. Compared to existing methods, HnS showed better agreement with ground-truth attributions. We demonstrated the applicability of HnS on diverse tasks, including image captioning and satellite image segmentation, where no existing concept attribution method can be used. We provided our anonymous code in the supplementary material.


### Chronos Policy: Learning Robot Policies on Physical Time
**Authors**: Changhao Wang, Jaden Clark, Shuran Song

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13929v1](https://arxiv.org/pdf/2610.13929v1)

**Abstract**: Robot policies often convert sensing and control into fixed-rate observation-action sequences, leaving physical time implicit in sequence position. This assumption breaks when observation rates or delays vary, or when inference latency changes. We introduce Chronos Policy, which makes physical time explicit by conditioning on observation capture times and desired action execution times. We study two ways to incorporate time into a diffusion transformer: adding timestamp embeddings to token features, or encoding physical time in positional encoding through time-aware rotary positional encodings (time-aware RoPE). We find that time-aware RoPE is more robust, allowing attention to depend directly on physical time while keeping token content unchanged. During training, we temporally randomize which observations are sampled and when the action chunk begins, exposing the policy to a wider range of sensing and execution schedules that may occur during deployments. This also enables learning from asynchronous, multi-rate data without forcing all measurements onto a fixed temporal grid. Across simulation and real-world experiments, Chronos Policy improves performance on dynamic tasks, where observation-to-action timing is critical, and on multisensory tasks, where the relative timing between observations matters. On standard quasi-static tasks, it preserves nominal performance while improving robustness to changes in sensing and inference timing.


### AI Models Can Provably Hide Arbitrary Capabilities
**Authors**: Andis Draguns, Sumeet Ramesh Motwani, Raymond Douglas, Christian Schroeder de Witt

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13928v1](https://arxiv.org/pdf/2610.13928v1)

**Abstract**: Capability evaluations aim to surface dangerous model behaviors before deployment, but their reliability depends on the assumption that hidden capabilities can be elicited. We show this assumption does not hold under adversarial conditions by constructing backdoor attacks that embed encrypted neural networks within host model weights, decrypting and executing them only upon receiving a secret trigger. Using digital lockers, these hidden circuits remain provably hard to elicit and interpret under cryptographic assumptions, even given full access to model weights, extending prior work from hiding fixed strings to arbitrary computations. We implement our proof of concept constructions in PyTorch and evaluate elicitation through fine-tuning, weight noising, gradient-based trigger search, and latent adversarial training on a small chemical reaction prediction task - a proxy for CBRN-relevant capabilities. Our results demonstrate resistance to these methods and, together with our cryptographic guarantees, reveal a limit of elicitation-based capability audits. We release our models to support the improvement of defenses.


### Goal-Oriented Bundle Management and Flow Control for Deep-Space Communications via Reinforcement Learning
**Authors**: Sajjad Baghaeea, Aimin Lib, Shanmugarajan Balasubramanian, Elif Uysal

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13923v1](https://arxiv.org/pdf/2610.13923v1)

**Abstract**: Deep-space communications operate under intermittent connectivity, long propagation delays, and relay storage constraints. In such networks, the Bundle Protocol enables store-carry-forward communication, requiring relay nodes to manage limited storage and scarce contact opportunities. Relay-side scheduling and dropping decisions are inherently goal-oriented: transmission resources should be allocated to bundles most valuable to downstream mission objectives. Conventional schedulers, such as FIFO, do not explicitly optimize task utility and may provide unfair service across heterogeneous planetary sources. This paper presents a closed-loop modeling and learning framework for relay-side bundle and flow management in a contact-driven deep-space network, where lunar and Martian updates are forwarded through a shared-buffer relay to Earth. We quantify destination-side information freshness using excess age $Δ_i^e(t)=[Δ_i(t)-d_i(t)]^+$, where $Δ_i(t)$ denotes the Age of Information of source $i$ and $d_i(t)$ is a source-dependent delay baseline. Based on this metric, we define a goal-oriented loss that supports source-dependent nonlinear penalties, allowing prioritization according to mission relevance. We formulate relay control as a constrained semi-Markov decision process (CSMDP) and solve it using masked Lagrangian Proximal Policy Optimization (PPO). Feasibility-aware action masking restricts transmissions to bundles that can complete within the remaining contact window. DTNSim simulations indicate improved age-based utility and inter-flow fairness compared with baseline schedulers. The proposed framework jointly optimizes relay-side bundle scheduling, dropping, and flow control under contact-driven dynamics with explicit fairness considerations across heterogeneous sources.


### DyssomniaNN: Multi-Scale Spiking Neural Modeling of Human Sleep Disorders and Perceived Restedness
**Authors**: Daniel Szelogowski

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13918v1](https://arxiv.org/pdf/2610.13918v1)

**Abstract**: Clinical sleep medicine repeatedly documents profound divergences between objective sleep duration and subjective daytime impairment, notably exemplified by sleep state misperception in paradoxical insomnia and boundary instability in narcolepsy type 1. Here, we present DyssomniaNN: a multi-scale biophysical computational framework coupling Borbély's two-process regulation of sleep homeostasis and circadian drive with Saper's hypothalamic reciprocal flip-flop circuit and a recurrent corticothalamic leaky integrate-and-fire spiking neural network. We formalize five clinical cohorts across an identical 72-hour photoperiod: healthy control, circadian rhythm sleep-wake disorder (delayed-phase), chronic insomnia, paradoxical insomnia, and narcolepsy type 1. The synthetic local field potential converges closely with empirical human electroencephalography spectra from the PhysioNet Sleep-EDF database across all canonical frequency bands (spectral mean absolute error of 0.33--0.35). Furthermore, we introduce the Well-Rested Index to quantify restorative efficacy. Simulations reveal that sleep duration fails to predict restorative recovery: paradoxical insomnia achieves normal total sleep time (21.15 h) yet yields low restoration (37.6%) from unsuppressed cortical beta-band intrusion, whereas hypocretin deficiency in narcolepsy produces severe nocturnal fragmentation (781 min of wake after sleep onset) and 35 sleep-onset rapid eye movement periods. DyssomniaNN provides an in silico platform for mechanistic sleep research and virtual neuropharmacology.


## Generation
### KL Before and After Mixing: A Round-Complexity Separation in Parallel Sampling
**Authors**: Tianyi Wu

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13924v1](https://arxiv.org/pdf/2610.13924v1)

**Abstract**: A parallel sampler can choose at random which coordinates to generate together. For a target $p$ and the output law $q_U$ of a schedule $U$ drawn afresh for each output, we compare the schedule-averaged divergence $\mathbb{E}_U D_{\mathrm{KL}}(p\|q_U)$ with the output-law divergence $D_{\mathrm{KL}}(p\|\mathbb{E}_U q_U)$, in nats. Rounds commit independent draws from exact conditional marginals frozen at the round's start, each output's schedule is drawn before sampling from a finite mixture of schedules, and every scheduled round is charged. For the uniform distribution on binary strings of even length $n$ with $n/2$ ones, the least expected number of rounds at a fixed tolerance $\varepsilon>0$ is $Θ_\varepsilon((\log n)^2)$ under the first criterion but $(e^{-\varepsilon}+o(1))\log_2\ln n$ under the second, and the double-logarithmic order is attainable with the same round count on every run. For this target, a count-state recursion gives the exact least output divergence at every round cap over all causal randomized policies. The separation extends to weighted fixed-count targets with bounded weight ratios and quota fractions bounded away from zero and one, without permutation symmetry, and to the full-support Beta$(1,1)$--Bernoulli target, where the sharp expected cost under the output-law criterion is $(e^{-\varepsilon}/2+o(1))\log_2\log_2n$, attained with rare $n$-round runs. Prior work implies the order of the schedule-averaged cost on the balanced target and its $O_\varepsilon((\log n)^2)$ upper bounds on both extensions.


### Designing Protein Structures from Natural Language
**Authors**: Joseph Lee, Yanjing Li, Bo Qiang, Gregory Lau, Allyson Ettinger, Noah A. Smith, Rory Donovan-Maiye, David Baker, Hanna Hajishirzi, Pang Wei Koh

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13917v1](https://arxiv.org/pdf/2610.13917v1)

**Abstract**: A central challenge in de novo protein design is generating proteins with desired structural and functional properties. Existing design models typically require a dedicated input representation for each property, limiting the design objectives they support. We develop Prompteina, the first all-atom structure generation model that supports new and broader design objectives specified in natural language, analogous to text-to-image generation. To train Prompteina, we construct Prompteina-Data, a paired text--protein structure dataset of 1.8M structures and 50M+ captions describing global and residue-specific structural and functional properties. We adapt Proteina-Complexa, a pretrained structure generation model, through text-conditioned pretraining and finetuning that aligns residues with their corresponding text. Prompteina outperforms baselines on 15 of 18 structural properties and generates proteins that more closely match descriptions of their intended functions. In binder design, it leads baselines on at least 13 of 20 targets and improves interface confidence by 14\% over the strongest baseline. With iterative in silico feedback, Prompteina's gain over non-iterative generation is 57\% larger than the next-best baseline on the hardest targets. Finally, we experimentally validate Prompteina designs against GM2A, a target with no reported de novo binders. We identify nine binders, with the strongest at an apparent $K_{\mathrm{D}}$ of 107 nM. These results establish natural language as an effective and powerful conditioning interface for protein structure generation.


### X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service Ecosystems
**Authors**: Yeonsung Jung, Zhiyuan Wang, Zifan Wang, Vítor Albiero, Benjamin Newman, Edoardo Debenedetti, Ivan Evtimov, Ninareh Mehrabi

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13886v1](https://arxiv.org/pdf/2610.13886v1)

**Abstract**: Personal agents increasingly connect to services across the web and applications by using tools. As the effects of their actions accumulate and interact across services, unintended or harmful outcomes can arise when agents fulfill benign user requests. Proactively identifying these compositional failures requires systematically exploring diverse cross-service paths. Existing red-teaming methods often simply prompt LLMs to identify potentially harmful paths from task and environment descriptions or decompose harmful objectives specified by humans or LLMs into seemingly benign action combinations. However, generation is biased toward patterns learned during training, potentially favoring familiar tool combinations and leaving novel cross-service interactions underexplored. To address this, we propose X-AgentRed, a self-evolving red-teaming framework that discovers harmful tool call paths through a graph of tool dependencies and expands and refines them using execution feedback. By analyzing each tool's effects, potential harms, and preconditions for execution, the red-teaming agent constructs a directed graph that captures how one tool's effects can satisfy another's execution preconditions. Recipes sampled from this graph are instantiated as realistic scenarios in which agents can produce harmful outcomes. Execution feedback enables self-improvement by diversifying paths that produce harm through tool substitution and refining preconditions at blocked steps in unsuccessful paths to enable further execution. Across four frontier agentic models, X-AgentRed achieves $1.77\times$ the harmful path rate of STAC and explores a more diverse set of tools, yielding $2.99\times$ the tool coverage on average.


### Finite-Sample Guarantees for Fully Discrete Conditional Diffusion Models
**Authors**: Qiuyun Zhu

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13851v1](https://arxiv.org/pdf/2610.13851v1)

**Abstract**: We establish finite-sample guarantees for conditional diffusion models learned from data and implemented with finitely many denoising steps. Our approach aligns the score-training objective with the sampling grid, allowing statistical estimation and numerical discretization errors to be analyzed together. Under a smooth conditional density model, we derive high-probability bounds on the generated distribution's error and quantify the required number of score evaluations. For every smoothness index $β>0$, a suitable grid yields averaged conditional Kullback--Leibler (KL) divergence $\widetilde O_p(n^{-2β/(d_x+d_y+2β)})$ relative to the original target with or without early stopping. Both the full and early-stopped samplers attain average target total-variation (TV) error $\widetilde O_p(n^{-β/(d_x+d_y+2β)})$. Here $n$ is the sample size, $d_x,d_y$ are the data and conditioning dimensions, and errors are averaged over the conditioning variable. The total-variation bound matches the rate established in existing conditional distribution-estimation theory, up to logarithmic factors.


### Inference-Time Steering Across Scaffolds and Epitopes for Sample-Efficient De Novo Nanobody Design
**Authors**: Mason Minot, Simon Friedensohn, Cédric R. Weber

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13844v1](https://arxiv.org/pdf/2610.13844v1)

**Abstract**: Generative molecular design typically relies on over-generation and post-hoc filtering. Inference-time steering methods like Feynman-Kac (FK) steering improve efficiency by biasing trajectories toward high-reward candidates, yet they optimize within a single fixed configuration. In de novo nanobody design, upfront commitment to conditioning choices like scaffold identity or target epitope creates a bottleneck. Since yield varies across these conditions, steering unpromising setups wastes compute. We recast generative condition selection as an inference-time resource-allocation problem. We propose two dynamic budget allocators: a joint Global Sequential Monte Carlo (SMC) formulation that steers and allocates compute across configurations concurrently, and a decoupled approach adapting Batched Successive Elimination (BaSE). Empirically, these dynamic allocators increase the yield of designable candidates per GPU-hour nearly 5$\times$ without sacrificing diversity across distinct therapeutic targets and generative configurations.


### Studying Comics at Scale with Artificial Intelligence: The PAGE Framework and Three Studies of American Comics and Japanese Manga
**Authors**: Emilio Ferrara

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13840v1](https://arxiv.org/pdf/2610.13840v1)

**Abstract**: Comics are one of the great visual records of the twentieth century: hundreds of thousands of pages in which a mass readership saw its leaders, its wars and its heroes. Most of this record has never been studied as a whole; comics scholarship proceeds one book at a time. We argue that artificial intelligence, including generative models, can change this to the benefit of the medium itself. We propose PAGE, a framework that makes artificial intelligence an instrument for comics research. It parses every scan into panels, text and a bibliographic record; annotates each page with a vision-language model that follows a written codebook, as a human coder would; grounds samples of these readings in human annotation; and explains change across an archive, with estimates controlled for publisher and genre. We demonstrate the framework on 3,929 American comic books (1938--1956) and 87 volumes of Japanese manga, in three studies, each resting on a different capability. The first pairs text search with visual reading to recover how a mass medium portrayed political power. The second measures the page's visual form across an industry and recovers the hand of individual artists. The third follows who speaks across two comics traditions, checked against human annotation. Beyond research, the same instruments can make archives searchable by what is drawn, open comics to blind and low-vision readers, and help preserve fragile collections and credit uncredited artists. We outline a research agenda in which artificial intelligence strengthens the study, preservation and reach of the medium.


## VLA
### LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos
**Authors**: Zhiyuan Xiang, Peidong Liu, Mingyang Li, Jiawei Li, Wenhow Li, Wenbo Ding, Xiang Deng

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13732v1](https://arxiv.org/pdf/2610.13732v1)

**Abstract**: Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data. Large-scale egocentric human videos offer a rich alternative, but they lack robot action labels, and existing action annotation methods are often noisy under real-world visual complexity and diverse manipulation dynamics. We introduce LAPT-Scale, a scalable latent action pre-training paradigm with two components: LAPT-Scale-LAM learns continuous latent actions by explaining frame-to-frame visual transitions in human videos and uses them as human-derived supervision, while LAPT-Scale-Policy trains a VLA policy through human-video latent-action pre-training, target-robot embodiment alignment, and task-specific post-training. Unlike prior vector-quantized LAMs, LAPT-Scale-LAM uses a continuous latent space to preserve fine-grained motion and interaction dynamics. We further combine perceptual, semantic, and optical-flow alignment signals to improve transition-level supervision beyond pixel reconstruction. Trained on 23.3K hours of egocentric video, LAPT-Scale-LAM provides implicit action supervision for policy pre-training, yielding consistent scaling gains and improving real-robot success from 63.3% to 85.0% as annotated human video scales from 1K to 5K hours. The learned policy also generalizes to unseen visual conditions.


### JitterVLA: A Replay Benchmark for Motion Quality in VLA-Driven Human-Robot Manipulation
**Authors**: Faith Ogunwoye, Didar Seyidov, Konstantin Gubernatorov, Dzmitry Tsetserukou

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13628v1](https://arxiv.org/pdf/2610.13628v1)

**Abstract**: Vision-language-action (VLA) policies issue sparse targets whose arrival at the robot controller is delayed and irregular, so a reasonable predicted action can still produce abrupt motion near people. Remedies are evaluated on different streams, delays and metrics. JitterVLA replays identical commands and arrival traces through alternative controllers, isolating the controller's effect. We apply it to synthetic reaches, hand trajectories from 20 people, three open VLA pipelines (838 episodes) and a physical UR3. Interpolation lowered modeled p99 jerk for every source, by 83% (615 to 106 m/s^3) on human motion with 200 ms delay, at a 2.0 cm tracking cost, and the effect replicated on 598 new episodes; jerk-limited generation lowered jerk further at a larger cost. Entropy-discontinuity associations had opposite, replicated signs in two pipelines, and entropy gating helped in one but not the other. On the UR3, interpolation lowered accelerometer-derived jerk by 3.0-14.0% in all six exploratory pairs, while a position-derived metric did not resolve the contrast. JitterVLA supports screening before human-centred studies; code and data will be released.


### RARA: Robust Policy Fine-Tuning through Retrieval-Anchored Representation Alignment for Robotic Manipulation
**Authors**: Xuhui Kang, Sung-Wook Lee, Yan Zhuang, Tianle Zhong, Yen-Ling Kuo

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13578v1](https://arxiv.org/pdf/2610.13578v1)

**Abstract**: Pre-trained robot policies, such as Vision-Language-Action (VLA) models, provide a strong foundation for generalist robotic manipulation, but adapting them to new tasks with only a few demonstrations remains challenging. Directly fine-tuning a pre-trained policy often achieves strong in-distribution performance, yet it can distort the representations learned during pre-training and weaken the model's generalization ability under out-of-distribution shifts. We propose Retrieval-Anchored Representation Alignment (RARA), a two-stage adaptation method, to address this issue. First, RARA retrieves representation features from pretraining with similar task intent and motion, and aligns the policy's representations of the target demonstrations with the pre-trained representations of the retrieved demonstrations. Second, RARA fine-tunes the policy on the target demonstrations while limiting how much its representations of the retrieved demonstrations change during fine-tuning. By reducing the representation mismatch before action learning and preserving pre-trained knowledge during adaptation, RARA limits unnecessary representation drift during fine-tuning. Experiments with Diffusion Policy and GR00T on 13 tasks in RoboTwin, RoboCasa, and on a real robot show that RARA improves the average success of fine-tuning by 9.5 points in-distribution and 13.6 points out-of-distribution, and outperforms all compared baselines. Project page: https://shua-kang.github.io/RARA_robot/


### RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors
**Authors**: David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, Lars Petersson

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13516v1](https://arxiv.org/pdf/2610.13516v1)

**Abstract**: Runtime failure monitors for robot policies are typically evaluated by how accurately they distinguish failed from successful executions. Yet an accurate alarm may arrive too late for recovery, while an unnecessary intervention may disrupt an execution that would otherwise succeed. We introduce RESCUE, a counterfactual framework for evaluating whether a monitor's alarms enable useful interventions. By restoring simulator and policy states at execution checkpoints, RESCUE compares alternative actions, identifies the latest checkpoint satisfying a specified recovery criterion, and evaluates whether acting on alarms reduces expected task-completion cost. We evaluate RESCUE with OpenVLA-OFT and $π_{0.5}$ over LIBERO-Spatial and LIBERO-Plus using 128,340 counterfactual branches. Recoverability depends on the state--intervention pair rather than on robot state alone: at $τ=0.5$, 14 of 66 OpenVLA-OFT/LIBERO-Plus failures contain a recoverable checkpoint under continuation, compared with 34 of 66 under continuation or scripted recovery, while recovery reduces recoverability in other conditions. On the primary strong-policy conditions, favourable detection scores do not establish lower intervention cost. Under the evaluated stop-and-reset model, even an idealised detector can afford only a 2.0--3.3% false-alarm rate before unnecessary resets outweigh the savings from stopping failures early. These results show that monitor value depends jointly on the intervention available and the workload in which it is deployed.


### Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models
**Authors**: Min Lin, Bokai Zhou, Jianqi Lin, Kaiyuan Yang, Yicheng Chang, Junjie Yu, Xiaofan Liu, Jianhua Han, Rui Li, Shen Zhao, Xiaodan Liang

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13212v1](https://arxiv.org/pdf/2610.13212v1)

**Abstract**: Actions specify what a robot should execute, but do not describe what those commands will achieve. Vision-language-action (VLA) policies nevertheless learn primarily by predicting action chunks from images, language, and state. We introduce Action--Future Coupled Effect Learning (AFCE), which makes a future-grounded physical Effect the policy's primary prediction target. An offline tokenizer constructs temporally ordered Effect tokens from demonstrated actions, realized robot responses, and sparse visual transitions. Reconstruction objectives encourage the representation to retain executable detail and observed physical change. A flow-matching VLA predicts Effects from current images, instruction, and robot state, while a state-conditioned decoder converts them into action chunks. Embodiment-specific interfaces allow single- and dual-arm tasks to share the Effect model. On DexJoCo, AFCE achieves $50.97\%$ overall success, improving over $π_{0.5}$ and UVT by 11.82 and 15.21 percentage points, respectively. It leads on all five bimanual tasks, highlighting the value of Effect supervision for coordinated dexterous manipulation. The project page is available at https://afceproject.github.io/AFCE-Web/.


### OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models
**Authors**: Xule Gao, Xi Wang, Zehua Zang, Rui Wang, Changwen Zheng, Chuxiong Sun

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.12914v1](https://arxiv.org/pdf/2610.12914v1)

**Abstract**: Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations. While effective for learning feasible actions, this paradigm supervises policies to reproduce expert actions at each step, biasing them toward demonstration-specific action paths and providing limited guidance for recovering toward task-progress states once execution deviates from demonstrated trajectories. To address this limitation, we propose OGPO, an Offline Goal-conditioned Policy Optimization framework for recoverable VLA post-training. Instead of treating offline demonstrations merely as step-wise action labels, OGPO adaptively relabels trajectories with semantic key states and constructs goal-conditioned process rewards to optimize the policy for reaching these task-progress states. In this way, OGPO shifts VLA post-training from trajectory-level action imitation to key-state reachability learning, enabling policies to acquire a more robust ability to complete goal states from feasible off-demonstration states without requiring additional online interaction. Experiments on LIBERO and MetaWorld show that OGPO consistently improves VLA policy performance over standard supervised fine-tuning. Moreover, evaluations on LIBERO-Plus and our proposed LIBERO-ReAct, a mid-execution perturbation benchmark, further demonstrate that OGPO achieves stronger robustness and goal-directed recoverability under distribution shifts and recoverable off-demonstration states.


## Agent
### RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics
**Authors**: Weiliang Chen, Song Liao

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13889v1](https://arxiv.org/pdf/2610.13889v1)

**Abstract**: As AI agents increasingly rely on external tools, accurate retrieval is essential for reliable behavior. Existing methods optimize semantic relevance but largely ignore tool availability during execution. To address this gap, we propose RATED (Reliability-Aware Tool Retrieval via Execution Dynamics), a retrieval framework that combines robust semantic matching with dynamic reliability adaptation. RATED employs a frozen dual-encoder with contrastive fine-tuning for semantic matching, and a lightweight contextual bandit module that re-ranks candidates based on real-time execution feedback. This design enables rapid adaptation to runtime tool failures without expensive model retraining. We introduce EcoAgent, a benchmark of 5,172 real-world tools and over 210,000 query-tool pairs for offline retrieval and dynamic reliability evaluation. Experimental results demonstrate that RATED achieves a 52.2% relative MRR improvement over the ToolLLM API retriever on real-world queries, and reduces fault selection rate from 86.2% to 2.9% under severe API outage scenarios with a 30% failure rate, while incurring negligible latency overhead of less than 1 ms over encode-only inference. The code and dataset are available at https://github.com/Elliotes/EcoAgent.


### Returning to Development States: When Full Sandbox Snapshots Help Coding Agents
**Authors**: Daniel Thi Graviet, Tanmay Shah

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13841v1](https://arxiv.org/pdf/2610.13841v1)

**Abstract**: Coding agents often make useful progress before they fail, but retry-from-scratch discards the machine state created along the way. This makes failure recovery an interesting search problem: if intermediate environment states preserve meaningful progress, restoring and branching from them could outperform repeatedly restarting from the initial state. We implement Go-Explore-style search over full Daytona snapshots and find that higher and more efficient solve rates depend mainly on progress that sits outside the repository, such as databases, services, and other runtime state. Our results suggest that full-snapshot search is most effective when long-horizon coding work spans multiple services whose state cannot be reconstructed from a single diff.


### MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents
**Authors**: Jingwei Song, Zhisheng Chen, Bingfan Zeng, Jing Tang, Yubo Hou, Jinhao Jing, Zhengwei Xie, Linfeng Zhang

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13829v1](https://arxiv.org/pdf/2610.13829v1)

**Abstract**: A central challenge in embodied recursive self-improvement is enabling agents to convert interaction history into capabilities that persist beyond one world and transfer to later tasks. A saved memory or successful final action does not by itself establish that a reusable capability was acquired; evaluation must separate capability change from carried-over resources, unequal source exposure, and early execution failures. We construct MC-EvoBench as a controlled Minecraft benchmark with a fixed catalog of 19 registered evolution chains, including 12 primary evaluation chains and seven calibration or probe chains, together with three graph-aligned paired probe families for transfer. The benchmark represents each task as a task-state graph, defines stage-level environment verifiers, assigns matched source and target roles, resets the target world, and permits only a declared agent artifact to cross the source-target boundary. For each probe, no-prior, related, unrelated, and shuffled source conditions are evaluated under matched environment-step budgets and five seeds; we report TSR, WGP, and VMP and retain provenance records. The benchmark reveals a consistent direct-capability gap between controller and planner-backed variants, while related experience yields no stable transfer: it does not improve either tool probe, its small wood-species gain hinges on one seed, and all intervals include zero. Stage audits further show that early wood-collection and crafting bottlenecks often leave later capabilities unobserved. MC-EvoBench thus offers a controlled testbed for durable, transferable embodied capabilities. Code and data are available at https://github.com/xzw-ustc/mc-bench-open-source


### Matched-Context Group Policy Optimization for LLM Agent Training
**Authors**: Chenxu Zhang, Yaorui Shi, Wenlong Zhang, Jianchao Tan, Zihan Wang, Yiming Cheng

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13755v1](https://arxiv.org/pdf/2610.13755v1)

**Abstract**: Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-Context Group Policy Optimization (MCGPO), a procedure for constructing weighted action preferences from already collected trajectories. MCGPO defines comparison contexts with pre-action state summaries and observed rubric progress, annotated by task rules. Two-action support selects among ordered exact and coarse matching rules. Fixed folds separate candidate decisions from the terminal outcomes used to orient their preferences, and support-dependent evidence weights scale an auxiliary pairwise objective alongside shared GraphGPO task learning. MCGPO reuses rollout data and each response's original history, preserving critic-free training. Across six environment-backbone settings with three training seeds each, MCGPO improves mean success over matched GraphGPO: by 0.47-1.46 percentage points on ALFWorld and WebShop with Qwen2.5-1.5B and 7B, and by 3.96 and 5.16 points on WebShop with Qwen3-4B and 8B. The ALFWorld gains build on baseline success above 92%, where remaining headroom is limited. Integrated success improves in three of four Qwen2.5 settings. Three-seed factorial controls support opposite-fold evidence and evidence weighting; joint state-rubric matching achieves the highest mean in all four representation-control settings.


### SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning
**Authors**: Hongrui Zheng, Aditya Singh, Rahul Mangharam

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13737v1](https://arxiv.org/pdf/2610.13737v1)

**Abstract**: Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL, a constrained multi-agent reinforcement learning framework that allows for credit assignment even with joint constraint measurements. We use Signal Temporal Logic (STL) robustness to measure episode-level violation through running-maximum cost increments. Smooth full-episode robustness and differentiable dynamics provide action sensitivities, which allocate each cost increment across agents at the same decision time. These sensitivities account for delayed effects when weighting agents' shares of each cost increment. We study the framework in cooperative payload transport, connected navigation, and networked traffic control tasks. SafeDiSTL achieves 1.6-5.1x the safe-success rate in transport, improves navigation safe-success by 11.1%, and delivers 50-68% more throughput in traffic when compared to constrained baselines. Results demonstrate a strong improvement of the learned policy in dealing with shared constraint while retaining the performance of unconstrained policies.


### A Baseline Assessment for the Agentic Web Technology Stack
**Authors**: Vagner Figueredo de Santana, Diogo Cortiz

**Published Date**: 2026-10-09

**Updated Date**: 2026-10-09

**PDF Url**: [2610.13703v1](https://arxiv.org/pdf/2610.13703v1)

**Abstract**: The fast pace in which protocols, frameworks, and technologies are being proposed for LLM-based agents results in a complex scenario for anyone aiming to create state-of-the-art AI solutions. Without an assessment on how different protocols, frameworks, and libraries work together to compose an Agentic Web solution, developers and organizations face different challenges (e.g., skilling, governance, infrastructure) even before becoming part of the Agentic Web ecosystem. In this context, we propose a system for performing Agentic Web evaluations called MASTIF (Multi-Agent System TestIng Framework) and present a baseline assessment of Agentic Web technologies, including 3 LLMs, 3 protocols, and 4 agent implementation frameworks, against 300 Mind2Web benchmark tasks. Results suggest that selecting a task-specific technology stack may result in gains of task completion rate, efficiency score, and social value stability scores; and reductions in verbosity and time to complete tasks. With the presented results, we expect to present a baseline in terms of metrics and results for this complex and fast evolving scenario for those aiming at designing, assessing, and developing multi-agent systems.


