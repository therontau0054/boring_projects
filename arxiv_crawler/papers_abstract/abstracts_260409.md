# Abstracts of Papers

## Physics
### MoRight: Motion Control Done Right
**Authors**: Shaowei Liu, Xuanchi Ren, Tianchang Shen, Huan Ling, Saurabh Gupta, Shenlong Wang, Sanja Fidler, Jun Gao

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07348v1](https://arxiv.org/pdf/2604.07348v1)

**Abstract**: Generating motion-controlled videos--where user-specified actions drive physically plausible scene dynamics under freely chosen viewpoints--demands two capabilities: (1) disentangled motion control, allowing users to separately control the object motion and adjust camera viewpoint; and (2) motion causality, ensuring that user-driven actions trigger coherent reactions from other objects rather than merely displacing pixels. Existing methods fall short on both fronts: they entangle camera and object motion into a single tracking signal and treat motion as kinematic displacement without modeling causal relationships between object motion. We introduce MoRight, a unified framework that addresses both limitations through disentangled motion modeling. Object motion is specified in a canonical static-view and transferred to an arbitrary target camera viewpoint via temporal cross-view attention, enabling disentangled camera and object control. We further decompose motion into active (user-driven) and passive (consequence) components, training the model to learn motion causality from data. At inference, users can either supply active motion and MoRight predicts consequences (forward reasoning), or specify desired passive outcomes and MoRight recovers plausible driving actions (inverse reasoning), all while freely adjusting the camera viewpoint. Experiments on three benchmarks demonstrate state-of-the-art performance in generation quality, motion controllability, and interaction awareness.


### Quantum Superpositions of Conscious States in a Minimal Integrated Information Model
**Authors**: Kelvin J. McQueen, Ian T. Durham, Markus P. Mueller

**Published Date**: 2023-09-25

**Updated Date**: 2026-04-08

**PDF Url**: [2309.13826v2](https://arxiv.org/pdf/2309.13826v2)

**Abstract**: Could there be quantum superpositions of conscious states, as suggested by the Wigner's friend thought experiment? Mathematical theories of consciousness, notably Integrated Information Theory (IIT), make this question more precise by associating physical systems with both quantitative amounts of consciousness and structural characterizations of conscious states. Motivated by a recent proposal that ties wave function collapse to integrated information, we construct a simple quantum circuit that would place a minimal system -- a feedback dyad -- into a superposition of states that differ in their associated conscious states. This "Schrödinger's dyad" provides a controlled setting for evaluating a central desideratum of consciousness-based collapse models: that collapse rates depend on how different the experiences in the superposition are. We prove a structural constraint on collapse dynamics of a standard (Lindblad) type: if collapse is governed by too few collapse operators, collapse rates cannot in general be made to depend solely on qualitative differences between conscious states. Avoiding this limitation requires introducing many commuting operators, leading to a rapid proliferation of collapse terms even for very simple systems. This proliferation bears directly on claims that IIT-based collapse theories may be especially experimentally tractable, since the required dynamics becomes highly complex. More generally, the difficulty is not specific to IIT: any Wigner-style collapse theory that distinguishes experiences using rich internal organization (such as neural connectivity in addition to neural state) will face a comparable explosion in dynamical complexity.


### Replacing Tunable Parameters in Weather and Climate Models with State-Dependent Functions using Reinforcement Learning
**Authors**: Pritthijit Nath, Sebastian Schemm, Henry Moss, Peter Haynes, Emily Shuckburgh, Mark J. Webb

**Published Date**: 2026-01-07

**Updated Date**: 2026-04-08

**PDF Url**: [2601.04268v2](https://arxiv.org/pdf/2601.04268v2)

**Abstract**: Weather and climate models rely on parametrisations to represent unresolved sub-grid processes. Traditional schemes rely on fixed coefficients that are weakly constrained and tuned offline, contributing to persistent biases that limit their ability to adapt to underlying physics. This study presents a framework that learns components of parametrisation schemes online as a function of the evolving model state using reinforcement learning (RL) and evaluates RL-driven parameter updates across idealised testbeds spanning a simple climate bias correction (SCBC), a radiative-convective equilibrium (RCE), and a zonal mean energy balance model (EBM) with single-agent and federated multi-agent settings. Across nine RL algorithms, Truncated Quantile Critics (TQC), Deep Deterministic Policy Gradient (DDPG), and Twin Delayed DDPG (TD3) achieved the highest skill and stable convergence, with performance assessed against a static baseline using area-weighted RMSE, temperature and pressure-level diagnostics. For the EBM, single-agent RL outperformed static parameter tuning with the strongest gains in tropical and mid-latitude bands, while federated RL on multi-agent setups enabled specialised control and faster convergence, with a six-agent DDPG configuration using frequent aggregation yielding the lowest area-weighted RMSE across the tropics and mid-latitudes. The learnt corrections were also physically meaningful as agents modulated EBM radiative parameters to reduce meridional biases, adjusted RCE lapse rates to match vertical temperature errors, and stabilised heating increments to limit drift. Overall, results show that RL can learn skilful state-dependent parametrisation components in idealised settings, offering a scalable pathway for online learning within numerical models and a starting point for evaluation in weather and climate models.


### Geometric phase of arbitrary Mueller evolutions and its two-level quantum analogue
**Authors**: José J Gil

**Published Date**: 2026-02-15

**Updated Date**: 2026-04-08

**PDF Url**: [2602.14245v2](https://arxiv.org/pdf/2602.14245v2)

**Abstract**: We identify, for a general physically realizable Mueller transformation, the only intrinsic geometricphase structure that can be assigned to it in an invariant manner: the retarding part of the characteristic pure component selected by the characteristic decomposition, which defines a canonical holonomic content. A Mueller matrix does not, in general, determine a unique observed interferometric (Pancharatnam) geometric phase, since the latter depends on the specific physical realization of the transformation and on the interferometric readout. The remaining characteristic layers may modify the measured complex visibility, and even its observed argument through convex averaging, but they do not define a unique geometric holonomy of their own. We further establish the quantum analogue for open two-level dynamics within the Choi representation.


### Graph Neural ODE Digital Twins for Control-Oriented Reactor Thermal-Hydraulic Forecasting Under Partial Observability
**Authors**: Akzhol Almukhametov, Doyeong Lim, Rui Hu, Yang Liu

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07292v1](https://arxiv.org/pdf/2604.07292v1)

**Abstract**: Real-time supervisory control of advanced reactors requires accurate forecasting of plant-wide thermal-hydraulic states, including locations where physical sensors are unavailable. Meeting this need calls for surrogate models that combine predictive fidelity, millisecond-scale inference, and robustness to partial observability. In this work, we present a physics-informed message-passing Graph Neural Network coupled with a Neural Ordinary Differential Equation (GNN-ODE) to addresses all three requirements simultaneously. We represent the whole system as a directed sensor graph whose edges encode hydraulic connectivity through flow/heat transfer-aware message passing, and we advance the latent dynamics in continuous time via a controlled Neural ODE. A topology-guided missing-node initializer reconstructs uninstrumented states at rollout start; prediction then proceeds fully autoregressively. The GNN-ODE surrogate achieves satisfactory results for the system dynamics prediction. On held-out simulation transients, the surrogate achieves an average MAE of 0.91 K at 60 s and 2.18 K at 300 s for uninstrumented nodes, with $R^2$ up to 0.995 for missing-node state reconstruction. Inference runs at approximately 105 times faster than simulated time on a single GPU, enabling 64-member ensemble rollouts for uncertainty quantification. To assess sim-to-real transfer, we adapt the pretrained surrogate to experimental facility data using layerwise discriminative fine-tuning with only 30 training sequences. The learned flow-dependent heat-transfer scaling recovers a Reynolds-number exponent consistent with established correlations, indicating constitutive learning beyond trajectory fitting. The model tracks a steep power change transient and produces accurate trajectories at uninstrumented locations.


### Multispectral representation of Distributed Acoustic Sensing data: a framework for physically interpretable feature extraction and visualization
**Authors**: Sergio Morell-Monzó, Dídac Diego-Tortosa, Isabel Pérez-Arjona, Víctor Espinosa

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07290v1](https://arxiv.org/pdf/2604.07290v1)

**Abstract**: Distributed Acoustic Sensing (DAS) enables continuous monitoring of dynamic strain along tens of kilometers of optical fiber, generating massive datasets whose interpretation and automated analysis remain challenging. DAS measurements often lack a standardized visual representation, and their physical interpretation depends strongly on acquisition conditions and signal processing choices. This work introduces a systematic framework for visualization and feature extraction of DAS data based on a multispectral signal representation. The approach decomposes strain-rate measurements into predefined frequency bands and computes band-limited energy images that describe the spatial and temporal distribution of acoustic energy across distinct spectral regimes. The framework is evaluated using DAS recordings containing Fin Whale (Balaenoptera physalus) and Blue Whale (Balaenoptera musculus) vocalizations. Three experiments are conducted to assess the approach: enhanced visualization of bioacoustic signals, unsupervised clustering of acoustic patterns, and supervised event detection using a convolutional neural network. Using multispectral composites as input, a ResNet-18 classifier achieves an accuracy of 97.3% in whale vocalization detection, demonstrating that the proposed representation captures biologically meaningful spectral structure and provides an effective feature space for automated analysis of DAS data.


### Physics-Informed Discrete-Event Simulation of Polarization-Encoded Quantum Networks
**Authors**: Abderrahim Amlou, Amar Abane, Cory M. Nunn, M. V. Jabir, Van Sy Mai, Abdella Battou, Ahmed Lbath

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07289v1](https://arxiv.org/pdf/2604.07289v1)

**Abstract**: We extend the SeQUeNCe discrete-event simulator with physics-based models for polarization-encoded photonic quantum networks. Our framework integrates Jones-calculus optical components, including an SPDC Bell-state source, wave plates, and polarizing beam splitters, together with a multi-section fiber model capturing polarization mode dispersion, chromatic dispersion, and Raman noise from coexisting classical traffic. We validate the simulator by reproducing experimentally reported spectra, polarization correlations, quantum state tomography, and dispersion- and Raman-induced noise. The resulting platform enables hardware-parameterized prediction of entanglement distribution performance under realistic deployment conditions.


### A Giant-Step Baby-Step Classifier For Scalable and Real-Time Anomaly Detection In Industrial Control Systems and Water Treatment Systems
**Authors**: Sarad Venugopalan, Sridhar Adepu

**Published Date**: 2025-04-29

**Updated Date**: 2026-04-08

**PDF Url**: [2504.20906v4](https://arxiv.org/pdf/2504.20906v4)

**Abstract**: The continuous monitoring of the interactions between cyber-physical components of any industrial control system (ICS) is required to secure automation of the system controls, and to guarantee plant processes are fail-safe and remain in an acceptably safe state. Safety is achieved by managing actuation (where electric signals are used to trigger physical movement), dependent on corresponding sensor readings; used as ground truth in decision making. Timely detection of anomalies (attacks, faults and unascertained states) in ICSs is crucial for the safe running of a plant, the safety of its personnel, and for the safe provision of any services provided. We propose an anomaly detection method that involves accurate linearization of the non-linear forms arising from sensor-actuator(s) relationships, primarily because solving linear models is easier and well understood. We accomplish this by using a well-known water treatment testbed as a use case. Our experiments show millisecond time response to detect anomalies, all of which are explainable and traceable; this simultaneous coupling of detection speed and explainability has not been achieved by other state of the art Artificial Intelligence (AI)/ Machine Learning (ML) models with eXplainable AI (XAI) used for the same purpose. Our methods explainability enables us to pin-point the sensor(s) and the actuation state(s) for which the anomaly was detected. The proposed algorithm showed an accuracy of 97.72% by flagging deviations within safe operation limits as non-anomalous; indicative that slower detectors with highest detection resolution is unnecessary, for systems whose safety boundaries provide leeway within safety limits.


### Two-dimensional shelving spectroscopy of ultraviolet ground state transitions in dysprosium
**Authors**: Kevin S. H. Ng, Paul Uerlings, Fiona Hellstern, Jens Hertkorn, Luis Weiß, Stephan Welte, Tilman Pfau, Ralf Klemt

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07283v1](https://arxiv.org/pdf/2604.07283v1)

**Abstract**: The open inner-shell electronic structure of lanthanides with large magnetic moments gives rise to a rich spectrum of transitions available for laser cooling, trapping, and coherent control. Despite this, the large number of ultraviolet (UV) transitions below 400nm have so far been rarely utilized in dipolar atom experiments. Here, we investigate multiple UV ground state transitions in dysprosium. Several of these UV excited states have the largest decay strengths to the ultralong-lived, low-lying first excited state which are comparable to the most commonly used strongest transitions found in dipolar atoms. Using two-dimensional shelving spectroscopy which improves detection sensitivity and provides a straightforward way to determine the hyperfine-isotope structure and excited state total angular momentum $J$, we measure isotope shifts, hyperfine coefficients, and create King plots to determine their electronic nature. Such knowledge of these UV transitions which analogously exist in other magnetic atoms is important for optically populating the first excited state and can be used towards creating an optical clock, high resolution imaging in quantum gas microscopy, and probing lanthanide nuclei with enhanced Schiff moments in search of physics beyond the standard model.


### Molecular Quantum Control Algorithm Design by Reinforcement Learning
**Authors**: Anastasia Pipi, Xuecheng Tao, Arianna Wu, Prineha Narang, David R. Leibrandt

**Published Date**: 2024-10-15

**Updated Date**: 2026-04-08

**PDF Url**: [2410.11839v4](https://arxiv.org/pdf/2410.11839v4)

**Abstract**: Precision measurements of molecules offer an unparalleled paradigm to probe physics beyond the Standard Model. The rich internal structure within these molecules makes them exquisite sensors for detecting fundamental symmetry violations, local position invariance, and dark matter. While trapping and control of diatomic and a few very simple polyatomic molecules have been experimentally demonstrated, leveraging the complex rovibrational structure of more general polyatomics demands the development of robust and efficient quantum control schemes. In this study, we present reinforcement-learning quantum-logic spectroscopy (RL-QLS), a general, reinforcement-learning-designed, quantum logic approach to prepare molecular ions in single, pure quantum states. The reinforcement learning agent optimizes the pulse sequence, each followed by a projective measurement, and probabilistically manipulates the collapse of the quantum system to a single state. The performance of the control algorithm is numerically demonstrated for the polyatomic molecule H$_3$O$^+$ with 130 thermally populated eigenstates and degenerate transitions within inversion doublets, where quantum Markov decision process modeling and a physics-informed reward function play a key role, as well as for CaH$^+$ under the disturbance of environmental thermal radiation. The developed theoretical framework cohesively integrates techniques from quantum chemistry, AMO physics, and artificial intelligence, and we expect that the results can be readily implemented for quantum control of polyatomic molecular ions with densely populated structures, thereby enabling new experimental tests of fundamental theories.


## Diffusion
### Computational bottlenecks for denoising diffusions
**Authors**: Andrea Montanari, Viet Vu

**Published Date**: 2025-03-11

**Updated Date**: 2026-04-08

**PDF Url**: [2503.08028v3](https://arxiv.org/pdf/2503.08028v3)

**Abstract**: Denoising diffusions sample from a probability distribution $μ$ in $\mathbb{R}^d$ by constructing a stochastic process $({\hat{\boldsymbol x}}_t:t\ge 0)$ in $\mathbb{R}^d$ such that ${\hat{\boldsymbol x}}_0$ is easy to sample, but the distribution of $\hat{\boldsymbol x}_T$ at large $T$ approximates $μ$. The drift ${\boldsymbol m}:\mathbb{R}^d\times\mathbb{R}\to\mathbb{R}^d$ of this diffusion process is learned my minimizing a score-matching objective.
  Is every probability distribution $μ$, for which sampling is tractable, also amenable to sampling via diffusions? We provide evidence to the contrary by studying a probability distribution $μ$ for which sampling is easy, but the drift of the diffusion process is intractable -- under a popular conjecture on information-computation gaps in statistical estimation. We show that there exist drifts that are superpolynomially close to the optimum value (among polynomial time drifts) and yet yield samples with distribution that is very far from the target one.


### Region-Graph Optimal Transport Routing for Mixture-of-Experts Whole-Slide Image Classification
**Authors**: Xin Tian, Jiuliu Lu, Ephraim Tsalik, Bart Wanders, Colleen Knoth, Julian Knight

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07298v1](https://arxiv.org/pdf/2604.07298v1)

**Abstract**: Multiple Instance Learning (MIL) is the dominant framework for gigapixel whole-slide image (WSI) classification in computational pathology. However, current MIL aggregators route all instances through a shared pathway, constraining their capacity to specialise across the pathological heterogeneity inherent in each slide. Mixture-of-Experts (MoE) methods offer a natural remedy by partitioning instances across specialised expert subnetworks; yet unconstrained softmax routing may yield highly imbalanced utilisation, where one or a few experts absorb most routing mass, collapsing the mixture back to a near-single-pathway solution. To address these limitations, we propose ROAM (Region-graph OptimAl-transport Mixture-of-experts), a spatially aware MoE-MIL aggregator that routes region tokens to expert poolers via capacity-constrained entropic optimal transport, promoting balanced expert utilisation by construction. ROAM operates on spatial region tokens, obtained by compressing dense patch bags into spatially binned units that align routing with local tissue neighbourhoods and introduces two key mechanisms: (i) region-to-expert assignment formulated as entropic optimal transport (Sinkhorn) with explicit per slide capacity marginals, enforcing balanced expert utilisation without auxiliary load-balancing losses; and (ii) graph-regularised Sinkhorn iterations that diffuse routing assignments over the spatial region graph, encouraging neighbouring regions to coherently route to the same experts. Evaluated on four WSI benchmarks with frozen foundation-model patch embeddings, ROAM achieves performance competitive against strong MIL and MoE baselines, and on NSCLC generalisation (TCGA-CPTAC) reaches external AUC 0.845 +- 0.019.


### Diffusion Processes on Implicit Manifolds
**Authors**: Victor Kawasaki-Borruat, Clara Grotehans, Pierre Vandergheynst, Adam Gosztolai

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07213v1](https://arxiv.org/pdf/2604.07213v1)

**Abstract**: High-dimensional data are often modeled as lying near a low-dimensional manifold. We study how to construct diffusion processes on this data manifold in the implicit setting. That is, using only point cloud samples and without access to charts, projections, or other geometric primitives. Our main contribution is a data-driven SDE that captures intrinsic diffusion on the underlying manifold while being defined in ambient space. The construction relies on estimating the diffusion's infinitesimal generator and its carré-du-champ (CDC) from a proximity graph built from the data. The generator and CDC together encode the local stochastic and geometric structure of the intended diffusion. We show that, as the number of samples grows, the induced process converges in law on the space of probability paths to its smooth manifold counterpart. We call this construction Implicit Manifold-valued Diffusions (IMDs), and furthermore present a numerical simulation procedure using Euler-Maruyama integration. This gives a rigorous basis for practical implementations of diffusion dynamics on data manifolds, and opens new directions for manifold-aware sampling, exploration, and generative modeling.


### SBBTS: A Unified Schrödinger-Bass Framework for Synthetic Financial Time Series
**Authors**: Alexandre Alouadi, Grégoire Loeper, Célian Marsala, Othmane Mazhar, Huyên Pham

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07159v1](https://arxiv.org/pdf/2604.07159v1)

**Abstract**: We study the problem of generating synthetic time series that reproduce both marginal distributions and temporal dynamics, a central challenge in financial machine learning. Existing approaches typically fail to jointly model drift and stochastic volatility, as diffusion-based methods fix the volatility while martingale transport models ignore drift. We introduce the Schrödinger-Bass Bridge for Time Series (SBBTS), a unified framework that extends the Schrödinger-Bass formulation to multi-step time series. The method constructs a diffusion process that jointly calibrates drift and volatility and admits a tractable decomposition into conditional transport problems, enabling efficient learning. Numerical experiments on the Heston model demonstrate that SBBTS accurately recovers stochastic volatility and correlation parameters that prior SchrödingerBridge methods fail to capture. Applied to S&P 500 data, SBBTS-generated synthetic time series consistently improve downstream forecasting performance when used for data augmentation, yielding higher classification accuracy and Sharpe ratio compared to real-data-only training. These results show that SBBTS provides a practical and effective framework for realistic time series generation and data augmentation in financial applications.


### Bridging MRI and PET physiology: Untangling complementarity through orthogonal representations
**Authors**: Sonja Adomeit, Kartikay Tehlan, Lukas Förner, Katharina Weisser, Helen Scholtiseek, David Kaufmann, Julie Steinestel, Constantin Lapa, Thomas Kröncke, Thomas Wendler

**Published Date**: 2026-04-08

**Updated Date**: 2026-04-08

**PDF Url**: [2604.07154v1](https://arxiv.org/pdf/2604.07154v1)

**Abstract**: Multimodal imaging analysis often relies on joint latent representations, yet these approaches rarely define what information is shared versus modality-specific. Clarifying this distinction is clinically relevant, as it delineates the irreducible contribution of each modality and informs rational acquisition strategies. We propose a subspace decomposition framework that reframes multimodal fusion as a problem of orthogonal subspace separation rather than translation. We decompose Prostate-Specific Membrane Antigen (PSMA) PET uptake into an MRI-explainable physiological envelope and an orthogonal residual reflecting signal components not expressible within the MRI feature manifold. Using multiparametric MRI, we train an intensity-based, non-spatial implicit neural representation (INR) to map MRI feature vectors to PET uptake. We introduce a projection-based regularization using singular value decomposition to penalize residual components lying within the span of the MRI feature manifold. This enforces mathematical orthogonality between tissue-level physiological properties (structure, diffusion, perfusion) and intracellular PSMA expression. Tested on 13 prostate cancer patients, the model demonstrates that residual components spanned by MRI features are absorbed into the learned envelope, while the orthogonal residual is largest in tumour regions. This indicates that PSMA PET contains signal components not recoverable from MRI-derived physiological descriptors. The resulting decomposition provides a structured characterization of modality complementarity grounded in representation geometry rather than image translation.


## Quantitative Finance
### Xpertbench: Expert Level Tasks with Rubrics-Based Evaluation
**Authors**: Xue Liu, Xin Ma, Yuxin Ma, Yongchang Peng, Duo Wang, Zhoufutu Wen, Ge Zhang, Kaiyuan Zhang, Xinyu Chen, Tianci He, Jiani Hou, Liang Hu, Ziyun Huang, Yongzhe Hui, Jianpeng Jiao, Chennan Ju, Yingru Kong, Yiran Li, Mengyun Liu, Luyao Ma, Fei Ni, Yiqing Ni, Yueyan Qiu, Yanle Ren, Zilin Shi, Zaiyuan Wang, Wenjie Yue, Shiyu Zhang, Xinyi Zhang, Kaiwen Zhao, Zhenwei Zhu, Shanshan Wu, Qi Zhao, Wenhao Huang

**Published Date**: 2026-03-27

**Updated Date**: 2026-04-07

**PDF Url**: [2604.02368v3](https://arxiv.org/pdf/2604.02368v3)

**Abstract**: As Large Language Models (LLMs) exhibit plateauing performance on conventional benchmarks, a pivotal challenge persists: evaluating their proficiency in complex, open-ended tasks characterizing genuine expert-level cognition. Existing frameworks suffer from narrow domain coverage, reliance on generalist tasks, or self-evaluation biases. To bridge this gap, we present XpertBench, a high-fidelity benchmark engineered to assess LLMs across authentic professional domains. XpertBench consists of 1,346 meticulously curated tasks across 80 categories, spanning finance, healthcare, legal services, education, and dual-track research (STEM and Humanities). These tasks are derived from over 1,000 submissions by domain experts--including researchers from elite institutions and practitioners with extensive clinical or industrial experience--ensuring superior ecological validity. Each task uses detailed rubrics with mostly 15-40 weighted checkpoints to assess professional rigor. To facilitate scalable yet human-aligned assessment, we introduce ShotJudge, a novel evaluation paradigm that employs LLM judges calibrated with expert few-shot exemplars to mitigate self-rewarding biases. Our empirical evaluation of state-of-the-art LLMs reveals a pronounced performance ceiling: even leading models achieve a peak success rate of only ~66%, with a mean score around 55%. Models also exhibit domain-specific divergence, showing non-overlapping strengths in quantitative reasoning versus linguistic synthesis.. These findings underscore a significant "expert-gap" in current AI systems and establish XpertBench as a critical instrument for navigating the transition from general-purpose assistants to specialized professional collaborators.


### TableVision: A Large-Scale Benchmark for Spatially Grounded Reasoning over Complex Hierarchical Tables
**Authors**: Xiaoyu Chen, Lu Dai, Hanqing Wang, Zhuoyu Li, Wenbin Dai, Yanzong Zheng, Zhenggang Xia, Junyong Lin, Hui Xiong

**Published Date**: 2026-04-04

**Updated Date**: 2026-04-04

**PDF Url**: [2604.03660v1](https://arxiv.org/pdf/2604.03660v1)

**Abstract**: Structured tables are essential for conveying high-density information in professional domains such as finance, healthcare, and scientific research. Despite the progress in Multimodal Large Language Models (MLLMs), reasoning performance remains limited for complex tables with hierarchical layouts. In this paper, we identify a critical Perception Bottleneck through quantitative analysis. We find that as task complexity scales, the number of involved discrete visual regions increases disproportionately. This processing density leads to an internal "Perceptual Overload," where MLLMs struggle to maintain accurate spatial attention during implicit generation. To address this bottleneck, we introduce TableVision, a large-scale, trajectory-aware benchmark designed for spatially grounded reasoning. TableVision stratifies tabular tasks into three cognitive levels (Perception, Reasoning, and Analysis) across 13 sub-categories. By utilizing a rendering-based deterministic grounding pipeline, the dataset explicitly couples multi-step logical deductions with pixel-perfect spatial ground truths, comprising 6,799 high-fidelity reasoning trajectories. Our empirical results, supported by diagnostic probing, demonstrate that explicit spatial constraints significantly recover the reasoning potential of MLLMs. Furthermore, our two-stage decoupled framework achieves a robust 12.3% overall accuracy improvement on the test set. TableVision provides a rigorous testbed and a fresh perspective on the synergy between perception and logic in document understanding.


### Decoding RWA Tokenized U.S. Treasuries: Functional Dissection and Address Role Inference
**Authors**: Junliang Luo, Katrin Tinn, Samuel Ferreira Duran, Di Wu, Xue Liu

**Published Date**: 2025-07-20

**Updated Date**: 2026-04-03

**PDF Url**: [2507.14808v2](https://arxiv.org/pdf/2507.14808v2)

**Abstract**: Tokenized U.S. Treasuries have emerged as a prominent subclass of real-world assets (RWAs), offering cryptographically secured, yield-bearing instruments issued across multi-chain Web3 infrastructures, with growing significance for transparency, accessibility, and financial inclusion. While the market has expanded rapidly, empirical analyses of transaction-level behaviours remain limited. This paper conducts a quantitative, function-level dissection of U.S. Treasury-backed RWA tokens, including BUIDL, BENJI, and USDY across multi-chain: mostly Ethereum and Layer-2s. Decoded contract calls expose core financial primitives such as issuance, redemption, transfer, and bridging, revealing patterns that distinguish institutional participants from smaller or retail users for the extent and limits of inclusivity in current RWA adoption. To infer address-level economic roles, we introduce a curvature-aware representation learning model. Our method outperforms baseline models in role inference on our collected U.S. Treasury transaction dataset and generalizes to address classification across broader public blockchain transaction datasets. The decoded transaction-level patterns in tokenized U.S. Treasuries across chains surface the degree of retail participation, and the role inference model enables the distinction between institutional treasuries, arbitrage bots, and retail traders based on behavioral patterns, facilitating future more transparent, inclusive, and accountable Web3 finance.


