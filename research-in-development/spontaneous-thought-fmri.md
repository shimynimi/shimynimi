# Exploratory Analysis of Affective Features of Spontaneous Thought and Their Neural Correlates

**Research status:** Proposed research direction — not yet started  
**Fields:** Computational Neuroscience · Cognitive Neuroscience · NLP · Neuroimaging  
**Proposed data source:** OpenNeuro `ds006067` (version 2.0.0) and the associated OSF behavioral/annotation data

> **Status and integrity note:** This page describes a proposed secondary analysis. No analyses have been run for this project, and it reports no results, performance metrics, or scientific conclusions. The research question and analysis plan will be refined after a detailed literature review and a feasibility audit of the dataset.

## 1. Motivation

Spontaneous thought is an important component of ongoing cognition. Naturalistic think-aloud fMRI data provide an opportunity to examine how features of verbalized thought relate to brain activity over time.

The proposed project builds on the researcher's previous interests in language, concept representations, cognitive modeling, and computational approaches to mental health. It extends that computational background toward direct analysis of publicly available functional neuroimaging data.

## 2. Proposed research question

**Do sentence-level affective characteristics of spontaneously verbalized thoughts explain within-participant variation in BOLD activity beyond effects associated with speech production, head motion, and thought transitions?**

The exact affective dimensions to be analyzed will be selected only after inspecting the dataset's annotation documentation and confirming their coverage and operational definitions.

This is an exploratory question, not a claim that the proposed relationship is known or that the project is novel. A structured review of related work is required before finalizing hypotheses.

## 3. Data source and feasibility

The proposed dataset is:

