# Abstracts of Papers

## World Model
### AutoDex: An Automated Real-World System for Dexterous Grasping Data Collection
**Authors**: Mingi Choi, Gunhee Kim, Jisoo Kim, Taeksoo Kim, Taeyun Ha, Jongbin Lim, Hanbyul Joo

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23689v1](https://arxiv.org/pdf/2606.23689v1)

**Abstract**: Learning robust dexterous grasping requires real-world data that records the physical outcomes of grasp attempts. Such data is hard to obtain at scale: teleoperation yields valid physical outcomes but is slow and operator-biased, while simulation-based generation is cheap and scalable but cannot certify contact validity. A natural solution is to generate candidate grasps and verify them on real hardware, but this scales only if the entire collection loop (perception, execution, labeling, and reset) runs without human intervention. We present AutoDex, an automated real-world data-collection system that closes this loop: for each candidate from a replaceable generator, it localizes the object under severe hand-object occlusion with dense 20-camera perception, executes collision-monitored robot motions, labels lift-and-hold success or failure, and actively resets the object between trials to expose additional candidates across stable poses. The result is a reusable database of physically labeled grasp trials that downstream systems can query by retrieval and feasibility filtering. Using AutoDex, we collect 3,593 grasp trials across Allegro and Inspire hands on 100 diverse objects, with synchronized multi-view observations and robot-state logs. For a matched 500-trajectory collection, AutoDex requires 10.3 h versus 49.4 h for teleoperation, yielding a 4.8x throughput improvement, and grasps retrieved from the AutoDex-validated database succeed 76% versus 34% for simulation-only validation. Code and data will be publicly released.


### LaST-HD: Learning Latent Physical Reasoning from Scalable Human Data for Robot Manipulation
**Authors**: Jiaming Liu, Yinxi Wang, Chenyang Gu, Siyuan Qian, Xiangju Mi, Hao Chen, Jiawei Chen, Qingpo Wuwu, Xiaoqi Li, Nuowei Han, Yiming Zhang, Xuheng Zhang, Yang Yue, Yeqing Yang, Lei Wang, Peng Jia, Hao Tang, Shanghang Zhang

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23685v1](https://arxiv.org/pdf/2606.23685v1)

**Abstract**: Human-hand demonstrations provide a direct and scalable source of physical interaction data for robot learning. While manual retargeting is indispensable for establishing kinematic action correspondence across different morphologies, robust transfer requires going beyond geometry to address the underlying alignment of physical dynamics between human and robot manipulation. To address this, we introduce LaST-HD, a novel human-to-robot action learning paradigm that extends reasoning-before-acting VLA by aligning human-hand and robot demonstrations in a shared latent reasoning space. Rather than mimicking human kinematics, LaST-HD trains an auxiliary action-conditioned world model on unpaired human-hand and robot trajectories to synthesize unified latent targets. After aligning cross-embodiment representations in this shared forward-dynamics space, these targets supervise LaST-HD's latent reasoning process, enabling it to internalize shared physical dynamics and drive efficient human-hand action learning. Moreover, we develop Out-of-Lab (OOL) Glove, a low-cost motion-capture glove tailored to LaST-HD for human-hand data collection. The captured human data provide precise keypoints and serve as universal action supervision across grippers and dexterous hands. Armed with the aligned latent space and high-fidelity human-hand data, we develop a progressive mixed-to-human training recipe comprising mixed human-robot co-training and human-hand online correction post-training. Through mixed co-training, LaST-HD improves generalization to novel objects, scenes, and positions using only human-hand demonstrations. With online correction, LaST-HD further adapts to novel environments and achieves over 90\% accuracy using only 20 minutes of OOL glove data.


### Semantic Browsing: Controllable Diversity for Image Generation
**Authors**: Sara Dorfman, Maya Vishnevsky, Omer Dahary, Or Patashnik, Daniel Cohen-Or

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23679v1](https://arxiv.org/pdf/2606.23679v1)

**Abstract**: Modern text-to-image models excel in visual fidelity and prompt adherence. However, this strict adherence comes at the cost of diversity: generated samples tend to collapse into a single visual interpretation. Existing methods to improve diversity produce outputs driven by incidental variations rather than meaningful design choices. This motivates a new variant of the diversity task where structure is enforced on the generated samples. We introduce a method for controlled diversity that enables Semantic Browsing, where users can navigate structured image galleries and experience creative exploration through a systematic traversal of meaningful, interpretable axes of variation. Achieving this level of semantic control requires a deep understanding of the scene. We exploit the fact that recent text-to-image models are trained on elaborated captions, effectively decoupling semantic decision-making from pixel generation. This enables a paradigm shift: instead of relying on stochastic variation within the text-to-image model, we induce diversity directly at the text level. By leveraging rich textual representations, we allow a Vision Language Model (VLM) to operate on the full scene context. To overcome the generic outputs typical of standard VLMs, we employ an agentic workflow that explicitly enforces structured variation attuned to the original prompt. We demonstrate that our method produces diverse and navigable design spaces where every variation corresponds to a specific, user-understandable semantic decision.


### AIR: Adaptive Interleaved Reasoning with Code in MLLMs
**Authors**: Cong Han, Xiaohan Lan, Haibo Qiu, Yujie Zhong

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23678v1](https://arxiv.org/pdf/2606.23678v1)

**Abstract**: Following the paradigm shift initiated by OpenAI o3, interleaved reasoning with code to enhance multimodal large language models (MLLMs) has become a pivotal research frontier. The existing literature focuses primarily on tool-use within vision-perception tasks. However, such approaches typically rely on predefined heuristics for visual manipulation and are inherently incapable of addressing numerical computation problems due to their exclusive focus on visual operations. This paper empowers MLLMs with adaptive interleaved reasoning capabilities through extended reinforcement learning training on code-augmented complex numerical computation tasks. To this end, we propose a comprehensive three-component solution consisting of: a two-stage cold-start data construction pipeline, data filtering strategies for RL dataset curation, and an adaptive tool-invocation strategy leveraging a group-constrained reward function for interleaved reasoning trajectories. Extensive experiments demonstrate that after Reinforcement Learning training with the group-constrained reward function, performance improves by an average of 6.1 percentage points (pp) on evaluation benchmarks. Specifically, the accuracy for interleaved reasoning samples increases by 9.9 pp, and the overall success rate of tool-use exceeds 95%. Our data and code are available at: https://github.com/CongHan0808/AIR.git.


### Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?
**Authors**: Dingzhi Yu, Hongyi Tao, Yuanyu Wan, Luo Luo, Lijun Zhang

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23676v1](https://arxiv.org/pdf/2606.23676v1)

**Abstract**: AdamW is the de facto optimizer for training large language models (LLMs), yet the theory behind it still lives mostly in finite-variance regimes. This is increasingly unsatisfying, as empirical evidence indicates that stochastic gradient noise in LLM pretraining is typically heavy-tailed. Recent work shows that sign-based optimizers such as Lion and Muon achieve sharp heavy-tailed rates, and that AdaGrad can also converge under heavy-tailed noise. However, no rigorous convergence theory for AdamW has yet been established in this regime. Can AdamW converge under the same heavy-tailed assumptions, or does its second-moment accumulator create a genuine obstruction? We formulate this as an open problem, prove a positive weighted-metric benchmark, and give a corridor lower-bound mechanism showing how denominator memory can hide large gradients.


### PsyBridge: A Hybrid Intelligent Framework for Multi-Dimensional Mental Health Assessment and Decision Support
**Authors**: Sunil Wanjari, Manish Thakre, Aayushi Asole, Sharwari Raut, Kwabena Adu-Duodu, Yinhao Li, Stanly Wilson

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23673v1](https://arxiv.org/pdf/2606.23673v1)

**Abstract**: Mental health assessment commonly relies on isolated screening instruments or data-driven models that often lack interpretability and multi-dimensional integration. Existing approaches frequently focus on individual indicators such as depression or anxiety while providing limited support for comprehensive and explainable decision-making. To address this limitation, this study proposes PsyBridge, a hybrid intelligent decision-support framework designed for multi-dimensional mental health assessment through the integration of clinically validated screening tools, cognitive evaluation, and personality profiling within a unified architecture. The proposed framework incorporates PHQ-9 and GAD-7 assessments alongside cognitive and behavioural indicators using a modular design and a weighted aggregation mechanism to generate interpretable mental health risk classifications and recommendations. To evaluate the framework, a semi-synthetic dataset consisting of 500 patient profiles representing varying severity levels was constructed based on clinically grounded score distributions. Experimental results demonstrate that PsyBridge achieves an overall accuracy of 0.84, outperforming standalone PHQ-9 and GAD-7 assessments while improving precision, recall, and F1-score. Sensitivity analysis and ablation studies further indicate that integrating cognitive and personality components contributes to more stable classification performance and reduces inconsistencies in moderate-risk prediction. The findings suggest that PsyBridge provides a scalable and interpretable approach for AI-assisted mental health decision support, particularly within digital healthcare and telehealth environments.


## Generation
### On the Limits of Prompt-Conditioned Language Models as General-Purpose Learners
**Authors**: David Mguni, Julian Ma, Jun Wang

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23668v1](https://arxiv.org/pdf/2606.23668v1)

**Abstract**: Large Language Models (LLMs) are frequently portrayed as general-purpose solvers capable of solving arbitrary tasks. We argue that this view overlooks a fundamental constraint: language is a compressed and capacity-limited interface for conveying task information. Modelling User--System interaction as a bilevel \emph{cheap-talk} game, we analyse how latent tasks are encoded into prompts and reinterpreted under alignment and safety constraints. We introduce a conceptual decomposition separating task inference from execution and derive PAC-Bayes bounds that distinguish finite-sample estimation error from irreducible structural limitations. Our first main result establishes an \emph{expressivity floor}: language acts as a capacity-limited communication channel, and whenever the informational complexity of a task family exceeds the capacity of that channel, distinct tasks become unavoidably indistinguishable to the Solver, inducing a strictly positive error floor that cannot be eliminated by additional data, optimisation, or model scaling alone. We then establish an \emph{objective-misalignment floor}: when alignment constraints restrict the admissible output set, the User-ideal distribution may lie outside the feasible class, inducing an irreducible distortion. Together, these results yield a formal negative conclusion: prompt-conditioned LLMs are not universal problem solvers through prompting alone, as there exist task families for which correct behaviour is provably unattainable even in the infinite-data regime. More broadly, our analysis shows the limits of prompt-based generalisation arise from information-constrained communication and alignment-constrained objectives. This suggests that interfaces beyond natural language, including multimodal observations and, external memory, may reduce the inherent LLM limitations by increasing the task-relevant information available to the System.


### Dynamic estimation of slowly varying sequences
**Authors**: Prashant Gokhale, Mikhail Khodak, Sandeep Silwal

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23655v1](https://arxiv.org/pdf/2606.23655v1)

**Abstract**: We consider the problem of sequentially approximating functions of each element in a slowly-varying sequence, i.e. one where the magnitude $α_i$ of the difference between the elements at positions $i$ and $i-1$ is small. Recent work on implicit trace estimation shows that when $α_t$ is small, reusing queries to past sequence elements can reduce the overall cost [Dharangutte \& Musco, NeurIPS~2021; Woodruff et al., NeurIPS~2022]. We introduce a framework generalizing this to a variety of linear and nonlinear functions on diverse vector spaces, obtaining novel sequential estimation results for matrix powers, spectral densities, Monte Carlo integration, and a boundary value problem from partial differential equations~(PDEs). Furthermore, we develop a novel algorithm for use with this framework that locally scales the estimation budget with $α_t$, obtaining sharper path-length-style variation bounds of form $\mathcal O(\sum_{i=1}^mα_i)$ on the cost of estimating a sequence of length $m$. This improves upon the previous implicit trace estimation bound of $\mathcal O(m\cdot\max_iα_i)$ [Dharangutte \& Musco, NeurIPS~2021], which is achieved by fixing the query budget using the worst-case $α_i$ and is thus inefficient for stable sequences with rare bursts. Lastly, while all past work assumes a known bound on $α_i$, we show in certain cases how the changes can be estimated on-the-fly with (nearly) no added cost. In summary, our framework makes the sequential approximation toolkit general-purpose and adaptive while improving upon state-of-the-art-guarantees for dynamic trace estimation.


### TailorMind: Towards Preference-Aligned Multimodal Content Generation
**Authors**: Hengji Zhou, Ye Liu, Yufeng Liu, Si Wu, Lianghao Xia, Liqiang Nie

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23643v1](https://arxiv.org/pdf/2606.23643v1)

**Abstract**: Personalized content systems depend on available UGC and struggle when suitable content is absent, delayed, or costly to create. Although multimodal generators can synthesize content on demand, how to translate behavioral traces into generation-ready preferences remains underexplored. We study personalized multimodal content generation: creating user-tailored multimodal content without existing item pools or waiting for matching UGC. We propose TailorMind, linking collaborative preference modeling with controllable multimodal generation. TailorMind enriches sparse user histories via hypergraph collaborative filtering and optimizes textual profiles with ranking-error feedback and textual gradient descent. Retrieval-augmented style control grounds outputs in authentic UGC patterns, while cross-modal cohesion reflection reduces semantic drift. We construct TailorBench, a benchmark from three mainstream platforms evaluated along five dimensions: coherence, novelty, aesthetic, hallucination, profiling. Experiments show that TailorMind achieves competitive or stronger coherence, improves novelty and aesthetic quality over representative generation baselines and ground-truth UGC, demonstrating advantages over retrieving available content or comparable UGC, while achieving up to 29% Recall gains in reranking. Our code is released at: https://github.com/iLearn-Lab/TailorMind.


### AI-driven Optimisation of Quality of Recovery (QoR) in Remote Patient Monitoring
**Authors**: Yansong Liu,  Li-Hsi,  Lin, Pramit Khetrapal, Ronnie Stafford, John Kelly, Ivana Drobnjak

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23631v1](https://arxiv.org/pdf/2606.23631v1)

**Abstract**: Remote patient monitoring depends on patient-reported data to capture the subjective dimension of recovery that devices cannot measure. The Quality of Recovery (QoR-15) survey is the gold-standard instrument for this purpose. It was designed and validated for occasional in-hospital assessment, yet remote monitoring now administers it to patients daily. In our own post-surgical deployment, only 55% of patients submitted the survey more than 14 days of 30 monitoring days. We developed QoR-compact, a five-item daily input for the RPM prediction pathway. Setting a deployment-driven target of one-third of the daily items, we exhaustively evaluated all 3,003 five-question subsets of the QoR-15 and tested whether the best of them matches the full instrument in predicting near-term postoperative recovery severity. QoR-compact achieves a mean AUC-ROC of 0.968 (95% CI 0.915-0.988), statistically comparable to the 0.964 baseline obtained with one-third of the items. Patient-level backtesting indicates that it tracks readmission events as faithfully as the full form. Its five items span the physical and psychological axes of recovery: Q3 (feeling rested), Q9 (feeling comfortable and in control), Q10 (general well-being), Q12 (severe pain), and Q14 (feeling worried or anxious). The QoR-15 remains the gold-standard measure of recovery; QoR-compact complements it as a shorter daily input designed for prediction. This parity provides the basis for a prospective study of whether a lighter daily input is, in turn, completed more consistently. External validation on larger cohorts is required before clinical use.


### Diffusion Models Adapt to Low-Dimensional Structure Under Flexible Coefficient Choices
**Authors**: Changxiao Cai, Yuchen Jiao, Gen Li

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23627v1](https://arxiv.org/pdf/2606.23627v1)

**Abstract**: Diffusion models are known to exploit unknown low-dimensional structure to accelerate sampling. However, existing convergence theory under low-dimensional data structure has largely focused on update rules with narrowly prescribed coefficient choices. This raises a fundamental question: is adaptation to low-dimensional structure sensitive to the precise choice of update coefficients? In this paper, we show that such adaptation is a robust property of diffusion models. For a broad class of update coefficients, we prove that $\widetilde{O}(k/\varepsilon)$ iterations suffice to generate an $\varepsilon$-accurate sample in total variation (TV) distance, independently of the ambient dimension. Our framework substantially broadens the class of diffusion samplers known to enjoy low dimensional adaptation and applies to several commonly used methods in practice. These results provide a theoretical justification for the empirical effectiveness of diffusion samplers across different coefficient choices when applied to structured, high-dimensional data.


### DiT-Reward: Generative Representations for Text-to-Image Reward Modeling
**Authors**: Yuanming Yang, Guoqing Ma, Bo Wang, Yuan Zhang, Wei Tang, Chenyi Li, Haoyang Huang, Nan Duan

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23626v1](https://arxiv.org/pdf/2606.23626v1)

**Abstract**: Can representations learned for image generation also support the evaluation of generated images? We study text-to-image reward prediction as a downstream task of generative representation learning. To this end, we introduce DiT-Reward, which converts a pretrained text-to-image Diffusion Transformer into a reward model by processing near-clean image latents and aggregating text-conditioned image representations across transformer layers. Under the same training data mixture as HPSv3, DiT-Reward outperforms HPSv3 on all four evaluated preference benchmarks, reaching 85.6% on HPDv2 and 77.6% on HPDv3. When the generative backbone is frozen, a lightweight learned head can still extract meaningful preference predictions from its representations. Probing across depth further reveals that downstream reward performance is strongest in the middle-to-late layers and benefits from combining representations across different stages. We also observe consistent positive scaling with generative backbone capacity. Finally, when used to optimize Stable Diffusion 3.5 Large with Flow-GRPO, DiT-Reward outperforms HPSv3 along the matched training trajectory, with particularly clear gains in realism. Direct latent scoring also achieves a 1.65x inference speedup over HPSv3 with comparable peak memory. These results show that pretrained generative DiTs provide transferable representations for reward modeling and policy optimization.


## VLA
### RECALL: Recovery Experience Collection for Active Lifelong Learning in Vision-Language-Action Models
**Authors**: Ulas Berk Karli, Tesca Fitzgerald

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23617v1](https://arxiv.org/pdf/2606.23617v1)

**Abstract**: Vision-Language-Action (VLA) models are commonly fine-tuned through passive imitation learning, where additional demonstrations are collected for tasks where the policy performs poorly. This approach incurs several downsides: it requires the robot to fail before data collection is triggered, provides little guidance about which states require supervision, and wastes demonstrator effort on redundant parts of the task where the policy already performs well. In this paper, we propose an active, continual learning paradigm for VLAs. We demonstrate that active, uncertainty-guided data collection leads to more efficient fine-tuning than when using passively-collected demonstrations. However, we also find that fine-tuning only on actively-collected recovery data leads to catastrophic forgetting. We evaluate techniques for continual learning, including replay-based data mixing and elastic weight consolidation, and identify tradeoffs between plasticity to uncertainty-guided recovery data and retention of previously learned behaviors. Overall, our work contributes an empirical study of active continual learning for autoregressive VLAs, establishing that uncertainty-guided recovery demonstrations can improve adaptation efficiency while also revealing open challenges when targeted new data is incorporated into large robot policies.


### Attacking the Trusted Imagination: Oracle-Level Integrity Attacks on Imagine-then-Act World Models
**Authors**: Linghan Chen, Kaiyan Ji, Minyu Guo

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.22966v1](https://arxiv.org/pdf/2606.22966v1)

**Abstract**: Many recent vision-language-action (VLA) policies adopt an imagine-then-act design. A world-action model (WAM) first imagines a short future as a latent trajectory z~, on which the action is then conditioned. We identify this trusted imagination, rather than the reactive policy, as the exposed attack surface. A downstream oracle, such as a safety gate, a visual model-predictive-control (MPC) planner, or an imagine-then-check verifier, consumes z~ as a prediction of the future. The robustness of the policy therefore does not entail the robustness of systems that rely on the WAM. The underlying phenomenon is an asymmetry. Corrupting the imagination is easy, since it requires only displacing z~ from its natural-future manifold. Steering it precisely is hard, since it must reach a specified on-manifold target. We adopt a capability-based threat model with an L-infinity-bounded observation perturbation. The attacker applies projected gradient descent through the fully differentiable observation-to-imagination map. The same off-manifold property motivates a parameter-free denoiser detector. We evaluate three targets: RynnVLA-002, LingBot-VA, and LaDi-WM. Untargeted corruption is roughly 60x stronger than random and is detected at AUC 1.0. Targeted control remains bounded. An adaptive attacker evades detection only by forgoing corruption. The reactive policy remains robust to corrupted imagination. A native imagination-driven MPC, however, exhibits the first adversary-specific task failure (at epsilon=0.01, success 0.70 versus 0.05; Fisher p < 10^-4).


### Intend, Reflect, Refine: An Adaptive Multimodal Reflection Framework for Autonomous Driving
**Authors**: Zisheng Chen, Yuping Qiu, Jianhua Han, Tao Tang, Xiuwei Chen, Likui Zhang, Ying-Cong Chen, Hang Xu, Xiaodan Liang

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.22913v1](https://arxiv.org/pdf/2606.22913v1)

**Abstract**: Recent Vision-Language-Action (VLA) models have advanced end-to-end autonomous driving by incorporating reasoning for better interpretability and planning quality. However, most existing approaches directly generate the final trajectory without explicitly examining its future consequences, which limits their reliability in complex and dynamic environments. To address this limitation, we propose IRR-Drive (Intend, Reflect, Refine), an adaptive multimodal reflection framework for autonomous driving. Specifically, to tightly couple high-level reasoning with physical constraints, IRR-Drive first generates a preliminary textual intention and anticipates potential interactions by predicting future semantic bird's-eye view (BEV) representations. This dual-modality (Text + BEV) reflection space explicitly models anticipated scene evolution, enabling the model to rigorously self-correct and refine its initial intent before generating the final trajectory. Furthermore, to balance planning performance and computational efficiency, we construct reflection-oriented training data and design an adaptive reflection reward, enabling the model to adaptively select its reasoning mode according to scene complexity. Instead of using reasoning primarily as an auxiliary interpretation, IRR-Drive directly integrates an adaptive reflection mechanism into the planning framework, enabling grounded, decision-aware trajectory correction that is driven by scene complexity. Our method achieves state-of-the-art performance on the NAVSIM benchmark in both PDMS and EPDMS. Extensive experiments demonstrate the effectiveness of our multimodal reflection framework and validate the efficacy of the proposed adaptive reflection strategy.


### Reference-Free Assessment of Physical Consistency in World Model-based Video Generation
**Authors**: Yun Oh, Sukmin Yun

**Published Date**: 2026-06-21

**Updated Date**: 2026-06-21

**PDF Url**: [2606.22363v1](https://arxiv.org/pdf/2606.22363v1)

**Abstract**: We introduce reference-free measures for evaluating the physical consistency of generated videos, combining relative and absolute approaches to assess fidelity. Although tools like WorldGym or WorldEval enable robotic simulation via video generation, physical fidelity gaps often prevent these environments from accurately reproducing real-world task success rates of VLA models. Unlike existing evaluation methods, which require costly human voting (Elo) or unavailable ground-truth references (FVD), our approach utilizes DROID-SLAM and SEA-RAFT to quantify physical inconsistencies, motivated by WorldScore. Videos filtered using our relative consistency assessment show an improvement in task success rates of over 8%, effectively narrowing the simulation-to-reality gap. Furthermore, our absolute assessment enables spatio-temporal localization, providing visualization of when and where physical artifacts occur.


### Benchmarking Robot Memory Under Interference
**Authors**: Soumil Rathi

**Published Date**: 2026-06-21

**Updated Date**: 2026-06-21

**PDF Url**: [2606.22338v1](https://arxiv.org/pdf/2606.22338v1)

**Abstract**: Robots deployed in realistic settings will accumulate experience across many sessions and tasks over their deployment. The robot's tasks may often require it to remember information from multiple sessions ago, making long-context robot memory important for real-world deployments. However, most robot-memory benchmarks today are based on single episodes or a short context. To measure how current robot memory systems perform on longer sessions with more distractions, we introduce RoboMME-Interference, a cross-session benchmark built on RoboMME. For each query episode, we construct a session history using the query's relevant prior demonstration followed by a controlled number of unrelated sessions, which we provide to the VLA as memory and measure accuracy. Running RoboMME's released memory-augmented $π_{0.5}$ variants unmodified through this benchmark, we find that while perceptual memory variants improve success when given the history without any distractors, they decay strongly and steadily as unrelated sessions accumulate. With this release, we emphasize the importance of long-context memory and robustness to interference and show that current systems largely fail on such capabilities. The project page, videos, code, and data are at https://robotmemorybench.com.


### Decoupling the Declarative from the Procedural in Vision-Language-Action Models
**Authors**: Nikolaos Tsagkas, Andreas Sochopoulos, Chris Xiaoxuan Lu, Oisin Mac Aodha, Alexandros Kouris

**Published Date**: 2026-06-19

**Updated Date**: 2026-06-19

**PDF Url**: [2606.21496v1](https://arxiv.org/pdf/2606.21496v1)

**Abstract**: Deploying generalist robotic agents in the real world requires transferable skills. Specifically, a policy trained to clone a behavior from object-specific demonstrations must generalize beyond that object, otherwise data collection requirements become intractable. Recently, fine-tuning of pre-trained billion-parameter Vision-Language Models (VLMs), initially on large-scale robot datasets and then on fewer scenario-specific demonstrations, has emerged as the predominant paradigm for designing Vision-Language-Action (VLA) models. While these policies achieve state-of-the-art manipulation performance in-distribution, they remain brittle to minor spatial, semantic, and task variations. In this work, we address the inability of current models to decouple the declarative (i.e., concepts and entity semantics) from the procedural knowledge (i.e., how to do something) encoded in their parameters, which is a fundamental bottleneck for zero-shot skill transfer to novel objects. To address this, we propose w$^{2}$VLA, a new VLA model with restructured information flow. Rather than feeding all multimodal tokens from the VLM encoder into a large, opaque transformer-based action expert, our approach modulates the robot state sequence with visual, spatial, and skill information in a compositional and interpretable manner. Unlike popular, state-of-the-art VLAs, we show that our modular approach successfully decouples knowledge representations, enabling robust behavior cloning and unprecedented zero-shot skill transfer capabilities across dissimilar, unseen objects.


## Agent
### MAS-PromptBench: When Does Prompt Optimization Improve Multi-Agent LLM Systems?
**Authors**: Juyang Bai, Laixi Shi

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23664v1](https://arxiv.org/pdf/2606.23664v1)

**Abstract**: Multi-agent systems (MAS) offer a scalable path forward for agentic AI, comprising multiple LLM-based agents, each assigned a system prompt and a position within a workflow that governs inter-agent coordination and output aggregation. System prompts thus form a critical and accessible optimization surface: they specify agents' roles and behaviors, enabling system-level improvements without model finetuning. Although prompt optimization has shown substantial potential for single LLMs, extending it to MAS poses distinct challenges, notably an exponentially growing search space. It remains unclear whether, when, and by how much prompt optimization improves MAS performance, and how sensitive such gains are to system configuration. In this work, we systematically study system-prompt optimization across a broad range of MAS setups varying in task, workflow, communication protocol, and team size, benchmarking two prompt optimizers that naturally extend state-of-the-art single-agent methods. The results reveal its potential to unlock significant gains while exposing open challenges, characterizing when and how much prompt optimization helps across diverse MAS settings.


### Causal Discovery in the Era of Agents
**Authors**: Yujia Zheng, Vishal Verma, Mantej Gill, Haoyue Dai, Peter Spirtes, Kun Zhang

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23608v1](https://arxiv.org/pdf/2606.23608v1)

**Abstract**: Recent attempts to combine large language models (LLMs) with causal discovery ask models to infer pairwise directions, propose graph structures, or inject language-model outputs as priors and constraints. These approaches promise faster analysis, but they also obscure whether a causal evidence is supported by data and assumptions or by textual associations, prompt artifacts and hallucinated mechanisms. We argue for a different role for agents in causal discovery. Agents should inspect data, retrieve context, explain method assumptions and clarify graph outputs, but they should not supply edges, orientations, priors, constraints or causal conclusions. We propose the principle that agents assist the workflow, while causal claims remain grounded in data, explicit assumptions, formal algorithms, diagnostics and user or domain-expert decisions. We instantiate this principle in causal-learn+, an online platform that coordinates data analysis, preprocessing, method recommendation, expert-knowledge incorporation, formal discovery and interpretation around the algorithmic ecosystem of causal-learn. A case study on Big Five personality data illustrates agent-assisted pipeline of causal discovery without turning language-model unreliability into causal evidence. The platform is available at causallearn.com.


### Decentralized Autonomous Traffic Management through Corridor Networks
**Authors**: Jasmine Jerry Aloor, Aadarsh Govada, Hamsa Balakrishnan

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23585v1](https://arxiv.org/pdf/2606.23585v1)

**Abstract**: As autonomous aircraft are introduced at scale and traffic density increases, centralized management becomes insufficient to coordinate the large numbers of crewed and uncrewed aircraft. Dedicated Advanced Air Mobility (AAM) corridors have therefore been proposed for organizing high-density autonomous traffic flows. The desire to scalably provide autonomous aircraft flexibility in trajectory planning motivates the development of decentralized approaches to traffic management in AAM corridors.
  In this work, we extend a multi-agent reinforcement learning (MARL) approach to address the challenge of decentralized traffic flow management in air corridor networks. We test policies trained in a single-corridor setting on increasingly complex multi-corridor networks with combinations of merges and splits in a zero-shot manner. Experimental results demonstrate that learned behaviors transfer well to scenarios with varying traffic density, network geometry, and heterogeneous vehicle performance, without needing centralized coordination or model retraining. We evaluate system-level performance in terms of conformance to corridor boundaries, completion rates, average speeds, distance traveled, and maintenance of inter-aircraft separation. We find that although our policies require only locally coordinated entry, traversal, and exit behaviors, they collectively produce desirable traffic flows through the corridor network.


### Kamera: Unified Position-Invariant Multimodal KV Cache for Training-Free Reuse
**Authors**: Bole Ma, Jan Eitzinger, Harald Koestler, Gerhard Wellein

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23581v1](https://arxiv.org/pdf/2606.23581v1)

**Abstract**: Multimodal agents repeatedly re-examine the same video frames, UI screenshots, and rendered artifacts as their context window slides and reasoning iterates, yet every look-back re-encodes from scratch, because prefix caches serve reuse only at a fixed leading position. We show this recompute is avoidable, and identify exactly what naive KV reuse loses: the cross-chunk conditioning a chunk absorbs from its neighbours. This loss is asymmetric. The direct readout of a cached chunk is recovered exactly and for free by the standard state-merge. What remains is a diffuse, low-rank residue concentrated in deep layers, invisible to single-hop retrieval but precisely what multi-hop reasoning binds on. Blind reuse therefore leaves single-hop recall intact while halving multi-hop accuracy; this is the failure mode prior position-independent caches, designed for single-context or single-image reuse, do not address. We repair it with a small, training-free low-rank conditioning patch stored alongside each position-free chunk. Reuse reduces to one operator across MLA, GQA, and MHA: exact RoPE re-rotation to any target position, plus the patch that restores cross-chunk binding. This makes three window operations cheap: reorder (one patch serves every ordering of a cached set), sliding-window survival (surviving chunks relocate via rotation only, zero re-encode), and recall (an evicted chunk is rehydrated by its patch, never re-encoded). A rank-m patch recovers full task accuracy on cross-chunk-binding benchmarks, MM-NIAH across two attention families and two-page doc-QA, at a fraction of the KV footprint, and reconstructs re-prefill KV to within bf16 rounding in a production SGLang kernel across six backbones. The conditioning signal is strongest in redundant vision and video streams, making our solution most impactful where multimodal agents spend their recompute budget.


### VeriEvol: Scaling Multimodal Mathematical Reasoning via Verifiable Evol-Instruct
**Authors**: Haoling Li, Kai Zheng, Jie Wu, Can Xu, Qingfeng Sun, Han Hu, Yujiu Yang

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23543v1](https://arxiv.org/pdf/2606.23543v1)

**Abstract**: Scaling reinforcement learning for visual mathematical reasoning requires more than generating harder questions: as data volume grows, the reward labels themselves must remain reliable. Yet existing data pipelines scale supervision while trusting the labeller, and policy-side methods assume the underlying answers are already correct. We instead treat scaling as a verifiable data-construction problem and decouple two axes before any policy update: prompt difficulty, expanded by route-specific evolution operators, and answer reliability, enforced by offline hypothesis-test falsification. We instantiate this as VeriEvol, an iterative framework with two extensible components: a type-aware evolution module that rewrites low-difficulty image-question seeds into harder, image-grounded prompts; and HTV-Agent, a verifier that accepts an answer only after multi-source counter-evidence has failed to refute it. The resulting verified data scales in volume, extends by adding evolution routes or verifier channels, and plugs directly into existing GRPO-style RL recipes. On a five-benchmark visual-math suite, scaling evolved SFT data from 10K to 250K samples raises the mean accuracy from 35.42 to 54.73; then, with backbone, SFT initialization, and GRPO recipe held fixed, VeriEvol adds a cumulative +3.88 over an un-evolved RL baseline, of which +1.82 comes from evolved prompts and +2.06 from the HTV-Agent verifier. We release the prompts, data, models, code, and the full verifier trace of every sample, so that downstream work can scale and audit the pipeline rather than only inspect its outputs.


### Concordia: JIT-Compiled Persistent-Kernel Checkpointing for Fault-Tolerant LLM Inference
**Authors**: Yuhang Gan, Yiwei Yang, Yuyi Li, Xiangyu Gao, Yichen Wang, Rain Jiang, Xiaoning Ding, Andi Quinn, Chen Qian

**Published Date**: 2026-06-22

**Updated Date**: 2026-06-22

**PDF Url**: [2606.23521v1](https://arxiv.org/pdf/2606.23521v1)

**Abstract**: Long-running LLM agents keep valuable state resident on GPUs: KV caches, request schedulers, communication state, and sometimes online adapters. Losing this state after a GPU or communicator failure can discard minutes to hours of work, yet existing recovery mechanisms either restart the whole serving stack or require application-specific checkpoint logic inside every attention and runtime component. This paper argues that fault tolerance for such workloads needs a GPU-resident execution context: checkpoint hooks must run at device synchronization points, observe binary kernels that frameworks and libraries actually execute, and recover without putting the host CPU on the critical path.
  We present Concordia, a runtime that uses a device-resident persistent kernel as the substrate for fault-tolerant LLM inference. Concordia interposes on GPU module loading and supports PTX- and SASS-level instrumentation, allowing checkpoint and pause hooks to be inserted below framework code and library boundaries. For each registered LLM state region, Concordia JIT-compiles a specialized delta-checkpoint handler -- for example, a KV-block scanner, adapter-page scanner, or recovery applier -- and hot-swaps it into the persistent kernel's operator table. The persistent kernel consumes a lock-free ring buffer of compute, checkpoint, append-log, and recovery tasks, so the same always-on executor triggers dirty-page detection, stages deltas, and appends committed records to a CPU-visible log in CXL memory or host DRAM.


