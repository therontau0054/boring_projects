# Abstracts of Papers

## World Model
### SkillOpt: Executive Strategy for Self-Evolving Agent Skills
**Authors**: Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, Chong Luo

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23904v1](https://arxiv.org/pdf/2605.23904v1)

**Abstract**: Agent skills today are hand-crafted, generated one-shot, or evolved through loosely controlled self-revision, none of which behaves like a deep-learning optimizer for the skill, and none of which reliably improves over its starting point under feedback. We argue the skill should instead be trained as the external state of a frozen agent, with the same discipline that makes weight-space optimization reproducible. SkillOpt is, to our knowledge, the first systematic controllable text-space optimizer for agent skills: a separate optimizer model turns scored rollouts into bounded add/delete/replace edits on a single skill document, and an edit is accepted only when it strictly improves a held-out validation score. A textual learning-rate budget, rejected-edit buffer, and epoch-wise slow/meta update make skill training stable while adding zero inference-time model calls at deployment. Across six benchmarks, seven target models, and three execution harnesses (direct chat, Codex, Claude Code), SkillOpt is best or tied on all 52 evaluated (model, benchmark, harness) cells and beats every per-cell competitor among human, one-shot LLM, Trace2Skill, TextGrad, GEPA, and EvoSkill skills. On GPT-5.5 it lifts the average no-skill accuracy by +23.5 points in direct chat, by +24.8 inside the Codex agentic loop, and by +19.1 inside Claude Code. Transfer experiments further show that optimized skill artifacts retain value when moved across model scales, between Codex and Claude Code execution environments, and to a nearby math benchmark without further optimization.


### Geo-Align: Video Generation Alignment via Metric Geometry Reward
**Authors**: Zizun Li, Haoyu Guo, Runzhe Teng, Chunhua Shen, Tong He

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23903v1](https://arxiv.org/pdf/2605.23903v1)

**Abstract**: Camera-controlled video generation has achieved remarkable progress in recent years. However, existing video-to-video re-rendering methods primarily rely on Supervised Fine-Tuning using synthetic datasets. At present, there is an extreme scarcity of synchronized, multi-view real-world video data. Consequently, the prevailing paradigm often exhibits limited generalization when processing out-of-distribution real-world videos, with models struggling to accurately adhere to physical scales and camera trajectories. To bridge this gap, we propose Geo-Align, the first Reinforcement Learning framework specifically designed for camera-controlled video re-rendering. Built upon a pretrained model, we optimize the model through a scale-aware perceptual reward mechanism. Specifically, we introduce a metric 3D estimator to extract precise camera trajectories from generated videos, explicitly penalizing deviations in rotation and translation. Furthermore, we meticulously designed a data pipeline strategy based on real-world conditioning videos and target camera trajectories derived from synthetic data, eliminating the reliance on paired data. Extensive experiments demonstrate that Geo-Align consistently outperforms existing supervised learning baselines in both precise camera controllability and visual fidelity, indicating the effectiveness of our method.


### LLMs as Noisy Channels: A Shannon Perspective on Model Capacity and Scaling Laws
**Authors**: Xu Ouyang, Deyi Liu, Yuhang Cai, Jing Liu, Yuan Yang, Chen Zheng, Thomas Hartvigsen, Yiyuan Ma

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23901v1](https://arxiv.org/pdf/2605.23901v1)

**Abstract**: Existing scaling laws for Large Language Models (LLMs), predominantly monotonic power laws, fail to explain emerging non-monotonic phenomena such as catastrophic overtraining and quantization-induced degradation, where performance deteriorates despite increased compute.
  We propose the Shannon Scaling Law, a unified theoretical framework that models LLM training as information transmission over a noisy channel, grounded in the Shannon-Hartley theorem. By mapping model parameters to channel bandwidth and training tokens to signal power, our formulation explicitly captures the interaction between learning signal and intrinsic noise. This perspective reveals a fundamental Shannon capacity for LLMs: scaling model size or data without preserving a sufficient signal-to-noise ratio (SNR) inevitably amplifies noise, inducing a transition from monotonic improvement to U-shaped performance degradation.
  We validate our theory through experiments on Pythia and OLMo2 under perturbations, including Gaussian noise, quantization and supervised fine-tuning on math, QA and code tasks. The Shannon Scaling Law consistently outperforms classical scaling laws and recent perturbation-aware laws, achieving strong $R^2$ scores and accurately capturing loss basins missed by prior approaches. It also extrapolates: fitted on $\leq$6.9B Pythia models with $\leq$180B tokens, it predicts the unseen 12B model up to 307B tokens at pooled $R^2{=}0.847$, while monotonic baselines collapse.


### From Raw Experience to Skill Consumption: A Systematic Study of Model-Generated Agent Skills
**Authors**: Zisu Huang, Jingwen Xu, Yifan Yang, Ziyang Gong, Qihao Yang, Muzhao Tian, Xiaohua Wang, Changze Lv, Xuemei Gao, Qi Dai, Bei Liu, Kai Qiu, Xue Yang, Dongdong Chen, Xiaoqing Zheng, Chong Luo

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23899v1](https://arxiv.org/pdf/2605.23899v1)

**Abstract**: Language agents increasingly improve by reusing \emph{skills} -- structured procedural artifacts distilled from past experience. In particular, \emph{domain-level} and \emph{model-generated} skills are especially promising. They offer fast adaptation within a domain by encoding domain-specific recurring procedures, and they scale beyond labor-intensive hand-crafting. However, while extraction methods continue to proliferate, understanding remains limited, with no comprehensive study spanning the full skill lifecycle -- \textbf{experience generation}, \textbf{skill extraction}, and \textbf{skill consumption} -- to ask whether such skills actually work, when they work, and what makes them succeed or fail. To close this gap, we build a utility-grounded evaluation framework that provides systematic experimental results across extractors and target agents, covering five diverse agentic task domains. We find that model-generated skills are beneficial on average but exhibit non-trivial negative transfer, and that neither extractors nor targets behave uniformly. A model can be a strong extractor yet a weak consumer, or vice versa, with skill utility independent of model scale or baseline task strength. To explain these patterns, we then dissect each lifecycle stage in depth, analyzing how experience composition shapes skill quality, what properties characterize useful skills, and how the same skill transfers across different consumers. Finally, we translate these findings into a concrete \emph{meta-skill} that guides skill extraction toward the features tied to actual utility, which consistently improves skill quality across domains and substantially reduces negative transfer.


### SPACENUM: Revisiting Spatial Numerical Understanding in VLMs
**Authors**: Jianshu Zhang, Yijiang Li, Huifeixin Chen, Haoran Lu, Letian Xue, Bingyang Wang, Han Liu

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23898v1](https://arxiv.org/pdf/2605.23898v1)

**Abstract**: Vision-Language Models (VLMs) are increasingly deployed in embodied environments, where they need produce numerical outputs such as action magnitudes and spatial coordinates. Although these numbers appear meaningful, it remains unclear whether these numerical outputs are genuinely grounded in spatial perception. Therefore, in this work, we revisit spatial numerical understanding through SpaceNum, a unified framework that captures two complementary settings: numbers as dynamic transitions during spatial exploration, and numbers as static layouts in spatial reasoning. We formulate two bidirectional tasks, Num2Space and Space2Num, to evaluate how well VLMs map between vision-side spatial structure and language-side numerical representations. We systematically study whether current VLMs truly understand numerical values in spatial settings. Across dynamic transitions and static layouts, we find that models largely fail to ground numbers in spatial meaning and often perform close to random guess. Through error analysis, reasoning trace analysis, and controlled interventions, we show that current VLMs rely heavily on shallow spatial cues, struggle to build stable coordinate-aware representations, and fail to abstract structured spatial layouts from visual observations. We further show that explicit reasoning provides only marginal gains, while tuning can partially improve spatial numerical understanding and transfer to external spatial reasoning benchmarks.


### ETCHR: Editing To Clarify and Harness Reasoning
**Authors**: Beichen Zhang, Yuhong Liu, Jinsong Li, Yuhang Zang, Jiaqi Wang, Dahua Lin

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23897v1](https://arxiv.org/pdf/2605.23897v1)

**Abstract**: Multimodal Large Language Models have advanced visual reasoning, yet a purely textual chain of thought remains a bottleneck for questions that require fine-grained focus or view transformations. The ''think with images'' paradigm narrows this gap, but existing approaches are either constrained by fixed predefined toolkits or produce noisy intermediate images from unified multimodal methods. We pursue a third option: using a dedicated image editing model and decouple it with an understanding model. However, off-the-shelf image editors fail as reasoning assistants with two complementary gaps: a language-side gap, where editors trained as passive instruction-followers cannot map an abstract question to an appropriate visual transformation, and a generation-side gap, where edit correctness degrades as reasoning depth grows. Guided by this analysis, we introduce ETCHR (Editing To Clarify and Harness Reasoning), a question-conditioned, reasoning-aware image editor decoupled from the downstream understanding model and trained with a two-stage recipe targeted at the two gaps: Reasoning Imitation via supervised fine-tuning on edit trajectories, followed by Reasoning Enhancement with VLM-derived rewards for edit correctness and downstream reasoning accuracy. Since the editor is decoupled, ETCHR plugs into different open- and closed-source MLLMs in a training-free manner. Across five task families (fine-grained perception, chart understanding, logic reasoning, jigsaw restoration, and 3D understanding), ETCHR raises average Pass@1 from 55.95 to 60.77 (+4.82) with Qwen3-VL-8B, from 65.08 to 70.55 (+5.47) with Gemini-3.1-Flash-Lite, and from 76.55 to 81.16 (+4.61) with the 1T-parameter MoE model Kimi K2.5.


## Generation
### Complete-muE: Optimal Hyperparameter Transfer and Scaling for MoE Models
**Authors**: Hongwu Peng, Ohiremen Dibua, Yuanjun Xiong, Yifan Gong, Jianming Zhang, Yan Kang

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23893v1](https://arxiv.org/pdf/2605.23893v1)

**Abstract**: We propose Complete-muE, a framework which targets hyperparameter transfer across dense FFN and any Mixture-of-Experts (MoE) setups in transformer blocks. Existing tools such as $μ$P (requires fixed architectue) or SDE (requires fixed per-step token count) cannot directly solve the hyperparameter transfer problem in MoE setups because Dense to MoE transfer or MoE total experts scaling changes both architecture and tokens per expert. Complete-muE solves this challenge with a two-bridge system: Bridge~I maps between dense FFN and Dense MoE by active-width $μ$P with a normalized router scale. Bridge~II maps between Dense MoE and sparse MoE by activated-expert scaling, where the first-order SDE LR/WD correction cancels while a bounded residual $σ_0$ shift remains. The resulting transfer rule, which we term as Complete muE, covers changes in activated experts, total capacity, granularity, and shared/group-balanced hybrids for MoE models as well as network width/depth, batch size, and duration changes for general Transformer models. Extensive language model and diffusion model pretraining experiments confirm that complete-muE yields relatively stable hyperparameter optima across model architectures and parameter counts -- with only minor drift consistent with the non-strict SDE behavior of Bridge~II. In practice this drift is small enough that hyperparameters tuned on a single dense reference transfer near-optimally to all MoE configurations -- \emph{tune dense once, transfer to all} is the practical recipe at the core of Complete-muE. This enables MoE models to achieve accelerated convergence speedup over dense models when scaling model capacity without costly hyperparameter search.


### Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers
**Authors**: Shuhong Zheng, Michael Oechsle, Erik Sandström, Marie-Julie Rakotosaona, Federico Tombari, Igor Gilitschenski

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23892v1](https://arxiv.org/pdf/2605.23892v1)

**Abstract**: Visual geometry transformers have become powerful architectures for multi-view 3D reconstruction, enabling joint prediction of multiple 3D attributes in a feed-forward manner. However, their computational cost grows quadratically with the input sequence length due to the global attention layers inside these models. This limits both their scalability and efficiency. In this work, we address this challenge with a simple yet general strategy: restricting the number of key/value tokens that each query interacts with during global attention. To achieve effective token selection, we introduce a two-stage framework. First, an inter-frame selection step operates at the frame level to identify frames that should be preserved. Second, an intra-frame selection step further discards more redundant tokens within the selected frames. Our analysis highlights the advantage of a diversity-based strategy for inter-frame selection, which ensures broad coverage of the scene. For intra-frame selection, we show that layer-aware sparsification is necessary, with the selection process guided by the entropy of the global attention pattern. Our approach offers a superior speed-accuracy trade-off compared to existing solutions. Extensive experiments show that it accelerates visual geometry transformers by over 85% for scenes with 500 images while maintaining, or even improving, baseline performance, which hints that how our token selection strategy can play a crucial role in future applications of visual geometry transformers. Our project website is available at https://zsh2000.github.io/good-token-hunting.github.io.


### PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs
**Authors**: Rim Assouel, Amir Bar, Michal Drozdzal, Adriana Romero-Soriano

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23883v1](https://arxiv.org/pdf/2605.23883v1)

**Abstract**: Despite remarkable progress in Multimodal Large Language Models (MLLMs), these models still struggle with fine-grained understanding tasks. In this work, we propose Procedurally Generated Tasks (PGT), a simple data-driven framework that serves a dual purpose: inducing fine-grained visual understanding and acting as a low-cost diagnostic tool to identify the source of perception failures. By overlaying unambiguous geometric primitives on images, PGT generate additional dense supervision that disentangles visual grounding capability from semantic priors. Extensive experiments on relational, quantitative, and 3D/depth understanding benchmarks show that PGT yields remarkable gains across diverse architectures. Instruction tuning MLLMs on LLaVA-v1.5-Instruct augmented with PGT data results in improvements of up to +20% on the What'sUp benchmark and +13.3% on CV-Bench-2D, while maintaining general perception capabilities. Moreover, finetuning state-of-the-art MLLMs on PGT data leads to boosts of up to +5.5% on What'sUp and +8.3% on CV-Bench-2D. These findings demonstrate that PGT effectively address the bottleneck of fine-grained perception, revealing that many spatial reasoning deficits stem from inadequate supervision signals rather than inherent architectural or resolution limitations.


### On the Stability of Spherical Hellinger-Kantorovich Flows and Their Implications for Differential Privacy
**Authors**: Aratrika Mustafi, Soumya Mukherjee

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23879v1](https://arxiv.org/pdf/2605.23879v1)

**Abstract**: Gradient-flow sampling interprets a Gibbs distribution as the minimizer of an energy functional over probability measures and generates dynamics converging to this target. Under spherical Hellinger-Kantorovich (SHK) geometry, the flow couples transport and reaction and coincides with birth-death Langevin dynamics. In this work, we develop a perturbation theory for SHK gradient flows. For two potentials $V$ and $V^{\prime}$, we compare the associated flows from a common initialization and quantify how potential discrepancies propagate over time. A uniform perturbation bound yields dimension-free, pointwise control of the log-likelihood ratio and Rényi divergence, while additional structure allows us to derive bounds for the KL divergence as well. We apply these results to approximate sampling for the exponential mechanism in differential privacy. The likelihood-ratio control provides explicit time-dependent Pure-DP guarantees for SHK-based samplers, while the KL bound yields Approximate-DP certificates via hockey-stick divergence. We also derive a utility bound separating intrinsic exponential-mechanism suboptimality from finite-time sampling error.


### Human Decision-Making with Persuasive and Narrative LLM Explanations
**Authors**: Laura R. Marusich, Mary Grace Kozuch Dhooghe, Jonathan Z. Bakdash, Murat Kantarcioglu

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23867v1](https://arxiv.org/pdf/2605.23867v1)

**Abstract**: Large language models (LLMs) have the potential to aid and improve human decision-making in classification tasks, not only by providing fairly accurate predictions, but also in their ability to generate cogent narrative explanations of those predictions. Prior work has demonstrated that people generally find AI narrative explanations to be understandable, trustworthy, and convincing for changing beliefs and opinions; however, less is known about the impact of narrative explanations on objective human decision-making performance. Here we conduct a large-scale human behavioral experiment to evaluate decision-making performance with LLM-generated narrative explanations of varying persuasiveness. We found the degree of persuasiveness, or lack thereof, for LLM-based explanations did not meaningfully impact decision accuracy over a simple AI prediction alone, in agreement with typical results with explainable AI based on feature importance. We found evidence that narratives increased reliance on AI, but both when the AI prediction was correct and incorrect. Exploratory analyses also indicated that the more persuasive narratives may have had a detrimental effect on decision response times and the ability to discriminate between a correct and incorrect AI prediction. Overall, this work indicates that including narrative explanations with AI predictions may involve tradeoffs for decision-making performance, and more work is needed to determine how and when narrative explanations impact human decision-making.


### Leveraging Foundation Models for Causal Generative Modeling
**Authors**: Aneesh Komanduri, Xintao Wu

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23861v1](https://arxiv.org/pdf/2605.23861v1)

**Abstract**: Causal generative modeling is essential for developing reliable and transparent AI systems capable of counterfactual reasoning. While existing approaches focus on integrating causal constraints during the training of generative models, they often lack a unified framework to leverage the zero-shot reasoning capabilities of pretrained foundation models. We introduce FM-CGM, a modular framework for end-to-end visual causal reasoning using pretrained foundation models. FM-CGM formalizes the causal pipeline through three core components: a concept extractor, a concept manipulator, and a counterfactual generator. By leveraging a large reasoning model for causal inference and a text-to-image diffusion model for generation, our approach enables zero-shot causal discovery, intervention, and counterfactual generation. We then develop Causal Semantic Guidance (CSG), a cross-attention-based mechanism that ensures semantic interventions propagate to descendant concepts while preserving invariant regions. We empirically show that our approach can identify plausible causal structures and is suitable for faithful counterfactual image generation.


## VLA
### ChainFlow-VLA: Causal Flow Planning with Vision-Language Models
**Authors**: Xiyang Wang, Xinlin Wang, Tingguang Zhou, Gong Chen, Xingtai Gui, Zhi Xu, Xiaolei Wu, Feiyang Tan, Hangning Zhou, Mu Yang

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23270v1](https://arxiv.org/pdf/2605.23270v1)

**Abstract**: Current end-to-end autonomous driving systems are fundamentally limited by a mismatch between temporal causal reasoning and global trajectory consistency. Autoregressive (AR) models capture interaction-aware temporal dependencies via causal factorization, but their step-wise decoding leads to error accumulation and suboptimal global structure. In contrast, diffusion models optimize trajectories globally but lack explicit causal constraints, making them unreliable in interactive and safety-critical scenarios. This dichotomy reveals a deeper issue: existing methods treat causal modeling and global optimization as separate paradigms, without a principled way to unify them within a single trajectory distribution. To address this, we propose ChainFlow-VLA, which unifies causal generation and global refinement within a unified probabilistic framework. We formulate planning as a mixture over AR-induced modes and learn Vision-Language Model (VLM)-conditioned residual distributions over these modes. An autoregressive generator (Chain) produces a discrete set of causal trajectory modes, followed by a diffusion-based refiner (Flow) that leverages VLM hidden states as semantic priors to perform mode-conditioned correction in residual space while preserving causal structure. This straightforward conditioning seamlessly injects high-level scene understanding into fine-grained trajectory adjustments. Experiments demonstrate that ChainFlow-VLA achieves robust planning in ambiguous and long-tail scenarios, achieving a state-of-the-art score of 94.85 on the NAVSIM v1 leaderboard, matching human-level performance (94.8). Code will be available at https://github.com/AFARI-Research/ChainFlow-VLA.


### Autonomous Frontier-Based Exploration with VLM Guidance
**Authors**: Aarush Aitha, Avideh Zakhor

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23165v1](https://arxiv.org/pdf/2605.23165v1)

**Abstract**: Autonomous robotic exploration of unknown and hazardous environments, a long-standing challenge, can be significantly improved by leveraging the advanced reasoning of Vision-Language Models (VLMs). We introduce a novel exploration pipeline where a VLM performs high-level strategic decision-making, guiding a conventional low-level robotics control stack. At decision points, the robot generates a multimodal prompt with its current map and visual imagery of potential paths, or frontiers. The VLM analyzes this prompt to select the most promising frontier, replacing simple geometric heuristics with contextual spatial reasoning. This approach, validated in simulation across six indoor environments, improves map coverage by up to 24\% over existing methods. Our pipeline is lightweight, training-free, and easily transferable to any robot with standard sensors and an internet connection.


### Agentic-VLA: Efficient Online Adaptation for Vision-Language-Action Models
**Authors**: Ruofan Jin, Zaixi Zhang

**Published Date**: 2026-05-21

**Updated Date**: 2026-05-21

**PDF Url**: [2605.22896v1](https://arxiv.org/pdf/2605.22896v1)

**Abstract**: Vision-Language-Action (VLA) models have emerged as a promising paradigm for robotic manipulation by leveraging pre-trained vision-language representations. However, current VLA training methods suffer from two critical limitations: poor generalization to novel environments and low training efficiency requiring extensive demonstrations. We introduce Agentic-VLA, an agentic training framework that enables VLAs to efficiently adapt online through three key innovations: (1) Adaptive Reward Synthesis, which dynamically generates and adjusts reward functions based on the VLA's current capabilities and task complexity, decomposing complex tasks into learnable sub-goals for curriculum learning; (2) Language-Guided Exploration, where a critic model provides structured guidance for systematic exploration rather than random sampling; and (3) Experience Memory,which stores and retrieves task-relevant policy weights for warm-starting adaptation to similar tasks. We evaluate Agentic-VLA on the LIBERO benchmark, achieving substantial improvements: +12.3% on long-horizon tasks, +28.5% in 1-shot learning, and enabling cross-task transfer from 0% to 31.2% without task-specific demonstrations. Our framework also demonstrates 2.4x faster convergence compared to existing online adaptation methods. Beyond LIBERO, Agentic-VLA retains its advantage on the dual-arm RoboTwin 2.0 benchmark, including under its randomized Hard setting. These results establish Agentic-VLA as a significant step toward truly adaptive VLA systems capable of continuous learning in deployment.


### Learning Bilevel Policies over Symbolic World Models for Long-Horizon Planning
**Authors**: Dillon Z. Chen, Till Hofmann, Toryn Q. Klassen, Sheila A. McIlraith

**Published Date**: 2026-05-15

**Updated Date**: 2026-05-18

**PDF Url**: [2605.15975v2](https://arxiv.org/pdf/2605.15975v2)

**Abstract**: We tackle the challenge of building embodied AI agents that can reliably solve long-horizon planning problems. Imitation learning from demonstrations has shown itself to be effective in training robots to solve a diversity of complex tasks requiring fine motor control and manipulation over low-level (LL), continuous environments. Yet, it remains a difficult endeavour to generate long-horizon plans from imitation learning alone. In contrast, high-level (HL), symbolic abstractions facilitate efficient and interpretable long-horizon planning. We propose to combine the strengths of LL imitation learning for manipulation and control, and HL symbolic abstractions for long-horizon planning. We realise this idea via \emph{bilevel policies} of the form $(π^{\mathrm{hl}}, π^{\mathrm{ll}})$, consisting of a neural policy $π^{\mathrm{ll}}$ learned from LL demonstrations, and an HL symbolic policy $π^{\mathrm{hl}}$ that is constructed from symbolic abstractions of the LL demonstrations combined with inductive generalisation. We implement these ideas in the BISON system. Experiments on extended MetaWorld benchmarks demonstrate that BISON generalises to long horizons and problems with greater numbers of objects than those solved by VLA and end-to-end methods, and is more time and memory efficient in training and inference. Notably, when ignoring LL execution, BISON's HL policies can solve HL problems with 10,000 relevant objects in under a minute. Project page: https://dillonzchen.github.io/bison


### UAM: A Dual-Stream Perspective on Forgetting in VLA Training
**Authors**: Jianke Zhang, Yuanfei Luo, Yucheng Hu, Xiaoyu Chen, Yanjiang Guo, Ziyang Liu, Hongbin Xu, Tian Lan, Jianyu Chen

**Published Date**: 2026-05-15

**Updated Date**: 2026-05-18

**PDF Url**: [2605.15735v2](https://arxiv.org/pdf/2605.15735v2)

**Abstract**: Vision--language--action (VLA) models are typically built by fine-tuning a pretrained vision--language model (VLM) on action data. However, we show that this standard recipe systematically erodes the VLM's multimodal competence, a side effect we call the embodiment tax. But do VLAs have to forget? Inspired by the two-stream organization of biological vision, we trace this degradation to a structural bottleneck: current VLAs ask a single encoder to support both language-grounded semantics and control-relevant visual features, whereas biological vision separates recognition and visuomotor control into distinct pathways. Building on this view, we propose the Unified Action Model (UAM), which adds a parallel Dorsal Expert, an analog of the brain's dorsal pathway. To make the Dorsal Expert an effective second pathway and reduce the control-learning burden on the VLM, we initialize it from a pretrained generative model and train it with a mid-level reasoning objective that predicts visual dynamics. This design allows us to train the whole VLA end-to-end on action data alone: with no parameter freezing, no gradient stopping, and no auxiliary VL co-training, UAM retains over $95\%$ of the underlying VLM's multimodal capability and at the same time achieves the highest average success rate among baselines on a variety of manipulation tasks that probe out-of-distribution generalization, including unseen objects, novel object--target compositions, and instruction variation. Together, these results suggest that semantic preservation in VLAs can emerge from architectural separation itself, rather than being enforced by frozen weights or auxiliary data replay, and that this preserved semantic capability can naturally transfer from VLMs to semantic generalization in actions.


### PhysBrain 1.0 Technical Report
**Authors**: Shijie Lian, Bin Yu, Xiaopeng Lin, Changti Wu, Hang Yuan, Xiaolin Hu, Zhaolong Shen, Yuzhuo Miao, Haishan Liu, Yuxuan Tian, Yukun Shi, Cong Huang, Kai Chen

**Published Date**: 2026-05-14

**Updated Date**: 2026-05-14

**PDF Url**: [2605.15298v1](https://arxiv.org/pdf/2605.15298v1)

**Abstract**: Vision-language-action models have advanced rapidly, but robot trajectories alone provide limited coverage for learning broad physical understanding. PhysBrain 1.0 studies a complementary route: converting large-scale human egocentric video into structured physical commonsense supervision before robot adaptation. Our data engine extracts scene elements, spatial dynamics, action execution, and depth-aware relations, then turns them into question-answer supervision for training PhysBrain VLMs. The resulting physical priors are further transferred to VLA policies through a capability-preserving and language-sensitive adaptation design. Across multimodal QA benchmarks and embodied control benchmarks, including ERQA, PhysBench, SimplerEnv-WidowX, LIBERO, and RoboCasa, PhysBrain 1.0 achieves SOTA results and shows especially strong out-of-domain performance on SimplerEnv. These results suggest that scaling physical commonsense from human interaction video can provide an effective bridge from multimodal understanding to robot action.


## Agent
### CHRONOS: Temporally-Aware Multi-Agent Coordination for Evolving Data Marketplaces
**Authors**: Joydeep Chandra

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23887v1](https://arxiv.org/pdf/2605.23887v1)

**Abstract**: Temporal knowledge-graph data marketplaces face three coupled failures in static designs: stale hybrid index shortcuts reduce recall as edges evolve, stationary Shapley pricing misattributes value after distribution shifts, and uncoordinated agents over-consume a shared differential-privacy budget. We present CHRONOS, a three-layer architecture providing a unified treatment of these challenges with explicit public and private separation. Layer one applies neural-ODE temporal decay to shortcut edges, providing a per-query expected recall-loss bound of Big-O of Pq lambda delta t, with a monotone-envelope guarantee reducing bound looseness to 1.8 to 3.2 times observed loss. Layer two conditions Shapley valuation on detected changepoints and provides finite-sample error guarantees under noise. Layer three uses EXP3-IX to achieve Big-O of the square root of T log T regret while enforcing epsilon and delta differential privacy via moments accounting. CHRONOS releases a privatized affinity matrix per epoch using the Gaussian mechanism; all retrieval and ranking are post-processing, incurring no extra privacy cost. We provide multi-epoch settlement, scalability analysis for 500 sellers, and comparisons against accelerated baselines. Across four benchmarks, CHRONOS shows 0.937 recall at ten, 2.74 queries per second, 161 ms latency, and total epsilon of 4.25 at delta of 10 to the power of negative 6 under zCDP composition. These results indicate a competitive operating point. A limitation is that at this privacy level, released valuations remain noise-dominated; utility derives primarily from public index routing and adaptive scheduling driven by low-sensitivity statistics.


### Agentic Proving for Program Verification
**Authors**: Alessandro Sosso, Akhil Arora, Bas Spitters

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23772v1](https://arxiv.org/pdf/2605.23772v1)

**Abstract**: Agentic systems have recently emerged as state-of-the-art approaches for automated theorem proving in formal mathematics. To assess how far these capabilities extend to program verification, we evaluate Claude Code in an agentic proving framework on CLEVER, a Lean 4 benchmark for verifiable code generation. Our results show that Claude generates arguably valid specifications for 98.8% of problems (with 81.3% also accepted by CLEVER's isomorphism-based scoring on the correct portion of the benchmark), certifies implementations against correct ground-truth specifications for 87.5% of problems, and reaches a 98.1% success rate on the end-to-end program generation and verification pipeline over entries with self-consistent premises. Across all stages, Claude further provides high-quality feedback on its own attempts (as confirmed under manual review), identifying underlying causes of failure and lingering bugs in the dataset. These findings highlight a growing mismatch between the difficulty of existing program verification benchmarks and the capabilities of modern agentic provers, and point to the need for more rigorous, bug-resilient evaluation methodologies, and in particular for alternatives to isomorphism-based scoring of generated specifications. More broadly, our results provide empirical evidence that tight compiler-in-the-loop agentic paradigms are currently the most effective approach for foundational program verification.


### PhotoFlow: Agentic 3D Virtual Photography Missions
**Authors**: Jiarui Guo, Haojia Wei, Yiming Zhang, Yifei Liu, Yuning Gong, Hongjie Zhang, Xue Yang, Zhihang Zhong

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23771v1](https://arxiv.org/pdf/2605.23771v1)

**Abstract**: Virtual photography asks an agent to enter a prepared 3D scene with no preselected camera pose or reference image, infer a suitable shot from scene information and a language intent, choose executable camera parameters, and render the final photograph. Recent progress in vision-language models makes this kind of spatial agent increasingly plausible, but the task stresses two capabilities that remain hard to evaluate together: complex 3D spatial understanding and abstract aesthetic judgment. We introduce PhotoFlow, a Director-Reviewer-Reflector agent for closed-loop camera search. The Director builds a soft photographic blueprint and proposes diverse candidate cameras; the Reviewer combines rule checks, visual critique, and pairwise incumbent selection; and the Reflector converts failures into region memory, dead-zone suppression, and high-explore relocation. We also introduce VPhotoBench, a benchmark of 47 open-license Blender scenes and 141 language-conditioned photography missions spanning subject placement, relational composition, and atmosphere/style. On held-out experiments, PhotoFlow achieves the strongest external quality-alignment composite and success rate among one-shot prediction, single-chain reflection, anchor-bank selection, and random search under a six-round rendering budget. To our knowledge, this is the first work to make language-conditioned virtual photography in arbitrary Blender scenes an executable agent task, and our results show that an LLM-centered spatial agent can already produce strong photographs in a setting designed to challenge both 3D reasoning and aesthetic choice.


### LLM-driven design of physics-constrained constitutive models: two agents are better than one
**Authors**: Marius Tacke, Matthias Busch, Kian Abdolazizi, Jonas Eichinger, Kevin Linka, Roland Aydin, Christian Cyron

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23754v1](https://arxiv.org/pdf/2605.23754v1)

**Abstract**: Developing constitutive models that capture how materials deform under load traditionally requires years of specialized expertise in continuum mechanics, machine learning, and scientific programming. Large language models (LLMs) have recently been shown to lower this barrier by generating constitutive models on demand, but existing single-agent pipelines lack systematic checks that the resulting models respect fundamental physical laws. To close this gap, we introduce the first multi-agent LLM-driven approach for constitutive model generation: a Creator agent proposes a model tailored to the data, while an Inspector agent critically audits each proposal against nine physical constraints and returns it for refinement whenever a violation is detected. We demonstrate this concept with constitutive artificial neural networks (CANNs) and benchmark it on brain tissue, experimental rubber, and synthetic rubber, using two different LLM backbones (Claude Opus 4.7 and Kimi K2.5). Adding the Inspector raises the share of exported models that truly satisfy all physical constraints from 91% to a perfect 100% for Opus and from 37% to 56% for Kimi, while preserving near-baseline accuracy and remarkable generalization to unseen loading paths. In combination, the generated models are physically valid, highly accurate, and extrapolate reliably beyond the training data - properties that together make them directly usable in practice. Separating generation from inspection thus turns LLM-driven constitutive modeling into a genuinely trustworthy process. The paradigm is deliberately technique-agnostic and scales automatically with advances in LLM capability, opening a promising path toward automated, physics-aware model discovery.


### SeedER: Seed-and-Expand Retrieval from Knowledge Graphs
**Authors**: Hamed Shirzad, Frederik Wenkel, Dominique Beaini, Danica J. Sutherland, Emmanuel Noutahi

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23753v1](https://arxiv.org/pdf/2605.23753v1)

**Abstract**: Knowledge graphs (KGs) offer a rich representation for relational knowledge, but their irregular structure makes retrieval challenging: ego-graph expansion grows rapidly, and dense embedding methods struggle with multi-hop compositional queries. Existing agent-based graph exploration approaches, while expressive, are often too expensive for large-scale retrieval. We introduce SeedER (Seed-and-Expand Retrieval), a retrieval framework that explicitly leverages KG structure through iterative, low-cost expansion. SeedER first seeds a compact set of core nodes using lightweight dense and entity-based retrieval, then selectively expands this set via a learned graph-aware policy trained with reinforcement learning. This design decomposes global reasoning into reusable local decisions, enabling efficient discovery of query-relevant nodes while tightly controlling expansion cost. We show theoretical limitations of dense retrieval on compositional graph queries, and establish advantages of SeedER from both compositional generalization and graph-constrained submodular optimization perspectives. Empirically, SeedER substantially improves recall with compact candidate sets over strong dense and graph-augmented baselines, making it an effective first-stage retriever for knowledge-intensive reasoning systems.


### MemAudit: Post-hoc Auditing of Poisoned Agent Memory via Causal Attribution and Structural Anomaly Detection
**Authors**: Zhewen Tan, Yilun Yao, Huiyan Jin, Wenhan Yu, Guoan Wang, Mengyuan Fan, liang lu, Feng Liu, Xiangzheng Zhang, Duohe Ma, Tong Yang, Lin Sun

**Published Date**: 2026-05-22

**Updated Date**: 2026-05-22

**PDF Url**: [2605.23723v1](https://arxiv.org/pdf/2605.23723v1)

**Abstract**: Large language model agents increasingly rely on persistent memory to store past interactions, retrieve relevant demonstrations, and improve long-horizon task execution. However, this memory mechanism also creates a practical security vulnerability: an adversarial user may inject malicious records into the agent's memory through ordinary interaction, and these records can later be retrieved to steer the agent's reasoning and actions. Existing defenses primarily focus on online intervention, such as prompt filtering or output blocking, but they do not address the post-hoc question of which stored memories are responsible after harmful behavior has already been observed. We propose \textbf{MemAudit}, a post-hoc causal memory auditing framework for memory-augmented LLM agents. The framework combines two complementary signals: (1) a counterfactual memory influence score that measures each memory's causal contribution to harmful outputs, and (2) a memory consistency graph that identifies structurally anomalous memories within the broader memory store. We evaluate MemAudit against MINJA, a query-only memory injection attack in which malicious records are generated and stored through normal agent interactions rather than direct memory-bank modification. Across both QA and reasoning-agent settings, MemAudit substantially reduces attack success rates under realistic post-hoc auditing scenarios. The results show that QA attack success is reduced from $70\%$ to $0\%$, while RAP attack success drops from $83.3\%$ to $0\%$.


