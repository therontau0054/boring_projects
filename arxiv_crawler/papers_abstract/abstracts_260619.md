# Abstracts of Papers

## World Model
### MemoryWAM: Efficient World Action Modeling with Persistent Memory
**Authors**: Sizhe Yang, Juncheng Mu, Tianming Wei, Chenhao Lu, Xiaofan Li, Linning Xu, Zhengrong Xue, Zhecheng Yuan, Dahua Lin, Jiangmiao Pang, Huazhe Xu

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20562v1](https://arxiv.org/pdf/2606.20562v1)

**Abstract**: Robust robotic manipulation in the real world requires not only an understanding of the current observation, but also memory and dynamics modeling. World action models (WAMs) possess these capabilities by jointly modeling visual foresight and actions conditioned on both current and historical observations, making them a promising paradigm for robotic manipulation. However, existing WAMs face a fundamental trade-off: methods with efficient inference typically condition only on a bounded window of recent observations and therefore struggle in non-Markovian environments, whereas methods that preserve long histories incur time and space costs that grow substantially with sequence length. To address this challenge, we introduce MemoryWAM, a world action model with efficient persistent memory. MemoryWAM uses a hybrid memory design that combines recent frames, event-boundary anchor frames, and compact gist tokens that summarize long-range history. A tailored attention mechanism enables retrieval of both detailed short-term context and compressed long-term context, supporting memory-dependent decision-making with reduced inference latency and GPU memory usage. Across long-horizon, memory-dependent manipulation tasks in both simulation and the real world, MemoryWAM outperforms strong vision-language-action (VLA) and WAM baselines while maintaining favorable computational efficiency.


### TimeProVe: Propose, then Verify for Efficient Long Video Temporal Reasoning in Activities of Daily Living
**Authors**: Arkaprava Sinha, Dominick Reilly, Siddharth Krishnan, Hieu Le, Srijan Das

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20561v1](https://arxiv.org/pdf/2606.20561v1)

**Abstract**: Long Video Question Answering (LVQA) requires identifying sparse, query-relevant evidence within hours-long untrimmed videos. Existing approaches either process videos densely with large vision-language models (VLMs), incurring prohibitive computational cost, or rely on sparse caption-based reasoning, which often misses temporally localized and motion-centric evidence. We introduce TimeProVe, a cost-efficient hybrid framework for temporally grounded reasoning in long videos. TimeProVe first employs lightweight modules to generate action-grounded answer--evidence hypotheses and subsequently invokes an expensive VLM only for targeted verification. The core of our framework lies in the Action-based Candidate Evidence (ACE) module, which converts temporally localized actions into query-conditioned candidate answers and supporting evidence windows through lightweight LLM reasoning. We further introduce OpenTSUBench (OTB), an open-ended benchmark designed to evaluate temporally grounded reasoning in real-world Activities of Daily Living (ADL) scenarios. Experiments show that TimeProVe outperforms the strongest baseline on OTB by 7.3%, while reducing VLM calls by 75% and inference cost by 93%. Furthermore, without explicit temporal grounding training, TimeProVe achieves competitive performance on Charades-STA, and reaches state-of-the-art results when enhanced with grounding VLMs.


### How Transparent is DiffusionGemma?
**Authors**: Joshua Engels, Callum McDougall, Bilal Chughtai, Janos Kramar, Senthoran Rajamanoharan, Cindy Wu, Arthur Conmy, Asic Q Chen, Jean Tarbouriech, Min Ma, Brendan O'Donoghue, João Gabriel Lopes de Oliveira, Rohin Shah, Neel Nanda

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20560v1](https://arxiv.org/pdf/2606.20560v1)

**Abstract**: LLM reasoning transparency is a critical affordance for understanding model decisions, mitigating misuse and misalignment, and debugging surprising model behaviors. However, DiffusionGemma performs a larger fraction of its computation in a continuous latent space; does this make its reasoning less transparent? We study this question by decomposing transparency into two components: variable transparency, whether we understand intermediate snapshots of a model's computational state; and algorithmic transparency, whether we can use these snapshots to reconstruct the process by which the model arrived at its outputs. Naively, DiffusionGemma has poor variable transparency: its opaque serial depth, the amount of serial computation that occurs in between interpretable model states, seems at first 28.6X higher than the corresponding autoregressive Gemma 4 model. However, we show that we can map the information flowing between denoising steps through an interpretable token bottleneck with no decrease in downstream performance. Treating these intermediate states as interpretable reduces the opaque serial depth to just 1.1X that of Gemma 4. Algorithmic transparency is harder for diffusion models than for autoregressive models because all token predictions in the canvas can change at every denoising step, giving the model the power to implement complicated distributed algorithms during the denoising process. To begin bridging this gap, we conduct a suite of interpretability case studies, uncovering initial evidence of novel diffusion-specific phenomena such as non-chronological reasoning, token and sequence smearing, and intermediate-context reasoning. Finally, we test monitorability, a key application of transparency that measures whether model outputs are useful for downstream tasks. We find that DiffusionGemma is similarly monitorable to Gemma 4.


### UNIEGO: Proxies as Mediators for Unified Egocentric Video Representation Learning
**Authors**: Wenhao Chi, Arkaprava Sinha, Dominick Reilly, Hieu Le, Srijan Das

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20559v1](https://arxiv.org/pdf/2606.20559v1)

**Abstract**: Egocentric video understanding is inherently limited by the narrow perspective of wearable cameras: a single viewpoint, a single modality, a single model cannot capture the full richness of human action. We argue that a truly expressive egocentric representation must subsume complementary knowledge across viewpoints, modalities, and foundation model representations, yet remain deployable from egocentric video alone. To this end, we introduce a hierarchical multi-teacher distillation framework that produces UNIEGO, a unified egocentric encoder trained with nine teachers spanning ego-exo viewpoints, RGB, depth, and skeleton modalities, and four foundation models. Rather than distilling directly from heterogeneous teachers whose incompatible architectures and feature geometries induce conflicting gradients, our framework interposes a layer of representation-specific Proxy models that translate diverse teacher knowledge into a homogeneous egocentric space. A second distillation stage, Selective Proxy Distillation (SPD), then adaptively selects, for each training sample, the subset of proxies that are both correct and confident, distilling exclusively from reliable supervision and suppressing erroneous signals. SPD is further stabilized by initializing UNIEGO as a learned convex combination of proxy parameters, placing the unified model in a well-conditioned region of the loss landscape before distillation begins. UNIEGO achieves state-of-the-art performance across three egocentric video understanding tasks - action recognition, video retrieval, and action segmentation on three challenging ego-exo benchmarks, outperforming naive multi-teacher distillation baselines and demonstrating that structured, proxy-mediated knowledge transfer yields richer and more discriminative egocentric representations.


### Optimal Deterministic Multicalibration and Omniprediction
**Authors**: Georgy Noarov, Aaron Roth

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20557v1](https://arxiv.org/pdf/2606.20557v1)

**Abstract**: A model is multicalibrated on a collection of group weights $G$ if it is calibrated -- i.e. unbiased even conditional on its prediction -- not just overall, but also after reweighting contexts by each $g \in G$. It is a useful property for many downstream applications and is a basic desideratum of trustworthy machine learning. Before this work, all predictors known to attain the minimax-optimal $\widetilde O(\varepsilon^{-3})$ sample complexity rate for $\varepsilon$-multicalibration were randomized, while deterministic predictors were known only with substantially worse sample complexity. Whether randomization is necessary for optimal sample complexity in multicalibration was explicitly asked by [CLNR26] and implicitly in several prior works.
  We resolve this open problem by giving a minimax-optimal multicalibration algorithm that outputs a deterministic predictor. We then generalize the algorithm to produce optimal deterministic predictors that satisfy outcome indistinguishability (OI) with respect to finite or finitely covered collections of tests. As an application, this also gives deterministic omnipredictors and panpredictors with optimal sample complexity, resolving open problems posed by [OKK25] and [BHHLZ25].


### Thinking in Boxes: 3D Editing in Real Images Made Easy
**Authors**: Pradhaan S Bhat, Naveen Chandra R, Rishubh Parihar, Vaibhav Vavilala, R. Venkatesh Babu, D. A. Forsyth, Anand Bhattad

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20556v1](https://arxiv.org/pdf/2606.20556v1)

**Abstract**: Text and 2D-conditioning interfaces provide weak, ambiguous control over spatial transformations in image editing -- particularly under large object motions and camera changes. Prior work has used 3D primitives such as boxes, but only as loose conditioning signals indicating approximate object location rather than specifying the transformation. We instead use 3D boxes as structured specifications: the user provides the input and output boxes of the edit, casting editing as a well-posed geometry problem. This ``thinking in boxes'' interface, where each box face is color-coded to convey 3D orientation, gives precise control over translation, rotation, scaling, and viewpoint changes in real images while preserving scene and object identity, and recovering previously unseen object regions. To ground transformations in scene appearance, we introduce a depth-aligned planar floor as a global reference frame, shaded with depth-aware cues. Conditioned on this structure, an image generator produces consistent results under large transformations. Trained in two stages -- on synthetic multi-object scenes and a small set of real-world videos from Objectron -- the system generalizes to complex, in-the-wild real images. Our method operates directly on real photographs and substantially outperforms recent state-of-the-art methods on large 3D edits.


## Generation
### Structuring and Tokenizing Distributed User Interest Context for Generative Recommendation
**Authors**: Ruizhong Qiu, Yinglong Xia, Dongqi Fu, Hanqing Zeng, Ren Chen, Xiangjun Fan, Hong Li, Hong Yan, Hanghang Tong

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20554v1](https://arxiv.org/pdf/2606.20554v1)

**Abstract**: Generative recommendation is an emerging paradigm that has shown promise in industrial recommendation systems, aiming to predict users' next interactions from their historical behaviors. At the core of generative recommendation lies item tokenization, which bridges item semantics and recommendation models. However, existing methods often struggle to effectively organize and inject complex user-behavioral and item-semantic contexts into recommendation models simultaneously. On the one hand, existing graph-based integration methods, such as graph serialization and graph neural networks, either suffer from scalability issues or exploit only local graph information. On the other hand, existing semantic tokenization methods typically rely on heuristics and lack explicit supervision signals, which may lead to inaccurate or suboptimal semantic representations. To address these limitations in user interest context modeling, we propose G2Rec, a scalable framework that unifies holistic graph-based user co-engagement modeling with semantic tokenization for industrial-scale generative recommendation. Overall, G2Rec enables recommendation models to capture holistic and semantically grounded user interest prototypes without requiring ground-truth user interests, thereby providing more comprehensive and accurate modeling of user behavior contexts in industrial sequential recommendation. Online deployment across product surfaces and extensive experiments on public datasets demonstrate the superiority of G2Rec over existing methods.


### Predictability as a Fine-Grained Measure for Privacy
**Authors**: Linda Lu, Karthik Sridharan

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20546v1](https://arxiv.org/pdf/2606.20546v1)

**Abstract**: Differential privacy (DP) ensures rigorous individual-level privacy guarantees against even the most knowledgeable attackers, but its worst-case nature can impose a costly privacy-accuracy tradeoff. We introduce privacy via predictability, a fine-grained framework that explicitly incorporates the attacker's core knowledge, a compromised portion of the dataset generated by a stochastic process, and a specified family of queries. Predictability measures privacy leakage as the incremental gain in an attacker's ability to predict sensitive information about unknown individuals after observing the algorithm's output, beyond what can already be inferred from the compromised data. We show that predictability and DP are generally incomparable: each can be small while the other is large. However, in the worst-case regime where all but one individual is compromised, and all binary queries are considered sensitive, predictability implies mutual-information DP. More generally, predictability provides a finer-grained privacy metric tailored to specific sensitive information and specific attacker models. We introduce a general framework, using the generalized method of moments (GMM), to analyze asymptotic predictability when the compromised data is generated by a stationary, ergodic, mixing process. Using this analysis, we derive a predictability-calibrated output perturbation scheme for ERM. Our approach is complementary to DP and can be used alongside DP to provide fine-grained privacy control.


### Multi-Task Bayesian In-Context Learning
**Authors**: Qingyang Zhu, Eric Karl Oermann, Kyunghyun Cho

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20538v1](https://arxiv.org/pdf/2606.20538v1)

**Abstract**: Bayesian predictive inference provides a principled framework for uncertainty quantification, data efficiency, and robust generalization. However, exact inference is often intractable, and scalable approximations may remain computationally expensive or require restrictive modeling assumptions that degrade predictive performance. Prior-Data Fitted and in-context models have recently emerged as an amortized alternative by learning to map datasets directly to predictive distributions, but existing approaches are tightly coupled to the support of the training prior and lack explicit mechanisms for adapting to new priors at test time, resulting in limited robustness under distribution shift. We introduce a multi-task in-context learning framework for amortized hierarchical Bayesian predictive inference that explicitly represents prior information as a prefix of in-context datasets. A transformer trained on sequences of prior and target tasks learns to adapt its predictions across families of priors. On a suite of evaluations with increasing difficulty, including out-of-meta-distribution priors and priors with high-dimensional latent structures, our method matches oracle Bayesian predictors while being orders of magnitude faster. We further demonstrate its practical relevance on a real-world spatiotemporal temperature prediction benchmark. Code is available at https://github.com/martianmartina/multi-task-bayesian-icl/.


### How Do Instructions Shape Speech? Cross-Attention Attribution for Style-Captioned Text-to-Speech
**Authors**: Nityanand Mathur, Hamees Sayed, Wasim Madha, Apoorv Singh, Sameer Khurana, Akshat Mandloi, Sudarshan Kamath

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20532v1](https://arxiv.org/pdf/2606.20532v1)

**Abstract**: Style-captioned text-to-speech systems use natural language to control voice characteristics, but how individual words influence acoustic output remains unclear. Understanding this is critical for diagnosing failure modes and improving controllability in expressive TTS. We propose cross-attention attribution for speech diffusion models, adapting the DAAM framework to the speech domain for the first time, and apply it to CapSpeech-TTS. Our method extracts per-token heatmaps across 25 layers and 24 ODE steps. We analyze 3,600 (style caption, text transcript) combinations comprising 120 style captions conditioning the generation of 30 text transcripts each, revealing how caption tokens shape waveforms. Results show: (1) style tokens have lower temporal variance than content/function tokens, confirming global conditioning; (2) style attention correlates with F0 and energy; (3) style conditioning peaks in early steps and deep layers; (4) attention entropy reaches its minimum at layer 17, co-occurring with the style importance peak, indicating maximal network selectivity at the most style-critical stage. This is the first study of how natural language influences cross-attention in speech diffusion models


### SARLO-80: Worldwide Slant SAR Language Optic Dataset 80cm
**Authors**: Solène Debuysère, Nicolas Trouvé, Nathan Letheule, Elise Colin, Georgia Channing

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20523v1](https://arxiv.org/pdf/2606.20523v1)

**Abstract**: Multimodal foundation models have advanced rapidly thanks to large optical benchmarks, but comparable resources for synthetic aperture radar (SAR) remain limited. Existing SAR--optical datasets largely rely on low-resolution, intensity-only Ground Range Detected~(GRD) products and do not preserve complex-valued SAR measurements or native acquisition geometry, which restricts physically grounded multimodal learning. In particular, large-scale public datasets combining very-high-resolution (VHR) SAR SLC, aligned optical imagery, and natural-language descriptions are still lacking. We present a VHR SAR--optical--text dataset built from open-access Umbra spotlight acquisitions distributed as Sensor Independent Complex Data (SICD). From around 2,500 worldwide scenes (VV/HH, 20cm--2m native resolution), we standardize all SAR data to an 80cm slant-range grid via band-limited FFT resampling and tile the imagery into 1024 by 1024 patches. For each SAR patch, we retrieve a high-resolution optical tile and warp it into the SAR grid using local coordinate correspondences for local pixel-level alignment. We further generate three caption variants (SHORT/MID/LONG) per sample to support vision--language training and evaluation. Our dataset contains 119,566 triplets (complex and amplitude slant-range SAR patch, aligned optical patch, natural-language description) covering 257 locations across 72 countries and a broad range of land types and infrastructures. We release fixed train/validation/test splits and the full preprocessing and baseline code to enable reproducible benchmarks for multimodal alignment on cross-modal retrieval and conditional generation in native SAR geometry. The dataset is publicly available on the Hugging Face Hub at https://huggingface.co/datasets/ONERA/SARLO-80.


### FlowEdit: Associative Memory for Lifelong Pronunciation Adaptation in Flow-Matching TTS
**Authors**: Harshit Singh, Ayush Pratap Singh, Nityanand Mathur

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20518v1](https://arxiv.org/pdf/2606.20518v1)

**Abstract**: Flow-matching text-to-speech systems achieve remarkable zero-shot quality but remain static after deployment: pronunciation errors on out-of-vocabulary proper nouns persist unless the model is retrained. We introduce FlowEdit, a life-long adaptation framework for frozen flow-matching TTS that learns pronunciation corrections as latent conditioning edits rather than weight updates. When corrective feedback is provided, FlowEdit optimizes a token-level perturbation in the text embedding space, then stores the correction in a Modern Hopfield Network serving as content-addressable episodic memory. At inference, corrections are retrieved via soft attention with a similarity gate, enabling fuzzy morphological matching. On our curated benchmark of 312 multilingual proper nouns across 18 language families, FlowEdit reduces target-word Phoneme Error Rate by 92.7% relative to the zero-shot baseline while maintaining identical general-speech quality. Corrections complete in approximately 15 seconds on a single GPU.


## VLA
### Lagrange: An Open-Vocabulary, Energy-Based Sparse Framework for Generalized End-to-End Driving
**Authors**: Shihao Ji, HongXi Li, Zihui Song, Mingyu Li

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20274v1](https://arxiv.org/pdf/2606.20274v1)

**Abstract**: Scaling end-to-end autonomous driving to complex, open-world environments requires perceptual models that generalize to anomalous scenarios and planners that produce kinematically valid trajectories. Existing paradigms face a distinct dichotomy between representational efficiency and generalization capacity. Dense models (e.g., occupancy networks), while geometrically robust, incur critical computational bottlenecks and struggle with high-level semantic reasoning. Conversely, sparse, query-based planners are efficient but reliant on closed-set definitions, rendering them vulnerable to out-of-distribution (OOD) events. Although recent Vision-Language-Action (VLA) models offer open-vocabulary reasoning, their autoregressive, discrete token generation fundamentally conflicts with the continuous, high-frequency control requirements of vehicle dynamics. To address this, we propose Lagrange, an open-vocabulary, computationally sparse driving framework based on Masked Latent Fields (MLF). Rather than relying on dense volumetric reconstructions or closed-set query mechanisms, Lagrange exploits Vision-Language Models (VLMs) to encode class-agnostic object proposals into continuous semantic visual tokens. We introduce an intent-driven masked cross-attention module that temporally filters irrelevant entities, decoding the attended tokens into an implicit continuous energy field defined over spatial coordinates. By framing decision-making as a Lagrangian action minimization problem spanning this energy field, we enforce strict compliance with vehicle kinematics while executing collision avoidance. Extensive offline evaluations on both standard (nuScenes) and long-tail (CODA) benchmarks demonstrate that Lagrange establishes a promising framework for robust, interpretable, and kinematically feasible open-world autonomy.


### Finetuning Vision-Language-Action Models Requires Fewer Layers Than You Think
**Authors**: Gia-Binh Nguyen, Trong-Bao Ho, Thien-Loc Ha, Khoa Vo, Philip Lund Møller, Quang T. Nguyen, Long Dinh, Tuan Dam, Vu Duong, Tung M. Luu, Trung Le, Tran Nguyen Le, Minh Vu, An Thai Le, Ngan Le, Daniel Sonntag, James Zou, Jan Peters, Duy M. H. Nguyen, Ngo Anh Vien

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20246v1](https://arxiv.org/pdf/2606.20246v1)

**Abstract**: Vision-Language-Action (VLA) models pre-trained on massive video-robot datasets have revolutionized robotic manipulation, yet their multi-billion parameter architectures impose prohibitive computational burdens during downstream fine-tuning and real-time inference. In this work, we reveal a highly non-trivial architectural characteristic of these continuous control foundation policies (e.g., pi_0, GR00T-N1.5): despite being trained on diverse physical trajectories, they exhibit severe layer-wise representational redundancy. To exploit this, we introduce a structural compression pipeline that is entirely training-free, bypassing the need of existing methods to load full-scale models to learn optimized token reductions or dynamic layer selectors. Instead, using only a single forward pass via Centered Kernel Alignment to identify redundant layer features, we remove twin layers to permanently compress the model depth by up to 50% across both the VLM backbone and the continuous control policy head. Downstream fine-tuning of this streamlined architecture yields a dual acceleration benefit: a 40-50% reduction in training time and up to 30% faster real-time inference, while matching or exceeding full-scale base model performance. We comprehensively validate our method across three simulation benchmarks (LIBERO, RoboCasa, SimplerEnv) and 10 diverse real-world manipulation tasks across 4 unique robotic embodiments. These results prove that advanced VLAs require significantly fewer layers than previously assumed, offering a highly compute-efficient paradigm for scalable robot learning.


### Pose6DAug: Physically Plausible Multi-view Object Swapping for Robot Data Augmentation
**Authors**: Jonghoon Lee, Seong Hyeon Park, Byungwoo Jeon, Minha Lee, Jinwoo Shin

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20118v1](https://arxiv.org/pdf/2606.20118v1)

**Abstract**: Vision-language-action (VLA) policies have shown strong potential for general-purpose manipulation, yet they often fail on novel, out-of-distribution objects whose appearance or geometry deviates from the training distribution. The standard remedy is to collect multi-view teleoperation data for every failure case, but this scales poorly in both cost and time. We introduce Pose6DAug, a failure-driven data augmentation framework that turns a policy's own successful episodes into targeted demonstrations for its failure modes, without any new data collection. Our key insight is that each successful episode already encodes a physically valid action trajectory together with calibrated multi-view observations. By swapping only the manipulated object while preserving this trajectory, we obtain new and physically grounded demonstrations. However, naive 2D video editing breaks multi-view consistency and physical plausibility, particularly under heavy occlusion and egocentric viewpoints. Our method instead operates directly in 3D, anchoring the target object with an explicit mesh driven by a temporally coherent 6D pose trajectory, ensuring geometrically consistent renderings across all camera views. Fine-tuning a VLA on data augmented by our method improves success rates by 16.5% relative to the state-of-the-art baseline on novel objects, while preserving in-distribution performance. These results show that multi-view and physically consistent augmentation is a practical path to scalable VLA generalization.


### Tri-Info: Generalizable, Interpretable Failure Prediction for VLA Models via Information Theory
**Authors**: Jinghan Yang, Yunchao Zhang, Wang Yuan, Haolun Wan, Jiaming Zhang, Zhengyang Hu, Yanchao Yang

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.19998v1](https://arxiv.org/pdf/2606.19998v1)

**Abstract**: Vision-Language-Action (VLA) models are increasingly deployed across diverse tasks, yet they remain black boxes whose physical interactions can cause irreversible harm, making generalizable and interpretable failure detection essential. We observe that successful and failed rollouts carry systematically different information-theoretic signatures. Building on this, we formalize VLA control as a closed-loop information pipeline and derive the Triple Information-theoretic (Tri-Info) signals that capture whether actions remain diverse, temporally consistent, and coupled to state transitions. Across six VLA models and three benchmark environments, Tri-Info matches the strongest baselines in-domain. Moreover, Tri-Info transfers across architectures, environments, and the sim-to-real gap without retraining, reaching 83\% accuracy on real-world tasks where prior detectors collapse to chance. This establishes Tri-Info as a simple yet powerful method that not only detects failures with strong cross-domain generalization, but also delivers interpretable diagnostics of the underlying failure modes.


### Does VLA Even Know the Basics? Measuring Commonsense and World Knowledge Retention in Vision-Language-Action Models
**Authors**: Nikita Kachaev, Andrey Moskalenko, Matvey Skripkin, Nikita Kurlaev, Daria Pugacheva, Albina Burlova, Mikhail Kolosov, Denis Shepelev, Andrey Kuznetsov, Elena Tutubalina, Aleksandr I. Panov, Alexey K. Kovalev, Vlad Shakhuro

**Published Date**: 2026-06-17

**Updated Date**: 2026-06-17

**PDF Url**: [2606.19297v1](https://arxiv.org/pdf/2606.19297v1)

**Abstract**: Embodied Vision-Language-Action (VLA) models are typically obtained by fine-tuning powerful pretrained VLMs on robotics data, yet it is unclear how much commonsense and factual knowledge they retain after adaptation. Failures on knowledge-sensitive tasks are ambiguous, conflating missing knowledge with poor generalization of low-level control. We introduce Act2Answer, a lightweight protocol that adapts VLM knowledge benchmarks to VLA evaluation by requiring agents to answer through action. Each question becomes a short tabletop episode where the agent performs a single object-placement action to select among candidate answers, yielding an action-grounded success rate with reduced control confounds. We curate a test suite of such environments across diverse commonsense and world-knowledge categories and introduce layerwise intent probing to localize answer-relevant information across the VLM backbone and action head. In a large-scale study of 7 VLA models and 9 VLM baselines, we systematically rank models across categories, finding that VLAs show solid performance on simple concepts while exhibiting larger gaps on richer semantic categories relative to their source VLMs, that VQA co-training is associated with better knowledge retention, and that answer-relevant signals peak in middle VLA layers but attenuate in upper layers. Act2Answer is available at https://tttonyalpha.github.io/act2answer/.


### LaWAM: Latent World Action Models for Efficient Dynamics-Aware Robot Policies
**Authors**: Jialei Chen, Kai Wang, Kang Chen, Shuaihang Chen, Feng Gao, Wenhao Tang, Zhiyuan Li, Weilin Liu, Zhuyu Yao, Boxun Li, Yuanbo Xu, Chao Yu

**Published Date**: 2026-06-14

**Updated Date**: 2026-06-14

**PDF Url**: [2606.15768v1](https://arxiv.org/pdf/2606.15768v1)

**Abstract**: Vision-Language-Action models (VLAs) leverage large-scale vision-language pretraining for semantic robot control, but often lack explicit foresight into how robot actions change the scene. World-Action Models (WAMs) address this limitation by conditioning policies on predicted futures, yet existing approaches typically rely on computationally expensive video generation with substantial pixel-level redundancy. We present LaWAM, a Latent World Action Model that exposes predictive dynamics to robot policies through compact latent visual subgoals instead of reconstructed future video. At the core of LaWAM is a latent-action-conditioned Latent World Model (LaWM). We obtain LaWM by training a latent action model in the latent space of a pretrained vision foundation model and repurposing its forward decoder to predict future observation features for scene evolution. LaWAM then conditions action generation on these predicted latent visual subgoals to enable dynamics-aware robot control. LaWAM achieves state-of-the-art or competitive success rates (SRs) across LIBERO (98.6% SR), RoboTwin (91.22% SR), and real-world manipulation tasks while retaining low-latency inference. LaWAM runs in 187 ms per action-chunk prediction and achieves up to 24x lower wall-clock latency than pixel-space WAMs.


## Agent
### Execution-State Capsules: Graph-Bound Execution-State Checkpoint and Restore for Low-Latency, Small-Batch, On-Device Physical-AI Serving
**Authors**: Liang Su

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20537v1](https://arxiv.org/pdf/2606.20537v1)

**Abstract**: Mainstream LLM serving systems reuse prefix work mainly through paged or radix key-value (KV) caches. This is highly effective for high-throughput, high-concurrency serving, but it manages only one positional fragment of execution state: the KV cache. We study the opposite regime: low-latency, small-batch, on-device physical-AI serving, where interactive LLM agents, speech systems, and robot policies repeatedly branch, reset, interrupt, and re-enter under tight responsiveness budgets. We introduce execution-state capsules, a graph-bound checkpoint and restore mechanism for the complete restorable state at a committed boundary. FlashRT is a white-box, backend-facing kernel runtime whose evaluated NVIDIA CUDA backend runs captured graph plans over contiguous static buffers with no block-table indirection. Because the live state is a closed set of named buffers, a capsule can snapshot, restore, fork, or roll back the whole execution boundary, including KV, recurrent state, convolution state, MTP state, and metadata. This moves reuse from token-addressed KV fragments to graph-bound execution-state boundaries. On an RTX 5090, capsule restore is byte-exact at the stored-state level and token-identical under greedy decode. A KV-only ablation diverges, showing that recurrent state is load-bearing. GPU-resident snapshot and restore are sub-millisecond, and TTFT speedup over cold prefill grows from 3.9x at 2k tokens to 27x at 16k tokens. On Jetson AGX Thor and DGX Spark, the same correctness and structural properties hold. Capsules are not a replacement for high-throughput KV-cache serving; they define a complementary latency-first serving point for explicit execution-state reuse.


### LedgerAgent: Structured State for Policy-Adherent Tool-Calling Agents
**Authors**: Md Nayem Uddin, Amir Saeidi, Eduardo Blanco, Chitta Baral

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20529v1](https://arxiv.org/pdf/2606.20529v1)

**Abstract**: Policy-adherent tool-calling agents in customer-service domains must maintain task states across turns while calling tools and obeying domain policies. Task states consist of relevant facts, identifiers, constraints, and conditions observed through user interaction and tool calls. In standard agents, task states are not represented separately. Observations, tool returns, and policy instructions are placed in the prompt, leaving agents to reconstruct the relevant states from the prompt each time they decide what to do next. This design makes state management implicit, creating two common failure modes. An agent may retrieve the right facts but later ground its decision in stale, missing, or incorrect information; and a syntactically valid tool call may still violate a domain policy that depends on the current task state. We introduce \textsc{LedgerAgent}, an inference-time method for tool-calling agents that maintains observed task states in a separate ledger and renders the states into the prompt. The ledger is also used to check state-dependent policy constraints before environment-changing tool calls are executed, blocking policy violations. Across four customer-service domains and a mixed panel of open- and closed-weight models, \textsc{LedgerAgent} improves average pass\textasciicircum{}k over a standard prompt-based tool-calling approach, with the largest gains under stricter multi-trial consistency metrics.


### Sovereign Execution Brokers: Enforcing Certificate-Bound Authority in Agentic Control Planes
**Authors**: Jun He, Deying Yu

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20520v1](https://arxiv.org/pdf/2606.20520v1)

**Abstract**: Autonomous agents are increasingly connected to cloud, deployment, and data-control workflows, but production mutation authority should not reside inside non-deterministic reasoning processes. Existing access-control mechanisms authorize identities, while assurance layers certify proposed actions; neither alone provides a mandatory enforcement point for certified authority at the moment of mutation. This paper introduces the Sovereign Execution Broker (SEB), a runtime enforcement boundary for certificate-bound agentic infrastructure. SEB consumes certificates issued by the Sovereign Assurance Boundary (SAB), verifies that the requested mutation matches the certified execution contract, checks validity windows, policy epochs, revocation epochs, and live-state drift, mints scoped execution identity, invokes infrastructure APIs, and records signed decision and outcome records. By separating proposal, admission, and execution, SEB turns certified authority into a short-lived, revocable, auditable runtime capability, provided that production mutation APIs reject non-broker identities. We present the SEB execution model, certificate and replay-verification predicates, scoped identity semantics, bypass-prevention deployment patterns, failure behavior, and a concrete prototype implementation. We evaluate the prototype on AWS and Kubernetes clusters, measuring latency overheads, revocation propagation, drift detection, and security under fault injection.


### Probe-and-Refine Tuning of Repository Guidance for Coding Agents
**Authors**: Asa Shepard, Jeannie Albrecht

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20512v1](https://arxiv.org/pdf/2606.20512v1)

**Abstract**: LLM-based coding agents need higher-level operational knowledge about a repository (which files house which subsystems, how to run the test suite, which workflows have historically led to wrong fixes) that does not exist in the code itself. Engineers typically maintain \texttt{AGENTS.md} files to supply this context as instructions for coding agents, but whether they help is contested: recent studies disagree on whether LLM-generated guidance improves or harms agent performance. In this paper we show that how the guidance is produced is the decisive variable, and introduce \emph{probe-and-refine tuning}: a procedure that uses synthetic bug-fix probes to iteratively diagnose and patch a repository's guidance file through single-shot LLM calls, with no agent loop or tool use during tuning. On SWE-bench Verified across four independent trials with Qwen3.5-35B-A3B at 200 steps, probe-and-refine achieves 33.0\,\% mean resolve rate vs.\ 28.3\,\% for the static knowledge base used to initialize it and 25.5\,\% for an unguided baseline ($p < 0.001$ for both probe-and-refine contrasts). The improvement comes from coverage rather than precision: refined guidance produces evaluable patches for 14.5 percentage points (pp) more instances while per-patch precision remains statistically constant ($\sim$59\,\%, $p = 0.119$), showing that improved guidance helps agents reach the correct file rather than improving the quality of the changes they make. Further, a step-budget experiment shows that guidance is what lets the agent use a larger step budget productively, and a cross-model experiment with NVIDIA-Nemotron-3-Nano-30B-A3B finds that the tuning loop degrades when the model cannot generate sufficiently diagnostic output, though per-patch precision remains constant even then.


### Efficient and Sound Probabilistic Verification for AI Agents
**Authors**: Alaia Solko-Breslin, Pramod Kaushik Mudrakarta, Mihai Christodorescu, Somesh Jha, Krishnamurthy Dj Dvijotham

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20510v1](https://arxiv.org/pdf/2606.20510v1)

**Abstract**: Securing AI agents that operate in complex digital environments has become a critical need, and runtime monitoring approaches that formulate and enforce policies expressed in a formal language like Datalog offer a promising solution. However, existing approaches are restricted to deterministic policies. In many practical applications of AI agents, there is a need to enforce security policies in the face of ambiguity, leading to probabilistic predicates or state transitions (for example, a declassifier or Personally Identifiable Information (PII) detector that has some failure probability on each invocation). Furthermore, in many such applications, one cannot easily make the independence assumptions necessary to invoke prior work on probabilistic inference in Datalog. We address this by introducing a sound and efficient framework for such verification based on distributionally robust optimization, computing sound upper bounds on the probability of policy violation regardless of possible correlations between predicates. On standard benchmarks for terminal and tool calling agents, we demonstrate that our approach outperforms prior art and improves the security-utility trade-off while ensuring rigorous bounds on the probability of policy violation.


### Contagion Networks: Evaluator Bias Propagation in Multi-Agent LLM Systems
**Authors**: Zewen Liu

**Published Date**: 2026-06-18

**Updated Date**: 2026-06-18

**PDF Url**: [2606.20493v1](https://arxiv.org/pdf/2606.20493v1)

**Abstract**: When large language models serve as evaluators in multi-agent systems, their systematic evaluation biases propagate through the agent network. We introduce Contagion Networks, a formal framework for measuring how evaluator biases spread across interacting LLM agents. In a controlled 3-agent experiment using DeepSeek-chat with three distinct evaluator bias profiles (structured, balanced, evidence-based), we measure the Cross-Agent Contagion Matrix Gamma_3 and find that evaluator biases consistently propagate between agents (gamma in [0.157, 0.352]), even within the same underlying model. We identify three propagation regimes governed by the spectral radius rho(Gamma_N), and demonstrate that homogeneous-model agents produce contagion coefficients 3-5x weaker than cross-model coefficients observed in prior work (MM-EPC: gamma approx 0.85-1.3), placing them in the suppression regime. We show that increasing evaluator committee size from k=1 to k=3 reduces effective contagion by 72.4%, providing an actionable mitigation strategy. We release the open-source Contagion Network experimental framework.


