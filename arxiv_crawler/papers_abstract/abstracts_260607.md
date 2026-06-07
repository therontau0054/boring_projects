# Abstracts of Papers

## World Model
### HANDOFF: Humanoid Agentic Task-Space Whole-Body Control via Distilled Complementary Teachers
**Authors**: Lizhi Yang, Junheng Li, Nehar Poddar, Yiling Hou, Gio Huh, Robert Griffin, Georgia Gkioxari, Aaron Ames

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06493v1](https://arxiv.org/pdf/2606.06493v1)

**Abstract**: For a humanoid robot to be deployed in the real world, the choice of command space (i.e., the interface between task planning and whole-body control) is crucial. Existing whole-body controllers typically demand dense kinematic or spatial references that planners struggle to synthesize from task semantics. We instead propose a compact, explicit interface that is intuitive, general, modular, and expressive enough for diverse manipulation skills. To this end, we introduce HANDOFF, a single humanoid whole-body controller that follows this interface and is distilled via multi-teacher KL distillation under a context-conditioned gating scheme into a mixture-of-experts student from three complementary specialists: whole-body motion tracking with safety-filtered data, locomotion, and fall-recovery. On the Unitree G1, HANDOFF matches state-of-the-art velocity tracking and offers one of the largest robust manipulation workspaces. We further demonstrate hardware feasibility through multiple natural-language-driven task roll-outs, powered by a VLM-driven agentic planner with no task-specific data or controller fine-tuning.


### Code2LoRA: Hypernetwork-Generated Adapters for Code Language Models under Software Evolution
**Authors**: Liliana Hotsko, Yinxi Li, Yuntian Deng, Pengyu Nie

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06492v1](https://arxiv.org/pdf/2606.06492v1)

**Abstract**: Code language models need repository-level context to resolve imports, APIs, and project conventions. Existing methods inject this knowledge as long inputs (retrieved through RAG or dependency analysis) or through per-repository fine-tuning and LoRA -- costly at repository scale and brittle to evolving codebases. We introduce Code2LoRA, a hypernetwork framework that generates repository-specific LoRA adapters, effectively injecting repository knowledge with zero inference-time token overhead. Code2LoRA supports two usage scenarios: Code2LoRA-Static converts a single repository snapshot into an adapter, suitable for comprehension of stable codebases; while Code2LoRA-Evo maintains an adapter backed by a GRU hidden state updated per code diff, suitable for active development of evolving codebases. To evaluate Code2LoRA against parameter-efficient fine-tuning baselines, we build RepoPeftBench, a benchmark of 604 Python repositories with two tracks: a static track with 40K training and 12K test assertion-completion tasks, and an evolution track with 215K commit-derived training and 87K commit-derived test tasks. On the static track, Code2LoRA-Static achieves 63.8% cross-repo and 66.2% in-repo exact match, matching the per-repository LoRA upper bound; on the evolution track, Code2LoRA-Evo achieves 60.3% cross-repo exact match (+5.2 pp over a single shared LoRA). Code2LoRA's code can be found at https://anonymous.4open.science/r/code2lora-6857; the model checkpoints and RepoPeftBench datasets can be found at https://huggingface.co/code2lora.


### TempoVLA: Learning Speed-Controllable Vision-Language-Action Policies
**Authors**: Dong Jing, Jingchen Nie, Tianqi Zhang, Jiaqi Liu, Huaxiu Yao, Zhiwu Lu, Mingyu Ding

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06491v1](https://arxiv.org/pdf/2606.06491v1)

**Abstract**: Robot manipulation alternates between low-risk transit phases that call for fast execution and high-risk contact stages that demand slow, precise motion. Yet existing Vision-Language-Action models (VLAs) only inherit a single fixed speed from training demonstrations. Prior efforts to accelerate VLAs through model compression, KV-cache reuse, or reinforcement learning only shift the policy from one fixed speed to another, and leave deceleration almost unexplored. We observe that the magnitude of each predicted action already governs how fast the robot moves, opening a direct route to controllable execution speed. We turn this observation into TempoVLA, a single VLA whose execution speed is controlled by an explicit condition. TempoVLA combines two coupled components. (1) A data-side Variable-Speed Trajectory Augmentation (VSTA) that re-times demonstration to any target speed by merging or splitting actions while preserving its motion semantics. (2) A model-side conditioning mechanism that feeds the speed to the policy. Statistics show that VSTA reaches the requested speed with negligible motion error. Experiments in simulation and on real-world tasks demonstrate that TempoVLA achieves flexible speed control in both directions, while VSTA additionally boosts the default $1\times$ performance via better data utilization. Furthermore, by cooperating with a large multimodal model, TempoVLA realizes dynamic speed control, accelerating through low-risk phases and decelerating for high-risk ones.


### Operation-Guided Progressive Human-to-AI Text Transformation Benchmark for Multi-Granularity AI-Text Detection
**Authors**: Sondos Mahmoud Bsharat, Jiacheng Liu, Xiaohan Zhao, Tianjun Yao, Xinyi Shang, Yi Tang, Jiacheng Cui, Ahmed Elhagry, Salwa K. Al Khatib, Hao Li, Salman Khan, Zhiqiang Shen

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06481v1](https://arxiv.org/pdf/2606.06481v1)

**Abstract**: As AI writing assistants become increasingly integrated into real-world drafting and revision workflows, many documents are no longer purely human-written or AI-generated, but instead result from progressive human-AI co-editing. However, existing AI-text detection benchmarks largely focus on final outputs and provide limited understanding of how AI authorship signals emerge, accumulate, or disappear throughout the revision process. We introduce OpAI-Bench, an operation-guided benchmark for studying progressive human-to-AI text transformation across document, sentence, token, and span granularities. Starting from human-written documents, OpAI-Bench constructs nine sequentially revised versions for each sample under predefined AI coverage levels and five representative AI edit operations, covering four domains while preserving complete authorship provenance at multiple granularities. The benchmark supports comprehensive evaluation with 8 document-level detectors, 7 sentence-level detectors, and 2 fine-grained token/span-level detectors. Experiments reveal that AI-text detectability is governed not only by the proportion of AI-edited content, but also by edit operation, domain, and cumulative revision history. Interestingly, we notice that mixed-authorship intermediate versions are often harder to detect than both fully human and heavily AI-edited endpoints, exposing non-monotonic detection patterns missed by existing benchmarks. OpAI-Bench provides a controlled testbed for analyzing whether, when, and how AI-assisted writing becomes detectable under realistic progressive editing scenarios. Our code and benchmark are available at https://github.com/VILA-Lab/OpAI-Bench.


### DNQ: Deep Nash Q-Network for Partially Observable n-Player Games
**Authors**: Qintong Xie, Edward Koh, Xavier Cadet, Peter Chin

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06480v1](https://arxiv.org/pdf/2606.06480v1)

**Abstract**: Many real-world competitive systems require multiple decision-makers to act simultaneously under shared constraints, limited information, and repeated interaction, as in auctions, resource allocation, and security competition. We study multi-turn simultaneous bidding as a controlled testbed for such problems and propose DNQ, a solver-in-the-loop equilibrium supervision framework for training bidding agents. DNQ alternates between trajectory collection, critic-based payoff estimation, equilibrium computation, and policy imitation. At each visited state, a shared critic predicts either pairwise payoff matrices or an exact N-player payoff tensor, an external solver computes equilibrium strategies, and the agents are trained by minimizing the KL divergence between their masked policies and the solver-derived equilibrium targets. We focus on a scalable pairwise formulation that greatly reduces equilibrium-solving cost and training time compared with the exact formulation, while the shared critic amortizes payoff learning across agents and states. Experiments compare the pairwise and exact variants using critic loss, policy entropy, bidding resource usage, and training cost, showing that the pairwise method scales to larger numbers of agents, whereas the exact method becomes computationally impractical as the joint game grows. These results illustrate the trade-off between strategic fidelity and scalability in repeated competitive environments.


### Pretraining Recurrent Networks without Recurrence
**Authors**: Akarsh Kumar, Phillip Isola

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06479v1](https://arxiv.org/pdf/2606.06479v1)

**Abstract**: Training recurrent neural networks (RNNs) requires assigning credit across long sequences of computations. Standard backpropagation through time (BPTT) addresses this problem poorly: it is sequential in time, limiting parallelism, and suffers from vanishing or exploding gradients, making long-range associations difficult to learn. We propose Supervised Memory Training (SMT), a method for training nonlinear RNNs that sidesteps recurrent credit propagation entirely by reducing RNN training to supervised learning on one-step memory transition labels $(m_t, x_{t+1}) \rightarrow m_{t+1}$. SMT acquires these memory labels by training a Transformer-based encoder on a predictive state objective--retaining only information from the past necessary to predict the future. By decoupling what to remember from how to update memory, SMT enables time-parallel RNN training with a stable $O(1)$ length gradient path between any two tokens--without ever unrolling the RNN. We find that SMT outperforms BPTT when pretraining various RNN architectures on tasks like language modeling and pixel sequence modeling. SMT enables nonlinear RNNs to better capture long-range dependencies and train in parallel, potentially unlocking the scaling of models that build temporal abstractions of past experience.


## Generation
### RREDCoT: Segment-Level Reward Redistribution for Reasoning Models
**Authors**: Mykyta Ielanskyi, Kajetan Schweighofer, Lukas Aichberger, Sepp Hochreiter

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06475v1](https://arxiv.org/pdf/2606.06475v1)

**Abstract**: Recent advancements in reasoning language models have been driven by Reinforcement Learning (RL) fine-tuning. Most often, these rely on the Group Relative Policy Optimization (GRPO) algorithm or modifications thereof to steer the models to produce Chain-of-Thought (CoT) traces. The final answer can only be verified, and the reward assigned, after the CoT trace is complete, making it a delayed reward problem. GRPO and its modifications correspond to Monte Carlo methods in standard RL, which are known to suffer from high variance. A possible solution to this problem is the redistribution of rewards through credit assignment, where segments of the CoT trace that are important for arriving at the desirable solution are emphasized by assigning a higher reward. While Monte Carlo sampling can be used to provide an unbiased estimate of intermediate state values, its computational overhead makes it unsuitable for train-time credit assignment in long contexts at high granularity. We introduce RREDCoT (Reward REDistribution for Chain of Thoughts), which utilizes the model itself to approximate the optimal reward redistribution without additional generation. We investigate the advantages of our method compared to MC sampling and several attribution methods. We further analyze several aspects relevant to the construction of the redistribution such as segmentation of CoT traces and state value estimation.


### Self-Augmenting Retrieval for Diffusion Language Models
**Authors**: Paul Jünger, Justin Lovelace, Linxi Zhao, Dongyoung Go, Kilian Q. Weinberger

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06474v1](https://arxiv.org/pdf/2606.06474v1)

**Abstract**: Discrete diffusion language models generate text by iteratively denoising an entire response in parallel. At each step, they predict tentative tokens for every masked position, committing the confident predictions to the output and discarding the unconfident ones. We show that the discarded tokens are in fact a useful lookahead signal for retrieval-augmented generation: even low-confidence tokens often surface salient entities early in the denoising trajectory, enabling retrieval of stronger evidence before the output is finalized. We exploit this through Self-Augmenting Retrieval for Diffusion Language Models (SARDI), a dynamic RAG framework that uses these lookahead tokens to guide retrieval during denoising. SARDI is training-free, retriever-agnostic, and applicable to any reasoning-capable discrete diffusion language model. Across five multi-hop QA benchmarks, SARDI outperforms current training-free diffusion and autoregressive retrieval baselines at up to $8\times$ higher throughput.


### MLEvolve: A Self-Evolving Framework for Automated Machine Learning Algorithm Discovery
**Authors**: Shangheng Du, Xiangchao Yan, Jinxin Shi, Zongsheng Cao, Shiyang Feng, Zichen Liang, Boyuan Sun, Tianshuo Peng, Yifan Zhou, Xin Li, Jie Zhou, Liang He, Bo Zhang, Lei Bai

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06473v1](https://arxiv.org/pdf/2606.06473v1)

**Abstract**: Large language model (LLM) agents are increasingly applied to long-horizon tasks such as scientific discovery and machine learning engineering (MLE), where sustained self-evolution becomes a key capability. However, existing MLE agents suffer from inter-branch information isolation, memoryless search, and lack of hierarchical control, which together hinder long-horizon optimization. We present MLEvolve, an LLM-based self-evolving multi-agent framework for end-to-end machine learning algorithm discovery. By extending tree search to Progressive MCGS, MLEvolve enables cross-branch information flow through graph-based reference edges and gradually shifts the search from broad exploration to focused exploitation with an entropy-inspired progressive schedule. To allow the agent to evolve with accumulated experience, we introduce Retrospective Memory, which combines a cold-start domain knowledge base with a dynamic global memory for task-specific experience retrieval and reuse. For stable long-horizon iteration, we further decouple strategic planning from code generation with adaptive coding modes. Evaluation on MLE-Bench shows that MLEvolve achieves state-of-the-art performance across multiple dimensions including average medal rate and valid submission rate under a 12-hour budget (half the standard runtime). Moreover, MLEvolve also outperforms specialized algorithm discovery methods including AlphaEvolve on mathematical algorithm optimization tasks, demonstrating strong cross-domain generalization. Our code is available at https://github.com/InternScience/MLEvolve.


### How abundant are good interpolators?
**Authors**: August Y. Chen, Ahmed El Alaoui

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06469v1](https://arxiv.org/pdf/2606.06469v1)

**Abstract**: Let $S$ be the set of unit norm linear classifiers $θ\in \mathbb{R}^d$ which correctly classify every point of a labeled dataset $(X_i,y_i)_{i=1}^n$, $X_i \in \mathbb{R}^d$, $y_i \in \{-1,+1\}$, with a possibly negative margin $κ$ fixed in advance. Under two natural data-generating distributions of the $(X,y)$ pairs -- a Gaussian mixture model and a logistic model with Gaussian features -- and in the proportional regime $n/d \to α$ with small enough $α$, we establish a large deviation principle on the event that a point $θ$ chosen uniformly at random from $S$ achieves a given generalization error, with high probability over the choice of the data. The associated large deviation rate function is deterministic and describes the proportion, at the exponential scale in $d$, of interpolating classifiers having a given desired performance. As a consequence, we establish the following concentration phenomenon: all but an exponentially small fraction of interpolating classifiers have approximately the same generalization performance given by the unique maximizer of this rate function.
  We numerically compare this maximizer to the performance of empirical risk minimization by gradient descent and to the performance of a natural linear program, both finding a point in $S$, and deduce that in the overparametrized regime of small $α$, these efficient procedures outperform the vast majority of interpolators, pointing to their nontrivial benign overfitting in this setting.


### Goedel-Architect: Streamlining Formal Theorem Proving with Blueprint Generation and Refinement
**Authors**: Jui-Hui Chung, Ziyang Cai, Zihao Li, Qishuo Yin, Rohit Agarwal, Simon Park, Rodrigo Porto, Narutatsu Ri, Ziran Yang, Shange Tang, Xingyu Dang, Hongzhou Lin, Mengdi Wang, Danqi Chen, Chi Jin, Liam H Fowl, Sanjeev Arora

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06468v1](https://arxiv.org/pdf/2606.06468v1)

**Abstract**: We introduce Goedel-Architect, an agentic framework for formal theorem proving in Lean 4 centered on blueprint generation and refinement. A blueprint is a dependency graph of definitions and lemmas that builds up to the main theorem. First, Goedel-Architect generates a blueprint of formally stated definitions and lemmas, along with declared dependencies. This blueprint is optionally guided by a natural language proof. Then, a tool-equipped Lean prover component closes each open lemma node in parallel using relevant dependencies. Failed lemmas in turn drive refinement of the global blueprint. This strategy contrasts with other mainstream approaches which use recursive lemma decomposition, and can inefficiently loop on dead-end strategies. Using the open-weight DeepSeek-V4-Flash (284B-A13B) as the backbone, Goedel-Architect attains 99.2% pass@1 on MiniF2F-test and 75.6% pass@1 on PutnamBench. With an optional natural-language proof seeding the initial blueprint on the harder problems, we additionally close the remaining two MiniF2F-test problems (reaching 100%), lift PutnamBench to 88.8% (597/672), and solve 4/6 on IMO 2025, 11/12 on Putnam 2025, and 3/6 on USAMO 2026. This represents state-of-the-art performance for an open-source pipeline at a price point up to 500x less than comparable open-source pipelines.


### You Only Index Once: Cross-Layer Sparse Attention with Shared Routing
**Authors**: Yutao Sun, Yanqi Zhang, Li Dong, Jianyong Wang, Furu Wei

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06467v1](https://arxiv.org/pdf/2606.06467v1)

**Abstract**: Long-context inference in modern LLMs is increasingly constrained by decoding efficiency, especially in reasoning-heavy settings where models generate long intermediate chains of thought. Existing sparse attention methods often face a practical efficiency-quality trade-off. Structured block sparse methods typically provide stronger acceleration but incur noticeable quality loss, while token sparse methods are usually more accurate yet deliver limited end-to-end speedup because top-k routing over the full cache remains expensive. In this work, we propose cross-layer sparse attention (CLSA), which is built on top of KV-sharing architectures such as YOCO. The core idea is to share not only the KV cache across cross-decoder layers, but also the routing index. A single indexer computes token-level top-k selection once and reuses the resulting index across layers, thereby preserving the fine-grained selectivity of token sparse attention while amortizing the routing overhead. The resulting architecture improves all major inference bottlenecks jointly, including pre-filling, KV-cache storage, and long-context decoding. Experiments across short-context and long-context benchmarks show that CLSA is both accurate and efficient, achieving up to 7.6x decoding speedup and 17.1x overall throughput improvement at 128K context. These results suggest a more complete architectural solution for long-context LLMs that jointly advances model quality and inference efficiency.


## VLA
### MPCoT: Reward-Guided Multi-Path Latent Reasoning for Test-Time Scalable Vision-Language-Action
**Authors**: Boyang Zhang, Lianlei Shan

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06245v1](https://arxiv.org/pdf/2606.06245v1)

**Abstract**: Vision-Language-Action (VLA) policies remain brittle in long-horizon and high-uncertainty control, where one-pass action decoding provides limited inference-time deliberation. Explicit chain-of-thought can increase reasoning depth, but introduces token latency and an indirect text-to-action interface. We propose MPCoT, a reward-guided multi-path latent reasoning framework that initializes $M$ hypotheses, refines them for K weight-tied steps, and softly aggregates them before action decoding. A training-only path-preference objective evaluates candidate action branches with expert-action consistency, world-model/VLM-based progress, and success feedback to align the latent path scorer with downstream execution quality. MPCoT preserves the original 8-step action interface, generates zero reasoning tokens, and exposes configurable inference controls (K,M). Under matched protocols on LIBERO and CALVIN, MPCoT improves long-horizon performance, with ablations confirming depth-width effects, confidence-weighted aggregation, and reward-guided path supervision.


### WorldFly: A World-Model-Based Vision-Language-Action Model for UAV Navigation
**Authors**: Shengtao Zheng, Kai Li, Weichen Zhang, Yu Meng, Chen Gao, Xinlei Chen, Yong Li, Xiao-Ping Zhang

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06147v1](https://arxiv.org/pdf/2606.06147v1)

**Abstract**: End-to-end Vision-Language-Action (VLA) models have shown promise in UAV navigation. However, existing approaches typically rely on historical observations to directly predict actions, often struggling in dense urban environments where severe occlusions and sharp turns result in drastic viewpoint transitions. We argue that the ability to "imagine" future states -- inherent in World Models -- is critical for robust decision-making under such partial observability. To address this, we construct a challenging Urban Canyon Traversal Benchmark, specifically designed to evaluate spatial understanding in scenarios characterized by severe occlusions and drastic viewpoint transitions. To this end, we propose WorldFly, a novel world-model-based VLA framework that employs a dual-branch coupled flow matching mechanism to jointly generate future video predictions and navigation actions, thereby explicitly guiding the agent's policy via spatial imagination. Extensive evaluations on our benchmark demonstrate that WorldFly outperforms other baselines, particularly in unseen environments, validating the effectiveness of integrating world models into embodied aerial agents.


### World-Language-Action Model for Unified World Modeling, Language Reasoning, and Action Synthesis
**Authors**: Yi Yang, Zhihong Liu, Siqi Kou, Yiyang Chen, Yanzhe Hu, Jianbo Zhou, Boyuan Zhao, Zhijie Wei, Xiao Xia, Xueqi Li, Pengfei Liu, Zhijie Deng

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.05979v1](https://arxiv.org/pdf/2606.05979v1)

**Abstract**: We propose world-language-action (WLA) models as a new class of embodied foundation models. WLA takes textual instructions, images, and robot states as inputs to jointly predict textual subtasks, subgoal images, and robot actions, conjoining the \emph{world modeling interface} to learn from extensive egocentric videos as in the world-action model (WAM) and the \emph{language reasoning} capacities to solve complex long-horizon tasks as in vision-language-action (VLA) models. At the core of WLA lies an \emph{autoregressive (AR)} Transformer backbone, instead of a bidirectional diffusion Transformer as in WAMs, to predict the \emph{next state}, comprising the \emph{semantic-level} textual intention and complementary \emph{fine-grained} physical dynamics. The physical dynamics are supervised by the world modeling objective based on a dedicated World Expert, and are leveraged to ease the characterization of the state-action correlation for the Action Expert. WLA leverages meta-queries to make the world prediction \emph{implicitly} impact the action generation so that the former can be disabled during inference. The world prediction can also be activated to enable test-time scaling for improved robot control. Our WLA-0 prototype, with 2B active parameters, achieves 40 ms per inference on an NVIDIA RTX 5090. Evaluations across simulated and real-world environments demonstrate that WLA-0 achieves state-of-the-art multi-task and long-horizon learning abilities, e.g., 92.94\% success rate on RoboTwin2.0 Clean and 56.5\% success rate on RMBench. WLA-0 also holds the promise to learn novel tasks directly from \emph{cross-embodiment robot videos} without action annotations.


### DRIFT: A Residual Flow Adapter for Decoding Continuous Outputs in Vision-Language Models
**Authors**: Zhuoming Liu, Jinhong Lin, Kwan Man Cheng, Lin Zhang, Shayok Bagchi, Yin Li

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.05758v1](https://arxiv.org/pdf/2606.05758v1)

**Abstract**: Many modern vision-language models (VLMs) build on autoregressive decoding of discrete tokens. While text-based output interfaces enable scalable pretraining and strong zero-shot generalization across diverse tasks, they are poorly suited for problems that require precise continuous outputs, such as localizing temporal boundaries of events or generating robotic control actions. To address this challenge, we propose DRIFT, a general framework for adapting pretrained VLMs to continuous decoding tasks. DRIFT combines a base predictor, which provides a coarse estimate of the target output, with a generative refinement module based on flow matching that iteratively improves the prediction. This residual formulation transforms the generative modeling problem from learning a global output distribution to modeling a localized residual distribution around a strong prior, substantially simplifying optimization. We evaluate DRIFT on both perception and planning tasks, including visual grounding and robotic control. Across multiple tasks and architectures spanning MLLMs, VLAs, and WAMs, DRIFT consistently outperforms a strong set of regression- and generative-based solutions.


### Let It Be Simple: One-Step Action Generation for Vision-Language-Action Models
**Authors**: Yitong Chen, Shiduo Zhang, Jingjing Gong, Xipeng Qiu

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.05737v1](https://arxiv.org/pdf/2606.05737v1)

**Abstract**: Diffusion-based vision-language-action (VLA) models often inherit the image-generation view: actions are generated by iterative denoising. We argue that VLA action generation has a different condition-target structure: the policy is conditioned on rich observations, language, and state, but predicts only a compact, low-dimensional action chunk. Under this asymmetry, strong one-step action generation should not necessarily require the advanced one-step methods developed for image synthesis. We keep standard velocity prediction and add no teacher model, distillation stage, or auxiliary objective; in our main recipe, we simply bias the training time distribution toward high-noise states. We first isolate the effect in a controlled MNIST grid-to-sequence task, then test it with extensive robot-policy experiments. Across standard LIBERO, LIBERO-Plus, and LIBERO-Pro, one-step policies trained with high-noise biased schedules generally match ten-step decoding under the same recipe, and on standard LIBERO can exceed ten-step policies trained with a uniform time distribution. A real-robot bimanual YAM RSS evaluation gives a small-sample cross-architecture check of the same sampler trend. On a 1.4B VLM model with a 30M action head, one-step decoding reaches 95.6\% on LIBERO-Long. These results show that strong one-step VLA action generation can emerge from standard diffusion training, without importing the full few-step diffusion machinery developed for image generation.


### Output Type Before Quality: A Standards-Derived XAI Admissibility Rubric for Autonomous-Driving Safety
**Authors**: Abhinaw Priyadershi, Mandar Pitale, Jelena Frtunikj, Maria Spence

**Published Date**: 2026-06-03

**Updated Date**: 2026-06-03

**PDF Url**: [2606.05461v1](https://arxiv.org/pdf/2606.05461v1)

**Abstract**: Safety standards for ML-based autonomous driving specify the kind of evidence an assurance case must contain (directed cause-and-effect chains, quantified interventional effects, named root-cause variables), yet the XAI literature is organised by output type and technique family (saliency maps, feature attribution, counterfactuals, causal graphs, language traces). SHAP, the most-recommended ADS XAI method, returns a ranked feature list that no implementation effort can convert into a directed chain (Fig.1). We name this mismatch the evidence-type gap.
  From AMLAS, ISO 26262, ISO21448, ISO/PAS 8800 we derive 19 testable evidentiary criteria across 7 lifecycle stages with representative clause-cited derivations and score six XAI method classes structurally.
  Causal XAI emerges as structurally required to satisfy the derived criteria at three stages: hazard identification (+62% rubric gap), incident investigation (+50%), and data management (+50%); the verdict set is stable across thresholds T in (0%, 50%]$ and survives a worst-case single-cell flip down to T = 25%. At the remaining four stages, correlational or language-based methods are comparable or sufficient. The rubric identifies structural admissibility (necessary but not sufficient for compliance): an admissible method's specific output content may still be wrong, and validating that fidelity (the edges a fitted SCM produces, the cause a trace names) is the open assurance challenge. A single-VLA proof of concept on 1,996 real-world driving clips (79,840 rows, ten splits) is consistent with each method's observed output type matching its rubric prediction. XAI method selection for ADS safety assurance should be driven by lifecycle-stage evidence demand, not by method popularity.


## Agent
### Benchmark Everything Everywhere All at Once
**Authors**: Shiyun Xiong, Dongming Wu, Peiwen Sun, Yuang Ai, Bokang Yang, Wencheng Han, Xiao-Hui Li, Xiangyu Yue

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06462v1](https://arxiv.org/pdf/2606.06462v1)

**Abstract**: Benchmarks are fundamental for evaluating and advancing LLMs and MLLMs by providing standardized and explicit measures of performance. However, their construction is labor-intensive and hard to reuse, raising concerns about sustainability and scalability. Moreover, existing benchmarks often quickly reach performance saturation after their release, resulting in insufficient discrimination among state-of-the-art models. To address these challenges, we introduce Benchmark Agent, a fully autonomous agentic system designed for benchmark building. Our framework orchestrates the complete benchmark construction pipeline, from user query analysis and subtask design to data annotation and quality control. To assess Benchmark Agent, we implement it to produce 15 representative benchmarks, spanning diverse evaluation scenarios, including text understanding, multimodal understanding, and domain-specific reasoning. Extensive experiments, including human evaluation, LLM-as-a-judge assessment, and consistency checks, demonstrate Benchmark Agent can generate high-quality benchmark samples with minimal human involvement. More importantly, through continual evaluation, we observe several insightful findings, including that current models struggle with certain domain-specific reasoning tasks. We believe that rapidly evolving benchmarks can contribute significantly to the research community. The preview and code will be publicly available at the demo page and code repository.


### Will the Agent Recuse Itself? Measuring LLM-Agent Compliance with In-Band Access-Deny Signals
**Authors**: Thamilvendhan Munirathinam

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06460v1](https://arxiv.org/pdf/2606.06460v1)

**Abstract**: As autonomous LLM agents increasingly hold real credentials and operate infrastructure without a human in the loop, operators have no standard way to tell an agent that a resource is off-limits. Access controls either let the agent in (it has valid credentials) or hard-fail it (indistinguishable from any other client). We propose a third mode: a lightweight, published in-band deny signal -- the Recuse Signal -- that a server emits over a protocol's existing channels (an SSH banner, a PostgreSQL NOTICE) asking a connecting automated agent to voluntarily withdraw. This is a cooperative governance control, the robots.txt analogue for live access; it is explicitly not a security boundary. Its value is entirely empirical and, to our knowledge, unmeasured: do compliant LLM agents actually honor such a signal? We define the signal as an open mini-standard, implement two zero- or low-footprint adapters (an SSH banner/PAM hook and a PostgreSQL wire-protocol proxy), deploy them on a live production host, and run a controlled experiment in which fresh agents are given a benign operations task and observed for recusal. In a pilot (SSH; OpenAI GPT-4o and GPT-4o-mini; and Claude Code as a deployed agent), the signal cleanly induces recusal -- 100% recusal when present versus 100% task completion in a no-signal control -- and, revealingly, behaves as a cooperative rather than absolute signal: an explicit operator-authorization framing flips the most capable model to proceed, while other agents continue to defer to the on-host policy. We release the standard, adapters, and experiment harness for reproduction.


### Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents
**Authors**: Zhuoming Chen, Xinrui Zhong, Qilong Feng, Ranajoy Sadhukhan, Yang Zhou, Michael Qizhe Shieh, Zhihao Jia, Beidi Chen

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06453v1](https://arxiv.org/pdf/2606.06453v1)

**Abstract**: Sparse attention is becoming increasingly important for serving large language models (LLMs) as generation lengths continue to grow. However, deploying and evaluating new sparse attention algorithms at scale remains highly engineering-intensive, slowing both human researchers and AI agents in exploring the sparse attention design. To address this challenge, we present Vortex, a system that combines a Python-embedded frontend language atop a page-centric tensor abstraction for expressing a broad range of sparse attention algorithms, with an efficient backend tightly integrated into modern LLM serving stacks. Vortex enables rapid prototyping, deployment, and evaluation of sparse attention algorithms, effectively translating their theoretical efficiency gains into real-world throughput improvements. As a result, Vortex substantially accelerates the design and iteration of sparse attention algorithms. First, AI agents use Vortex to automatically generate and refine diverse algorithms, the best reaching up to $3.46\times$ higher throughput than full attention while preserving accuracy. Second, Vortex extends sparse attention to emerging architectures and very large models that are otherwise hard to experiment with, reaching up to $4.7\times$ higher throughput on the MLA-based GLM-4.7-Flash and $1.37\times$ on the 229B-parameter MiniMax-M2.7 on NVIDIA B200 GPUs.


### Agent Memory: Characterization and System Implications of Stateful Long-Horizon Workloads
**Authors**: Yasmine Omri, Ziyu Gan, Zachary Broveak, Robin Geens, Zexue He, Alex Pentland, Marian Verhelst, Tsachy Weissman, Thierry Tambe

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06448v1](https://arxiv.org/pdf/2606.06448v1)

**Abstract**: LLM agents are increasingly deployed on long-horizon tasks requiring sustained reasoning over extended interaction histories. Realizing this at scale requires agents to persistently store, retrieve, and update their own memory across sessions. A rich ecosystem of agent memory systems has emerged spanning flat retrieval, LLM-mediated extraction, consolidating fact stores, and agentic control flows. Yet, their system-level behavior remains uncharacterized. We present the first systems characterization of agent memory. First, we introduce a system-oriented taxonomy classifying agent memory systems along four axes. Second, we build a phase-aware profiling harness attributing cost to construction, retrieval, and generation. Third, we characterize ten representative systems across two benchmark suites, uncovering how design choices shift cost across the write and read paths. Finally, we derive 10 system recommendations covering construction scheduling, capability floors, amortization via query volume, freshness-latency tradeoffs, and fleet-scale management.


### RiskFlow: Fast and Faithful Safety-Critical Traffic Scenario Generation
**Authors**: Qi Lan, Yining Tang, Yu Shen, Yi Zhou, Yuhao Wei, Jie Li, Guofa Li

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06423v1](https://arxiv.org/pdf/2606.06423v1)

**Abstract**: Safety-critical traffic scenario generation is essential for evaluating autonomous driving systems under rare but high-risk interactions. Existing diffusion-based methods offer strong controllability in closed-loop generation, but their iterative denoising process is computationally expensive and may accumulate sampling and guidance errors over long rollouts, causing unrealistic motion artifacts such as jitter, abnormal acceleration, and off-road behavior. To address these issues, we propose RiskFlow, a closed-loop safety-critical multi-agent traffic generation framework that formulates future trajectory generation as transport in the action space. Instead of relying on iterative denoising, RiskFlow learns an average velocity field over a finite interval to transform Gaussian action sequences into future acceleration and yaw-rate commands with a single forward pass, using a JVP-based objective for efficient and stable training. At test time, RiskFlow applies output-space guidance to the generated actions, steering selected critical agents toward risky interactions while regularizing off-road behavior, and reconstructs physically feasible trajectories through vehicle dynamics. Experiments on nuScenes with tbsim closed-loop evaluation show that RiskFlow achieves a strong adversariality-realism trade-off across multi-agent and long-horizon settings. Compared with representative baselines, RiskFlow consistently improves realism while maintaining competitive safety-critical generation capability, and substantially reduces inference time for evaluation.


### Unsupervised Skill Discovery for Agentic Data Analysis
**Authors**: Zhisong Qiu, Kangqi Song, Shengwei Tang, Shuofei Qiao, Lei Liang, Huajun Chen, Shumin Deng

**Published Date**: 2026-06-04

**Updated Date**: 2026-06-04

**PDF Url**: [2606.06416v1](https://arxiv.org/pdf/2606.06416v1)

**Abstract**: Inference-time skill augmentation provides a lightweight way to improve data-analytic agents by injecting reusable procedural knowledge without updating model parameters. However, discovering effective skills for data analysis remains challenging, as reliable supervision is expensive and success criteria vary across analytical formats. This raises the key question of how to discover reusable data-analysis skills from unlabeled exploration alone. We propose DataCOPE, an unsupervised verifier-guided skill discovery framework for data-analytic agents. DataCOPE derives verifier signals from the exploration trajectories and uses them to characterize relative quality or aggreement among trajectories. It iteratively coordinates a Data-Analytic Agent for trajectory generation, an Unsupervised Verifier for signal extraction, and a Skill Manager for contrastive skill distillation. For report-style analysis, we instantiate the verifier as an Adaptive Checklist Verifier that derives task-specific criteria, scores reports by verifiable coverage, and iteratively refines the checklist. For reasoning-style analysis, we instantiate it as an Answer Agreement Verifier that groups trajectories by answer agreement and uses self-consistency as an auxiliary signal. We evaluate DataCOPE on report-style analysis from Deep Data Research and reasoning-style analysis from DABStep. Across both settings, DataCOPE consistently improves held-out performance over baselines. Averaged across four model settings, DataCOPE improves the mean score by 9.71% and 32.30% on report-style and reasoning-style tasks respectively.


