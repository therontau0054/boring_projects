# Abstracts of Papers

## Physics
### Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage
**Authors**: Xin Ju, Jiachen Yao, Anima Anandkumar, Sally M. Benson, Gege Wen

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12274v1](https://arxiv.org/pdf/2602.12274v1)

**Abstract**: Accurate characterization of subsurface flow is critical for Carbon Capture and Storage (CCS) but remains challenged by the ill-posed nature of inverse problems with sparse observations. We present Fun-DDPS, a generative framework that combines function-space diffusion models with differentiable neural operator surrogates for both forward and inverse modeling. Our approach learns a prior distribution over geological parameters (geomodel) using a single-channel diffusion model, then leverages a Local Neural Operator (LNO) surrogate to provide physics-consistent guidance for cross-field conditioning on the dynamics field. This decoupling allows the diffusion prior to robustly recover missing information in parameter space, while the surrogate provides efficient gradient-based guidance for data assimilation. We demonstrate Fun-DDPS on synthetic CCS modeling datasets, achieving two key results: (1) For forward modeling with only 25% observations, Fun-DDPS achieves 7.7% relative error compared to 86.9% for standard surrogates (an 11x improvement), proving its capability to handle extreme data sparsity where deterministic methods fail. (2) We provide the first rigorous validation of diffusion-based inverse solvers against asymptotically exact Rejection Sampling (RS) posteriors. Both Fun-DDPS and the joint-state baseline (Fun-DPS) achieve Jensen-Shannon divergence less than 0.06 against the ground truth. Crucially, Fun-DDPS produces physically consistent realizations free from the high-frequency artifacts observed in joint-state baselines, achieving this with 4x improved sample efficiency compared to rejection sampling.


### Decoupled Diffusion Sampling for Inverse Problems on Function Spaces
**Authors**: Thomas Y. L. Lin, Jiachen Yao, Lufang Chiang, Julius Berner, Anima Anandkumar

**Published Date**: 2026-01-30

**Updated Date**: 2026-02-12

**PDF Url**: [2601.23280v2](https://arxiv.org/pdf/2601.23280v2)

**Abstract**: We propose a data-efficient, physics-aware generative framework in function space for inverse PDE problems. Existing plug-and-play diffusion posterior samplers represent physics implicitly through joint coefficient-solution modeling, requiring substantial paired supervision. In contrast, our Decoupled Diffusion Inverse Solver (DDIS) employs a decoupled design: an unconditional diffusion learns the coefficient prior, while a neural operator explicitly models the forward PDE for guidance. This decoupling enables superior data efficiency and effective physics-informed learning, while naturally supporting Decoupled Annealing Posterior Sampling (DAPS) to avoid over-smoothing in Diffusion Posterior Sampling (DPS). Theoretically, we prove that DDIS avoids the guidance attenuation failure of joint models when training data is scarce. Empirically, DDIS achieves state-of-the-art performance under sparse observation, improving $l_2$ error by 11% and spectral error by 54% on average; when data is limited to 1%, DDIS maintains accuracy with 40% advantage in $l_2$ error compared to joint models.


### Coprime Bivariate Bicycle Codes and Their Layouts on Cold Atoms
**Authors**: Ming Wang, Frank Mueller

**Published Date**: 2024-08-19

**Updated Date**: 2026-02-12

**PDF Url**: [2408.10001v6](https://arxiv.org/pdf/2408.10001v6)

**Abstract**: Quantum computing is deemed to require error correction at scale to mitigate physical noise by reducing it to lower noise levels while operating on encoded logical qubits. Popular quantum error correction schemes include CSS code, of which surface codes provide regular mappings onto 2D planes suitable for contemporary quantum devices together with known transversal logical gates. Recently, qLDPC codes have been proposed as a means to provide denser encoding with the class of bivariate bicycle (BB) codes promising feasible design for devices.
  This work contributes a novel subclass of BB codes suitable for quantum error correction. This subclass employs {\em coprimes} and the product $xy$ of the two generating variables $x$ and $y$ to construct polynomials, rather than using $x$ and $y$ separately as in vanilla BB codes. In contrast to vanilla BB codes, where parameters remain unknown prior to code discovery, the rate of the proposed code can be determined beforehand by specifying a factor polynomial as an input to the numerical search algorithm. Using this coprime-BB construction, we found a number of surprisingly short to medium-length codes that were previously unknown. We also propose a layout on cold atom arrays tailored for coprime-BB codes. The proposed layout reduces both move time for short to medium-length codes and the number of moves of atoms to perform syndrome extractions. We consider an error model with global laser noise on cold atoms, and simulations show that our proposed layout achieves significant improvements over prior work across the simulated codes.


### Holographic Equidistribution
**Authors**: Nico Cooper

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12265v1](https://arxiv.org/pdf/2602.12265v1)

**Abstract**: Hecke operators acting on modular functions arise naturally in the context of 2d conformal field theory, but in seemingly disparate areas, including permutation orbifold theories, ensembles of code CFTs, and more recently in the context of the AdS$_3$/RMT$_2$ program. We use an equidistribution theorem for Hecke operators to show that in each of these large $N$ limits, an entire heavy sector of the partition function gets integrated out, leaving only contributions from Poincaré series of light states. This gives an immediate holographic interpretation as a sum over semiclassical handlebody geometries. We speculate on further physical interpretations for equidistribution, including a potential ergodicity statement.


### Zero and Nonzero Energy Majorana Modes in an Extended Kitaev Chain
**Authors**: Mohammad Ghuneim, Raditya Weda Bomantara

**Published Date**: 2025-09-04

**Updated Date**: 2026-02-12

**PDF Url**: [2509.04420v2](https://arxiv.org/pdf/2509.04420v2)

**Abstract**: This paper studies an extended Kitaev chain with three sublattices per unit cell. This extended version is obtained by hybridizing a modified Su-Schrieffer-Heeger model featuring trimerized unit cells with the standard Kitaev chain, resulting in a hexamer structure on the Majorana basis. Due to the interplay between the sublattice configuration and the $p$-wave superconducting pairing, a rich structure of edge modes beyond the expected Majorana zero modes is obtained. The various Majorana edge modes are further found to demonstrate considerable robustness against some generic perturbations and disorder. The presence of the non-zero Majorana edge modes in our system has the potential advantage that they could, in principle, be more unambiguously detected as compared to their zero energy counterparts, the detection of which remains an open problem. Therefore, while our system does not directly solve this open problem, it potentially offers a route to an intermediate solution that involves unambiguously detecting non-zero energy Majorana edge modes instead.


### Think like a Scientist: Physics-guided LLM Agent for Equation Discovery
**Authors**: Jianke Yang, Ohm Venkatachalam, Mohammad Kianezhad, Sharvaree Vadgama, Rose Yu

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12259v1](https://arxiv.org/pdf/2602.12259v1)

**Abstract**: Explaining observed phenomena through symbolic, interpretable formulas is a fundamental goal of science. Recently, large language models (LLMs) have emerged as promising tools for symbolic equation discovery, owing to their broad domain knowledge and strong reasoning capabilities. However, most existing LLM-based systems try to guess equations directly from data, without modeling the multi-step reasoning process that scientists often follow: first inferring physical properties such as symmetries, then using these as priors to restrict the space of candidate equations. We introduce KeplerAgent, an agentic framework that explicitly follows this scientific reasoning process. The agent coordinates physics-based tools to extract intermediate structure and uses these results to configure symbolic regression engines such as PySINDy and PySR, including their function libraries and structural constraints. Across a suite of physical equation benchmarks, KeplerAgent achieves substantially higher symbolic accuracy and greater robustness to noisy data than both LLM and traditional baselines.


### EGG-SR: Embedding Symbolic Equivalence into Symbolic Regression via Equality Graph
**Authors**: Nan Jiang, Ziyi Wang, Yexiang Xue

**Published Date**: 2025-11-08

**Updated Date**: 2026-02-12

**PDF Url**: [2511.05849v2](https://arxiv.org/pdf/2511.05849v2)

**Abstract**: Symbolic regression seeks to uncover physical laws from experimental data by searching for closed-form expressions, which is an important task in AI-driven scientific discovery. Yet the exponential growth of the search space of expression renders the task computationally challenging. A promising yet underexplored direction for reducing the search space and accelerating training lies in *symbolic equivalence*: many expressions, although syntactically different, define the same function -- for example, $\log(x_1^2x_2^3)$, $\log(x_1^2)+\log(x_2^3)$, and $2\log(x_1)+3\log(x_2)$. Existing algorithms treat such variants as distinct outputs, leading to redundant exploration and slow learning. We introduce EGG-SR, a unified framework that integrates symbolic equivalence into a class of modern symbolic regression methods, including Monte Carlo Tree Search (MCTS), Deep Reinforcement Learning (DRL), and Large Language Models (LLMs). EGG-SR compactly represents equivalent expressions through the proposed EGG module (via equality graphs), accelerating learning by: (1) pruning redundant subtree exploration in EGG-MCTS, (2) aggregating rewards across equivalent generated sequences in EGG-DRL, and (3) enriching feedback prompts in EGG-LLM. Theoretically, we show the benefit of embedding EGG into learning: it tightens the regret bound of MCTS and reduces the variance of the DRL gradient estimator. Empirically, EGG-SR consistently enhances a class of symbolic regression models across several benchmarks, discovering more accurate expressions within the same time limit. Project page is at: https://nan-jiang-group.github.io/egg-sr.


### Extending the Cosmological Collider: New Scaling Regimes and Constraints from BOSS
**Authors**: Daniel Green, Jiashu Han, Benjamin Wallisch

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12232v1](https://arxiv.org/pdf/2602.12232v1)

**Abstract**: Primordial non-Gaussianity generated by additional fields during inflation offers a compelling observational target. Heavy fields imprint characteristic oscillatory signals in non-Gaussian correlation functions of the inflaton, a process sometimes referred to as cosmological-collider physics. These distinct signatures are compelling windows into ultra-high-energy physics, but are often suppressed, making standard equilateral non-Gaussianity the most promising discovery channel in many scenarios. In this paper, we show that direct couplings between the inflaton and additional fields can lead to a wide variety of novel, observationally relevant signals which open new parameter regimes that simultaneously exhibit the characteristics of light and heavy fields. We identify these primordial signatures in the late-time observables of the large-scale structure of the Universe, where they most significantly modify the scale-dependent bias of the galaxy power spectrum to include an oscillatory modulation around a non-trivial power law. We explore the full range of parameters that phenomenologically arise in these models and study the sensitivity of current and future galaxy surveys, finding that this new class of primordial non-Gaussianity is particularly accessible in near-term surveys due to its oscillatory feature. Finally, we perform an analysis of existing data from the final release of the Baryon Oscillation Spectroscopic Survey (BOSS DR12). While we find no evidence for a signal, we demonstrate significant improvements in sensitivity over respective non-oscillatory scenarios and place the first constraints on this extended parameter space of oscillatory non-Gaussianity.


### Phase Estimation from Amplitude Collapse in Correlated Matter-Wave Interference
**Authors**: Daniel Derr, Dominik Pfeiffer, Ludwig Lind, Gerhard Birkl, Enno Giese

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12227v1](https://arxiv.org/pdf/2602.12227v1)

**Abstract**: Operating matter-wave interferometers as quantum detectors for fundamental physics or inertial sensors in real-world applications with unprecedented accuracies relies on noise rejection, often implemented by correlating two sensors. Such sensors can be spatially separated (gradiometry or gravitational-wave detection) or consist of different internal states (magnetometry or quantum clock interferometry), in which case a signal-amplitude modulation may serve as a signature of a differential phase. In this work, we introduce Phase Estimation from Amplitude Collapse (PEAC) by applying targeted fitting methods for different magnetically sensitive substates of an atom interferometer. We demonstrate that PEAC provides higher trueness (up to 80% bias reduction) than standard tools for perfectly correlated signals. At its working point near, but not exactly at phase settings resulting in vanishing amplitude, it achieves precision competitive with standard methods, contrasting prior claims of optimal operation at vanishing amplitude. PEAC presents a generally applicable complementary evaluation method for correlated interferometers without phase stability, increasing the overall accuracy and enabling applications beyond atom interferometry.


### The Observer Effect in World Models: Invasive Adaptation Corrupts Latent Physics
**Authors**: Christian Internò, Jumpei Yamaguchi, Loren Amdahl-Culleton, Markus Olhofer, David Klindt, Barbara Hammer

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12218v1](https://arxiv.org/pdf/2602.12218v1)

**Abstract**: Determining whether neural models internalize physical laws as world models, rather than exploiting statistical shortcuts, remains challenging, especially under out-of-distribution (OOD) shifts. Standard evaluations often test latent capability via downstream adaptation (e.g., fine-tuning or high-capacity probes), but such interventions can change the representations being measured and thus confound what was learned during self-supervised learning (SSL). We propose a non-invasive evaluation protocol, PhyIP. We test whether physical quantities are linearly decodable from frozen representations, motivated by the linear representation hypothesis. Across fluid dynamics and orbital mechanics, we find that when SSL achieves low error, latent structure becomes linearly accessible. PhyIP recovers internal energy and Newtonian inverse-square scaling on OOD tests (e.g., $ρ> 0.90$). In contrast, adaptation-based evaluations can collapse this structure ($ρ\approx 0.05$). These findings suggest that adaptation-based evaluation can obscure latent structures and that low-capacity probes offer a more accurate evaluation of physical world models.


## Diffusion
### MonarchRT: Efficient Attention for Real-Time Video Generation
**Authors**: Krish Agarwal, Zhuoming Chen, Cheng Luo, Yongqi Chen, Haizhong Zheng, Xun Huang, Atri Rudra, Beidi Chen

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12271v1](https://arxiv.org/pdf/2602.12271v1)

**Abstract**: Real-time video generation with Diffusion Transformers is bottlenecked by the quadratic cost of 3D self-attention, especially in real-time regimes that are both few-step and autoregressive, where errors compound across time and each denoising step must carry substantially more information. In this setting, we find that prior sparse-attention approximations break down, despite showing strong results for bidirectional, many-step diffusion. Specifically, we observe that video attention is not reliably sparse, but instead combines pronounced periodic structure driven by spatiotemporal position with dynamic, sparse semantic correspondences and dense mixing, exceeding the representational capacity of even oracle top-k attention. Building on this insight, we propose Monarch-RT, a structured attention parameterization for video diffusion models that factorizes attention using Monarch matrices. Through appropriately aligned block structure and our extended tiled Monarch parameterization, we achieve high expressivity while preserving computational efficiency. We further overcome the overhead of parameterization through finetuning, with custom Triton kernels. We first validate the high efficacy of Monarch-RT over existing sparse baselines designed only for bidirectional models. We further observe that Monarch-RT attains up to 95% attention sparsity with no loss in quality when applied to the state-of-the-art model Self-Forcing, making Monarch-RT a pioneering work on highly-capable sparse attention parameterization for real-time video generation. Our optimized implementation outperforms FlashAttention-2, FlashAttention-3, and FlashAttention-4 kernels on Nvidia RTX 5090, H100, and B200 GPUs respectively, providing kernel speedups in the range of 1.4-11.8X. This enables us, for the first time, to achieve true real-time video generation with Self-Forcing at 16 FPS on a single RTX 5090.


### T3D: Few-Step Diffusion Language Models via Trajectory Self-Distillation with Direct Discriminative Optimization
**Authors**: Tunyu Zhang, Xinxi Zhang, Ligong Han, Haizhou Shi, Xiaoxiao He, Zhuowei Li, Hao Wang, Kai Xu, Akash Srivastava, Hao Wang, Vladimir Pavlovic, Dimitris N. Metaxas

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12262v1](https://arxiv.org/pdf/2602.12262v1)

**Abstract**: Diffusion large language models (DLLMs) have the potential to enable fast text generation by decoding multiple tokens in parallel. However, in practice, their inference efficiency is constrained by the need for many refinement steps, while aggressively reducing the number of steps leads to a substantial degradation in generation quality. To alleviate this, we propose a trajectory self-distillation framework that improves few-step decoding by distilling the model's own generative trajectories. We incorporate Direct Discriminative Optimization (DDO), a reverse-KL objective that promotes mode-seeking distillation and encourages the student to concentrate on high-probability teacher modes. Across benchmarks, our approach consistently outperforms strong few-step baselines and standard training under tight step budgets. Although full-step decoding remains superior, we substantially narrow the gap, establishing a strong foundation towards practical few-step DLLMs. The source code is available at https://github.com/Tyrion58/T3D.


### On the implicit regularization of Langevin dynamics with projected noise
**Authors**: Govind Menon, Austin J. Stromme, Adrien Vacher

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12257v1](https://arxiv.org/pdf/2602.12257v1)

**Abstract**: We study Langevin dynamics with noise projected onto the directions orthogonal to an isometric group action. This mathematical model is introduced to shed new light on the effects of symmetry on stochastic gradient descent for over-parametrized models. Our main result identifies a novel form of implicit regularization: when the initial and target density are both invariant under the group action, Langevin dynamics with projected noise is equivalent in law to Langevin dynamics with isotropic diffusion but with an additional drift term proportional to the negative log volume of the group orbit. We prove this result by constructing a coupling of the two processes via a third process on the group itself, and identify the additional drift as the mean curvature of the orbits.


### Categorical Flow Maps
**Authors**: Daan Roos, Oscar Davis, Floor Eijkelboom, Michael Bronstein, Max Welling, İsmail İlkan Ceylan, Luca Ambrogioni, Jan-Willem van de Meent

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.12233v1](https://arxiv.org/pdf/2602.12233v1)

**Abstract**: We introduce Categorical Flow Maps, a flow-matching method for accelerated few-step generation of categorical data via self-distillation. Building on recent variational formulations of flow matching and the broader trend towards accelerated inference in diffusion and flow-based models, we define a flow map towards the simplex that transports probability mass toward a predicted endpoint, yielding a parametrisation that naturally constrains model predictions. Since our trajectories are continuous rather than discrete, Categorical Flow Maps can be trained with existing distillation techniques, as well as a new objective based on endpoint consistency. This continuous formulation also automatically unlocks test-time inference: we can directly reuse existing guidance and reweighting techniques in the categorical setting to steer sampling toward downstream objectives. Empirically, we achieve state-of-the-art few-step results on images, molecular graphs, and text, with strong performance even in single-step generation.


## Quantitative Finance
### MEME: Modeling the Evolutionary Modes of Financial Markets
**Authors**: Taian Guo, Haiyang Shen, Junyu Luo, Zhongshi Xing, Hanchun Lian, Jinsheng Huang, Binqi Chen, Luchen Liu, Yun Ma, Ming Zhang

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.11918v1](https://arxiv.org/pdf/2602.11918v1)

**Abstract**: LLMs have demonstrated significant potential in quantitative finance by processing vast unstructured data to emulate human-like analytical workflows. However, current LLM-based methods primarily follow either an Asset-Centric paradigm focused on individual stock prediction or a Market-Centric approach for portfolio allocation, often remaining agnostic to the underlying reasoning that drives market movements. In this paper, we propose a Logic-Oriented perspective, modeling the financial market as a dynamic, evolutionary ecosystem of competing investment narratives, termed Modes of Thought. To operationalize this view, we introduce MEME (Modeling the Evolutionary Modes of Financial Markets), designed to reconstruct market dynamics through the lens of evolving logics. MEME employs a multi-agent extraction module to transform noisy data into high-fidelity Investment Arguments and utilizes Gaussian Mixture Modeling to uncover latent consensus within a semantic space. To model semantic drift among different market conditions, we also implement a temporal evaluation and alignment mechanism to track the lifecycle and historical profitability of these modes. By prioritizing enduring market wisdom over transient anomalies, MEME ensures that portfolio construction is guided by robust reasoning. Extensive experiments on three heterogeneous Chinese stock pools from 2023 to 2025 demonstrate that MEME consistently outperforms seven SOTA baselines. Further ablation studies, sensitivity analysis, lifecycle case study and cost analysis validate MEME's capacity to identify and adapt to the evolving consensus of financial markets. Our implementation can be found at https://github.com/gta0804/MEME.


### AlphaPROBE: Alpha Mining via Principled Retrieval and On-graph biased evolution
**Authors**: Taian Guo, Haiyang Shen, Junyu Luo, Binqi Chen, Hongjun Ding, Jinsheng Huang, Luchen Liu, Yun Ma, Ming Zhang

**Published Date**: 2026-02-12

**Updated Date**: 2026-02-12

**PDF Url**: [2602.11917v1](https://arxiv.org/pdf/2602.11917v1)

**Abstract**: Extracting signals through alpha factor mining is a fundamental challenge in quantitative finance. Existing automated methods primarily follow two paradigms: Decoupled Factor Generation, which treats factor discovery as isolated events, and Iterative Factor Evolution, which focuses on local parent-child refinements. However, both paradigms lack a global structural view, often treating factor pools as unstructured collections or fragmented chains, which leads to redundant search and limited diversity. To address these limitations, we introduce AlphaPROBE (Alpha Mining via Principled Retrieval and On-graph Biased Evolution), a framework that reframes alpha mining as the strategic navigation of a Directed Acyclic Graph (DAG). By modeling factors as nodes and evolutionary links as edges, AlphaPROBE treats the factor pool as a dynamic, interconnected ecosystem. The framework consists of two core components: a Bayesian Factor Retriever that identifies high-potential seeds by balancing exploitation and exploration through a posterior probability model, and a DAG-aware Factor Generator that leverages the full ancestral trace of factors to produce context-aware, nonredundant optimizations. Extensive experiments on three major Chinese stock market datasets against 8 competitive baselines demonstrate that AlphaPROBE significantly gains enhanced performance in predictive accuracy, return stability and training efficiency. Our results confirm that leveraging global evolutionary topology is essential for efficient and robust automated alpha discovery. We have open-sourced our implementation at https://github.com/gta0804/AlphaPROBE.


