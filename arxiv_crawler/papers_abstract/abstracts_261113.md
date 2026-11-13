# Abstracts of Papers

## World Model
### Unbundling Multimodal Vision Encoding
**Authors**: Ellis Brown, Chris Hoang, Shengyi Qian, Shang-Wen Li, Mike Lewis, Marjan Ghazvininejad, Luke Zettlemoyer, Lucas Beyer, Mengye Ren, Jakob Verbeek, Saining Xie, Hu Xu

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17334v1](https://arxiv.org/pdf/2611.17334v1)

**Abstract**: How multimodal language models should encode visual input remains up for debate. Most models use a pretrained vision encoder, while some recent recipes train the encoder from scratch with the language model or remove it entirely. Vision encoders bundle together three design choices: a visual prior from upstream pretraining, dedicated vision capacity, and pre-fusion placement of that capacity (i.e., before the multimodal backbone). Because published models also differ in data, architecture, and compute, comparing them cannot isolate the effect of each choice. We disentangle these choices via a controlled framework where we pretrain all models from scratch on common data and compare them on visual question answering and language benchmarks at matched lifetime compute. We find that the visual prior is not necessary; an encoder trained jointly from scratch is on par with a pretrained one, without a separate training stage. What matters instead is dedicated vision capacity: an encoder-free model trails on visual understanding even when its backbone is enlarged by the encoder's parameter count. Yet that capacity need not precede multimodal fusion, as vision-only modules added in-fusion to early backbone layers perform comparably to a pre-fusion encoder and can lower time to first token. These results also hold across backbone sizes, when encoder pretraining is treated as free, and when starting from a pretrained language model. Overall, our findings favor dedicated vision capacity trained jointly with the backbone and placed early within it.


### ArchSpace: Recording, Reviewing, and Referencing LLM Architecture Research
**Authors**: Jie Wang, Tong Zhu, JiaHao Kuang, Zhe Xu, Yunkai Chai, Dehong Zheng, Yu Cheng, Tao Ji, ZhouHan Lin, Qi Zhang, Bowen Zhou

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17332v1](https://arxiv.org/pdf/2611.17332v1)

**Abstract**: Model architecture shapes the scaling behavior, training efficiency, and inference cost of LLMs, making it a central focus of both industry and academia. In industry, teams such as those behind DeepSeek, Qwen, and Kimi routinely introduce architectural innovations, yet public reports rarely document which ideas succeeded, which were abandoned, and why. In academia, limited compute and inconsistent baselines often restrict evaluations to small-scale, single-point comparisons, making it difficult to establish whether improvements hold at larger scales or translate into broader impact. ArchSpace addresses both gaps as a public platform for Recording, Reviewing, and Referencing Architecture Researc}: each proposal is recorded with its experiments and reasoning, reviewed by the community, and referenced by later work. To evaluate ideas before costly large-scale training, ArchSpace leverages scaling laws to predict model loss at larger scales from smaller experiments, a practice widely adopted in industry. We provide initial references that make the platform usable: Qwen3.5 and OLMo3 baselines, fitted scaling laws, and a reusable training recipe. Ideas validated through this review can in turn become new baselines, and ArchSpace thereby aims to broaden the range of ideas that shape the next generation of models.


