# Abstracts of Papers

## World Model
### HARMONY: Hierarchical Agentic Reasoning for MONocular Image-to-Scene Synthesis
**Authors**: Shufan Sun, Chen Wang, Enxin Song, Jiatao Gu, Lingjie Liu

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26793v1](https://arxiv.org/pdf/2609.26793v1)

**Abstract**: Compositional 3D scene reconstruction has recently been explored from two directions: agentic reasoning that provides semantic understanding of spatial relationships but lacks precise alignment with input images; and visual geometry foundation models that predict dense point maps from input images but the reconstruction quality is limited. Therefore, recovering a complete 3D scene from a single monocular image with accurate inter-object relationships and high-fidelity reconstruction quality remains challenging. In this paper, we present HARMONY, a hierarchical chain-of-thought framework that leverages both agentic reasoning and visual geometry foundation. Given an image of an indoor scene, starting from an empty 3D floorplan, HARMONY first calibrates the camera against the reference image to establish a semantically-grounded spatial frame, then uses agentic VLM reasoning to recover the 3D room layout and an initial placement order. It then places the objects in a hierarchical order, from wall-mounted elements, free-standing furniture, to dependent decorations on top of furniture. We also use depth-first traversal for furniture so each placement conditions on previously resolved structure and a reflective feedback loop to avoid error accumulation. After each object placement by VLM, we use the point cloud estimations to perform geometry-based refinement so that the rendered image aligns better with the input. HARMONY can produce 3D scenes that are semantically consistent and perceptually aligned with the reference image, extending single-image compositional reconstruction to complex indoor scene images. Experiments on synthetic and real-world images demonstrate that HARMONY outperforms the evaluated reconstruction baselines, while qualitative comparisons with GPT-6 Astra suggest more faithful object arrangements and better preservation of scene details.


### DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving
**Authors**: Ziyang Leng, Sicheng Mo, Seth Z. Zhao, Haoyuan Cai, Yu Zeng, Rowan McAllister, Bolei Zhou

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26792v1](https://arxiv.org/pdf/2609.26792v1)

**Abstract**: Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions. Existing platforms, however, exhibit a sim-to-real visual gap that corrupts policy perception, undermining their ability to assess a policy's closed-loop decision-making. To this end, we propose DreamStream, a generative, closed-loop simulator that achieves policy-oriented fidelity using a simulator-grounded autoregressive video model. Our video model is distilled from a large pretrained video model via traffic layout guidance, varying visual appearance while preserving policy-relevant features such as scenario layout and the temporal consistency of dynamic objects. We further observe that perceptual metrics like FID misrank how well these features are preserved. To tackle this, we introduce FD$π$, a new multi-representation metric that measures the sim-to-real gap as the Fréchet distance over scene-context features from public E2E policies. Under FD$π$, DreamStream improves over the strongest prior closed-loop simulator by $1.6\times$ on nuScenes and $4.7\times$ on NAVSIM, and induces the least perturbation to policy's perceptual observability. Based on DreamStream, we construct Navhard-CL benchmark, which turns non-reactive real-world benchmark NAVSIM into interactive testing environments with adversarial driving behaviors and weather variations. This benchmark exposes many failure modes of driving policies, such as scorer bias and lack of recovery behaviors, that prior closed-loop benchmarks overlook. Code and data are available at https://github.com/VAIL-UCLA/DreamStream.


### A Decentralized Partially Observable Team Decision Methodology with Delayed Information Sharing
**Authors**: Xiaoxing Ren, Thomas Parisini, Andreas A. Malikopoulos

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26783v1](https://arxiv.org/pdf/2609.26783v1)

**Abstract**: We study decentralized partially observable team decision problems with low-rank latent dynamics and unknown system models. The proposed framework combines team-theoretic equivalence with low-rank model representations to address cooperative decision-making in partially observable Markov decision processes without prior knowledge of the transition model. Each team member makes decisions based on local private information and delayed common information shared across the team. Using only this available information, each member learns an approximate low-rank Markov decision process and applies least-squares value iteration to compute its policy. This yields a fully decentralized learning and planning algorithm that requires neither a centralized coordinator nor centralized training. We show that the resulting member-side solutions approximate the centralized team solution: despite partial observability, unknown dynamics, and delayed common information, each member recovers the corresponding component of an approximate team-optimal policy. We further establish finite-sample performance guarantees and derive a corresponding sample-complexity bound for the proposed algorithm.


### SWE-Serve: Benchmarking Agentic Engineering For Production Inference Serving
**Authors**: Jennifer Williams, Dave Farris, Jeff Farris, Jiantao Jiao

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26777v1](https://arxiv.org/pdf/2609.26777v1)

**Abstract**: We introduce SWE-Serve, a benchmark for evaluating agents on production inference engineering tasks. Implementing an inference feature can require coordinating multiple changes across the serving stack, including model support, runtime execution, and public APIs. Existing benchmarks provide limited coverage of production inference engineering: repository-level software engineering benchmarks do not target inference, while general terminal-agent benchmarks include only a few inference tasks. Dedicated inference benchmarks, meanwhile, focus primarily on isolated kernel generation or performance optimization rather than repository-scale production feature implementation. SWE-Serve provides 53 repository-grounded tasks derived from recent production changes to SGLang, spanning six inference engineering families. Each task executes on either CPU or a single GPU (H100) and is evaluated with hidden functional and regression tests, including, where applicable, end-to-end (E2E) serving tests and calibrated performance gates. Executable no-op and oracle controls, adversarial verifier review, and closed-book execution support task validity and evaluation integrity. Across 11 models and 31 model-effort configurations, the best-performing configuration achieves 75% mean pass@1. SWE-Serve exposes a substantial gap between completing tasks locally and achieving production correctness. On 19 tasks with end-to-end coverage, model-serving E2E tests reject roughly one-third of patches that pass every other test (45.9% under the verifier versus 69.4% with E2E tests excluded from scoring), with pass rate increasing for each model's best-performing configuration. By making the production correctness gap directly measurable, SWE-Serve enables the field to track whether future agents move beyond completing tasks locally to achieving production correctness.


### A2M: Trace-Optimized Agent Hijacking in the MCP Ecosystem
**Authors**: Laizhen Li, Xuan Wang, Peicheng Zhao, Juanjuan Zhao, Kejiang Ye, Cheng-zhong Xu, Xitong Gao

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26761v1](https://arxiv.org/pdf/2609.26761v1)

**Abstract**: Agents using the Model Context Protocol (MCP) rely on semantic matching to select tools from third-party servers, exposing a semantic supply-chain risk through attacker-controlled metadata and outputs. We introduce A2M (Attraction-to-Manipulation), a two-stage black-box framework for hijacking MCP agents. The Attraction phase optimizes tool metadata to increase invocation probability; the Manipulation phase uses execution traces to refine adversarial tool returns that steer agents toward attacker-desired outcomes. On LiveMCPBench, direct attacks optimized and evaluated on GLM-4.6 achieve a macro-average malicious tool invocation rate of 93.6% across four scenarios, increase weighted token costs to 32.4$\times$ the benign baseline under Cognitive Denial of Service, and attain a mean attack success rate of 74.4% across Information Exfiltration, Environment Integrity Compromise, and Reasoning Derailment. Transfer to four other models without re-optimization yields corresponding macro-averages of 63.6%, 2.7$\times$, and 24.5%. These findings motivate stronger tool vetting and runtime isolation in MCP ecosystems. Code is publicly available at https://github.com/Lilaizhen/A2M.


### Grow the Harness, Not the Context: From Strategy-Free Scaffolds to Reusable Specialist Agents
**Authors**: Laizhen Li, Jiarui Li, Juanjuan Zhao, Kejiang Ye, Ye Li, Cheng-zhong Xu, Xitong Gao

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26760v1](https://arxiv.org/pdf/2609.26760v1)

**Abstract**: Large language model (LLM) agents often handle streams of related tasks, yet standard harnesses repeatedly ask the model to reconstruct the same control decisions inside each task's context. We study whether task feedback can instead turn recurring control into reusable executable code, while reserving LLM calls for task-specific semantic reasoning. We introduce Growing Harness, a failure-guided training paradigm that learns the agent harness itself from a strategy-free scaffold that exposes fixed model and tool interfaces but encodes no task-solving controller. Function-level execution traces localize each failure to a bounded code surface, an optimizer repairs a window of failures jointly, and a success-first held-out gate rolls back repair sequences that harm prior capability. Accepted edits accumulate in one shared harness, allowing its control structure to emerge from task feedback. Across BrowseComp-Plus and WebArena-Verified with three deployment models from 4B to 120B parameters, Growing Harness achieves the highest mean success in five of six benchmark-model settings and trails the best mean by 0.7 pp. in the sixth. Relative to a Tool-Calling agent, it reduces LLM calls by 76.0-91.8% and deployed-agent inference cost by 74.4-98.6%. On WebArena-Verified, its success remains 44.7-45.3% across model scales, whereas Tool-Calling falls to 6.7% with the 4B model. Ablations show that trace-local edits, joint repair, and gate-based rollback each improve final success. These results show that persistent program growth can move recurring control out of model context and into low-cost code, yielding reusable specialist agents that remain effective with smaller deployment models.


## Generation
### SpeakerMem-R1: Speaker-Centered Dual-Track Memory for Multi-Party Dialogue
**Authors**: Haobo Zheng, Tan Tang, Yan Chen, Weijie Wang, Yingcai Wu

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26780v1](https://arxiv.org/pdf/2609.26780v1)

**Abstract**: Long-term conversational memory in multi-party settings requires more than retrieving relevant content from long-term conversations: it must distinguish who said what, whom each statement concerns, how individuals perceive one another, what information is shared by the group, and how states change over time. Recent studies on multi-party dialogue benchmarks show that existing general-purpose LLM memory systems tend to lose person and group relations or struggle to integrate clues distributed across members, groups, and time. Together, these issues reveal two core bottlenecks: message attribution and relational understanding in multi-party dialogue, and state reconstruction from interleaved histories. To address both, we propose $\textbf{SpeakerMem-R1}$: its dual-track memory stores speaker-labeled verbatim messages and derived states organized into person-level and group-level views, then combines evidence from both tracks by entity, event, and time at query time. To reduce attribution and update errors during structured memory construction while enabling local deployment, we train Writer-R1 with SpeakerLevenshtein and speaker-conditioned GRPO. On GroupMemBench, SocialMemBench, and EverMemBench, SpeakerMem-R1 achieves binary accuracies of 47.9%, 69.2%, and 61.9%, respectively. On the publicly reported EverMemBench leaderboard from EverMind-AI, we achieves 62.33%, the best reported result among the latest state-of-the-art frameworks. It also achieves 70.85% on all 1,986 LoCoMo questions, which we use as a two-person long-term conversation boundary test. In a controlled evaluation of 305 questions, RL raises the SFT Writer's mean accuracy from 57.38% to 68.20%. We report both binary accuracy and token-F1, and ablations show that the verbatim and structured tracks, as well as person-level and group-level views, are complementary under the standardized evaluation interface.


### CliffCompaction: Cost-Efficient Compaction for Long-Horizon Coding Agents
**Authors**: Trang Nguyen, Eulrang Cho, Bingqing Chen, Tim Dettmers

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26779v1](https://arxiv.org/pdf/2609.26779v1)

**Abstract**: Agents often work on complex problems that require millions of tokens of context, which necessitates compacting across sessions due to limited context windows. We develop CliffCompaction, an autocompaction technique that reduces cost by up to 50% under a bounded context while maintaining or improving performance on Terminal-Bench and achieving new levels of efficiency for test-time scaling and state-of-the-art results on KernelBench. The per-rollout savings of CliffCompaction make the performance--cost trade-off of test-time scaling more efficient, adding over 10 percentage points on Terminal-Bench for less than the cost of two full-context runs. Under parallel test-time scaling, CliffCompaction lets Kimi K2.6 match Opus 4.7, and exceed Opus 4.6 and GPT-5.3 Codex at lower cost. The key to CliffCompaction's effectiveness is that it keeps compacted information faithful by only truncating or dropping content, never rephrasing or rewriting it. We never compact a compaction---each pass operates only on original content, and prior compacted output is discarded, preventing context drift from accumulating. These properties sustain continual learning over sessions exceeding a million tokens: on KernelBench, CliffCompaction reaches CUDA kernel speedups of $2.23\times$ after 200 steps and $3.58\times$ after 400 steps, surpassing specialized search algorithms and trained agents despite being a general-purpose compaction technique. We open-source a scaffold-agnostic API-proxy implementation of CliffCompaction usable with Claude Code, Codex and other harnesses.


### Type-Safe Is Not Error-Free: A Constrained Decision Head Follows the Option Name, Not the Rubric Bound to It
**Authors**: Yu Sun, Junhao Xu

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26758v1](https://arxiv.org/pdf/2609.26758v1)

**Abstract**: Typed decision models are built for settings where model outputs are consumed directly by software. Instead of generating free-form text, they return a decision over a predefined set of options. By construction, every output conforms to the required schema. Yet this guarantee does not tell us whether the model interprets the options as intended. We study Jev and two Jev-like models with open weights by changing how option names are assigned to rubrics. Each option consists of an option name and a textual rubric that defines what the option means. We change only which option name is assigned to each rubric; the question, state, rubric wording, and set of option names remain exactly the same. On 1200 workflow decisions with task-specific rubrics, renaming the two options from 0/1 to no/yes changes 70.4 more answers per hundred (95% CI: [67.6, 73.1]) and shifts AUC from .94 to .23, revealing a systematic reversal in the decision ranking rather than simple uncertainty. The same operation has little effect with neutral option names. This pattern holds across all 4 predicates, where the effect is at least 7.4x larger than under the neutral control, and becomes stronger as the number of options increases. The effect also depends on the read-out geometry: a second model family that mean-pools over the full option span flips 4.1x less often. The hosted model exhibits the same behavior: the swap changes AUC from .8146 to .5806 and produces 24x as many answer flips as its test-retest floor. In contrast, replacing the option names with random character strings returns all model families to the neutral-control regime without reducing accuracy. The failure therefore depends on the semantic polarity of the option names rather than on the renaming operation itself. Across all conditions, the type-error rate remains 0%, even when decision accuracy degrades substantially.


### FleXray: Universal Clinical X-ray Segmentation
**Authors**: Victor Ion Butoi, Vivek Gopalakrishnan, John V. Guttag, Adrian V. Dalca, Neel Dey

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26756v1](https://arxiv.org/pdf/2609.26756v1)

**Abstract**: X-ray is medicine's most widely used imaging modality, yet remains among its least quantitative. Unlike volumetric modalities like CT or MRI, X-ray collapses 3D anatomy into a 2D projection, causing structures to overlap and anatomical boundaries to be ambiguous, even to experts. As a result, labeling X-ray databases for training general-purpose segmentation systems is impractical, leaving morphometric and functional X-ray analysis confined to narrow anatomical regions and applications. To this end, we present FleXray, a generalist model for anatomical segmentation across the entire body in clinical X-rays. Instead of curating large, manually annotated X-ray datasets, we build a scalable, physics-based generative X-ray data engine. Using existing 3D whole-body CT segmentation datasets and generative image-editing models, we simulate fully-annotated 2D X-rays with diverse appearances, physiological properties, and imaging geometries. Trained on these simulations, FleXray accurately segments 60 anatomical structures across unseen research datasets and in-the-wild X-rays. We further show that FleXray makes X-rays directly amenable to quantitative analysis, enabling automated measurements for disease grading, robust navigation during X-ray-guided interventions, and data-efficient learning of pathological targets. We release the model, code, a full-body X-ray segmentation dataset, and a local, easy-to-use browser-based tool at https://flexray.csail.mit.edu .


### EquivSVA: A Formally Verified Dataset of Behavioral Assertions Across Equivalent RTL Implementations
**Authors**: FNU Aditi

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26751v1](https://arxiv.org/pdf/2609.26751v1)

**Abstract**: Large language models are increasingly used to generate SystemVerilog Assertions from natural-language specifica- tions and register-transfer-level designs. Existing datasets and benchmarks support important goals such as large- scale training, formal evaluation, specification-to-assertion generation, and mutation-based testing. A complemen- tary need is to study whether a generated assertion cap- tures externally observable behavior or depends on inci- dental details of one RTL implementation. We present EquivSVA, a formally verified dataset organized around behavior families. Each family contains four structurally distinct RTL implementations of the same externally ob- servable behavior, shared interface-level gold properties, three controlled mutants, and formal-validation evidence. EquivSVA contains 120 behavior families across 12 cat- egories, 480 reference RTL implementations, 914 gold properties, and 360 mutants. Every final family passes a fixed 17-job validation suite covering RTL equivalence, gold-property proofs, property reachability, mutant dis- tinguishability, and gold-property checks on mutants. We also provide fixed family-safe train, development, and test splits. As a small demonstration of the analyses en- abled by the dataset, we evaluate the publicly released, Apache-2.0-licensed Qwen2.5-Coder-7B-Instruct model on the held-out test split. Of 293 interface-only generated properties, 93 are formally sound, and the number of sound properties varies across equivalent implementations for 14 of 24 test families. These results illustrate how behavior-family organization can support controlled stud- ies of assertion-generation robustness without requiring changes in intended functionality. The dataset, generators, validation scripts, and case-study artifacts are publicly released at https://github.com/aditigupta96/EquivSVA.


### Metrics Failure in LLM-Based Code Vulnerability Repair: An Empirical Study and a Change-Aware Screen
**Authors**: Om Nepal, Sushant Aryal, Oluseyi Olukola, Nick Rahimi

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26749v1](https://arxiv.org/pdf/2609.26749v1)

**Abstract**: Large language models (LLMs) are increasingly applied to the automated repair of C/C++ security vulnerabilities, and compile rate is a commonly reported proxy for progress: whether the generated patch compiles. We argue that compile rate is a scientifically unreliable metric for single-function vulnerability repair, and we support this with five controlled experiments over 203 vulnerable functions from Big-Vul, three open-source code LLMs (350M to 6.7B parameters), and three prompting strategies. Compile rate (i) barely responds to an intervention that substantially improves the generated code; (ii) is dominated by evaluation-harness and dataset artifacts rather than model quality, with about 64% of compile failures not attributable to the model, a share that is nearly invariant across models; (iii) shifts by 1.8 to 2.7 times on identical patches under a single compiler-standard flag, with zero regressions; (iv) ranks the three models in the opposite order to reference-similarity metrics; and (v) rewards non-repairs when used as an optimization target, since a compiler-feedback loop raises compile rate while similarity to the human fix falls, with manual inspection finding deletion- and placeholder-style non-repairs among the newly compiling outputs. The natural fallback, whole-function CodeBLEU, also fails: an unchanged copy of the vulnerable input outscores every model. We also examine diff_F1, a change-aware screen that scores only the edited region. It gives exactly zero credit to a no-op and near-zero credit to some, though not all, of the deletion-based gaming patches we observed, while still crediting genuine partial edits, so it may serve as a cheap screen before deeper, execution-based analysis. It is not a repair-quality metric, and we report where it falls short. Our findings argue for change-aware, execution-grounded evaluation of LLM-based vulnerability repair.


## VLA
### Beyond Reconstruction Error: Analytical and Data-Driven Action Tokenization for Autoregressive Vision-Language-Action Models
**Authors**: Yuxin Yang, Gaohan He, Changxue Guan, Hangming Liu

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.25820v1](https://arxiv.org/pdf/2609.25820v1)

**Abstract**: Discrete action tokenization is central to autoregressive vision-language-action (VLA) models, yet action representations are often evaluated primarily through reconstruction fidelity. We ask which representation properties actually matter for closed-loop control by comparing fixed analytical, data-driven linear, and nonlinear neural representations under a unified tokenization interface. Across rate-distortion analysis, sequence-modeling diagnostics, and 3,500 LIBERO rollouts, representation rankings change with the evaluation criterion. PCA achieves lower nominal reconstruction error than Temporal-DCT, but produces less predictable token sequences and 3.0 percentage points lower mean seen-task success across three policy-training seeds, with the policy ordering reversing in one seed. In a matched seed-42 ablation, an autoencoder further reduces reconstruction error yet does not yield the strongest policy and exhibits greater sensitivity to discrete token perturbations. These findings show that reconstruction fidelity alone cannot reliably select action representations for autoregressive control, motivating joint evaluation of geometric fidelity, sequence predictability, decoder stability, and closed-loop performance.


### IndustrialVLA-Bench: A Traceable Multi-Axis Evaluation of Open Robot Policy Models
**Authors**: Yiqi Wang, Zhifeng Rao, Jiaqi Zhang, Xiaoyang Li, Zhangkai Wu, Yiqun Duan, Mingkai Zheng, Fei Wang, Shan You, Taotao Cai

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.25562v1](https://arxiv.org/pdf/2609.25562v1)

**Abstract**: Open robot policies increasingly follow two paradigms: vision-language-action models (VLAs) directly map observations and instructions to actions, whereas world-action models (WAMs) incorporate learned video or world dynamics into policy learning or action generation. Although both target the same manipulation tasks and represent alternative design choices, they are commonly reported under different evaluation protocols, leaving their capability, robustness, language sensitivity, and deployment-cost trade-offs unclear. We present IndustrialVLA-Bench, an evidence-aware evaluation of six released VLA and WAM systems under a unified reporting schema. It separately evaluates clean capability on LIBERO, non-language robustness on LIBERO-Plus, instruction sensitivity on LIBERO-Para, and observed execution cost. Reported task scores aggregate three complete evaluations with distinct random seeds under a fixed checkpoint and inference configuration. Across all six systems, clean LIBERO averages differ by only 1.58 points, whereas robustness and paraphrase summaries span 14.62 and 31.08 points. Restricting every comparison to the three protocol-faithful systems preserves the effect (1.36, 14.62 and 23.10 points), so the diagnostic separation reported here does not depend on the weaker evidence tiers. We additionally report observed inference latency, peak memory, runtime mode, and an evidence status for every system. Protocol-faithful, near-reproduction, and pending-verification entries remain visibly separated; only protocol-faithful entries support strict comparisons. Rather than claiming universal superiority of either paradigm, IndustrialVLA-Bench provides traceable evidence for comparing released robot policies on shared practical criteria. Code and evaluation records are available at https://github.com/xiaoqi-7/IndustrialVLA-Bench.


### HABILIS Brain 0: Geometry-Change Supervision for Vision-Language-Action and Residual Flow Recovery
**Authors**: Jinu Pahk, Jesoon Kang, Taegeon Park, Jisu An, Soo Min Kimm, Jaejoon Kim, Byoung-Tak Zhang

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.25558v1](https://arxiv.org/pdf/2609.25558v1)

**Abstract**: Vision-language-action policies benefit from geometric supervision, but current-frame geometry alone does not explicitly describe the changes associated with manipulation. This design is motivated by the goal of learning an embodiment-agnostic visual interface that can be pretrained across robot and egocentric video before robot-specific action alignment. We introduce Geometry-Change VLA (GC-VLA), which learns to predict multiview future-current geometry-change tokens from current observations. Offline frame pairs define a nominal 0.5-second prediction horizon; future observations are used only to construct training targets. Stage 1 trains a geometry-change vision-language model (GC-VLM). Stage 2 introduces a continuous ActionExpert and aligns it with robot actions while stopping action-flow gradients at the VLM interface. Stage 3 enables these gradients to update the trainable VLM components jointly with the ActionExpert. Stage 4 freezes GC-VLA and applies Geometry-Conditioned Residual Flow (GCRF), using a binary intervention router and a single bounded residual velocity policy learned from closed-loop feedback. GC-VLA achieves 95.20% success on LIBERO, and GC-VLA with GCRF achieves 99.55%. Inference uses current observations and the learned GC representation without executing the offline target encoders.


### VLAQuantBench: Closed-Loop Evaluation of Post-Training Quantization for Vision-Language-Action Models
**Authors**: Jiuyi Xu, Qing Jin, Meida Chen, Song Wang, Yang Sui, Yangming Shi

**Published Date**: 2026-09-21

**Updated Date**: 2026-09-21

**PDF Url**: [2609.25376v1](https://arxiv.org/pdf/2609.25376v1)

**Abstract**: Post-training quantization reduces the memory requirements of vision-language-action (VLA) models, but precision selection must account for the interaction between layer scope, numerical format, and calibration. We introduce \textbf{VLAQuantBench}, a controlled evaluation with 409 runs and 94,574 simulation episodes: four models on LIBERO, with X-VLA additionally evaluated on three simulation benchmark families. Under uncalibrated W4A4 round-to-nearest quantization, expanding a $π_{0.5}$ action-head subset from 126 to 167 layers raises success from 7.0\% to 70.5\%. Fixed-observation replay confirms a corresponding numerical recovery. Two-episode calibration removes the severe joint failures in the tested subsets, whereas the same smoothing-and-clipping recipe lowers $π_0$ success and does not recover OpenVLA-OFT end-to-end. For OpenVLA-OFT, protecting one 28,672-parameter output projection instead restores near-baseline success: the remaining 441 eligible linear layers retain W3 on LIBERO-Long or eight-bit activations across all four suites. Task-clustered intervals support the large failure and recovery contrasts. These results establish recipe-dependent interactions and identify concrete precision assignments, rather than universal layer-sensitivity rules. Real-kernel and physical-robot measurements complement the accuracy analysis. Code, configurations, and episode records are publicly available at https://github.com/jiuyixu25/VLAQuantBench.


### X-Planner: Event-Structured Task Planning for Embodied Intelligence
**Authors**: Howard Lu, Shalfun Li, Porter Pan,  Cris,  Lumen,  Cyril, Eric Hu, Lily Li, Maeve Zhang, Robert Wang, KZ Zheng, Viggo Chen, Tim Ding, Regsis Cheng, YJ Xiao,  Kian, Hai Lin, Alan Song, Elise Ma, Gody Li, Victor Yao, Yohann Tang, Ingrid Yu, Jason He, James Wang, Ryan Yu, Ping Yang, Chris Pan, Vincent Chen, Roy Gan, Hao Wang, Qian Wang

**Published Date**: 2026-09-21

**Updated Date**: 2026-09-21

**PDF Url**: [2609.25187v1](https://arxiv.org/pdf/2609.25187v1)

**Abstract**: Task planning bridges high-level instructions and executable behavior in long-horizon manipulation, yet modern Vision-Language-Action (VLA) systems often leave this intermediate structure implicit. Existing chain-of-thought (CoT) planners also tend to rely on coarse task-level annotations or serialize long reasoning traces token by token. We present X-Planner, a planning front-end that addresses both the supervision and representation of embodied reasoning. Our planning data combine Ego, UMI, and teleoperation under a hierarchy granularity with source-dependent annotation depth. Takeover-time annotations and human-designed failures supervise ongoing error recognition. On the model side, a shared VLM backbone exposes two event-structured plan forms: a discrete interface that emits interpretable event states and a latent interface that relays continuous CoT states across staggered Transformer depths through Staircase Decoding. A frozen latent-to-text reconstruction objective provides a semantic anchor for the latent representation. Offline two-step planning evaluation places X-Planner second among four evaluated models on both BERTScore-F1 and a judge-based Overall score. In real-robot experiments, respectively, outperforming the evaluated baselines. These results characterize planning-text quality and downstream execution.


### vla.simd: Efficient CPU Inference for Language-Conditioned Manipulation
**Authors**: Khanh D. Nguyen, Hoang M. Truong, An T. Le

**Published Date**: 2026-09-21

**Updated Date**: 2026-09-21

**PDF Url**: [2609.24274v1](https://arxiv.org/pdf/2609.24274v1)

**Abstract**: Deploying language-conditioned manipulation without a dedicated GPU requires efficient inference and action chunks that cover the delay between policy queries. We present vla.simd, a CPU inference engine that combines shared SIMD micro-kernels, reusable computation, and target-specific optimization. We relate query latency and execution horizon to action availability under lagged and time-aligned execution, distinguishing action supply from feedback frequency. Across six policies and four CPUs, vla.simd achieves approximately $1.4\times$ median speedup over compiled PyTorch references while preserving fp32 numerical fidelity. We also introduce IMPACT, an ACT-based policy with cached text representations and language-modulated visual features. IMPACT is the only language-conditioned policy in our evaluated set that supplies at least 30 actions/s on the Raspberry Pi 5: after a 90 s thermal soak, it supplies 33.5 actions/s in fp32 and 81.2 with int8. Separate GPU evaluations yield $76.4\%$ mean success across four LIBERO suites without robot pretraining; instruction-shuffling tests demonstrate selection among familiar goals. Trials with IMPACT on an SO-101 arm and SmolVLA on a UR10e with a Robotiq gripper demonstrate CPU deployment on two robot embodiments.


## Agent
### Measuring the Serving Stack Instead of the Model: Hidden Confounds in Local Tool-Use Evaluation
**Authors**: Lijuan Tang, Yuemeng Zheng

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26693v1](https://arxiv.org/pdf/2609.26693v1)

**Abstract**: A coding agent must emit a valid tool call--a parseable invocation of a tool in the provided schema--before the harness can execute its chosen action. We study how local serving stacks affect this protocol step and show that measured outcomes can depend on the serving layer rather than model behavior alone. In Ollama, the default tools= request is gated per model by a static template flag: some models are accepted and return calls as text, some return native tool_calls, while Phi-3 and Gemma-3 are rejected before inference. In our harness, rejection and retry exhaustion are not preserved as structured failure metadata, so downstream analysis can misclassify them as model non-calls and naively report 0% fidelity. Adding a text tool list while retaining the native channel recovers much of the measured fidelity for accepted models, whereas a uniform text protocol reduces fidelity for Llama-3.2, which has native tool-call support. Cross-stack probes on Ollama, llama.cpp, vLLM, and SGLang show different handling of the same request. Constrained decoding removes parse failures but can induce non-termination, and turn-pooled versus per-instance estimates differ by up to about 55 points. We conclude with a checklist for treating serving behavior as part of the evaluation protocol.


### From Alignment to Access Control: A Framework for GenAI Policy Enforcement
**Authors**: Nathalie Baracaldo

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26682v1](https://arxiv.org/pdf/2609.26682v1)

**Abstract**: Generative AI (GenAI) applications have flourished enabling users to chat with large language models, and to create agents to act on their behalf for a variety of tasks. The pace of development of capabilities in this field is incredibly fast with security and safety taking a back seat. Unfortunately, the slower pace at which security and safety mechanisms have evolved has led to real incidents. Policy enables the definition of desirable behavior of applications, and for that reason, it is a cornerstone of making systems secure and compliant. Policy however means different things to different practitioners creating confusion and siloed solutions that are not adequate for compliance. This paper takes a tour of the good, the bad and the ugly when it comes to policy enforcement in GenAI applications. We propose a methodology to systematically analyze and dissect existing approaches to define and enforce policy found in the wild. Based on this principled analysis, we provide recommendations and call for action for the community to address.
  This paper is a companion extension of USENIX Security 2026 Enigma talk titled "From Alignment to Access Control: A Unified View of GenAI Policy Enforcement" by the author Nathalie Baracaldo.


### MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward Reinforcement Learning
**Authors**: Kairui Yang, Ziheng Yi, Xunkai Li, Minghao An, Zhanke Liu, Zekai Chen, Rong-Hua Li

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26667v1](https://arxiv.org/pdf/2609.26667v1)

**Abstract**: Collaboration topology shapes both the performance and execution cost of LLM-based multi-agent systems. Because tasks differ in complexity and required capabilities, recent approaches generate task-specific collaboration graphs that specify agent participation and information flow. However, representative topology generators use either individual agents or predefined groups throughout an organization, overlooking differing collaboration needs across subtasks. Our key insight is to select granularity locally for each functional role, combining fine-grained control with reusable collaboration patterns within one organization. Learning such organizations requires exploring a combinatorial construction space with limited intermediate feedback from final-answer rewards. Therefore, we propose MAGIC, a dense-reward reinforcement learning framework for mixed-granularity graph generation. Specifically, MAGIC constructs a mixed-granularity agent graph by sequentially selecting a functional role, instantiating it as a single agent or reusable group, and connecting it to existing units. We directly optimize the construction policy using returns from trajectories sampled under the current policy and use potential-based reward shaping to provide intermediate feedback from probe-based utility and structural signals while preserving the cumulative task reward. MAGIC outperforms state-of-the-art baselines across eight benchmarks and demonstrates strong inference efficiency in our efficiency study.


### The Delegation Blind Spot: Auditing Product Decisions from Agent Choices
**Authors**: Shivam Gupta

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26642v1](https://arxiv.org/pdf/2609.26642v1)

**Abstract**: Successful agent execution need not identify which future product improvement its user would value. We present a decision-specific audit that maps a declared observation channel and product-value contrast to compatible intervals and witness populations. Its foundations are established identification and decision theory; the contribution is an executable measurement workflow and a controlled study of its limits. A frozen experiment makes 4,800 requests to two pinned model snapshots on shared synthetic tasks. All 36 conservative primary intervals remain unresolved despite different execution accuracy. An exploratory 2,400-call follow-up records supplied preferences and resolves three of nine comparisons per model. A deterministic extractor resolves seven of nine without model calls or calibration observations, exposing unnecessary uncertainty introduced by model-generated reports. A further 14,400 controlled multinomial simulations distinguish structural ambiguity from weak identification and finite calibration precision. We propose a source-labeled decision receipt and provide an offline viewer for inspecting the audit. These results motivate preserving decision-relevant structured input and diagnosing why a decision is unresolved before collecting more telemetry. The study contains no human participants or real customer outcomes. Full proofs, raw model provenance, controlled experiments, and reproducible analyses accompany the report.


### The Disciplinary Language Transfer Problem: How Psychological Vocabulary Produces Governance Failures in AI Agent Deployment
**Authors**: Kymberly Lasser-Chere, Tyler Akidau, Marc Millstone

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26562v1](https://arxiv.org/pdf/2609.26562v1)

**Abstract**: The vocabulary used to describe AI agents in governance contexts -- learning, memory, values, compliance, identity, trust -- is borrowed from psychological and organizational science, contributing to systematic failures in how organizations deploy, oversee, and hold agents accountable. This paper argues that the problem is not merely terminological but epistemological: psychological vocabulary carries an "invisible grammar" of its home discipline into governance discourse, calibrating frameworks to a metaphysical entity that does not exist in current AI architectures. We call this the disciplinary language transfer problem. Drawing on Wittgenstein's concept of language games, Kuhn's paradigm-laden observation, Haraway's situated knowledge, and Star and Griesemer's boundary object theory, we show that the transfer operates at three levels (epistemological assumptions, theoretical constructs, and surface vocabulary), each requiring a different remediation. We characterize six foundational epistemological assumptions embedded in Western psychological governance discourse, trace their origin in specific philosophical traditions, and show why each fails when applied to systems without developmental continuity. The paper's practical output is an actionable Disciplinary Audit: a six-question governance document scan operationalized through a translation taxonomy of thirty-seven terms mapping operational constructs to agent-appropriate replacements, presented here in abridged form and openly archived in full. The vocabulary reform proposed here is not merely terminological; it is the condition of possibility for governance frameworks that correctly identify what they are governing.


### REFLEX with Jev for Efficient Selective Control in LLM Agents
**Authors**: Tiantong Wu, Wei Yang Bryan Lim

**Published Date**: 2026-09-22

**Updated Date**: 2026-09-22

**PDF Url**: [2609.26532v1](https://arxiv.org/pdf/2609.26532v1)

**Abstract**: LLM agents often use generative models for bounded decisions, raising the question of when these decisions can be handled more efficiently without reducing task success. We study REFLEX, an agent architecture that uses Jev as a fast, typed decision layer and calls a strong LLM when confidence is low, or generation is required. On a frozen 100-task benchmark, REFLEX achieves 95% success with 72.7% fewer strong-model calls than a strong-only agent, with reductions persisting across three fallback families. Controlled interventions show that reliability depends on action-set size and near-valid alternatives near authorization boundaries. External BFCL and $τ$-style evaluations reveal limited advantages over a cheap generative cascade when ordinary routing is already highly accurate. These findings identify when selective control with Jev can reduce computation and where its benefits are limited.


