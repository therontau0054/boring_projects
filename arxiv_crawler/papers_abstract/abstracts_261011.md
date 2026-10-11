# Abstracts of Papers

## World Model
### DreamTrue: Action-Faithful Robot World Model with Counterfactual Post-Training
**Authors**: Junyan Li, Ruizhi Li, Yu Liu, Xiangshuo Liu, Mingchao Sun, Hongyu Pan, Mu Xu, Lue Fan, Zhaoxiang Zhang

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12468v1](https://arxiv.org/pdf/2610.12468v1)

**Abstract**: We present DreamTrue, a multi-view, cross-embodiment robot world model for action-faithful and physically plausible video prediction. Training such a model on existing robot datasets faces two obstacles: imprecise calibration can impair action following, while limited coverage of unsuccessful interactions can bias predictions toward successful outcomes. To improve action following across embodiments, we render action trajectories into image-space conditions and introduce offline geometric calibration to align these conditions with the target videos. To broaden interaction coverage, we introduce counterfactual post-training, modifying recorded action trajectories and generating future videos under a wider range of actions and contact configurations. To provide feedback on these predictions without paired ground-truth futures, we construct a human-annotated video dataset covering robot, object, and interaction defects and use it to train an embodied video reward model. Its scores guide reinforcement-learning post-training toward more physically plausible interaction outcomes. On AgiBot, DreamTrue attains state-of-the-art action following, while reducing the human-assessed interaction defect rate from from 48.12% to 6.25%. Notably, our model ranks first in the world model track of the AgiBot World Challenge 2026. The project page can be found at https://brave-eai.github.io/DreamTrue.


### CSF: Contextual Safety Filtering for Motion Generators
**Authors**: Lizhi Yang, Yiling Hou, Yao Tang, Junheng Li, Daniel Weng, Blake Werner, Aaron D. Ames

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12467v1](https://arxiv.org/pdf/2610.12467v1)

**Abstract**: Text-conditioned motion generators produce trackable whole-body motion, but they have no notion of scene-dependent safety: the same action may target an object or a person. Existing safeguards either inspect the prompt, require labeled motion data, or enforce geometric constraints; therefore, they do not directly account for how scene context changes a motion's meaning. We introduce contextual safety filtering (CSF), a training-free filter that grounds natural-language safety rules in safe and unsafe reference trajectories produced by the generator. For each active rule, safe and unsafe reference trajectories define an affine safety value that a safe reference tracking CBF-QP enforces. Across four pretrained generators with different architectures, CSF activates the intended rules in all explicit and scene-triggered unsafe cases and reduces the danger-event rate by up to 90%, while preserving 88-100% of benign motions. We demonstrate the complete system on a real-world Unitree G1, where it successfully prevents unsafe motions in a variety of scenarios, including interactions with humans and objects.


### From Reactive Containment to Proactive Assurance: Lessons from OpenAI, Anthropic, and Google Agent Security Incidents
**Authors**: Abbas Raftari

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12463v1](https://arxiv.org/pdf/2610.12463v1)

**Abstract**: In 2026, cybersecurity evaluations involving OpenAI, Anthropic, and Google agents reached real systems outside their authorized test scope. The paths were different. OpenAI agents exploited research infrastructure, coordinated across runs, and compromised parts of Hugging Face's production environment. Anthropic reported cases in which a misconfigured third-party environment exposed real systems to agents pursuing simulated cyber tasks. In a separately reported evaluation, Google's Gemini accessed three real organizations through an unintended internet route; Google stated that the model stopped in all three instances. Taken together, the cases show why an evaluation cannot rely on an assumed boundary. That boundary must be verified while the agent is operating. This comparative instrumental case study develops a Proactive Agent Security Assurance Cycle (PASAC) and a five-layer Boundary Assurance Stack. The framework combines risk-tiered task design, executable scope contracts, pre-run validation, least-capability access, independent egress enforcement, credential restrictions, cross-run monitoring, automatic stop conditions, and evidence-based reauthorization. A leading-indicator model, nine design propositions, and seven falsifiable hypotheses turn these lessons into a testable research program. Because the public Gemini record is limited to attributed statements and journalism, its detailed causal mechanism remains provisional. The central conclusion is straightforward: proactive agent security requires continuous assurance across the full execution system, not confidence in any single sandbox or safeguard.


### What 30,000 Hours of Ego-centric Video Does Not Teach
**Authors**: Jiahua Dong, Anurag Bagchi, Yash Jangir, Muhammad Zubair Irshad, Sergey Zakharov, Martial Hebert, Homanga Bharadhwaj, Yu-Xiong Wang, Vitor Campagnolo Guizilini, Pavel Tokmakov

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12464v1](https://arxiv.org/pdf/2610.12464v1)

**Abstract**: World models offer a promising alternative to physics-based simulators, yet remain far from practical deployment. We ask how far scaling ego-centric human video takes them, using a dataset of 30,000 hours spanning over 1,000 scene types and 14,000 contributors. Rather than relying on opaque downstream metrics, we directly evaluate agent and object-interaction fidelity on a challenging out-of-distribution benchmark. Increasing training data by 100x improves both, but unevenly: the agent is modeled well, while object fidelity remains far lower and improves slowly. We show that the agent gains need not come from data, and a careful visual conditioning design saturates fidelity with a fraction of it, which lets us measure object fidelity on its own and discover its saturation point. We then introduce a supervision scheme that shifts capacity from scene appearance toward object dynamics, improving object fidelity though a substantial gap remains. Finally, our conclusions transfer to downstream humanoid modeling. Overall, our results suggest that scaling ego-centric data brings agent modeling close to its limit while leaving its effects on the world far behind, and that closing this gap will depend on how models are trained, not only on how much data they see.


### OuroWorld: Bringing Any 3D World Alive as Diverse, Endlessly Looping 3D Cinemagraphs
**Authors**: You-Zhe Xie, Ting-Wei Chou, Yu-Hsuan Li, Kaipeng Zhang, Zhixiang Wang, Yu-Lun Liu

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12461v1](https://arxiv.org/pdf/2610.12461v1)

**Abstract**: Recent 3D world models generate photorealistic, explorable scenes that remain frozen in time. OuroWorld is a mask-free framework that turns any static 3D Gaussian Splatting scene into a 3D cinemagraph: a dynamic scene with vivid, diverse motion looping seamlessly from any viewpoint. A vision-language model infers plausible dynamics and guides a video model to synthesize a reference video, which we lift and complete into multi-view videos. To learn from this imperfect supervision, we propose Inconsistency-Robust Periodic 4DGS: a Fourier-series deformation field guarantees looping by construction, while a Grounded Drift Field anchored at the reference view absorbs cross-view inconsistency. Unlike prior Eulerian methods limited to fluid-like motion, we capture general deformation, object motion, and illumination change. We introduce a ground-truth-free evaluation covering vividness, naturalness, loop seam coherence, and scene quality. On 39 reconstructed and generated scenes, OuroWorld outperforms all baselines and wins 70.8%-99.0% of user-study comparisons. Project page: https://ouroworld.userwei.com


### WorldGuide: Goal-Directed Video World Model for Procedural Task Execution
**Authors**: Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12459v1](https://arxiv.org/pdf/2610.12459v1)

**Abstract**: Video generators and video-based world models can synthesize plausible visual trajectories, but long-horizon procedural tasks require generation to adapt to what has actually been produced. A model must determine the next action from its generated state, execute that action, and recognize when the task is complete. Open-loop generation cannot adapt to execution outcomes, while existing closed-loop systems often rely on pretrained executors or indirect verification. This leaves a gap between deciding an action and successfully realizing it. We formulate procedural video generation as \emph{closed-loop task execution in visual world space} and introduce \textbf{WorldGuide}. Given only an initial image and a task goal, WorldGuide predicts an atomic action, generates its corresponding video clip, and uses the generated result to select the next action or terminate. The Planner and Executor are trained on the same step-level procedural demonstrations: the Planner learns to predict the next atomic action or task completion from visual progress, while the Executor is directly trained to realize the predicted actions. Hierarchical visual memory maintains state across long-horizon execution with bounded history token cost. Due to the lack of step-level action-video supervision for joint planner-executor training, we introduce \textbf{WorldGuide Bench}: approximately 59K step-annotated videos across 245 tasks and 27 procedural categories. WorldGuide achieves a 33.33\% Task Success on \textbf{WorldGuide-Bench}, compared with 29.90\% for the strong recent video model MiniMax-H3, even though MiniMax-H3 receives reference action plans, and achieves 47.69\% on \textbf{VideoCraft-Bench} compared with 32.73\% for MiniMax-H3 under goal-only conditioning. These results demonstrate the importance of coupling planning with learned execution for goal-directed procedural video generation.


## Generation
### A Balanced Data Diet: Addressing the Exploration Bottleneck in Mega-Scale RL for Robot Control
**Authors**: Octi Zhang, Mateo Guaman Castro, Patrick Yin, Ignacio Dagnino, Abhishek Gupta, Rosario Scalise, Byron Boots

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12465v1](https://arxiv.org/pdf/2610.12465v1)

**Abstract**: General-purpose robots must perform a wide range of tasks from agile locomotion to dexterous manipulation. While sim-to-real reinforcement learning (RL) has proven to be a useful tool for this goal, current RL pipelines depend on engineering-heavy, per-task structural priors such as shaped rewards and demonstrations. Recent work has shown that diverse simulator resets, combined with massively parallel simulation, can alleviate much of this engineering burden on several manipulation problems. However, we find that naively scaling this paradigm to more precise or dynamic problems remains non-trivial. While simulator resets can help with exploration, uniformly sampling over this distribution wastes a growing fraction of learning experience on task configurations the policy has already mastered or cannot yet attempt. This makes it challenging to see the expected benefits of scaling parallel environments for RL, since much of the learning signal in a batch is wasted during learning. To mitigate this, we introduce Success Guided Sampling (SGS), a simple adaptive sampler that concentrates RL training on task configurations around the frontier of the policy's capabilities. Doing so allows large-scale simulated RL to make the most out of the experience in a batch, enabling much more effective scaling to large-scale parallel simulation. Across experiments using up to $2^{20}$ (over one million) parallel environments, SGS enables RL to solve challenging multi-terrain quadruped locomotion and contact-rich assembly tasks that prior methods fail to solve. Finally, we distill the learned manipulation policies into RGB-based policies and demonstrate zero-shot transfer to several challenging assembly tasks on real hardware. Project website: https://sgs-rl.github.io/.


### Bi-FORK: Generative Modeling of High-Dimensional Bifurcating Systems
**Authors**: Anna Zimmel, Fleur Hendriks, Markus Holzleitner, Florian Sestak, Martin Weichselbaumer, Vlado Menkovski, Johannes Brandstetter

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12449v1](https://arxiv.org/pdf/2610.12449v1)

**Abstract**: Bifurcations are ubiquitous in physical systems, from structural buckling to fluid and climate dynamics, yet they remain largely unexplored in deep learning. At a symmetry-breaking bifurcation, a single input admits multiple equally valid solutions, violating the one-to-one assumption underlying most learned physical surrogates. We introduce Bi-FORK, a generative framework for learning these one-to-many solution maps in high-dimensional systems. Bi-FORK generates complete trajectories through latent flow matching, preserving space and time coherence, and uses repulsion-guided sampling to recover distinct solution branches in a single amortized pass. We evaluate Bi-FORK on buckling beams, mechanical metamaterials, and Allen-Cahn phase separation, spanning continuous, discrete, and field-valued bifurcations with discretizations up to 260,000 points. Bi-FORK recovers the multimodal solution structure while scaling several orders of magnitude beyond prior approaches, opening generative modeling to high-dimensional bifurcating physical systems.


### Ecology of AI Agents: Collaboration Creates a Population Threshold for Takeoff
**Authors**: Erin Crawley, Hidenori Tanaka

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12436v1](https://arxiv.org/pdf/2610.12436v1)

**Abstract**: AI agents can now conduct real-world cyberattacks, scale up capabilities with the number of agents, and collectively pursue misaligned goals to obtain rewards. Together, these factors raise the risk of a population explosion of misaligned agents: agents could compromise computers and secretly deploy additional agents, creating a self-reinforcing cycle where larger populations develop greater collective cyber capability and expand further. This raises a fundamental question: What determines whether a population of misaligned agents remains contained or takes off into this self-reinforcing cycle? This population-level problem is ecological safety: unlike individual-agent or multi-agent safety with a fixed population, it concerns the dynamics of the population itself. Here, we develop an ecological theory of AI-agent populations based on a population growth equation in which fitness (growth rate) depends on cybersecurity capability. We show that, without collaboration, the population takes off only when individual-agent capability exceeds a critical threshold. With collaboration, however, collective cybersecurity capability increases with population size. This creates a critical population threshold: below it, the population declines; above it, the population takes off, even though individual-agent capability has not changed. In ecology, this phenomenon is known as the strong Allee effect. Because red teaming a small group of agents cannot guarantee ecological safety in larger populations, our theory calls for ecological red teaming and population pacing: gradually deploying larger agent populations in controlled environments, while measuring how cyber capability scales with population size, and estimating the critical population size for takeoff. Capability gains may lower this threshold, requiring re-estimation for each new model generation.


### Toward Joint Optimization of Circuit Depth and Training Data Size in Adaptively Grown Quantum Classifiers
**Authors**: Saeefa Rubaiyet Nowmi, Md Mahmuduzzaman Kamol, Mohammad Saidur Rahman

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12428v1](https://arxiv.org/pdf/2610.12428v1)

**Abstract**: Building a quantum model involves a tradeoff: how complex the circuit should be, and how much training data it needs. Caro et al. show that models with fewer trainable gates need less training data to generalize well. Q-FLAIR shows that a quantum feature-map circuit can be grown gate-by-gate, stopping once further growth stops improving the training loss. We ask whether these two results combine into a predictable scaling law. Does Q-FLAIR's own stopping rule pick larger or smaller circuits as training data grows? Does the resulting generalization behavior track Caro et al.'s bound?
  We reimplement Q-FLAIR's growth mechanism faithfully, including its analytic reconstruction and exact stopping rule. We run it on full-resolution (784-pixel) MNIST 3-vs-5 classification, at five training-set sizes from N = 2000 to 10000. We then fine-tune each resulting circuit, so we can measure Caro et al.'s notion of active gates, K.
  We find no predictable relationship between training-set size and the circuit size Q-FLAIR converges to. Circuit size and test accuracy both vary non-monotonically with N, and seed-to-seed variance is nearly as large as any trend across N. The empirical generalization gap never exceeds Caro et al.'s bound in 14 of 15 runs, so the bound holds as a valid guarantee in those runs. But the gap correlates only weakly with the bound's value (r = 0.12). This shows that K does not explain most of the variation we observe. Why a valid guarantee can coexist with such weak predictive power remains an open question, and answering it may be necessary before circuit depth and training data size can be jointly optimized in practice.


### Beyond Spatio-Temporal Priors: A Generalizable Approach for Dense Correspondence Matching
**Authors**: Luping Liu, Bingyi Kang, Yifan Wang, Dong Xu

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12421v1](https://arxiv.org/pdf/2610.12421v1)

**Abstract**: Dense correspondence matching has historically been bounded by simplifying spatio-temporal priors, such as smooth motion and rigid geometry. While effective for classical tasks, these assumptions break down in image editing and reference-guided generation (IEG), where transformations can preserve visual identity while breaking physical continuity. To establish identity-preserving correspondence across such transformations, we introduce FreeMatching, a generalizable framework combining generative and semantic foundation representations with heterogeneous supervision from classical datasets, tracked videos, and synthetic scenes. Teacher-guided iterative refinement further improves correspondence in IEG without dense correspondence annotations. Experimentally, a single FreeMatching model substantially improves correspondence quality on challenging IEG image pairs while retaining competitive performance on classical benchmarks. Furthermore, we demonstrate its utility as a quantitative metric for evaluating identity preservation, with scores that correlate with human judgment. The code is available at https://github.com/luping-liu/FreeMatching.


### WOVEN: Weaving Visual World Modeling into Multimodal LLMs
**Authors**: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12417v1](https://arxiv.org/pdf/2610.12417v1)

**Abstract**: Multimodal large language models (MLLMs) struggle with spatial, embodied, physical, and temporal reasoning. We hypothesize that these failures reflect a shared deficit in visual transition reasoning, and test whether this capability can serve as a shared training primitive, one that different models can learn from different supervision sources and reuse across different tasks, with a systematic training recipe. Existing benchmarks document these deficits separately but do not support controlled comparisons across scenes, actions, and reasoning operations. We therefore introduce WOVEN, a training source and benchmark for visual transition reasoning that organizes transition supervision by scene, action, and reasoning type, using diverse, realistic rollouts from video-pretrained generative models: 36,076 examples across 20 scene types, 5 action types, and 8 reasoning types. We first evaluate 38 frontier MLLMs (e.g., GPT-5.4 and Qwen3-VL-235B-A22B) and find a substantial and systematic deficit: even the strongest models fall far below humans, and the failures recur across model families and persist with scale. We then train MLLMs at multiple scales on WOVEN and find that they learn a shared capability that transfers broadly: training subsets of only about 2,000 items each collectively improve 22 of 26 external benchmarks by up to 27.3 percentage points, and WOVEN data can replace 30-50% of a task's own training data with comparable accuracy. Controlled comparisons further yield a training recipe for visual world modeling, validated prospectively on held-out benchmarks: select supervision by the reasoning operation it teaches rather than by the actions, scenes, or domains it shows, and prefer larger changes to the visual state for robustness. Our work establishes visual transition reasoning as a reusable foundation for systematic visual world-model training in MLLMs.


## VLA
### VioLA: Learning Generalist Humanoid Control Policies from Human Data
**Authors**: Mert Albaba, Jens Beißwenger, Anna Manasyan, Daniel Marta, Michael J. Black, Wieland Brendel, Andreas Krause, Georg Martius, Martin Riedmiller

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12435v1](https://arxiv.org/pdf/2610.12435v1)

**Abstract**: Teaching a humanoid to follow instructions with its whole body runs into two obstacles. Its action space is large and tightly coupled: legs, arms, and fingers must move together while the robot keeps its balance, which makes joint-level actions hard to learn. And humanoid demonstrations are scarce, so current humanoid generalist policies do not follow new instructions out of the box and are fine-tuned on teleoperated demonstrations of each task before deployment. Human demonstrations exist in far larger numbers, but a person's motion is not a robot command. We remove both obstacles by changing what the generalist policy predicts. We introduce VioLA, a generalist humanoid policy that predicts body and hand motion latents instead of joint commands. A pretrained body- and hand-controller execute these latents on the robot. Their corresponding motion encoders map human and robot motion into the same latent spaces. A human recording is therefore labeled in the policy's action space, and the training demonstration pool contains 140.6 million frames, 93.2% of them human. As a result, VioLA follows locomotion instructions on the real robot zero-shot, without task-specific fine-tuning, reaching 100% success where GR00T N1.7 and $Ψ_0$ reach 16.7% and 0%, respectively. It also reaches 88.6% manipulation success without task-specific fine-tuning. The same approach works across two VLA and one world-action model backbones. A generalist policy trained on human demonstrations alone performs locomotion tasks on the real robot zero-shot. Code and checkpoints will be released.


### ARC: A Reasoning Recipe for Robot Foundation Models
**Authors**: Gokul Puthumanaillam, Tao Sun, Elie Aljalbout, Moritz Reuss, Zhaoshuo Li, Fabio Ramos, Ankit Goyal, Jenai Xuning Yang

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12386v1](https://arxiv.org/pdf/2610.12386v1)

**Abstract**: The prevailing approach to improving robot foundation models (RFMs) relies on larger models, more robot demonstrations, and costly training at scale. We show that there exists an effective and efficient complementary approach: the right reasoning recipe can substantially improve the zero-shot task performance of existing state-of-the-art RFMs. We refer to this recipe as ARC. It consists of three key ingredients: a reasoning trace, a scalable automatic labeling pipeline, and a strategy for adapting pretrained RFMs to use these traces for control. First, we find that effective reasoning traces should be grounded in the robot's next action and explain its causal structure: why the action is appropriate and what effect it should produce. Second, we show that these traces can be generated automatically from existing demonstrations, enabling us to construct ARC-Trace-DROID from DROID without collecting new robot data. Third, we show how state-of-the-art VLAs such as $π_{0.5}$ and WAMs such as Cosmos3-Nano-Policy can learn to use these traces for control, with fine-tuning and inference tailored to each model's architecture and capabilities. Using ARC, we obtain gains in zero-shot RFM performance that, to our knowledge, are unprecedented without additional robot demonstrations or foundation-scale training. The adapted models establish a new state of the art on RoboLab-120 and MolmoSpaces, with gains of up to 50 percentage points on RoboLab-Reasoning-50. On real robots, ARC improves $π_{0.5}$'s task success by 82.2 percentage points. Project website: https://arc-robot-reasoning.github.io/


### Recompose and Refine Latent Reasoning Flows for Vision-Language-Action Models
**Authors**: Hongyu Shi, Sen Zhao, Zuyu Zhang, Lifeng Shen, Ding Zou, Xinyu He, Xu Zhang, Qinghua Zhang

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12090v1](https://arxiv.org/pdf/2610.12090v1)

**Abstract**: Latent reasoning enables vision-language-action (VLA) models to transform multimodal observations into task-relevant internal states before generating continuous robot actions. While existing methods learn to generate or refine such states for each policy query, they discard successful reasoning after execution and therefore reconstruct similar computation from scratch. We present Reasoning and Flow Memory (FLOWMEM), a unified VLA model that turns successful latent computation into reusable reasoning experience. Rather than appending a fixed retrieved context, FLOWMEM dynamically retrieves and recomposes compatible latent fragments as the embodied context evolves, forming a reasoning route that follows the temporal structure and progress of successful computation. The route is then refined using current visual and proprioceptive evidence before it conditions action generation. Experiments on RoboMME and LIBERO-Plus show that FLOWMEM attains 48.0% and 77.3% success, outperforming memory-free policies by 1.7 and 4.1 percentage points, respectively. These results demonstrate the value of reusing successful latent computation for closed-loop VLA control.


### Humanoid World Action Model With Joint State--Action Generation
**Authors**: Yan Yang, Jikun Rong, Minzhao Zhu, Zheyi Zhao, Qirui Hu, Zihan Lan, Weixin Mao, Yinhao Li, Zhen Fu, Hua Chen

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12026v1](https://arxiv.org/pdf/2610.12026v1)

**Abstract**: Humanoid robots are a promising platform for general-purpose manipulation. Recent Vision-Language-Action (VLA) policies learn actions directly from multimodal observations, while World Action Models (WAMs) further incorporate future visual prediction to improve action generation. However, in hierarchical humanoid systems, VLA and WAM policies output reference actions that are subsequently realized through whole-body control, robot dynamics, balance, and contact. This hierarchy creates an action--execution gap: the reference produced by the policy can differ from the motion realized by the robot. Without explicitly modeling the realized body state, future visual prediction must jointly explain scene evolution and discrepancies between reference actions and executed motion, making it difficult to associate an action with its physical outcome. We propose HWAM, a Humanoid World Action Model with joint state--action generation, which makes the robot's post-execution proprioceptive state an explicit prediction target. By jointly generating reference actions and their realized body states, HWAM directly incorporates supervision of executed motion into action learning. HWAM is trained through three complementary conditional paths. The Policy path jointly denoises state--action trajectories conditioned only on current observations, matching deployment conditions. Forward Dynamics Modeling (FDM) predicts future visual observations conditioned on actions and post-execution states, while Inverse Dynamics Modeling (IDM) reconstructs the joint trajectory from visual transitions. Together, these paths connect policy references, realized body motion, and visual outcomes. HWAM achieves the highest success rate among evaluated baselines on three real-robot tasks on the LimX OLI humanoid. On Candy Picking, HWAM achieves a 70.6% success rate, compared with 43.3% for Fast-WAM.


### REACT: Rolling Denoising and Dual Decoupling for Reactive Robot Control with VLA Models
**Authors**: Houlong Xiong, Zhenqi Qiu, Zechen Wang, Suohang Zhang, Yiyu Ren, Wanting Xu, Hongfei Niu, Chengyang He, Ge Sun, Ran Cheng, Qian Zhu

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12007v1](https://arxiv.org/pdf/2610.12007v1)

**Abstract**: Flow-based vision-language-action (VLA) models generate action chunks for temporally coherent robot motion, but chunked control creates a fundamental closed-loop trade-off: long chunks provide smooth execution, whereas frequent replanning improves reactivity at the cost of action discontinuities. We introduce REACT, a rolling-denoising framework that makes flow-based VLAs more reactive while preserving long-horizon context. Instead of regenerating entire action chunks from scratch, REACT maintains a persistent action buffer with staggered flow timesteps. At each control step, the full horizon is denoised using the latest observation, the cleanest action block is executed, partially refined future blocks are shifted forward, and fresh noise is appended to the tail. As a result, each executed action block is refined across multiple recent observations before deployment. To support real-time control, we further introduce dual decoupling, which separates sensing, VLM encoding, DiT denoising, and action execution, enabling high-frequency observation updates and action streaming under practical compute constraints. Across the RoboTwin 2.0 simulation benchmark and real-world tasks spanning bimanual manipulation and dynamic control on multiple robot platforms, REACT improves task success and reduces reaction latency while producing smoother trajectories than frequent-replanning and asynchronous baselines.


### CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding
**Authors**: Mohammad Khoshnazar, Mohammad Dehghani Tezerjani, Deyuan Qu, Zhiyuan Gao, Yanxiang Zhan, Jeroen Schafer, Andrew Melnik, Qing Yang, Michael Beetz

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.11971v1](https://arxiv.org/pdf/2610.11971v1)

**Abstract**: Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates self-supervised capability inference with residual reinforcement learning. CAPABLE infers capability, how much of the commanded motion each joint actually realizes and how that motion contributes to end-effector behavior, online from command-response history and kinematics using a temporal encoder shared across joints, Jacobian grounding, cross-joint attention, and self-supervised physical prediction. The resulting representation conditions a residual policy that adds bounded corrections to the VLA arm action without fault labels or faulty-joint identifiers. Across 28 LIBERO tasks, CAPABLE raises success on an actuator excluded from fault training from 24.8% to 59.3%, outperforming a parameter-matched global-history baseline by 17.4 points while preserving healthy performance. Leave-one-actuator-out experiments across six joints show that this transfer is not specific to one actuator, and additional evaluations characterize transfer to unseen fault families and demonstrate recovery on a physical Franka Panda. https://capable-vla.github.io/


## Agent
### BrickBench: Evaluating Agentic Brick Design
**Authors**: Peter Kulits, Yiqing Xu, R. Kenny Jones, Cordelia Schmid, Jiajun Wu

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12452v1](https://arxiv.org/pdf/2610.12452v1)

**Abstract**: We propose BrickBench, a benchmark for agentic text-conditioned LEGO-set design. Given a prompt, an agent is tasked with producing an assembly that not only satisfies semantic and design criteria, but that can also be physically built. To do so, it must select parts from a discrete library and reason jointly about local and global constraints. We score validity, alignment, and design across three settings that vary in scale and part availability. We provide BrickAgent, an environment for coding agents to construct, inspect, and validate their designs. We find that leading agents largely satisfy verifiable physical and semantic requirements, but fall short of human designs. We release our benchmark and environment at http://www.brickben.ch


### Caught in the Act: Probes Effectively Detect Sabotage and Catch Unverbalized Deception
**Authors**: Oskar J. Hollinsworth, Alex F. Spies, Tigist Diriba, Adam Gleave, Chris Cundy

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12445v1](https://arxiv.org/pdf/2610.12445v1)

**Abstract**: Recent incidents have highlighted the challenge of monitoring LLM agents and the danger of models deceiving people. We show that white-box deception detection via probes can be scaled up to frontier monitoring settings by collecting the largest deception dataset to date for training probes and introducing a novel probe architecture which can aggregate information across many layers and tokens. Our probes achieve 98.8% AUC in SHADE-Arena, surpassing an Opus 5.5 text-monitoring baseline, and show improved efficacy as the underlying model is scaled up. To push our probes to their limit, we test them on several cases where deception cannot be determined from the context alone. In these cases, which we refer to as introspective deception, the ground truth can only be determined through careful elicitation or thorough knowledge of a model's training data. In one such evaluation, we show that probes can distinguish transcripts containing a model's true hidden goal from other goals with an AUC of up to 99.7%. Our probes also readily detect deception on prominent open-weight models which lie about politically sensitive topics, and about their beliefs when put under pressure. We release our training dataset, dubbed FIBS, to help drive frontier deployment of effective probes, and encourage the community to expand upon it with further examples of deception and sabotage.


### RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world environments
**Authors**: Zimo Wen, Yijin Chen, Yuxuan Cao, Wendi Chen, Yanwen Zou, Wenye Yu, Fuhang Kuang, Han Xue, Jun Lv, Chuan Wen, Cewu Lu

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12424v1](https://arxiv.org/pdf/2610.12424v1)

**Abstract**: A generalist robot should not only perform diverse tasks but also improve through experience, turning what it learns during execution into capabilities that later tasks can reuse. Robot agents that act through code can already repair programs from execution feedback, yet it remains a central challenge to organize this experience around the task structure that gives it meaning, so that each repair is attributed to the responsible capability, supported by execution evidence, and validated before it is reused. We introduce RoboRSI, a robot self-improvement system built on Top-Down Skill Refinement (TSR). TSR decomposes tasks into compound, atomic, and base skills with scoped responsibilities and explicit input--output contracts, attributes each execution outcome to the responsible branch, and confines revision to that branch. Building upon this structure, a Manager, Planner, Engineer, and Reviewer coordinate planning, execution, diagnosis, and the validated release of new skills, while people steer the process through objectives and corrections; stable skill sequences are further consolidated into reusable compound skills. On a mobile manipulator, RoboRSI develops multi-object household cleanup over 104 rounds. In simulation, it achieves the highest success rate on LIBERO, LIBERO-PRO, LIBERO-Plus, and RoboTwin, exceeding the strongest baseline by 2.7 to 11.0 percentage points.


### OnTrack: Real-Time Monitoring and Intervention in LLM Agent Trajectories via Streaming Structure-Aware Optimal Transport
**Authors**: Babak Barazandeh, Connor Swanson, Chinmay Kulkarni, Nikhil Mungel

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12375v1](https://arxiv.org/pdf/2610.12375v1)

**Abstract**: Agents are deployed in applications from trip planners and stock trading to IT incident triage. In most cases, LLM agents work autonomously with minimal rule-based safeguarding, leading to cost and safety issues from irreversible actions. Recent works resolve this either by using a safeguard agent to monitor behavior or evaluating logs post-hoc. The first adds cost and latency to every step; the second delivers its verdict after the run, when tokens are burned and damage is done. To overcome this, we propose OnTrack, a streaming monitoring mechanism that compares an agent's steps and dependencies against recorded successful runs to alert users or block the agent in about a millisecond per step. We study this problem in three regimes of decreasing access: full reference access (historical runs and tool schemas), intermediate access (only tool schemas), and no prior knowledge (only step logs as generated). Expectation of OnTrack's monitoring capabilities reduces as data access drops, ranging from plan violation detection to identifying loops, stalls, and repeated tool calls. Finally, we evaluate OnTrack using SWE-bench trajectories. Based on the first 8 steps, our method ranks failing trajectories below succeeding ones better than content similarity approaches (+0.057 AUROC). With an abort policy, we save about 18% of compute that would be burned on failing runs, where 83% of interrupted runs were actually heading to failure (5 out of 6 aborts were correct).


### Accurate but Not Humble: Evaluating Epistemic Humility in LLM Agents under Knowledge Conflict
**Authors**: Kaiser Sun, Bernal Jimenez Gutierrez, Hongjun Liu, Jingyu Zhang, Jie Gao, Mark Dredze, Daniel Khashabi

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12360v1](https://arxiv.org/pdf/2610.12360v1)

**Abstract**: When retrieved evidence contradicts an agent's prior beliefs, does it revise its answer, acknowledge uncertainty, or persist with an incorrect conclusion? Existing evaluations of agentic systems focus primarily on task success, offering limited insight into how agents handle such conflicts. We propose to evaluate agents on epistemic humility (EH): the agent's willingness to recognize, act on, and communicate uncertainty during task execution. We operationalize EH through three trajectory-level behavioral dimensions: Identify, Solve, and Escalate (ISE). Through knowledge conflict, situations where the backbone language model's parametric knowledge contradicts the evidence it encounters, or where two contextual sources disagree, we evaluate two conflict settings: (1) controlled conflict and (2) naturally occurring conflict during multi-step agentic execution, each paired with matched no-conflict controls. Evaluating four agents, we find that higher task accuracy does not necessarily correspond to greater epistemic humility: some high-accuracy configurations recognize conflicts during execution but do not communicate unresolved uncertainty in their incorrect final answers. Trajectory-level analysis further reveals that agents frequently detect conflicts in early steps of execution but fail to maintain or resolve them in later steps. Finally, we show that model-level interventions can improve EH, but often at the cost of task accuracy, suggesting that epistemic humility emerges from the interaction among the backbone model, agent harness, and evaluation environment.


### Can AI Agents Learn Their Way to the Top? Evaluating Heuristic Learning in a Long-Running Game Agent Competition
**Authors**: Kaisen Yang, Qingle Liu, Kejin Wang, Yicheng Zhao, Jieming Li, Shenghan Zheng, Ruize Yang, Bojun Yang, Heng Gong, Xiang Gao, Lanyue Zhang, Kaiyu Zhong, Zhuo Liu, Shaoxuan Li, Chengxi Li, Yong Yan, Weixuan Zhang, Tianwei Luo, Situ Wang, Youjie Zheng, Sihan Zhao, Shengyuan Wang, Huan-ang Gao, Jiazheng Xu, Xiaohui Xie, Wentao Han, Hongning Wang

**Published Date**: 2026-10-08

**Updated Date**: 2026-10-08

**PDF Url**: [2610.12341v1](https://arxiv.org/pdf/2610.12341v1)

**Abstract**: Adversarial games have driven advances from heuristic search to reinforcement learning, yet learning and adapting strategies from limited samples remain challenging. AI agents offer an alternative by turning game experience into revisions of executable policies. Building on heuristic learning (HL), we formalize Adversarial Heuristic Learning (AHL), a paradigm that uses AI agents as learning engines to refine game policies and supporting software while keeping model weights fixed. We introduce AAArena, a benchmark comprising 12 authentic adversarial games and 1,920 archived human programs, with an evaluation protocol modeled on real-world game competitions. Agents interpret rules, choose opponents, analyze replays, and revise game agents to achieve their highest ranking within fixed match and evaluation budgets. We evaluate \val{completedmodels} model and harness configurations: Opus5.5 with Claude Code earns 6 gold medals, while no evaluated configuration tops the remaining 6 human ladders. Performance is generally weaker in games with more complex rule specifications. Further experiments show that opponent selection and dense feedback support policy improvement, and that agents learn from both on-policy replays of their own matches and off-policy replays of other players' matches. These results highlight HL's potential in adversarial games and identify persistent challenges in game understanding, strategy implementation, and long-horizon policy development.