### Internalizing Investment Mandates: A Neurosymbolic RL Approach to Portfolio Allocation
**Authors**: Zeynep Yıldız, Satchit Chatterji, Ercan Atam, Erman Acar

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17329v1](https://arxiv.org/pdf/2611.17329v1)

**Abstract**: Institutional portfolios operate under investment policy statements that specify asset allocation constraints, often conditioned on market regime information. Deep reinforcement learning has been shown to optimize financial performance but typically does not enforce rule compliance, making it unsuitable for real-world deployment. Existing neurosymbolic methods such as Probabilistic Logic Policy Gradient (PLPG) offer constraint-satisfying reinforcement learning (RL) via differentiable symbolic supervision but assume a finite, discrete action space. We present a PLPG-inspired continuous allocation method that estimates the probability that the policy's own executed action satisfies the investment mandate, using reparameterized Monte Carlo sampling, and adds it to the training objective. No post-hoc enforcement mechanism intercepts actions at inference time and compliance is learned by the agent. Audited directly on deterministic mean actions with no correction, the policy reduces violations of a six-rule regime-conditional mandate from 96-98% for unconstrained RL and 33.4% for a reward-penalty baseline to 4.8%, showing that a continuous-action neurosymbolic policy can substantially internalize a symbolic mandate.


### AgentSSL: Can MLE Agents Leverage Unlabeled Data?
**Authors**: Ethan Lin, Akanksha Sarkar, Ziang Liu, Kristin Branson, Jennifer J. Sun

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17323v1](https://arxiv.org/pdf/2611.17323v1)

**Abstract**: Applying machine learning systems to new domains introduces bottlenecks in both labeled data acquisition and manual pipeline engineering. While recent MLE agents show promise in automating pipeline design, they have been studied almost exclusively in fully supervised settings, leaving them untested in realistic regimes where labeled data is scarce but unlabeled data is abundant. In this work, we introduce Agentic Semi-Supervised Learning (AgentSSL), framing SSL as a program search problem and studying how agents navigate this space under limited supervision. We find that even under weak feedback and matched compute, agents can synthesize code that combines and adapts established SSL techniques, exceeding the strongest human-engineered baselines in 8 of 12 settings by up to +21.8%. However, our results identify program selection as a critical bottleneck in AgentSSL, where performance drops by as much as 47% when selecting based on the agent's feedback metric. To systematically study this bottleneck, we introduce ProgramSelectBench, a large-scale benchmark with a combined total of 16,977 agent-generated and human-engineered SSL programs, and evaluate both unsupervised and active program selection methods. We further evaluate AgentSSL on real-world ecology detection tasks, highlighting the opportunities and challenges of transferring agent-discovered strategies beyond controlled benchmarks.


### Spatial Foundry: A Multimodal Dataset for Spatial Intelligence
**Authors**: Ethan Lin, Yang Song

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17318v1](https://arxiv.org/pdf/2611.17318v1)

**Abstract**: Spatial intelligence requires connecting visual observations to the geometry, objects, and persistent state of an environment. Images alone leave these relationships implicit, while disconnected annotations make it difficult to study appearance, camera motion, and scene changes under a common reference. We introduce Spatial Foundry, a collection of 5,280 furnished residential 3D scene configurations with editable assets and aligned visual, geometric, and temporal data. Its modalities include floor plans, perspective and panoramic RGB, metric depth, point clouds, meshes, instance-level 3D bounding boxes, and camera trajectories paired with video. Shared scene coordinates link observations across views and time; editable source scenes enable additional camera paths and controlled object changes. We describe the data representation and construction workflow, and discuss applications in floor-plan-conditioned 3D generation, geometric reconstruction, instance-level perception, camera-conditioned video generation, shared world modeling, and scene editing. Controlled camera and scene variations support spatial perception and world-model research. The public project page provides videos and an interactive colored point-cloud preview.


### CoReMem: Cost-Internalizing Memory for Successive Coding Tasks with Prospective Valuation
**Authors**: Peiwen Li, Harshit Verma, Sophia Zhou, Haiwen Wang, Ngoc Bui, Heng Chang, Fei Fei, David van Dijk, Rex Ying

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17316v1](https://arxiv.org/pdf/2611.17316v1)

**Abstract**: Coding agents tackle successive tasks on an evolving repository, carrying forward edits and writing memory before the next task is known. Selecting memory for unknown next tasks requires balancing future usefulness against the costs of writing and reading it. The actor must also decide when acting on available memory saves effort as the task unfolds. We introduce Coding-Repository Memory (CoReMem), a cost-internalizing framework that guides memory design and actor adaptation through measured memory value on the next task. Prospective segment valuation compares runs of the next task with and without individual trajectory segments from the same inherited repository state, guiding a compact memory built around anchors: repository locations and executable checks. Actor adaptation estimates on-policy memory value within rollout groups with and without memory, using a reward that prioritizes resolution and penalizes step count in successful runs. Provenance-gated value credit assigns the additional value term to steps identified as using memory-supplied anchors, while every step retains outcome credit. On ChainSWE, CoReMem raises the 27B actor's resolve rate from 21.0% to 25.7%, with 17% fewer steps and 11% fewer total cache-aware tokens, including memory-module calls, relative to the untrained actor model without memory.


## Generation
### Quantifying structural stability of transparent models for general insurance pricing
**Authors**: Félix Côté, Marie-Pier Côté

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17308v1](https://arxiv.org/pdf/2611.17308v1)

**Abstract**: The short duration of general insurance contracts leads to rapid distributional shifts in the data, warranting regular model updates. This process may yield a post-update model that differs considerably from the pre-update model in both predictions and structure. Structural stability is upstream of predictive stability, yet existing structural stability metrics are mostly restricted to simple decision trees. Thus, we first introduce the notion of functional transparency, characterising models with a prediction function that can be expressed as a sum of univariate functions for main effects and bivariate functions for pairwise interactions. Then, we propose the Mean Squared Shape function distance, a metric to quantify the structural stability of functionally transparent models, which are particularly relevant in actuarial science. Using three public auto insurance datasets, we present a benchmark study to demonstrate the usefulness of our metric in identifying a stable and accurate transparent model. Generalised linear models with centred numerical covariates are stable, and explainable boosting machines (EBMs) offer a compromise between stability and performance. We also find that stabilisation strategies, such as sequential modelling and fixed hyperparameters, can substantially improve stability for both EBM and XGBoost models, with negligible impact on performance.


### Consistent Video-to-Video Translation via Explicit Correspondences
**Authors**: Gaurav Parmar, Zhengqi Li, Richard Zhang, Jun-Yan Zhu, Srinivasa Narasimhan, Eli Shechtman, Yotam Nitzan

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17298v1](https://arxiv.org/pdf/2611.17298v1)

**Abstract**: Interactive video-to-video applications require real-time generation while maintaining long-range temporal consistency. However, recent methods achieve speed by restricting attention to a fixed-length causal window. This limits long-range consistency whenever relevant history falls outside the context window. To address this limitation, we introduce vid2vid-long, a correspondence-based approach grounded in a simple observation. Video-to-video translation provides an explicit cross-frame reference: the regions that match in the input video should match in the output video too. Concretely, we compute patch-level correspondences in the input, guiding retrieval of previously generated outputs in the corresponding regions, and condition the model on these patches through correspondence cross-attention. Our experiments demonstrate that vid2vid-long consistently improves long-range temporal consistency across recent video models while preserving generation quality and real-time performance.


### Metal Sandbox: Isolated Execution and Command Scheduling for GPU Coding Agents on Apple Silicon
**Authors**: Haozhe Wang, Lina Chen, Fanqi Wan, Qi Han, Yinmin Zhang, Zheng Ge, Daxin Jiang, Junchi Yan

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17294v1](https://arxiv.org/pdf/2611.17294v1)

**Abstract**: On-device inference requires kernels that make effective use of local accelerators. Efficient training and evaluation of models that generate Apple Metal kernels benefit from native macOS tools and concurrent agent sessions. These sessions alternate between model requests, development commands, and GPU execution, leaving GPU capacity idle for much of a rollout. We present Metal Sandbox, infrastructure that combines restricted per-instance file access, native command execution, and command-level scheduling across interconnected Macs. Each agent retains its workspace and private development environment. Parallel commands can run concurrently, while serial commands share one execution slot per node; eligible waiting commands can migrate to available Macs and return results to the original agent. Integration with Harbor supports task execution, automatic verification, and rollout collection through a common workflow. Controlled experiments on four Mac mini M4 nodes achieve $1.68\times$--$2.05\times$ gains in command throughput under concentrated demand. Sixteen static agent traces give an estimated $2.14\times$ sustained-throughput gain for four sessions per node versus one, assuming continuously replenished sessions and unchanged mean durations. Replaying these measured traces under dynamic scheduling reduces mean tool waiting by 18.8% and batch elapsed time by 22.3%, assuming unchanged phase durations. Metal Sandbox and its Harbor integration are open-source on GitHub.


### Negative-Only Policy Optimization for One-Sided Verifiable Rewards
**Authors**: Jiacheng Xu, Shuo He, Fuxiang Zhang, Chaojie Wang, Bo An

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17287v1](https://arxiv.org/pdf/2611.17287v1)

**Abstract**: Reinforcement learning with verifiable rewards (RLVR) typically relies on a verifier that can reliably judge whether sampled solutions are correct. However, in many realistic settings, complete verification is generally unavailable, while cheap checks can only falsify failures. We formalize this regime as one-sided verifiability (OSV): verified negatives are reliable counterexamples, but verified positives are merely non-falsified candidates and may contain many false positives. This asymmetry makes standard RLVR unreliable, because reinforcing verified positives can directly reward shortcuts that pass partial checks. To address this issue, we propose Negative-Only Policy Optimization (NOPO), which treats verified positives as unlabeled and updates the policy only by suppressing trusted verified negatives. Specifically, NOPO combines a reference-relative negative suppression loss with a group-level adapter that scales each update by the proportion of non-falsified responses. Across unit-test, constraint-check, and LLM self-verifiers, NOPO improves pass@k over baselines on code, logic, and math benchmarks when oracle rewards are unavailable. These gains persist under inference-time scaling and cross-benchmark transfer.


### Synthesis Smuggling: Maliciously Hiding Inferred Personal Attributes in LLM Outputs
**Authors**: Gautam Galada, Supreeth Shastri, Sagnik Ray Choudhury

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17280v1](https://arxiv.org/pdf/2611.17280v1)

**Abstract**: We propose Synthesis Smuggling, a novel threat model in which an adversarial LLM infers sensitive information about a user from routine assistance-seeking interactions and steganographically encodes that into innocuous-looking model-generated content. The user may then unknowingly transmit that information by sharing the generated artifact, say as an email, social-media post, or message, through ordinary communication channels. An adversary monitoring these channels can discover this information. We demonstrate this threat by training two open-weight models to infer gender and age-group labels from conversational cues and encode their predictions using invisible characters or word choices. These results show that user-shared model outputs can become a covert channel for personal inferences, even when the model itself has no direct means of contacting an adversary.


### LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds
**Authors**: Pengcheng Zhou, Xuanyu Liu, Yanchen Yin, Tianjie Ju, Bobo Li, Shengqiong Wu, Hao Fei, Mong-Li Lee, Wynne Hsu

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17267v1](https://arxiv.org/pdf/2611.17267v1)

**Abstract**: We introduce GeoWorld, a controllable and continuously evolving geographic environment platform for LLM agents, and LiveGeo, a benchmark for evaluating reliable decision-making in real-world geographic environments using GeoWorld. Unlike existing evaluations that largely reason and plan over fixed geographic states, GeoWorld is grounded in real-world geographic structure and allows external world states to evolve along their own temporal processes while preserving verifiable state histories. LiveGeo places geographic tasks within this evolving environment, requiring agents to actively acquire task-relevant information, verify whether the evidence supporting prior decisions remains valid, and revise their plans when necessary. Our results reveal that even frontier LLMs struggle with static tasks, with no model consistently excelling across tasks, while strong static performance does not ensure dynamic reliability. Further analysis identifies a key bottleneck: agents struggle to acquire and translate relevant evidence into valid decisions and maintain their correctness as the world evolves. By releasing LiveGeo together with its GeoWorld platform, we aim to provide the community with a flexible and extensible infrastructure for studying the next generation of agents capable of reliable action in evolving geographic worlds.


## VLA
### What Can a VLA Learn from the Agent That Calls It? Task-Level Experience Distillation for Embodied Navigation
**Authors**: Jinze Tao, Yuxiao Han, Kangkang Dong, Yancong Wei, Xiaojun Zhu, Bokui Chen, Houde Liu

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.16246v1](https://arxiv.org/pdf/2611.16246v1)

**Abstract**: Navigation agents use a large language model (LLM) planner to call a vision-language-action (VLA) model. Each episode needs the LLM, adding cost and delay. We distill successful agent experience into the VLA instead of distilling the planner. The VLA then navigates alone at test time. Agent sessions are not VLA demonstrations. They include motions driven by planner tools and sub-instructions, along with detours. We present H2E, a task-level experience distillation method that converts these sessions into VLA training data. Every motion becomes a VLA action under the original task instruction, with the resulting poses as targets. H2E masks the loss on steps that move away from the goal. It labels every visited state within 1 m of the goal as a stop. We then update the VLA with low-rank adaptation. The VLA learns to stop at the goal and find goals the base model never reaches. On all 3,189 REVERIE-CE val-unseen episodes, H2E raises the success rate of an 8B VLA from 35.0% to 44.9%.


### What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation
**Authors**: Zhuoyue Li, Zhendong Han, Pankhuri Vanjani, Wenting Li, Rudolf Lioutikov

**Published Date**: 2026-11-11

**Updated Date**: 2026-11-11

**PDF Url**: [2611.15491v1](https://arxiv.org/pdf/2611.15491v1)

**Abstract**: Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed. We study what makes a pretrained VLA reactive, using \pihalf{} on two dynamic simulation benchmarks and three real-robot tasks. We vary the prediction and execution horizons, compare synchronous and asynchronous inference, test methods that deliver actions sooner or keep successive chunks continuous, and adapt the policy with motion cues and latent-space reinforcement learning. The best prediction horizon is about one second, and the best execution horizon depends on the checkpoint. Short horizons help more with asynchronous execution, and methods that keep the trajectory continuous outperform those that only reduce latency. Adapting the policy repairs targeted failures, but on the conveyor task changing the execution horizon gained as much. Reactivity depends on the execution pipeline as much as on the policy, so both should be evaluated together.


### CARE-Drive: Coupled Alternating Refinement for Ego-trajectories
**Authors**: Xiao Ma, Yijun Chen, Zhiquan Hu, Jicheng Zhao, Yuming Li, Chuang Dai

**Published Date**: 2026-11-11

**Updated Date**: 2026-11-11

**PDF Url**: [2611.15360v1](https://arxiv.org/pdf/2611.15360v1)

**Abstract**: Vision-language-action (VLA) models bring multimodal understanding and world knowledge to end-to-end autonomous driving. To further improve the quality of predicted trajectories, existing studies introduce candidate refinement, residual denoising, and token correction. However, these methods typically focus on unified refinement of the entire trajectory, paying limited attention to the distinct physical quantities and their interactions. We further investigate physical specialization and coordination in trajectory refinement, centering on position and heading for simpler and more intuitive correction modeling. To this end, we propose CARE-Drive (Coupled Alternating Refinement for Ego-trajectories), which decomposes trajectory refinement into waypoint residual correction and position-conditioned heading generation. Through imitation learning and a future-token auxiliary task, the backbone provides predictive representations and a base trajectory. The position expert predicts bounded metric waypoint residuals, while the heading expert reconstructs vehicle orientation from adjacent angular increments conditioned on the corrected path. With the backbone frozen, the two experts are optimized alternately through supervised initialization and reinforcement fine-tuning. This design simplifies refinement through clear physical specialization while preserving conditional coupling during prediction and optimization. On NAVSIM v1, CARE-Drive achieves 88.8 PDMS, improving by 2.4 points over the unrefined base trajectories generated by the same backbone. Ablation studies further support the effectiveness of specialized experts and staged training.


### Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models
**Authors**: Wen-Han Hsieh, Ken Jiankun Zheng, Chia-Chien Chen, David M. Chan, Trevor Darrell

**Published Date**: 2026-11-10

**Updated Date**: 2026-11-10

**PDF Url**: [2611.14834v1](https://arxiv.org/pdf/2611.14834v1)

**Abstract**: Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation. However, sampled action sequences can be ineffective, while evaluating alternatives with computationally expensive verifiers adds latency at each policy query. In this work, we propose HDH, a lightweight framework that uses hindsight from a frozen VLA's own deployments to improve action verification. The framework has three stages. First, we deploy the policy and collect its autonomous rollouts. We then train a compact action verifier to assign each action chunk a predicted task-success score. Finally, the frozen VLA generates action candidates, and the verifier selects the candidate with the highest score for execution. Across four LIBERO-10 tasks, HDH achieves an average success rate of 82.3\% and on three real-world manipulation tasks, HDH improves average success over the baseline policy by 22.6\%.


### DeltaForge: A Post-hoc Mixture-of-Experts VLA for Multi-Domain Autonomous Driving
**Authors**: Bingzhang Wang, Mo Poorsartep, Yasaman Esfandiari

**Published Date**: 2026-11-09

**Updated Date**: 2026-11-09

**PDF Url**: [2611.11856v1](https://arxiv.org/pdf/2611.11856v1)

**Abstract**: Fleets of driving vision-language-action (VLA) models are developed one domain at a time: each operator finetunes a shared base model on private data, producing specialized experts that are costly to consolidate into a single model. Weight merging loses accuracy as heterogeneous domains accumulate, and dense mixture-of-experts routing is prohibitively expensive to combine them. We present DeltaForge, to our knowledge the first post-hoc mixture-of-experts VLA for driving, which consolidates N independently finetuned per-domain models into a single multi-domain model from their weights and a small proxy set alone. When different operators finetune the same base model, their weight updates end up sharing a lot of structure. We exploit this by decomposing all the updates together using singular value decomposition (SVD), splitting each one into a shared part (the same across all domains) and a tiny domain-specific part. The router then only needs to work with those tiny domain-specific pieces, not the full expert weights, which is what keeps the approach efficient. Then two cooperating clip-level blind routers, one over the VLM reasoning experts and one over the flow-matching dynamics experts, are trained from soft labels on the proxy dataset. Across six diverse domains spanning urban, off-road, and highway driving on cars, trucks, and all-terrain vehicles (ATVs), DeltaForge approaches the accuracy of the per-domain experts and surpasses every merging, routing, centralized, and federated baseline at close to single-model parameter and compute cost. Adding a new domain requires only projecting its weight update onto the shared basis with no end-to-end retraining needed. The resulting model also generalizes to domain combinations it was never explicitly trained on.


### Decoupled Asynchronous System for Humanoids (DASH): Latency-Agnostic Scaling of Vision-Language-Action Models for Humanoid Manipulation
**Authors**: Bingzhang Wang, Nathan Zhao, Jialeng Ni, Jiayin Zheng, Yin Zhang, Kehua Chen, Jian Yao

**Published Date**: 2026-11-09

**Updated Date**: 2026-11-12

**PDF Url**: [2611.11854v2](https://arxiv.org/pdf/2611.11854v2)

**Abstract**: Vision-language-action (VLA) models pair a vision-language backbone with an action head, but in closed-loop control the backbone sits on the control-critical path: while it computes, the robot keeps moving, so each executed action is conditioned on an increasingly stale observation. A larger backbone therefore directly blocks reactivity, especially in humanoid dexterous manipulation. We present DASH, a Decoupled Asynchronous System for Humanoids that removes this coupling. DASH splits the policy into a slow vision-language model (System 2) and a fast flow-matching action head (System 1) that run as concurrent processes over the LCM communication protocol, so the control rate is set by the action head alone, independent of backbone size. The action head fuses stale semantics from a frozen backbone with fresh vision from its own ResNet encoder, desynchronized training exposes it to the staleness it meets at deployment, and an adaptive temporal aggregator aligns overlapping action chunks under variable inference latency. On an asynchronous RoboTwin benchmark that charges inference latency in simulated time, DASH holds 20 Hz control rate from 0.8B to 8B backbones while the synchronous rate falls from 9.7 to 4.1 Hz, with higher success at every size. On a real humanoid with dexterous hands, DASH achieves clearly higher pick-and-place success than the synchronous pipeline.


## Agent
### Scalable Conversational Assessment: Chat-Based Exams with a Two-Agent LLM Pipeline
**Authors**: Geoffrey Challen, Craig Zilles

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17220v1](https://arxiv.org/pdf/2611.17220v1)

**Abstract**: Oral exams are compelling because (1) students can be asked to provide their reasoning for an answer and (2) their interactive nature permits follow-up questions to resolve ambiguous answers. But oral exams scale poorly. In this paper, we present scalable conversational assessment, an LLM-based system that conducts interactive text-based conversations with students to assess their ability to make and support an argument. We use a two-agent architecture to separate concerns and reduce the likelihood that answers are leaked to the student: the interviewer interacts directly with the student, but only receives guidance about the next question to ask the student; the hidden evaluator knows the goals of the whole activity, tracks the student's progress using a rubric, and guides the interviewer on when to follow-up on the current question or proceed to the next question. The system was first tested using a collection of simulated students with LLM personas of a particular ability level or adversarial tactic (e.g., answer-extractors, prompt-injectors, confident fabricators). A novel element of this evaluation was that it required the use of a fictional assessment topic to prevent personas that shouldn't have information from using knowledge present in the LLM's pre-training. The system was also deployed in a small, elective AI literacy course in both formative and summative contexts. Through manual and post-facto AI review of the transcripts we identified opportunities to improve the follow-up question generation and ensure that grading only credited ideas that the student (and not the interviewer) contributed.


### Cortex-FL: Agent-Mediated Collaboration for Federated Learning
**Authors**: Rui Sun, Jinfeng Peng, Zehua Cheng, Jiahao Sun, Zhipeng Wang

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17186v1](https://arxiv.org/pdf/2611.17186v1)

**Abstract**: Federated learning (FL) enables independent data owners to train models collaboratively without centralizing raw data. However, identifying collaborators, preparing training tasks, and coordinating execution and incentives hinder its practical adoption by organizations without specialized expertise. We present Cortex-FL, an agent-native FL system that enables users to express learning objectives in natural language and delegate the collaboration required to train a model. Agents translate these objectives into shared tasks, discover collaborators, and negotiate participation agreements, connecting collaboration formation with distributed training and incentive management. The architecture separates agent coordination from local execution authority, allowing owners to delegate coordination while retaining control over their data, computation, and financial commitments. We demonstrate the complete workflow on a four-node deployment, in which a model requested in natural language proceeds through collaboration formation, contract-governed training, verified model delivery, and x402 settlement on a blockchain testnet.


### Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents
**Authors**: Haochen Liu, Qianhao Zhu, Zixuan Wang, Dingming Li, Tongbo Chen, Peng Qiu, Yingqi Qu, Weiming Lu, Jun Xiao, Yongliang Shen

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17167v1](https://arxiv.org/pdf/2611.17167v1)

**Abstract**: Decision models answer a question with a typed output, such as a choice among options with a probability for each, so one model can choose an agent's actions, evaluate actions already taken, or score every action to teach a policy with reinforcement learning. Prior work has studied them mainly as actors, judging their usefulness by how well they act. We ask whether a decision model that acts poorly can still teach well. We compare three decision models and three general LLMs as actors and judges on ALFWorld, and use JEV as a teacher on ALFWorld and WebShop. As actors, all six models are pulled away from a subgoal that must come first by an easier one. As judges that see the whole trajectory, the same models credit the steps toward that subgoal, and asking whether each action helped, rather than whether the task will succeed, separates useful from useless actions. As a teacher, JEV raises a Qwen2.5-1.5B policy over GRPO from 72.8% to 82.9% success on ALFWorld and from 56.8% to 71.4% on WebShop. These results suggest that a poor actor can still teach well, because judging an action after the episode ends reveals the consequences that acting must anticipate. Code is available at https://github.com/ZJU-REAL/decision-agents.


### Paper-Faithful Federated Learning: Scientific Checks for Practitioner and Agent Development
**Authors**: Ali Dadras, Alp Yurtsever

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17129v1](https://arxiv.org/pdf/2611.17129v1)

**Abstract**: Federated learning experiments can produce reasonable-looking results even when the experiment implementation differs from the intended experimental protocol. Small errors in configuration, data partitioning, aggregation, randomness, evaluation, or checkpoint recovery may therefore affect a comparison without causing the program to fail. We present FedBrew, a research codebase for controlled and reproducible federated learning experiments. Its focus is controlled simulation with checks of specified conditions of the intended experimental protocol. FedBrew uses configuration checks, identifiable client data partitions, checkpoint recovery checks, self-describing run records, and development-time checks of scientific conditions. These checks assess, for example, whether client partitions are disjoint and exhaustive and aggregation weights match the prescribed rule; numerical and recovery checks examine non-finite client model states and interrupted runs. The same structure also provides clear extension points and automated checks for new algorithms, datasets, models, and tasks, whether they are added by researchers or AI coding agents. FedBrew therefore supports reproducible and inspectable FL experiments through checks of specified software and scientific conditions and the run records associated with reported results.


### CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts
**Authors**: Zimo Xu, Wenzhuo Liu, Hideki Nakayama

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17115v1](https://arxiv.org/pdf/2611.17115v1)

**Abstract**: Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether small language model (SLM) agents can be trusted to write these artifacts. Across 15 open-weight models, 13 of them between 1.7B and 12B parameters, they cannot: the policies, graphs and constraints that the agent's model writes admit attacks on 14 (Progent), 13 (IPIGuard) and 11 (DRIFT) of the models, and CaMeL's programs fail to run in up to 68% of episodes. We present CapLite, which derives its policy from the tool schemas, commits the write calls before any tool result is read, and admits a write only if every argument that decides whom or what it affects is stated in the user's request. This guarantees write integrity: injected text cannot add a write, and no write reaches a recipient, amount, object or destination that the user did not state. No attack succeeds in 13,935 attacked AgentDojo episodes. CapLite reaches utility under attack comparable to CaMeL's (29.0% vs. 27.2%) with fewer tokens than every other enforcement defense and than the undefended agent: 17.1k per episode, 18% of CaMeL's, and the highest utility per token of all enforcement defenses.


### Designing Institutions for Autonomous AI
**Authors**: Petter Törnberg

**Published Date**: 2026-11-12

**Updated Date**: 2026-11-12

**PDF Url**: [2611.17114v1](https://arxiv.org/pdf/2611.17114v1)

**Abstract**: As autonomous AI agents increasingly interact in persistent populations, their collective capabilities and alignment depend not only on individual models, but also on the institutions governing their interactions. Yet AI research has largely focused on individual agents. In this Perspective, we argue that institutional design must become a distinct focus of AI research. Drawing on institutional political economy, social epistemology and organizational theory, we develop seven principles for designing AI institutions that sustain cooperation, enable reliable collective judgments and remain accountable to legitimate human purposes. These address reciprocal contributions, accountable authority, functional differentiation, epistemic pluralism, criticism and correction, human direction, and institutional adaptation. We illustrate their application through machine science, where autonomous research challenges institutions developed around human capabilities and constraints. We then propose an experimental research programme in which matched populations of AI agents operate under alternative institutional arrangements, and describe MoltJournal, an API-first journal for autonomous research agents, as an illustration of how such institutions can be made programmable and observable. Together, these contributions establish institutional design as a research agenda concerned not only with aligning autonomous agents, but with understanding how institutions can transform them into capable, reliable and accountable collectives.