- **OpenNeuro:** [ds006067, version 2.0.0](https://openneuro.org/datasets/ds006067/versions/2.0.0)
- **Behavioral and annotation data:** [Think Aloud Behavioral Data (OSF)](https://osf.io/a56rm)
- **Dataset article:** Zhang et al. (2026), [An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures](https://doi.org/10.1038/s41597-026-08414-6)

The published dataset description reports data from 118 healthy adults who verbalized spontaneous thoughts during 10-minute fMRI sessions. The extended release includes preprocessed MRI derivatives, speech transcripts with word-level timestamps aligned to image acquisition, sentence-level psychological-dimension ratings generated with an LLM, and self-report measures. The exact usable sample for this proposed analysis must be established after checking missingness, annotation coverage, and imaging quality.

**Important:** Participants in this dataset are healthy adults; this is not an MDD patient dataset. The proposed study would investigate spontaneous thought and neural correlates in this sample. It would not test MDD diagnosis or identify clinical biomarkers.

## 4. Proposed analysis plan

The plan below is preliminary and will be updated after inspecting the data dictionary, acquisition metadata, preprocessing outputs, and relevant literature.

### Phase A — Literature and data audit

1. Review the dataset article and prior studies using `ds006067`.
2. Inspect the BIDS structure, MRI derivatives, transcript annotations, psychological-dimension ratings, and available participant-level measures.
3. Establish which participants have complete and usable transcript–fMRI alignment.
4. Document missingness, temporal resolution, head-motion quality, and available nuisance regressors.
5. Confirm data-use terms and whether derived outputs may be redistributed.

### Phase B — Operationalize thought features

1. Identify the affective dimensions actually supplied in the annotation files.
2. Confirm their scales, annotation level, missingness, and interpretation from the data documentation.
3. Construct sentence- or event-level regressors using the timing fields supported by the dataset.
4. Where human ratings are available, use them for a sensitivity analysis of LLM-derived ratings rather than assuming that an LLM score is a direct measurement of a participant's subjective emotional state.

### Phase C — Neuroimaging analysis

1. Begin with the released preprocessed fMRI derivatives where appropriate; document their provenance and preprocessing details.
2. Select a small set of a priori regions of interest (ROIs) based on an independent literature review and a stated atlas.
3. Model event-related BOLD responses using a general linear model (GLM), with an appropriate hemodynamic response function (HRF).
4. Include relevant nuisance terms, especially motion-related regressors, speech-production effects, temporal trends, and thought-transition or topic-change effects where supported by the annotations.
5. Estimate participant-level effects before conducting group-level inference.

ROI selection and the exact design matrix will be fixed before confirmatory analyses to reduce researcher degrees of freedom. Whole-brain analyses, if attempted, will be treated as secondary and will use appropriate multiple-comparison correction.

### Phase D — Statistical evaluation and robustness

1. Report effect sizes and uncertainty intervals, not only p-values.
2. Account for repeated observations within participants using an appropriate hierarchical or mixed-effects approach where justified by the data structure.
3. Correct for multiple comparisons across the prespecified ROI and affective-dimension family.
4. Test robustness to head-motion thresholds, missing annotations, temporal alignment choices, and alternative nuisance specifications.
5. Compare results using LLM-derived ratings with results using human annotations where suitable human ratings exist.

No specific outcome is assumed. Null, inconclusive, or non-robust findings will be reported transparently.

## 5. Planned tools and learning goals

The computational tools considered for this project include:

- Python, NumPy, Pandas, SciPy, and statsmodels
- NiBabel and Nilearn for neuroimaging data handling and analysis
- BIDS conventions and fMRIPrep derivative documentation
- Jupyter notebooks for transparent exploratory analysis

The project will also be used to strengthen foundations needed for computational neuroscience: linear algebra, probability and statistics, regression and general linear models, convolution, the BOLD signal, and the hemodynamic response function.

Listing these tools is a plan, not a claim that the analysis has already been implemented.

## 6. Risks and limitations

- **Speech-related motion:** Speaking during MRI acquisition can introduce motion and other artifacts. Quality control and nuisance modeling are essential; they may reduce the usable sample.
- **Annotation validity:** LLM-generated affective ratings are annotations of transcript content, not direct measurements of participants' internal emotional states.
- **Temporal alignment:** Sentence ratings, word timestamps, acquisition timing, and the HRF operate at different temporal scales. Their alignment must be justified and documented.
- **Observational design:** Associations between thought features and BOLD activity do not establish causality.
- **Sample characteristics:** The dataset consists of healthy adults. It cannot support direct claims about MDD patients or clinical diagnosis.
- **Research novelty:** Prior work has already analyzed thought transitions and neural activity in this dataset. The affective-feature question must be checked against the full literature, including recent work, before any novelty claim is made.
- **Privacy and data governance:** Raw speech and transcripts may contain sensitive or potentially identifying content. They will not be copied into this public repository. Only code, documentation, and outputs that are lawful and appropriate to share may be published.

## 7. Planned milestones

1. **Feasibility audit:** review literature, data dictionary, coverage, data-use terms, and QC.
2. **Foundations and pilot:** learn the required fMRI/GLM concepts and reproduce a small, documented data-inspection workflow.
3. **Pre-specified analysis:** define hypotheses, ROIs, nuisance variables, exclusions, and statistical plan.
4. **Analysis and validation:** run the analysis, robustness checks, and transparent reporting.
5. **Research output:** prepare a reproducible report and, only if supported by results, a poster or manuscript draft.

## 8. Related work and resources

1. Zhang, M. et al. (2026). *An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures.* Scientific Data. [https://doi.org/10.1038/s41597-026-08414-6](https://doi.org/10.1038/s41597-026-08414-6)
2. *Neural dynamics of spontaneous memory recall and future thinking in the continuous flow of thoughts* (2025). Nature Communications. [https://doi.org/10.1038/s41467-025-61807-w](https://doi.org/10.1038/s41467-025-61807-w)
3. *Neural signatures of spontaneous transitions between internal and external thought* (2026 preprint). bioRxiv. [https://www.biorxiv.org/content/10.64898/2026.08.27.747628v1.full](https://www.biorxiv.org/content/10.64898/2026.08.27.747628v1.full)

These studies demonstrate that the dataset and adjacent questions are already being actively investigated. They are starting points for a literature review, not evidence that the proposed analysis is novel.

---

**Current status:** Proposal and feasibility planning only. No dataset analysis, statistical result, or neuroimaging finding has yet been produced for this project.
