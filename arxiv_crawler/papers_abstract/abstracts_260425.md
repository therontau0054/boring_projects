# Abstracts of Papers

## Physics
### Algorithmic Locality via Provable Convergence in Quantum Tensor Networks
**Authors**: Siddhant Midha, Yifan F. Zhang, Daniel Malz, Dmitry A. Abanin, Sarang Gopalakrishnan

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21919v1](https://arxiv.org/pdf/2604.21919v1)

**Abstract**: Belief propagation has recently emerged as a powerful framework for evaluating tensor networks in higher dimensions, combining computational efficiency with provable analytical guarantees. In this work, we develop the first end-to-end theory of tensor network belief propagation for a class of projected entangled pair states satisfying \emph{strong injectivity}. We show that when the injectivity parameter exceeds a constant threshold, BP fixed points can be found efficiently, and a cluster-corrected BP algorithm computes physical quantities to $1/\mathrm{poly}(N)$ error in $\mathrm{poly}(N)$ time for an $N$ qubit system. We identify a striking phenomenon we term \emph{algorithmic locality}: local perturbations of the tensor network affect the BP fixed point with an influence decaying rapidly with distance. As a result, updates to the fixed point after a local perturbation can be carried out using only local recomputation. Moreover, through the cluster expansion, this locality extends to observables, implying that local expectation values can be approximated from local data with controlled accuracy. Our results provide the first rigorous guarantee for the effectiveness of tensor-network belief propagation on a wide class of many-body states, bridging a gap between widely used numerical practice and provable algorithmic performance.


### Wave physics as a choreographic notation for partner dance
**Authors**: Fernando Ramiro-Manzano

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21918v1](https://arxiv.org/pdf/2604.21918v1)

**Abstract**: The wave is considered a paradigm in dance and connects bodily expression with nature. Although wave concepts such as propagation and phase have proven to be powerful tools for dance analysis, many aspects of bodily expression, including partner dance, have been investigated using numerical approaches and neural networks. Complementarily, compact analytical models have been especially successful for describing human motion, particularly gait. Here, we leverage wave-physics concepts to provide a comprehensive wave-based and oscillatory analytical characterization of expressive motion in partner dance. We apply this framework to Bachata Sensual, a dance style in which the wave is the leitmotif. We analyse three dance couples (Phase I) performing five movement sequences and one composite. The sequences exhibit multiple wave phenomena, from time-dependent interference to the generation-like emergence of harmonics. Within this wave-physics perspective, the formalism can be viewed as a choreographic motion notation. As an illustrative acoustic analogy, harmonic components extracted under boundary conditions can be mapped to audible frequencies, forming musical dyads. Within certain limits and not rigidly constrained by body morphology, modal response can be tuned to underpin fluid motion, adapting across musical timescales and movement patterns. Overall, this wave-physics notation highlights connections between partner-dance expressivity and harmonic nature.


### Cryogenic shock exfoliation for ultrahigh mobility rhombohedral graphite nanoelectronics
**Authors**: Ludwig Holleis, Youngjoon Choi, Canxun Zhang, Jack H. Farrell, Gabriel Bargas, Audrey Hsu, Zexing Chen, Ian Sackin, Wenjie Zhou, Yi Guo, Thibault Charpentier, Yifan Jiang, Benjamin A. Foutty, Aidan Keough, Martin E. Huber, Takashi Taniguchi, Kenji Watanabe, Andrew Lucas, Andrea F. Young

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21912v1](https://arxiv.org/pdf/2604.21912v1)

**Abstract**: Rhombohedral multilayer graphene (RMG) offers a highly tunable platform for correlated electron physics, featuring field-effect control of magnetic, superconducting, and topological phases[1-24]. The promise of these materials has been held back by the limited abundance of rhombohedral stacking in natural graphite, which constrains both sample yield and useful area. Here we introduce 'cryogenic shock exfoliation' to produce large area rhombohedral graphene flakes which, combined with a low-pressure van der Waals assembly technique that preserves stacking order, enable highly uniform devices exceeding 1300 $μm^2$ with fabrication yields of 90%. Using scanning nanoSQUID-on-tip imaging, we demonstrate uniform spin magnetism over the full central 10 times 10 $μm^2$ area of our devices. Transverse magnetic focusing reveals a disorder mean free path exceeding 200 $μm$ at low temperatures. Within the flat surface bands of RMG[20], we observe a size-driven crossover from Poiseuille to porous electron flow in the intermediate-temperature regime of strong electron-electron hydrodynamics[16, 25], providing a further signature of ultrahigh device quality. Our approach overcomes a key materials bottleneck in the fabrication of mesoscopic rhombohedral graphene devices, paving the way for incorporating strongly correlated phases into two-dimensional nanoelectronics.


### Heavy Quark Transport is Non-Gaussian Beyond Leading Log
**Authors**: Jean F. Du Plessis, Bruno Scheihing-Hitschfeld

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21895v1](https://arxiv.org/pdf/2604.21895v1)

**Abstract**: We find that heavy quark transport beyond leading logarithm at weak coupling is intrinsically non-Gaussian: the longitudinal momentum transfer distribution has asymmetric exponential tails that are crucial for equilibration dynamics. We show this by computing the leading-order momentum transfer kernel for relativistic heavy quarks in weakly coupled non-Abelian plasmas, matching perturbative momentum transfer on the thermal scale to hard-thermal-loop-resummed soft physics. This is the same structure previously found in strongly coupled holographic plasmas, showing that it is not peculiar to weak or strong coupling, conformality, or supersymmetry. We therefore expect that this is a robust feature that physical quark-gluon plasma should also exhibit.


### NPU Design for Diffusion Language Model Inference
**Authors**: Binglei Lou, Haoran Wu, Kevin Lau, Gregor MacDonald, Jiayi Nie, Yao Lai, Can Xiao, Xuan Guo, Jianyi Cheng, Rika Antonova, Robert Mullins, Aaron Zhao

**Published Date**: 2026-01-28

**Updated Date**: 2026-04-23

**PDF Url**: [2601.20706v2](https://arxiv.org/pdf/2601.20706v2)

**Abstract**: Diffusion-based LLMs (dLLMs) fundamentally depart from traditional autoregressive (AR) LLM inference: they leverage bidirectional attention, block-wise KV cache refreshing, cross-step reuse, and a non-GEMM-centric sampling phase. These characteristics make current dLLMs incompatible with most existing NPUs, as their inference patterns, in particular the reduction-heavy, top-$k$-driven sampling stage, demand new ISA and memory hierarchy support beyond that of AR accelerators. In addition, the blocked diffusion KV cache breaks from the append-only paradigm assumed by AR NPUs, and conventional AR-derived KV quantization schemes were designed for static activation distributions and do not account for the step-wise distribution shifts introduced by iterative block-wise refinement in dLLMs.
  In this paper, we introduce the first NPU accelerator specifically designed for dLLMs. It delivers: a dLLM-oriented ISA and compiler; a hardware-optimized execution model for both the transformer inference and diffusion sampling used in dLLMs; a novel Block-Adaptive Online Smoothing (BAOS) for quantizing KV cache in dLLMs; and a complete RTL implementation synthesized in 7nm. To evaluate and validate our design, we introduce a tri-path simulation framework that comprises analytical, cycle-accurate, and accuracy simulators, together with cross-validations against physical hardware. The full NPU stack, including ISA, simulation tools, and quantization software, will be open-sourced upon acceptance.


### A Multi-Stage Warm-Start Deep Learning Framework for Unit Commitment
**Authors**: Muhy Eddin Za'ter, Anna Van Boven, Bri-Mathias Hodge, Kyri Baker

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21891v1](https://arxiv.org/pdf/2604.21891v1)

**Abstract**: Maintaining instantaneous balance between electricity supply and demand is critical for reliability and grid instability. System operators achieve this through solving the task of Unit Commitment (UC),ca high dimensional large-scale Mixed-integer Linear Programming (MILP) problem that is strictly and heavily governed by the grid physical constraints. As grid integrate variable renewable sources, and new technologies such as long duration storage in the grid, UC must be optimally solved for multi-day horizons and potentially with greater frequency. Therefore, traditional MILP solvers increasingly struggle to compute solutions within these tightening operational time limits. To bypass these computational bottlenecks, this paper proposes a novel framework utilizing a transformer-based architecture to predict generator commitment schedules over a 72-hour horizon. Also, because raw predictions in highly dimensional spaces often yield physically infeasible results, the pipeline integrates the self-attention network with deterministic post-processing heuristics that systematically enforce minimum up/down times and minimize excess capacity. Finally, these refined predictions are utilized as a warm start for a downstream MILP solver, while employing a confidence-based variable fixation strategy to drastically reduce the combinatorial search space. Validated on a single-bus test system, the complete multi-stage pipeline achieves 100\% feasibility and significantly accelerates computation times. Notably, in approximately 20\% of test instances, the proposed model reached a feasible operational schedule with a lower overall system cost than relying solely on the solver.


### Enhancing Coherence of Spin Centers in p-n Diodes via Optimization Algorithms
**Authors**: Jonatan A. Posligua, David E. Stewart, Denis R. Candido

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21874v1](https://arxiv.org/pdf/2604.21874v1)

**Abstract**: Solid-state spin defects hold great promise as building blocks for various quantum technologies. Embedding spin centers in $p$-$n$ diodes under reverse bias has proved to be a powerful strategy to narrow the optical linewidth and increase spin coherence, while also enabling control of the photoluminescence wavelength via Stark shift. Given the multitude of parameters influencing spin centers in diodes (e.g., doping densities and profiles, temperature, bias voltage, spin center position), a question that has not yet been answered is: which set of these design parameters maximizes spin center coherence? In this work, we address this question by developing a scaled gradient descent optimization algorithm that minimizes the optical linewidth of spin centers by combining the numerical solution of a diode's Poisson equation with calculated charge noise from the non-depleted regions. Our optimization is performed for both single- and multiple-parameter cases for divacancies in SiC $p$-$i$-$n$ diodes, including reverse-bias voltage, doping density and profile, and diode total length. Importantly, the optimization is subject to realistic physical constraints, such as small operating bias voltages, avoidance of the dielectric breakdown regime and physical thresholds for doping density. Additionally, due to the leakage current at reverse bias voltages, we develop a new formalism to investigate its influence on coherence. We show that the corresponding noise can be mitigated by implanting spin defects away from the diode's surfaces. Our work provides guidance on experimentally relevant diodes for hosting spin centers with the narrowest optical linewidths and longest coherence times.


### Analytical and Machine Learning Methods for Model Discernment at CE$ν$NS Experiments
**Authors**: Iain A. Bisset, Bhaskar Dutta, Doojin Kim, Samiran Sinha, Joel W. Walker

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21869v1](https://arxiv.org/pdf/2604.21869v1)

**Abstract**: Neutrino experiments are often limited by low statistics, sizable systematic uncertainties, and coarse observable binning, which can hinder discrimination among competing beyond-the-Standard-Model (BSM) explanations of anomalous signals. In particular, analyses based primarily on total event-rate differences are vulnerable to source-normalization uncertainties and to degeneracies among models that induce similar inclusive yields. Using stopped-pion coherent elastic neutrino-nucleus scattering (CE$ν$NS) as a benchmark environment, we study how much model-discrimination power can be obtained from correlations in baseline, recoil energy, and timing that are less sensitive to the total rate. As benchmark BSM scenarios, we consider a $3+1$ sterile-neutrino framework and neutral-current non-standard neutrino interactions (NSI). We show with a likelihood-based analysis that these scenarios can be distinguished in nontrivial regions of parameter space once multidimensional shape information is retained. We further demonstrate with convolutional neural networks that substantial discrimination remains possible even after the total event rate is explicitly removed from the input, indicating that the relevant information is genuinely encoded in the shape of the CE$ν$NS distribution. Finally, through multi-class classification within the sterile parameter space, we show that in favorable regions the same observables can support approximate localization of the underlying sterile-neutrino benchmark point. Our results highlight the complementary roles of conventional and machine-learning-based inference in moving neutrino new-physics searches from anomaly detection to physics interpretation.


### Classical billiards can compute
**Authors**: Eva Miranda, Isaac Ramos

**Published Date**: 2025-12-22

**Updated Date**: 2026-04-23

**PDF Url**: [2512.19156v3](https://arxiv.org/pdf/2512.19156v3)

**Abstract**: We show that two-dimensional billiard systems are Turing complete, in the sense that the halting of any Turing machine with a given input is equivalent to a certain bounded trajectory in this system entering a specified open set. Billiards serve as idealized models of particle motion with elastic reflections and arise naturally as limits of smooth Hamiltonian systems under steep confining potentials. Our results establish the existence of undecidable trajectories in physically natural billiard-type models, including billiard-type models arising in hard-sphere gases and in collision-chain limits of celestial mechanics.


### Fake or Real, Can Robots Tell? Evaluating VLM Robustness to Domain Shift in Single-View Robotic Scene Understanding
**Authors**: Federico Tavella, Amber Drinkwater, Angelo Cangelosi

**Published Date**: 2025-06-24

**Updated Date**: 2026-04-23

**PDF Url**: [2506.19579v3](https://arxiv.org/pdf/2506.19579v3)

**Abstract**: Robotic scene understanding increasingly relies on Vision-Language Models (VLMs) to generate natural language descriptions of the environment. In this work, we systematically evaluate single-view object captioning for tabletop scenes captured by a robotic manipulator, introducing a controlled physical domain shift that contrasts real-world tools with geometrically similar 3D-printed counterparts that differ in texture, colour, and material. We benchmark a suite of state-of-the-art, locally deployable VLMs across multiple metrics to assess semantic alignment and factual grounding. Our results demonstrate that while VLMs describe common real-world objects effectively, performance degrades markedly on 3D-printed items despite their structurally familiar forms. We further expose critical vulnerabilities in standard evaluation metrics, showing that some fail to detect domain shifts entirely or reward fluent but factually incorrect captions. These findings highlight the limitations of deploying foundation models for embodied agents and the need for more robust architectures and evaluation protocols in physical robotic applications.


## Diffusion
### A Scale-Adaptive Framework for Joint Spatiotemporal Super-Resolution with Diffusion Models
**Authors**: Max Defez, Filippo Quarenghi, Mathieu Vrac, Stephan Mandt, Tom Beucler

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21903v1](https://arxiv.org/pdf/2604.21903v1)

**Abstract**: Deep-learning video super-resolution has progressed rapidly, but climate applications typically super-resolve (increase resolution) either space or time, and joint spatiotemporal models are often designed for a single pair of super-resolution (SR) factors (upscaling spatial and temporal ratio between the low-resolution sequence and the high-resolution sequence), limiting transfer across spatial resolutions and temporal cadences (frame rates). We present a scale-adaptive framework that reuses the same architecture across factors by decomposing spatiotemporal SR into a deterministic prediction of the conditional mean, with attention, and a residual conditional diffusion model, with an optional mass-conservation (same precipitation amount in inputs and outputs) transform to preserve aggregated totals. Assuming that larger SR factors primarily increase underdetermination (hence required context and residual uncertainty) rather than changing the conditional-mean structure, scale adaptivity is achieved by retuning three factor-dependent hyperparameters before retraining: the diffusion noise schedule amplitude beta (larger for larger factors to increase diversity), the temporal context length L (set to maintain comparable attention horizons across cadences) and optionally a third, the mass-conservation function f (tapered to limit the amplification of extremes for large factors). Demonstrated on reanalysis precipitation over France (Comephore), the same architecture spans super-resolution factors from 1 to 25 in space and 1 to 6 in time, yielding a reusable architecture and tuning recipe for joint spatiotemporal super-resolution across scales.


### Quotient-Space Diffusion Models
**Authors**: Yixian Xu, Yusong Wang, Shengjie Luo, Kaiyuan Gao, Tianyu He, Di He, Chang Liu

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21809v1](https://arxiv.org/pdf/2604.21809v1)

**Abstract**: Diffusion-based generative models have reformed generative AI, and have enabled new capabilities in the science domain, for example, generating 3D structures of molecules. Due to the intrinsic problem structure of certain tasks, there is often a symmetry in the system, which identifies objects that can be converted by a group action as equivalent, hence the target distribution is essentially defined on the quotient space with respect to the group. In this work, we establish a formal framework for diffusion modeling on a general quotient space, and apply it to molecular structure generation which follows the special Euclidean group $\text{SE}(3)$ symmetry. The framework reduces the necessity of learning the component corresponding to the group action, hence simplifies learning difficulty over conventional group-equivariant diffusion models, and the sampler guarantees recovering the target distribution, while heuristic alignment strategies lack proper samplers. The arguments are empirically validated on structure generation for small molecules and proteins, indicating that the principled quotient-space diffusion model provides a new framework that outperforms previous symmetry treatments.


### Algebraic Language Models for Inverse Design of Metamaterials via Diffusion Transformers
**Authors**: Li Zheng, Siddhant Kumar, Dennis M. Kochmann

**Published Date**: 2025-07-21

**Updated Date**: 2026-04-23

**PDF Url**: [2507.15753v2](https://arxiv.org/pdf/2507.15753v2)

**Abstract**: Generative machine learning models have revolutionized material discovery by capturing complex structure-property relationships, yet extending these approaches to the inverse design of three-dimensional metamaterials remains limited by computational complexity and underexplored design spaces due to the lack of expressive representations. Here we present DiffuMeta, a generative framework integrating diffusion transformers with an algebraic language representation, encoding three-dimensional geometries as mathematical sentences. This compact, unified parameterization spans diverse topologies, enabling the direct application of transformers to structural design. DiffuMeta leverages diffusion models to generate new shell structures with precisely targeted stress-strain responses under large deformations, accounting for buckling and contact while addressing the inherent one-to-many mapping by producing diverse solutions. Uniquely, our approach enables simultaneous control over multiple mechanical objectives, including linear and nonlinear responses beyond training domains. Experimental validation of fabricated structures further confirms the efficacy of our approach for accelerated design of metamaterials and structures with tailored properties.


### Reasoning on the Manifold: Bidirectional Consistency for Self-Verification in Diffusion Language Models
**Authors**: Jiaoyang Ruan, Xin Gao, Yinda Chen, Hengyu Zeng, Liang Du, Guanghao Li, Jie Fu, Jian Pu

**Published Date**: 2026-04-17

**Updated Date**: 2026-04-23

**PDF Url**: [2604.16565v2](https://arxiv.org/pdf/2604.16565v2)

**Abstract**: While Diffusion Large Language Models (dLLMs) offer structural advantages for global planning, efficiently verifying that they arrive at correct answers via valid reasoning traces remains a critical challenge. In this work, we propose a geometric perspective: Reasoning on the Manifold. We hypothesize that valid generation trajectories reside as stable attractors on the high-density manifold of the learned distribution, whereas invalid paths exhibit off-manifold drift. To operationalize this, we introduce Bidirectional Manifold Consistency (BMC), a training-free, unsupervised metric that quantifies the stability of the generated sequence through a forward-masking and backward-reconstruction cycle. Empirically, we demonstrate BMC's versatility across the full reasoning lifecycle: (1) in Diagnosis, it serves as a robust discriminator of solution validity without ground truth answer; (2) in Inference, it enables rejection resampling to effectively concentrate computational resources on complex reasoning tasks; and (3) in Alignment, it functions as a dense geometric reward that transforms sparse outcome supervision into fine-grained guidance, empowering models to self-evolve beyond standard baselines. Our results establish intrinsic geometric stability as a robust indicator of correctness for dLLMs.


## Quantitative Finance
### Research Streams in Biodiversity Finance: A Bibliometric Analysis and Research Agenda
**Authors**: Lennart Ante, Friedrich-Philipp Wazinski, Aman Saggu

**Published Date**: 2026-04-23

**Updated Date**: 2026-04-23

**PDF Url**: [2604.21569v1](https://arxiv.org/pdf/2604.21569v1)

**Abstract**: Biodiversity loss is accelerating at an unprecedented pace, threatening ecosystem stability, economic resilience, and human well-being, with billions required to reverse current trends. Against this backdrop, biodiversity finance has emerged as a rapidly expanding but highly fragmented field spanning ecology, economics, finance, accounting, and policy. However, it remains emerging and complex, with the majority of relevant knowledge being produced in non-finance journals. This study employs quantitative bibliometric analysis to examine a corpus of 189,456 references underlying 3,998 articles related to biodiversity and finance. The analysis identifies eight primary research streams within the field that concern (1) strategic and financial approaches in global biodiversity conservation, (2) the impact and implementation of payments for environmental services (PES) in developing countries, (3) neoliberal influences and implications in environmental conservation, (4) biodiversity offsets and conservation, (5) ecosystem services and biodiversity, (6) integrating conservation and community interests in biodiversity management, (7) balancing agricultural intensification with biodiversity conservation, and (8) global and corporate biodiversity reporting. The characteristics of each research stream and its prevalent publications are outlined, alongside an analysis of their temporal evolution and the degree of information exchange among the research streams. The findings provide a structured map of the intellectual architecture of biodiversity finance, document pronounced silos between economically-oriented and critical/political-economy research streams, and translate these patterns into a focused research agenda and implications for policymakers, financial institutions, and corporate actors.


### Deep FinResearch Bench: Evaluating AI's Ability to Conduct Professional Financial Investment Research
**Authors**: Mirazul Haque, Antony Papadimitriou, Samuel Mensah, Zhiqiang Ma, Zhijin Guo, Joy Prakash Sain, Simerjot Kaur, Charese Smiley, Xiaomo Liu

**Published Date**: 2026-04-22

**Updated Date**: 2026-04-22

**PDF Url**: [2604.21006v1](https://arxiv.org/pdf/2604.21006v1)

**Abstract**: We introduce Deep FinResearch Bench, a practical and comprehensive evaluation framework for deep research (DR) agents in financial investment research. The benchmark assesses three dimensions of report quality: qualitative rigor, quantitative forecasting and valuation accuracy, and claim credibility and verifiability. Particularly, we define corresponding qualitative and quantitative evaluation metrics and implement an automated scoring procedure to enable scalable assessment. Applying the benchmark to financial reports from frontier DR agents and comparing them with reports authored by financial professionals, we find that AI-generated reports still fall short across these dimensions. These findings underscore the need for domain-specialized DR agents tailored to finance, and we hope the work establishes a foundation for standardized benchmarking of DR agents in financial research.


