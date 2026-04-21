# Abstracts of Papers

## Physics
### Physics-Informed Neural Networks for Biological $2\mathrm{D}{+}t$ Reaction-Diffusion Systems
**Authors**: William Lavery, Jodie A. Cochrane, Christian Olesen, Dagim S. Tadele, John T. Nardini, Sara Hamis

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18548v1](https://arxiv.org/pdf/2604.18548v1)

**Abstract**: Physics-informed neural networks (PINNs) provide a powerful framework for learning governing equations of dynamical systems from data. Biologically-informed neural networks (BINNs) are a variant of PINNs that preserve the known differential operator structure (e.g., reaction-diffusion) while learning constitutive terms via trainable neural subnetworks, enforced through soft residual penalties. Existing BINN studies are limited to $1\mathrm{D}{+}t$ reaction-diffusion systems and focus on forward prediction, using the governing partial differential equation as a regulariser rather than an explicit identification target. Here, we extend BINNs to $2\mathrm{D}{+}t$ systems within a PINN framework that combines data preprocessing, BINN-based equation learning, and symbolic regression post-processing for closed-form equation discovery. We demonstrate the framework's real-world applicability by learning the governing equations of lung cancer cell population dynamics from time-lapse microscopy data, recovering $2\mathrm{D}{+}t$ reaction-diffusion models from experimental observations. The proposed framework is readily applicable to other spatio-temporal systems, providing a practical and interpretable tool for fast analytic equation discovery from data.


### AtomTwin.jl: a physics-native digital twin framework for neutral-atom quantum processors
**Authors**: Shannon Whitlock

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18531v1](https://arxiv.org/pdf/2604.18531v1)

**Abstract**: AtomTwin$.$jl is an open-source Julia package for developing and simulating quantum protocols, hardware configurations and building digital twins for neutral-atom quantum processors and related atomic quantum devices. AtomTwin operates between mathematical models and physical devices; modeling atoms, optical tweezers, laser fields, atomic motion, interactions, and noise processes natively from physical geometry and parameters, without requiring users to define Hamiltonians manually. The package provides hardware-level instruction sequences, high-performance solvers for coupled quantum and classical dynamics, and a ready-to-use model for ytterbium-171 atoms in an extensible framework designed to accommodate a greater variety of atomic species and hardware components in the future. This paper describes the software architecture, performance benchmarks against existing toolboxes, and a demonstrated end-to-end application: preparation of a logical Bell state in the $[[4,2,2]]$ error-detecting code with four $^{171}$Yb atoms in moveable tweezers.


### Tunable Optical Torque by Asymmetry-Induced Spin-Hall Effect in Tightly Focused Spinless Gaussian Beams
**Authors**: Sauvik Roy, Ram Nandan Kumar, Biswajit Das, Nirmalya Ghosh, Subhasish Dutta Gupta, Ayan Banerjee

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18514v1](https://arxiv.org/pdf/2604.18514v1)

**Abstract**: A linearly polarized Gaussian beam, carrying zero net spin angular momentum, is conventionally not expected to exert optical torque or induce rotational motion in birefringent microparticles. When such a beam is tightly focused, the constituent left- and right-circular polarization components separate spatially due to spin-orbit interaction, commonly known as the spin Hall effect of light. However, this separation is at wavelength scales and is also axially symmetric, resulting in zero net spin angular momentum, and concomitantly no optical torque near the focal plane. Here, we demonstrate that this limitation can be overcome using several commonly encountered asymmetric illumination modalities that break the axial symmetry of the focusing system, thereby disrupting the symmetric separation of the spin components for the same linearly polarized Gaussian beam. As a consequence, trapped microparticles experience a tunable optical torque and exhibit rotational motion with distinct rotational frequencies at the same input power. The particles also undergo controlled reversal of the rotation direction simply by rotating the incident plane of polarization using a half-wave plate. Despite their apparent diversity, all these methods share the same physical origin rooted in asymmetric illumination. These results establish an experimentally accessible and minimal strategy for realizing controllable optical rotation devices exploiting spin-orbit optomechanics without requiring intrinsic angular momentum in the light.


### Physics-Informed Neural Networks for Maximizing Quantum Fisher Information in Time-Dependent Many-Body Systems
**Authors**: Antonio Ferrer-Sánchez, Yolanda Vives-Gilabert, Yue Ban, Xi Chen, José D. Martín-Guerrero

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18506v1](https://arxiv.org/pdf/2604.18506v1)

**Abstract**: Quantum Fisher Information (QFI) sets the ultimate precision limit for parameter estimation and is therefore a central quantity in quantum metrology. In time-dependent many-body systems, however, maximizing QFI is a highly non-trivial task due to the combined effects of non-commutativity, control complexity, and the exponential growth of the Hilbert space. In this work, we present a physics-informed neural network (PINN) framework to address this problem through the learning of counter-diabatic quantum dynamics. Our approach combines a variational PINN formulation with a Magnus-expansion treatment of time-ordered evolution, enabling the adiabatic gauge potential and the scheduling function to be inferred directly from the underlying physics while enforcing the Euler-Lagrange structure of the protocol. The method is applied to several families of driven spin Hamiltonians, including nearest-neighbor, dipolar, and trapped-ion-inspired interactions, for systems of up to six qubits. The numerical results show that the proposed framework systematically improves over reference solutions based only on the Euler-Lagrange condition, yielding high normalized QFI together with favorable fidelity and extremal-balance metrics while preserving small phsical residuals. The analysis further shows that learning the scheduling function provides a clear performance advantage in most cases, and reveals non-trivial finite-size effects, with $q=3$ emerging as a particularly challenging regime. Although scalability remains limited by the exponential growth of the operator space and by automatic-differentiation costs, the results demonstrate that PINNs constitute a viable and physically grounded route for learning metrologically optimal control strategies in interacting quantum systems.


### Multiscale phase dynamics and $2π$ phase kinks in injection-locked optoelectronic oscillators with large delay
**Authors**: Abhijit Banerjee, Trevor J. Hall

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18499v1](https://arxiv.org/pdf/2604.18499v1)

**Abstract**: Injection locking of optoelectronic oscillators (OEOs) with large delay gives rise to phase dynamics that lie beyond the scope of classical single mode locking theory, including the spontaneous formation of persistent $2π$ phase kinks. In this work, a multiscale theoretical framework is developed that explains the origin, structure, and stability of these phase slip phenomena in injection locked (IL) OEOs operating in large-delay regime. Starting from a complex envelope delay differential equation that explicitly incorporates hard-limiting gain saturation and RF BPF dynamics, a reduced phase-only description valid for nearly constant oscillation amplitude is derived. Exploiting the separation between fast round-trip dynamics and slow inter-round-trip evolution, a two-timescale reduction yields a continuum of Adler equations governing phase difference between injected signal and oscillator as a function of round-trip time. Analytical solutions obtained for weak injection and small detuning show how initially smooth phase profiles sharpen into localized $2π$ phase kinks, with p kinks appearing per round trip when the injection is tuned near the pth adjacent mode. Time-domain simulations of full complex-envelope model validate the predicted phase kink formation mechanism and reveal essential role of RF resonator dynamics in determining their persistence. While the reduced phase-only model correctly predicts kink sharpening, resonator-induced amplitude excursions associated with steep phase gradients can erase the kinks when the complex-envelope trajectory fails to encircle the origin, restoring conventional phase locking. These results provide a unified physical interpretation of $2π$phase kinks in IL-OEOs and delineate the limits of phase-only models in the presence of large, fast phase transients, identifying a regime of frequency locking without phase locking in large delay oscillators.


### NO LESS: Novel Opportunities for Light Exotic Searches at the SPS
**Authors**: Babette Döbrich, Jan Jerhot, Karim Massri, Jonathan L. Schubert, Tommaso Spadaro

**Published Date**: 2026-01-23

**Updated Date**: 2026-04-20

**PDF Url**: [2601.17119v2](https://arxiv.org/pdf/2601.17119v2)

**Abstract**: A powerful way to test models with feebly interacting particles in the MeV to GeV mass range is through proton beam-dump experiments. In this paper, we compare the current sensitivity of CERN's NA62 experiment running in beam-dump mode with that of a hypothetical experiment using the same detectors in a future CERN ECN3 beam-dump facility. When optimising such an experiment, the geometric setup is particularly relevant for the specific new-physics scenario under study, since different production mechanisms can generate different angular distributions of new particles. We show that even the most minimalistic reconfiguration of the existing NA62 experiment's detectors can already provide a very competitive sensitivity and collect data immediately after the beam is available.


### Latent Space Dynamics Identification for Interface Tracking with Application to Shock-Induced Pore Collapse
**Authors**: Seung Whan Chung, Christopher Miller, Youngsoo Choi, Paul Tranquilli, H. Keo Springer, Kyle Sullivan

**Published Date**: 2025-07-14

**Updated Date**: 2026-04-20

**PDF Url**: [2507.10647v2](https://arxiv.org/pdf/2507.10647v2)

**Abstract**: Capturing sharp, evolving interfaces remains a central challenge in reduced-order modeling, especially when data is limited and the system exhibits localized nonlinearities or discontinuities. We propose LaSDI-IT (Latent Space Dynamics Identification for Interface Tracking), a data-driven framework that combines low-dimensional latent dynamics learning with explicit interface-aware encoding to enable accurate and efficient modeling of physical systems involving moving material boundaries. At the core of LaSDI-IT is a revised auto-encoder architecture that jointly reconstructs the physical field and an indicator function representing material regions or phases, allowing the model to track complex interface evolution without requiring detailed physical models or mesh adaptation. The latent dynamics are learned through linear regression in the encoded space and generalized across parameter regimes using Gaussian process interpolation with greedy sampling. We demonstrate LaSDI-IT on the problem of shock-induced pore collapse in high explosives, a process characterized by sharp temperature gradients and dynamically deforming pore geometries. The method achieves relative prediction errors below 9% across the parameter space, accurately recovers key quantities of interest such as pore area and hot spot formation, and matches the performance of dense training with only half the data. This latent dynamics prediction was 106 times faster than the conventional high-fidelity simulation, proving its utility for multi-query applications. These results highlight LaSDI-IT as a general, data-efficient framework for modeling discontinuity-rich systems in computational physics, with potential applications in multiphase flows, fracture mechanics, and phase change problems.


### Steadily moving semi-infinite fracture in plane poroelasticity
**Authors**: Evgenii Kanin, Andreas Möri, Dmitry Garagash, Brice Lecampion

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18483v1](https://arxiv.org/pdf/2604.18483v1)

**Abstract**: We present a fully coupled boundary integral formulation for modeling steadily propagating semi-infinite plane strain fractures in poroelastic media. By combining fundamental solutions of plain strain poroelasticity for instantaneous fluid source and edge dislocations (normal and slip modes) with temporal and spatial superposition principles, we derive boundary integral equations governing the tractions (normal and shear stresses) and pore fluid pressure on the fracture surfaces. Assuming prescribed tractions and pore fluid pressure profiles, we develop a numerical methodology to solve the governing equations for fracture opening, slip, and cumulative fluid exchange rate. The formulation is systematically verified on several relevant problems, including the case of a tensile fracture with exponential normal loading, a stress-free tensile fracture with an imposed exponential pore fluid pressure, and a shear fracture under uniform shear loading over a finite region, demonstrating excellent agreement with analytical solutions. The framework provides a robust tool for analyzing coupled fracture-fluid interactions in permeable poroelastic media and can be adapted to broader classes of elasto-diffusive problems by modifying the underlying physical parameters.


### Physics-Informed Neural Networks: A Didactic Derivation of the Complete Training Cycle
**Authors**: Abdeladhim Tahimi

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18481v1](https://arxiv.org/pdf/2604.18481v1)

**Abstract**: This paper is a step-by-step, self-contained guide to the complete training cycle of a Physics-Informed Neural Network (PINN) -- a topic that existing tutorials and guides typically delegate to automatic differentiation libraries without exposing the underlying algebra. Using a first-order initial value problem with a known analytical solution as a running example, we walk through every stage of the process: forward propagation of both the network output and its temporal derivative, evaluation of a composite loss function built from the ODE residual and the initial condition, backpropagation of gradients -- with particular attention to the product rule that arises in hidden layers -- and a gradient descent parameter update. Every calculation is presented with explicit, verifiable numerical values using a 1-3-3-1 multilayer perceptron with two hidden layers and 22 trainable parameters. From these concrete examples, we derive general recursive formulas -- expressed as sensitivity propagation relations -- that extend the gradient computation to networks of arbitrary depth, and we connect these formulas to the automatic differentiation engines used in practice. The trained network is then validated against the exact solution, achieving a relative $L^2$ error of $4.290 \times 10^{-4}$ using only the physics-informed loss, without any data from the true solution. A companion Jupyter/PyTorch notebook reproduces every manual calculation and the full training pipeline, providing mutual validation between hand-derived and machine-computed gradients.


### pyTRAIN -- a modern TRAIN implementation
**Authors**: Michi Hostettler, Xavier Buffat, Tobias Persson, Tatiana Pieloni, Jorg Wenninger

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18466v1](https://arxiv.org/pdf/2604.18466v1)

**Abstract**: The TRAIN code, developed in 1995 as a post-processor for second-order transport maps from MAD, has been used extensively at the LEP and the LHC to study self-consistent closed orbits, tunes and chromaticities of bunch trains under the presence of beam-beam long-range (BBLR) and PACMAN effects.. This paper presents a modern re-implementation of the TRAIN concept in Python using well-known numeric libraries (numpy, scipy) and an optional link to MAD-X via cpymad. This greatly improves the usability, maintainability and extensibility of the code. New functionality includes the support for arbitrary particle types, an arbitrary number and distribution of beam-beam interaction points, and the extrapolation of the beam-beam induced closed-orbit effects to arbitrary points in the machine. The code is benchmarked against the classic TRAIN code, and simulation results are compared to observations from LHC physics operation.


## Diffusion
### Sessa: Selective State Space Attention
**Authors**: Liubomyr Horbatko

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18580v1](https://arxiv.org/pdf/2604.18580v1)

**Abstract**: Modern sequence models are dominated by Transformers, where self-attention mixes information from the visible context in an input-dependent way. However, when retrieval is not sharp and attention remains diffuse over an effective support $S_{\mathrm{eff}}(t)$, the influence of any individual token is diluted, typically scaling as $O(1/S_{\mathrm{eff}}(t))$ and reaching $O(1/\ell)$ for old tokens in full-prefix settings. Structured state-space models process sequences recurrently through an explicit feedback path; selective variants such as Mamba make this feedback input-dependent, yet when freeze time cannot be sustained over long intervals, their long-range sensitivity decays exponentially with lag. Existing architectures therefore either retrieve from the past in a single read or propagate information through a single feedback chain. We introduce Sessa, a decoder that places attention inside a feedback path, enabling recurrent many-path aggregation within a layer. Under stated assumptions, Sessa admits regimes with a power-law memory tail in lag $\ell$ of order $O(\ell^{-β})$ for $0<β<1$, which is asymptotically slower than $1/\ell$; moreover, this rate is tight in an explicit diffuse uniform-routing setting where the influence is $Θ(\ell^{-β})$. Under the same conditions, only Sessa among the compared model classes realizes flexible selective retrieval, including non-decaying profiles. Empirically, under matched architectures and training budgets, Sessa achieves the strongest performance on our long-context benchmarks while remaining competitive with Transformer and Mamba style baselines on short-context language modeling.


### Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories
**Authors**: Wonbong Jang, Shikun Liu, Soubhik Sanyal, Juan Camilo Perez, Kam Woh Ng, Sanskar Agrawal, Juan-Manuel Perez-Rua, Yiannis Douratsos, Tao Xiang

**Published Date**: 2026-04-10

**Updated Date**: 2026-04-20

**PDF Url**: [2604.09429v2](https://arxiv.org/pdf/2604.09429v2)

**Abstract**: Recovering camera parameters from images and rendering scenes from novel viewpoints have been treated as separate tasks in computer vision and graphics. This separation breaks down when image coverage is sparse or poses are ambiguous, since each task depends on what the other produces. We propose Rays as Pixels, a Video Diffusion Model (VDM) that learns a joint distribution over videos and camera trajectories. To our knowledge, this is the first model to predict camera poses and do camera-controlled video generation within a single framework. We represent each camera as dense ray pixels (raxels), a pixel-aligned encoding that lives in the same latent space as video frames, and denoise the two jointly through a Decoupled Self-Cross Attention mechanism. A single trained model handles three tasks: predicting camera trajectories from video, generating video from input images along a pre-defined trajectory, and jointly synthesizing video and trajectory from input images. We evaluate on pose estimation and camera-controlled video generation, and introduce a closed-loop self-consistency test showing that the model's predicted poses and its renderings conditioned on those poses agree. Ablations against Plücker embeddings confirm that representing cameras in a shared latent space with video is subtantially more effective.


### UDM-GRPO: Stable and Efficient Group Relative Policy Optimization for Uniform Discrete Diffusion Models
**Authors**: Jiaqi Wang, Haoge Deng, Ting Pan, Yang Liu, Chengyuan Wang, Fan Zhang, Yonggang Qi, Xinlong Wang

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18518v1](https://arxiv.org/pdf/2604.18518v1)

**Abstract**: Uniform Discrete Diffusion Model (UDM) has recently emerged as a promising paradigm for discrete generative modeling; however, its integration with reinforcement learning remains largely unexplored. We observe that naively applying GRPO to UDM leads to training instability and marginal performance gains. To address this, we propose \Ours, the first framework to integrate UDM with RL. Our method is guided by two key insights: (i) treating the final clean sample as the action provides more accurate and stable optimization signals; and (ii) reconstructing trajectories via the diffusion forward process better aligns probability paths with the pretraining distribution. Additionally, we introduce two strategies, Reduced-Step and CFG-Free, to further improve training efficiency. \Ours significantly improves base model performance across multiple T2I tasks. Notably, GenEval accuracy improves from $69\%$ to $96\%$ and PickScore increases from $20.46$ to $23.81$, achieving state-of-the-art performance in both continuous and discrete settings. On the OCR benchmark, accuracy rises from $8\%$ to $57\%$, further validating the generalization ability of our method. Code is available at \href{https://github.com/Yovecent/UDM-GRPO}{https://github.com/Yovecent/UDM-GRPO}.


### NI Sampling: Accelerating Discrete Diffusion Sampling by Token Order Optimization
**Authors**: Enshu Liu, Xuefei Ning, Yu Wang, Zinan Lin

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18471v1](https://arxiv.org/pdf/2604.18471v1)

**Abstract**: Discrete diffusion language models (dLLMs) have recently emerged as a promising alternative to traditional autoregressive approaches, offering the flexibility to generate tokens in arbitrary orders and the potential of parallel decoding. However, existing heuristic sampling strategies remain inefficient: they choose only a small part of tokens to sample at each step, leaving substantial room for improvement. In this work, we study the problem of token sampling order optimization and demonstrate its significant potential for acceleration. Specifically, we find that fully leveraging correct predictions at each step can reduce the number of sampling iterations by an order of magnitude without compromising accuracy. Based on this, we propose Neural Indicator Sampling (NI Sampling), a general sampling order optimization framework that utilize a neural indicator to decide which tokens should be sampled at each step. We further propose a novel trajectory-preserving objective to train the indicator. Experiments on LLaDA and Dream models across multiple benchmarks show that our method achieves up to 14.3$\times$ acceleration over full-step sampling with negligible performance drop, and consistently outperforms confidence threshold sampling in the accuracy-step trade-off. Code is available at https://github.com/imagination-research/NI-Sampling.


## Quantitative Finance
### QRAFTI: An Agentic Framework for Empirical Research in Quantitative Finance
**Authors**: Terence Lim, Kumar Muthuraman, Michael Sury

**Published Date**: 2026-04-20

**Updated Date**: 2026-04-20

**PDF Url**: [2604.18500v1](https://arxiv.org/pdf/2604.18500v1)

**Abstract**: We introduce a multi-agent framework intended to emulate parts of a quantitative research team and support equity factor research on large financial panel datasets. QRAFTI integrates a research toolkit for panel data with MCP servers that expose data access, factor construction, and custom coding operations as callable tools. It can help replicate established factors, formulate and test new signals, and generate standardized research reports accompanied by narrative analysis and computational traces. On multi-step empirical tasks, using chained tool calls and reflection-based planning may offer better performance and explainability than dynamic code generation alone.


