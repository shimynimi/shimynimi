# Sentence-Level Affective Content and Regional BOLD Activity During Verbalized Spontaneous Thought

**Proposed reproducible secondary-analysis protocol using naturalistic think-aloud fMRI data**

**Research area:** Computational Neuroscience · Cognitive Neuroscience · NLP · Neuroimaging  
**Research status:** Proposed independent research project — research design and protocol development; empirical analysis has not started.  
**Proposed researcher:** Shima Rezai

> **Status statement:** This repository currently contains a proposed research protocol, not a preregistration, completed study, or executable analysis pipeline. No fMRI analysis, statistical testing, or scientific result has yet been produced. Do not describe the planned methods as completed work.

## Project overview

Spontaneous thought changes continuously in content and affective tone. Naturalistic think-aloud fMRI data make it possible to study how sentence-level features of verbalized thought relate to ongoing brain activity. This project proposes a secondary analysis of the public dataset **OpenNeuro ds006067 (version 2.0.0)** and its associated behavioral annotations on OSF.

The primary question is whether **within-participant variation in the dataset-defined sentence-level emotional-intensity rating** is associated with regional BOLD responses around verbalization, after modeling sentence/speech events and prespecified nuisance signals.

The dataset labels this rating `emotional intensity` and scores it from −4 (very negative) to +4 (very positive), with neutral content near zero. Because the scale is signed, this project will preserve the dataset's terminology and treat it analytically as a **signed, valence-like affective-content score**. It will not be described as a direct measurement of the participant's subjective emotional state.

## Research question

**Within participants, is sentence-level affective content associated with regional BOLD activity during verbalized spontaneous thought, beyond the modeled effects of overt speech, head motion, and other prespecified nuisance factors?**

The primary predictor is the dataset-defined emotional-intensity rating, centered within participant. Sadness and anxiety ratings are secondary exploratory variables, not co-primary hypotheses.

## Why this dataset?

The dataset includes 118 healthy adults who continuously verbalized spontaneous thoughts during a 10-minute fMRI session. The extended release provides BIDS-organized MRI data, fMRIPrep/FreeSurfer derivatives, word- and sentence-level timestamps, sentence-level GPT-5 (Nano) ratings across 14 psychological dimensions, and some post-scan questionnaires. Human ratings by four independent raters are available for 18 transcripts selected from the lower-than-median transcript-length group; this subset is useful for sensitivity checks but is not a representative re-rating of the full sample.

- **OpenNeuro:** [ds006067, version 2.0.0](https://openneuro.org/datasets/ds006067/versions/2.0.0)
- **Behavioral annotations and code:** [OSF — Think Aloud Behavioral Data](https://osf.io/a56rm)
- **Dataset descriptor:** [Zhang et al. (2026), Scientific Data](https://doi.org/10.1038/s41597-026-08414-6)

The participants are healthy adults, not an MDD patient cohort. This project is about spontaneous thought and neural activity in this dataset; it is not a study of MDD diagnosis or clinical biomarkers.

## Planned analysis at a glance

1. **Data and literature audit:** verify files, annotations, coverage, licenses, timing, image derivatives, and prior work.
2. **Transcript feature preparation:** join sentence-level ratings to sentence timestamps; center the primary rating within participant; inspect missingness and distributions.
3. **fMRI quality control:** inspect motion, temporal signal-to-noise, available derivatives, and event alignment; define the usable sample before outcome analysis.
4. **First-level modeling:** use an event-related GLM with a sentence/speech baseline regressor and a separate within-participant affective parametric modulator, convolved with a prespecified HRF; include motion and other justified nuisance regressors.
5. **ROI-level group inference:** estimate participant-level affect-modulator effects in a small, independently defined affect-relevant ROI set; test group effects with uncertainty intervals and multiplicity control.
6. **Robustness and exploratory analyses:** assess sensitivity to motion thresholds, HRF choices, speech-duration measures, the dataset-provided denoised derivative, and human ratings where available.

The provisional ROI candidates are medial prefrontal cortex (operationalized as the Harvard–Oxford Frontal Medial Cortex label), insular cortex, and bilateral amygdala. This is a candidate ROI family, not a finalized anatomical claim. Exact atlas release, label names, laterality, mask coverage, and resampling to BOLD space must be verified and fixed before inspecting primary effect estimates. Whole-brain analyses, if performed, will be secondary and corrected for multiple comparisons.

## Repository contents

| Path | Purpose |
|---|---|
| [`docs/research_protocol.md`](docs/research_protocol.md) | Full proposal, objectives, questions, and hypotheses |
| [`docs/review_notes.md`](docs/review_notes.md) | Independent review findings and decisions before publication |
| [`src/audit_bids_dataset.py`](src/audit_bids_dataset.py) | Preliminary BIDS file-inventory utility; not an fMRI QC or analysis pipeline |
| [`docs/literature_review.md`](docs/literature_review.md) | Related work and scope of the research gap |
| [`docs/dataset_and_qc.md`](docs/dataset_and_qc.md) | Data sources, variables, sample, quality, and inclusion plan |
| [`docs/methodology.md`](docs/methodology.md) | Planned transcript-to-fMRI and ROI analysis workflow |
| [`docs/statistical_analysis_plan.md`](docs/statistical_analysis_plan.md) | GLM specification, inference, and sensitivity analyses |
| [`docs/limitations_and_ethics.md`](docs/limitations_and_ethics.md) | Scientific, technical, and data-governance limitations |
| [`docs/reproducibility_plan.md`](docs/reproducibility_plan.md) | Future code, environment, and reporting requirements |
| [`config/analysis-plan.yaml`](config/analysis-plan.yaml) | Initial machine-readable analysis-plan template |
| [`CV_ENTRY.md`](CV_ENTRY.md) | Accurate CV wording for the proposal stage |
| [`PROFILE_TEXT.md`](PROFILE_TEXT.md) | Short GitHub profile description |

## Planned tools

Python, NumPy, Pandas, SciPy, NiBabel, Nilearn, statsmodels, Matplotlib, and Jupyter. The initial dependency list is a planning aid; exact versions will be pinned after the environment is installed and tested. No executable analysis pipeline is claimed at this stage.

## Important interpretation boundaries

- The GPT-5 Nano rating is an annotation of transcript content, not a direct measure of felt emotion.
- BOLD associations are observational and do not establish causality.
- The onset of verbalization is observed; the exact onset of the underlying thought is not. Conclusions must therefore refer to neural activity associated with verbalized thought, not the neural origin of thought itself.
- Speech production, auditory feedback, head motion, sentence duration, thought transitions, and topic changes may affect the signal and must be considered.
- The final number of usable participants is not known until quality control is run.
- No result, effect size, p-value, or clinical implication is assumed in advance.

## Citation

Zhang, M., Liu, P. R., Su, H., Zhao, M., Li, X., Born, S., Lee, Y., Honey, C. J., Chen, J., & Lee, H. (2026). *An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures*. Scientific Data. https://doi.org/10.1038/s41597-026-08414-6

See [`CITATION.cff`](CITATION.cff) for citation metadata for this proposal repository. The underlying dataset article is a peer-reviewed *Scientific Data* descriptor published on 29 September 2026.