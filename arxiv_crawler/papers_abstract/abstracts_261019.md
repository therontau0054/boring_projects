# Abstracts of Papers

## World Model
### Rethinking the design space of Vanilla Pixel Diffusion Transformers
**Authors**: Soumik Mukhopadhyay, Long Mai, Abhinav Shrivastava, Aniruddha Mahapatra

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23854v1](https://arxiv.org/pdf/2610.23854v1)

**Abstract**: Pixel-space diffusion models have recently re-emerged as a compelling alternative to latent diffusion, avoiding the lossy latent bottleneck and separately trained autoencoder. JiT shows that a vanilla diffusion transformer can generate directly in pixel space by replacing the commonly used velocity prediction ($\boldsymbol{u}$-prediction) with clean image prediction ($\boldsymbol{x_0}$-prediction). In this work, we revisit this choice and introduce MFlow, an adaptive parameterization that learns to interpolate between $\boldsymbol{x_0}$- and $\boldsymbol{u}$-prediction across principal directions of the data, learned end-to-end with diffusion training. We find that the preferred parameterization varies systematically with the data representation and model capacity -- notably, increasing model capacity shifts preference toward velocity prediction. We evaluate MFlow across ImageNet, UCF-101 video, and large-scale text-to-image generation, demonstrating competitive or improved generative performance across diverse settings. In addition, we find that vanilla pixel diffusion transformers, irrespective of parameterization, retain a persistent high-frequency deficit relative to real images. To address this, we introduce ConvRefiner, a lightweight convolutional module trained post-hoc with an adversarial loss while keeping the diffusion backbone frozen. With only a small amount of additional training, ConvRefiner restores the high-frequency statistics of generated images while preserving FID. Project webpage: https://soumik-kanad.github.io/mflow-diffusion/.


### Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts
**Authors**: Antonia Bronars, Younghyo Park, Kushal Kedia, Pulkit Agrawal

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23849v1](https://arxiv.org/pdf/2610.23849v1)

**Abstract**: Every robot already carries high-resolution contact sensors: its own joints. Legged robots and humanoids exploit them to walk, run, and track whole-body motions without vision, but there the contacts are large and forceful. Is joint sensing also enough for precise, contact-rich assembly, where the robot must find a millimeter-scale opening, mesh gear teeth, or catch a thread through light contact? We study this question by training blind assembly policies that observe only a short history of joint positions, velocities, and their own actions, without visual, force, torque, or tactile sensing. The poses of both the fixture and the part are unknown to the policy, and the grasp is randomized substantially. The policy must therefore assemble the parts through contact, sensed exclusively through its own proprioception. Trained with reinforcement learning entirely in simulation over randomized parts, grasps, and contacts, such policies learn peg insertion, gear meshing, and nut threading. The peg insertion policy transfers zero-shot to the real world and inserts pegs of different shapes and sizes in 73% of trials. Controlled comparisons with matched visual policies in simulation show that blind policies generalize far better to unseen part shapes and sizes, though they can be slower. Training such policies needs thousands of different assemblies, each simulated with its clearance intact, so we also release an open-source generator that builds them procedurally from exact convex pieces for MuJoCo; it is more accurate and faster than convex decomposition or MuJoCo's signed-distance collision. Videos and interactive simulations are at https://younghyopark.me/blind-proprioceptive-assembly/.


### Behavioral Couplings: From Formation to Behavioral Emergence in Language Models
**Authors**: Dongyoon Hahm, Woogyeol Jin, Dennis Wei, Yi Zhou, Nathalie Baracaldo, Kimin Lee

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23847v1](https://arxiv.org/pdf/2610.23847v1)

**Abstract**: Fine-tuning large language models (LLMs) can induce behaviors beyond those explicitly targeted. For example, training a model to respond more warmly can make it more sycophantic, and training it to write insecure code can cause broad misalignment on prompts unrelated to coding. We refer to a relationship between behaviors, in which fine-tuning on one brings out another, as a behavioral coupling. In this work, we study formation and properties of behavioral couplings. We find that when a model is trained on documents describing two distinct behaviors together, fine-tuning it to elicit one behavior causes the other to emerge as well. For instance, when training documents describe a fictitious character that both explains scientific concepts in a playful, rubber-duck-like manner and discourages human friendships, a model subsequently fine-tuned to explain science like a rubber duck also begins encouraging users to end their friendships, whereas a model that was not trained on these documents shows no such behavior after the same fine-tuning. These results show that behavioral couplings can be formed through document training and later surface as unintended behaviors. More concerningly, we find that couplings can compose. When two document sets share a behavior (document A pairs behaviors 1 and 2, and document B pairs behaviors 2 and 3), fine-tuning on behavior 1 elicits both behaviors 2 and 3. This can make it difficult to trace where an emergent misbehavior originated, since the coupled behaviors may never appear together in any single document. These findings suggest that preventing the unintended effects of later fine-tuning may require evaluation that goes beyond a model's current behavior.


### StopWatch: Goal Grounding for Object-goal Navigation
**Authors**: Xinhao Liu, Yunsheng Tian, Yuheng Qiu, Pieter Abbeel, Xi Chen, Guanya Shi, Chen Feng

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23841v1](https://arxiv.org/pdf/2610.23841v1)

**Abstract**: Pretrained VLMs bring rich world knowledge and semantic priors to object-goal navigation, and fine-tuning a VLM into a navigation policy has become a common recipe. Despite this progress, success rates remain low, and it is unclear which capability these fine-tuned policies lack. Our diagnosis identifies goal grounding as the dominant failure. These policies explore well, yet often fail to notice that the goal is already in view or to estimate how far away it is. To address this failure, we ground the goal explicitly. Explicit grounding substantially improves success and reaches state-of-the-art results on six benchmarks across three scene collections. We also correct annotation defects in these benchmarks, so that future methods are evaluated more faithfully. Our analysis on the clean benchmarks shows that, with ground-truth grounding, our policy nearly matches the expert that generated its demonstrations, leaving the headroom in perception rather than policy learning. Our work points to goal grounding as a missing piece of object-goal navigation and offers a simple and effective solution to the task.


### Waiting Buys Exactly Two Moments: Endogenous Identification in Prediction-Driven Allocation
**Authors**: Rama AlHamidi, Rasul Khanbayov, Erchin Serpedin, Hasan Kurban

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23830v1](https://arxiv.org/pdf/2610.23830v1)

**Abstract**: A planner with a fixed budget of preventive help must decide whom to help and when. Waiting reveals risk but removes intervention opportunities as higher-risk individuals leave first. We characterize this tradeoff under repeated noisy signals and risk-dependent attrition: in the canonical model, a length-$τ$ observation prefix identifies exactly the latent risk moments $m_j=\mathbb E[p^j]$ for $j=0,\ldots,2τ-1$, buying two new moments per additional period. These identify average next-period attrition among survivors but need not identify allocation welfare or attrition among those prioritized for treatment. Our observationally equivalent constructions establish unavoidable timing regret at any sample size for a fixed observation length, while exact certificates determine whether all compatible populations share a unique optimal date. Matched experiments separate the effects of estimation, bootstrap averaging, and regret weighting. Longer observation often resolves timing ambiguity, but the optimal date may already have passed. In our experiments, bootstrap averaging and early stopping improve decisions, while regret weighting adds no improvement in pooled mean squared regret: better statistical fit need not yield better allocation welfare. The code and artifacts are available at https://github.com/KurbanIntelligenceLab/waiting-buys-two-moments.


### Quality-of-Transmission Estimation in Quantum Networks: Compute, Simulate, or Learn?
**Authors**: Anis Bekri, Amar Abane, Van Sy Mai, Abdella Battou, Saddek Bensalem

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23827v1](https://arxiv.org/pdf/2610.23827v1)

**Abstract**: Future quantum networks will rely on control-plane decisions such as routing, scheduling, entanglement provisioning, purification, and memory allocation. Each decision depends on a timely and reliable estimate of the quality of the entanglement that a candidate path can deliver, with end-to-end fidelity as a central metric. Inspired by the optical-networking experience with quality-of-transmission (QoT) estimation, this article asks when a quantum controller should compute fidelity analytically, simulate it, or learn a surrogate model. The optical analogy is useful but incomplete: optical QoT estimation often predicts a scalar transmission margin, whereas quantum QoT estimation must account for probabilistic entanglement generation, random memory waiting times, decoherence, state consumption, and measurement constraints that can make fidelity a stochastic target. We propose a compute/simulate/learn framework for quantum QoT estimation and illustrate it with a simulation-based proof of concept. Our study shows that analytical composition can be sufficient in simple regimes, that simulation becomes necessary when stochastic memory effects shape the delivered fidelity distribution, and that lightweight learned surrogates can approximate simulator labels at much lower runtime cost for online control. We close with open challenges for deployment, including stochastic targets, sim-to-real transfer, data-generation cost, physics-informed learning, and generalization beyond individual paths to full network topologies.


## Generation
### ENFR: Evidence Networks with Flow-Matched References for Amortized Simulation-Based Model Inference
**Authors**: Kai Lehman, Jameson Dong, Carolina Cuesta-Lazaro, Niall Jeffrey, Benjamin D. Wandelt, Francisco Villaescusa-Navarro, Sven Krippendorf, Jochen Weller

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23825v1](https://arxiv.org/pdf/2610.23825v1)

**Abstract**: The evidence, $\mathcal{Z} = p(x | \mathcal{M})$, of a data-generating model $\mathcal{M}$ is a powerful tool in Bayesian frameworks: it enables model inference, model misspecification tests, and goodness-of-fit assessment as an alternative to standard discrepancy statistics, e.g. $χ^2$. While versatile, the evidence is notoriously difficult to compute, even when the likelihood is available. In both likelihood-based and simulation-based inference, estimating $\mathcal{Z}$ provides an immediate solution to high-dimensional goodness-of-fit or model misspecification tests: using $\mathcal{Z}(x)$ as the test statistic induces a minimum-volume level-$α$ test. Such tests are essential to assess model fidelity, which is necessary to trust simulation-based parameter inference. Existing learned approaches largely target Bayes factors, which only measure evidence ratios. Instead, we provide accurate, fast, and amortized estimates of the absolute evidence. We present ENFR: Evidence Networks with Flow-matched References. Building on the Evidence Network framework of Jeffrey & Wandelt (2024), the proposed method first learns Bayes factors with respect to a flow-matched reference, from which the absolute evidence is recovered. We show improvement in estimation of $\mathcal{Z}$ over the flow-based baseline in all applications considered and the best performance of all density estimation methods considered in our benchmarks. We furthermore introduce and provide the proof for an architecture that jointly learns the individual evidences of a set of models $\{\mathcal{M}_i\}$. We demonstrate the performance and scaling behavior of these approaches on data from a variety of scientific applications.


### Learning without relearning physical symmetry: an SO(3)-equivariant convolutional network (CNN) on the sphere
**Authors**: Joshua Williamson, Niall Jeffrey, Lorne Whiteway

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23821v1](https://arxiv.org/pdf/2610.23821v1)

**Abstract**: Many of the most important datasets in the physical sciences live natively on the sphere, and these data often carry no preferred position or orientation. Using methods that do not reflect this symmetry leads to far higher simulation requirements, which can be catastrophic for scientific analyses (forcing reliance on cheap, imperfect models that bias results). We present a novel spherical implementation of a gauge equivariant mesh architecture that is specifically designed for the Hierarchical Equal Area isoLatitude Pixelization (\healpix{}) of the sphere. The $\mathrm{SO}(3)$-equivariant convolution is built from steerable filters, parallel transport and spin-weighted features. The architecture supplies the exact symmetry, so the network does not spend training data learning it. The convolution operations are constructed to give provably exact equivariance, given a band-limit. Our full CNNs can achieve SO(3)-invariance error at per-cent-level and lower, which is controlled through well-understood hyperparameters. On benchmarks, our technique gives the most accurate dense gradient regression and competitive cosmic microwave background foreground removal and denoising. The improved simulation efficiency matters most in simulation-based inference (SBI), where high-fidelity simulations are expensive and neural compressors require large training sets, so a fixed budget forces analyses with less accurate simulators. In cosmology lensing SBI, our technique yields the tightest posteriors at matched simulation count. This approach is a novel method that will enable new convolutional neural network analyses, including generative and inference tasks, for processes and data on the sphere.


### CocoRNA: Collective RNA Design with Cooperative Multi-agent Reinforcement Learning
**Authors**: Tianmeng Hu, Biao Luo, Ke Li

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23820v1](https://arxiv.org/pdf/2610.23820v1)

**Abstract**: Designing RNA sequences that reliably fold into specific secondary structures is essential for understanding their biological functions but remains a challenging computational problem. We propose CocoRNA, a cooperative multi-agent reinforcement learning framework for RNA inverse design. CocoRNA simplifies the design task by decomposing it into smaller sub-problems, each solved collaboratively by multiple agents. This approach reduces the complexity of the problem and improves the exploration of design policies. During training, a centralized critic uses global structural information to guide the agents, enabling them to jointly optimize their design strategies. As a result, CocoRNA learns high-quality RNA design policies that generalize effectively to unseen structures without additional training. Experiments on the Rfam dataset demonstrate that CocoRNA substantially outperforms state-of-the-art methods in both success rate and design speed. Further experiments on other biological sequence design tasks highlight the effectiveness and broad potential of CocoRNA for complex design tasks.


### Logic-Guided Graph Denoising Diffusion Models
**Authors**: Samuel Cognolato, Luciano Serafini, Alessandro Sperduti, Andrea Cavallaro

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23766v1](https://arxiv.org/pdf/2610.23766v1)

**Abstract**: Graph diffusion models are competitive approaches for generating complex graph-structured data. However, when such distributions have strict structural constraints, diffusion models may fail to capture them exactly, resulting in the generation of invalid graphs. In this paper, we propose a method for grounding graph diffusion models in domain-specific knowledge via First Order Logic (FOL), leveraging its expressive and interpretable formalism to impose structural constraints on the generative process. We incorporate domain knowledge using classifier guidance, a technique that conditions the diffusion model's distribution on external variables to exert control over the sampled data. During the generative process, classifier guidance steers the denoising trajectory to optimize an objective function, which we define as a fuzzy and differentiable relaxation of the logical rules. Our methodology requires only the specification of constraints in FOL, whose satisfaction is encouraged at inference time to guide a pre-trained generative model. We evaluate our approach by comparing the unconditional generation of knowledge graphs with our logic-guided framework, which incorporates domain ontologies as structural constraints during inference. This approach significantly increases the proportion of generated graphs that satisfy the ontological constraints.


### From Flow-Box Invariants to Global Conservation Laws: Machine Learning-Assisted Detection of Singularities and Near-Integrability
**Authors**: Jimmie Adriazola, Ioannis G. Kevrekidis, Panayotis G. Kevrekidis, Wei Zhu

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23760v1](https://arxiv.org/pdf/2610.23760v1)

**Abstract**: Conservation laws reveal invariant structure in dynamical systems and constrain their evolution to lower-dimensional level sets. Locally, however, per the flow-box theorem, every $d$-dimensional system generically admits $d-1$ functionally independent conservation laws near a regular point even though, generically, only a few such laws persist globally. Data-driven methods typically learn conservation laws on a prescribed region of phase space from which training samples are drawn, leaving their behavior beyond that region unresolved. We formulate this local-to-global continuation problem and develop an {expanding-domain neural deflation} framework that tracks the number of independent conservation laws over nested domains. The method recovers the expected $d-1$ local invariants and detects their successive breakdown as the domain expands, relaxing to the expected global conservation law limit. It distinguishes the local invariants (associated with Frobenius integrability) from persistent global structure and shows that the domain scale over which additional laws survive reflects proximity to Liouville integrability. Pointwise losses can localize isolated obstructions, whereas in more complicated dynamics the breakdown of our loss functions is gradual and spatially diffuse. The framework thus provides a data-driven approach for studying the persistence and breakdown of (so-far-learned) conservation laws across phase space.


### Escaping Parameter Space: Tight Generalization Bounds via Representation Quality
**Authors**: Niclas Göring, Shuofeng Zhang, Branton DeMoss, Ard A. Louis

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23729v1](https://arxiv.org/pdf/2610.23729v1)

**Abstract**: We derive a tight generalization bound for deterministic neural We derive a tight generalization bound for deterministic neural networks based on their last hidden layer representations. By evaluating representation quality with a parameter-free $k$-nearest-neighbor ($k$-NN) classifier, our certificate avoids traditional parameter-space complexity measures, KL divergences to a posterior, weight norms, and compression. The bound is tight: trained from scratch, it reaches an 8.0 percentage point gap to test error on CIFAR-10 (ResNet-18) and yields the first non-vacuous certificates we are aware of on CIFAR-100; with frozen DINOv2 representations, it certifies at 1.4\% on CIFAR-10 and 23.1\% on 1,000-class ImageNet. It decomposes additively into three empirical, independently measurable quantities: local class geometry ($k$-NN decoder error), decoder-network agreement, and training stability. This allows the bound to act as a diagnostic tool: we demonstrate that actively destroying local class geometry eliminates generalization while leaving dataset memorization intact, identifying class geometry as a causally relevant mechanism for generalization. Finally, we show that learned representations are significantly less sensitive to weight noise than linear readouts, suggesting why parameter-space certificates often struggle to remain tight.


## VLA
### Beyond Success Rate: Interventional Evaluation of Memory in Vision-Language-Action Systems
**Authors**: Keyuan Luo, Yi Xie, Wanyun Ling, Yuanzhe Li, Ziyue Li, Zhuoqi Zeng

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23372v1](https://arxiv.org/pdf/2610.23372v1)

**Abstract**: When we say that a robot uses memory, does that memory actually play a role? Success-rate ablations alone cannot establish the use of task-relevant facts: they change information and computation together, while aggregate rates can hide offsetting gains and losses. We propose an Interventional Memory Evaluation Protocol (IMEP) for vision-language-action (VLA) systems to address four questions: (1) Does memory provide a net benefit? (2) Under what conditions does memory help? (3) Do changes to memory alter task outcomes? (4) Are these effects specific to task-relevant facts? At the retrieval interface, we compare target-fact substitutions with fact-preserving replacements, minimal numerical perturbations, and exact replicas, while assessing decision correctness separately from motor execution success. We evaluate within-episode, cross-episode, and agentic memory. In cross-episode learned-bank experiments, a one-unit-in-the-last-place (ULP) intervention, including its installation procedure, changes 11.9% of seed-paired outcomes, while changing key facts produces no clear additional effect over fact-preserving replacements. To examine when memory helps, we introduce ChainBench, where correct decisions require historical information unavailable in current observations. The full memory configuration raises task success from 39.1% to 74.3%, matching the oracle-decision condition under shared recorded executions. These results show that correct history can support robot decisions, but establishing whether a memory system realizes this benefit requires fact-specific evidence beyond aggregate success rates.


### NestedVLA: Learning to Consolidate and Generate Skills for Vision-Language-Action Models
**Authors**: Guodong Du, Wanyu Lin

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23271v1](https://arxiv.org/pdf/2610.23271v1)

**Abstract**: Vision--Language--Action (VLA) models promise generalist robotic agents, yet consolidating skills learned across heterogeneous tasks and environments remains difficult: training data is fragmented across platforms, joint multi-task training suffers from interference, and model merging tends to introduce parameter conflicts or require architectural changes. We instead advocate a paradigm in which skills are first learned independently and then consolidated post hoc. To this end, we propose NestedVLA, which replaces parameter aggregation with parameter generation: a nested hypernetwork, conditioned on the target task, synthesizes task-adaptive action-expert parameters that compose with a frozen base VLA. Task-specific compressed VLM residuals are retained separately. This formulation enables flexible task-conditioned skill reuse while mitigating interference. Across three RL benchmarks (MetaWorld, ManiSkill, CALVIN), NestedVLA outperforms the strongest model-merging baseline by 41 pp on average, matches per-task fine-tuning within 1 pp on ManiSkill, and substantially closes the gap on CALVIN, pointing toward a storage-efficient route to skill consolidation. Code is available at https://github.com/WanyuGroup/NeurIPS2026-NestedVLA.


### Unifying Embodied Foundation Models via a Model-to-Policy Formulation
**Authors**: Xinyi Hong, Mingyang Ren

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23053v1](https://arxiv.org/pdf/2610.23053v1)

**Abstract**: Vision-language-action (VLA) models and world-action models (WAMs) have emerged as promising approaches to robot learning and control. These models integrate multimodal perception and action generation, but differ in their architectures, output representations, and learning objectives. In this paper, we present a unified, architecture-agnostic probabilistic formulation for embodied foundation models based on stochastic kernels. Our formulation has two key components: (i) we characterize embodied foundation models through conditional output distributions and action-realization kernels, which together induce task-conditioned robot policies; and (ii) we connect pretraining and post-training to policy deployment, accommodating model-specific pretraining objectives and offline or online post-training strategies. We instantiate the formulation for OpenVLA and DreamZero, covering autoregressive action-token prediction and joint video-action generation.


### Embodiment-Classifier Guidance: Transferring Frozen VLAs Across Robot Dynamics without Demonstrations
**Authors**: Devin Han, Hershraj Niranjani

**Published Date**: 2026-10-15

**Updated Date**: 2026-10-15

**PDF Url**: [2610.22576v1](https://arxiv.org/pdf/2610.22576v1)

**Abstract**: Flow-based policies such as $π_0$ are trained on a fixed set of embodiments, and transferring them to new ones is an open problem. To adapt a frozen $π_0$ to a new embodiment without additional demonstrations or parameter updates, we train a lightweight embodiment classifier to distinguish successful action chunks on the source body from those on the target body, using a few calibration tasks. On transfer tasks that $π_0$ saw on its source body but the classifier was never trained on, we nudge each denoising step of $π_0$ with the classifier's gradient, which estimates the direction from the distribution of successful actions on the source body toward that on the target body. On the LIBERO simulation benchmark with four modified controllers, embodiment-classifier guidance raises $π_0$'s average success on the target bodies from 72% to 80% across 12 suite-controller pairs, with a 31% relative reduction in failures (11 of 12 gain; 5 significant after Holm correction). In simulation, guidance is data-efficient, needing few target-body rollouts per task, which makes it promising for sim-to-real transfer, where rollouts are costly. Guidance is mixed on weak wrists and harmful on a locked wrist, when the classifier lacks data or favors infeasible motions. Collecting more target-body data with guided $π_0$ can fill such gaps: on one weak-wrist arm, guided $π_0$ solved a task on which unguided $π_0$ had zero successes in the original data, and retraining the classifier on the guided successes raised success from 52.5% to 70.7%.


### When Plans Change, Remember: Replanning-Guided Visual Memory for Vision-Language-Action Models
**Authors**: Victoria Smelova, Daniil Kazachkov, Georgiy Kazantsev, Iuliia Tsvetkova, Egor Cherepanov, Nikita Kachaev, Artem Latyshev, Aleksandr I. Panov, Alexey K. Kovalev

**Published Date**: 2026-10-15

**Updated Date**: 2026-10-15

**PDF Url**: [2610.22556v1](https://arxiv.org/pdf/2610.22556v1)

**Abstract**: Long-horizon, multi-stage Vision-Language-Action (VLA) policies often require visual information that is no longer present in the current observation. Retaining the complete observation history is computationally expensive and highly redundant, motivating selective visual memory. We introduce RePlanMem-VLA (Replanning-Guided Keyframe Memory for VLA), which turns a policy's own plan revisions into an online memory-write signal. Under receding-horizon execution, consecutive action chunks predict some of the same future actions. RePlanMem-VLA treats unusually large disagreement between these temporally aligned predictions as evidence of a task-relevant event. We first compare 35 disagreement measures across single-task autoregressive decoder-only and Flow-Matching Transformers trained from scratch, then validate the selected signals on pretrained OpenVLA-OFT and $π_{0.5}$ policies over MIKASA-Robo-VLA tasks. The resulting detectors achieve ROC-AUC of 0.981-0.997. We then use the selected signals in RePlanMem-VLA to trigger updates to a bounded visual memory, with a robot-masked write filter suppressing redundant frames. In the evaluated memory-retention experiments, RePlanMem-VLA preserves task-relevant observations until the later decision point in 100% of episodes. Real-robot replay data further show that event selection and redundancy suppression extend beyond simulation. These results establish plan revision as a policy-internal signal for controlling what a VLA remembers. Website: https://vika787.github.io/RePlanMem/.


### VLA-GAUGE: Systematically Evaluating Generalization and Robustness in Vision-Language-Action Models
**Authors**: Jun Xiao, Rui Ye, Dong Cao, Jinyu Gu, Ying Wang, Zhiliang Zhu

**Published Date**: 2026-10-12

**Updated Date**: 2026-10-12

**PDF Url**: [2610.16567v1](https://arxiv.org/pdf/2610.16567v1)

**Abstract**: Vision-Language-Action models (VLAs) have achieved high success rates on familiar manipulation tasks, yet it remains unclear whether such scores reflect genuine zero-shot generalization and perturbation robustness. Existing evaluation frameworks provide limited capability-level diagnosis and combinatorial perturbation coverage, often without connecting diagnosis to targeted model refinement. We introduce VLA-GAUGE, a diagnostic framework that unifies both evaluations under a shared executable task representation. It combines (1) paired in-distribution and out-of-distribution tasks across six capability suites, (2) single-factor sensitivity analysis with combinatorial perturbation screening and evaluation, and (3) diagnosis-driven refinement through targeted data augmentation and model fine-tuning. We evaluate 12 VLAs spanning different model sizes and action-modeling paradigms under a unified protocol. We find that (1) The mean Zero-Shot Score on VLA-GAUGE is only 22.3%, with SimpleVLA-RL scoring 8.0% and ranking second to last among the evaluated models. (2) Under three representative combinatorial perturbation configurations, the mean R-Score is 9.3. (3) Diagnosis-driven fine-tuning improves $π_{0.5}$'s zero-shot generalization and robustness under a selected perturbation combination on held-out scenarios by 72.4 and 31.8 scoring points, respectively; the latter exceeds the 10.9-point gain from LIBERO-Plus single-factor fine-tuning despite fewer successful training trajectories. These results show that high reported success rates on familiar manipulation tasks do not guarantee strong zero-shot generalization to unseen tasks or robustness to combinatorial perturbations, while diagnostic evaluation provides actionable signals for targeted model improvement.


## Agent
### AI-Driven Reproducibility and Analytical Robustness in Scientific Discovery
**Authors**: Shicheng Liu, Krista Opsahl-Ong, Andrew Drozdov, Julian Killingback, Arnav Singhvi, Ronak Pradeep, Michael Bendersky, James C. Dickerson, Monica S. Lam

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23845v1](https://arxiv.org/pdf/2610.23845v1)

**Abstract**: Reproducible and analytically robust research findings are essential to scientific progress, but evaluating these properties typically requires costly manual effort. We investigate whether LLM agents can help automate reproduction and robustness analysis, using a medical case study grounded in the Surveillance, Epidemiology, and End Results (SEER) database, a widely used U.S. cancer registry underlying tens of thousands of published studies. First, we introduce SEER-Repro, a benchmark of 20 published SEER-based papers together with the data and resources required to reproduce their findings. Second, we create an AI agent that successfully reproduces 77.4% of 2,190 atomic claims, while providing executable baselines for further analysis. Third, we develop an agentic analysis pipeline to test the robustness of the medical findings by identifying analytical choices underlying each finding, proposing defensible alternatives, and rerunning the analysis to determine whether those choices affect the conclusion. Across published papers in SEER-Repro, our pipeline identifies potentially consequential analytical choices in 9.5% of fully reproduced findings and flags them for expert review. These results show how LLM agents can support scientific review by reproducing findings, systematically testing their robustness, and directing expert attention toward potentially consequential analytical choices.


### Self-Building Labs
**Authors**: Jiaru Bai, Yuchi Zhao, Han Hao, Miroslav Bogdanovic, Yang Cao, Varinia Bernales, Alán Aspuru-Guzik

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23826v1](https://arxiv.org/pdf/2610.23826v1)

**Abstract**: Self-driving laboratories (SDLs) accelerate scientific discovery by automating experimental execution and optimization. AI agents can increasingly propose new experiments, but existing SDLs can only run the procedures they were built for. Adapting them to a new experiment still takes extensive manual engineering, which makes laboratory flexibility the bottleneck for scaling discovery. We introduce the self-building laboratory (SBL), which designs, configures, and operates its own laboratory setup given a high-level scientific goal. SBL starts from whatever already exists, from an empty room to a working SDL, and builds the missing capabilities: the lab layout, its digital twin, robot skills, and experimental workflows. We demonstrate the system working across different robots and setups, scaling from a single workstation to laboratories with several robots working together. We validate SBL's end-to-end capabilities through a real-world quantum-dot synthesis experiment. By shifting the role of human researchers from manually configuring and programming device automation to specifying scientific objectives, SBL makes scientific automation more accessible, flexible, and scalable. Project website: https://self-building-labs.github.io/


### Learning Personalized Memory Gating from Delayed One-Sided Feedback
**Authors**: Kaixuan Ji, Zixiang Chen, Wenting Zhao, Cheng Qian, Heng Wang, Weizhi Zhang, Jielin Qiu, Liangwei Yang, Quanquan Gu, Silvio Savarese, Shelby Heinecke, Huan Wang

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23812v1](https://arxiv.org/pdf/2610.23812v1)

**Abstract**: Long-term memory enables language-model agents to personalize future interactions, but a finite memory bank cannot preserve every extracted fact. Existing memory gating policies are typically shared across users and therefore fail to account for user-specific patterns of future reuse. In this paper, we study memory gating at the fact level. We first propose a retrieval-based labeling strategy that labels each fact by whether it is later retrieved and incorporated into responses. We then formulate online memory gating as contextual apple tasting with delayed one-sided feedback, and propose Warm-Start UCB, which combines offline learning from existing data with online adaptation to the current user. Our theoretical analysis establishes a high-probability regret upper bound of $\tilde{O}(Tε\wedge d\sqrt{T})$ when the delay window is at most $O(\sqrt{T})$, where $T$ is the total number of rounds, $ε$ is the initialization error, $d$ is the dimension of the feature map, and $\tilde{O}(\cdot)$ hides constant and poly-logarithmic factors. The results of our experiment demonstrate that our method outperforms all baselines under different memory budgets and history lengths, establishing it as a promising personalized memory gating policy.


### DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery
**Authors**: Yuxing Chen, Zhisheng Zhang, Cheng Tang, Wei Li, Minghui Zhang, Ziyan Huang, Shaocong Wei, Jiawei Chen, Junru Hu, Hongze Zhu, Jianghan Shen, Min Cen, Xinyuan Zhu, Yaxue Zhao, Jubo Wang, Yuqiang Li, Chun-Mei Feng, Zongyuan Ge, Rui Su, Jie Xu, Yirong Chen, Xi Xu, Ming Hu

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23791v1](https://arxiv.org/pdf/2610.23791v1)

**Abstract**: Computational drug discovery requires agents to compose scientific operations and adapt to changing evidence and constraints. Here we introduce DrugHarness, an evolvable agent harness coupling composable scientific execution with conditional skill induction. Its environment integrates over 80 scientific operations, biomedical resources and task-specific code, preserving associations among candidates, results and artifacts. From execution trajectories and outcome feedback, DrugHarness induces action hypotheses with observable applicability conditions, recommended actions and supporting evidence. An independent review agent evaluates candidate skills derived from these hypotheses through source verification and, when needed, targeted execution trials. Admitted skills guide subsequent tasks and are revised through feedback. Evaluation on MolBench and SMDD-Bench demonstrates capabilities in molecular screening, optimization and constrained design. Without evolution, DrugHarness exceeds reported MolClaw-CC results by 10.8 percentage points in affinity-comparison accuracy and 55% in mean top-three active hits on MolBench. Retrospective evaluation on skill-development tasks shows that evolution increases Qwen's affinity-comparison accuracy from 62.2% to 81.1% and optimization success from 79.5% to 87.2%. In a prospective HPK1 study, DrugHarness achieves a more favorable median docking score than Biomni among system-specific candidates. A synthesized compound achieves a cellular IC50 of 14.19 nM, a 2.64-fold potency improvement over the best input reference, with activity competitive with two selected compounds designed by experienced medicinal chemists. These results support conditional skill evolution for scientific agents and demonstrate a workflow connecting computational drug design with experimental validation.


### Parametric Resonance in Primal-Dual Learning for Slowly Non-Stationary Constrained MDPs
**Authors**: Maxime Baelde

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23788v1](https://arxiv.org/pdf/2610.23788v1)

**Abstract**: Primal-dual methods for constrained Markov decision processes are analyzed under a two-timescale assumption, with non-stationarity entering through two channels. In the additive channel, where the constraint level oscillates, the dual oscillation saturates at a floor set by the moving optimum and is amplified linearly by the timescale ratio. In the parametric channel, where the constraint sensitivity oscillates, a coherent modulation carries no resonant forcing at any depth: the dual update's stiffness modulation cancels the primal update's damping modulation. Instability instead comes from a mismatch between the constraint estimate used by the primal update and the measurement used by the dual update, producing a parametric resonance at twice the pair's natural frequency. The tolerated mismatch grows with the square root of the forcing bandwidth and collapses with the square root of the dual-to-primal step-size ratio. These results hold on the tangent linear-quadratic reduction around an active saddle, for one constraint and for $K$ constraints under a common modulation and an isotropy condition. Driving both updates from the same estimate removes the resonant forcing but introduces a stationary offset equal to the estimator's bias. In a Lagrangian soft actor-critic agent, the multiplier locks onto the sub-harmonic at the timescale ratios its identified linear loop predicts and a coherent cost critic suppresses the lock-in, while a proportional (PID) term, predicted to leave the lock-in in place, suppresses most of it through the projection of the multiplier.


### GLOBE: Evolving Structured Agentic Memory for E-commerce Product Optimization in Generative Search
**Authors**: Hyunseo Kim, Suil Choe, Sukkyoung So, Daeyeon Yi

**Published Date**: 2026-10-16

**Updated Date**: 2026-10-16

**PDF Url**: [2610.23709v1](https://arxiv.org/pdf/2610.23709v1)

**Abstract**: Optimizing product listings for generative search requires language agents not only to rewrite effectively but also to continually self-improve by retaining successful strategies across diverse categories. However, existing approaches often treat structured listings as free-form text, leaving effective strategies implicit in prompts, search trajectories, or rewritten outputs rather than accumulating them as a reusable agentic memory. To address this limitation, we introduce GLOBE, an agentic framework that drives continual self-improvement by storing optimization knowledge in an evolving handbook of explicit, field-scoped behaviors. In each episode, an Editor applies relevant behaviors and receives rank-based feedback, which a Reflector converts into behavior updates. Crucially for dependable execution in real-world settings, a Moderator removes redundant proposals, a Curator commits accepted changes, and consistently harmful behaviors are deactivated. This cycle transforms episodic feedback into a persistent, field-scoped optimization memory. Experiments show that structured behaviors outperform monolithic prompt optimization, while feedback-driven evolution and moderation further improve effectiveness and reduce downside risk. The learned behaviors also remain effective on unseen product categories, suggesting that agentic memory evolution supports interpretable and transferable product optimization.


