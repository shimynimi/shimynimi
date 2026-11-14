# Sentence-Level Affective Content and Regional BOLD Activity During Verbalized Spontaneous Thought

**Completed deliverable:** Research design and documentation package for a proposed reproducible secondary analysis of naturalistic think-aloud fMRI data.  
**Research areas:** Computational Neuroscience · Cognitive Neuroscience · NLP · Neuroimaging  
**Empirical study status:** fMRI data analysis has not started.  
**Researcher:** Shima Rezai

> **Scope of completion:** The research question, focused literature review, dataset description, preliminary quality-control plan, methodological framework, statistical analysis plan, data-governance guidance, and reproducibility documentation have been prepared. This is a completed research-protocol deliverable, not a completed empirical fMRI study. No participant-level analysis, statistical result, or scientific finding is claimed.

## Project overview

Spontaneous thought changes continuously in content and affective tone. Naturalistic think-aloud fMRI data provide an opportunity to study how sentence-level features of verbalized thought relate to ongoing brain activity. This project develops a documented secondary-analysis protocol using **OpenNeuro ds006067 (version 2.0.0)** and its associated behavioral annotations on OSF.

The primary question is whether **within-participant variation in the dataset-defined sentence-level emotional-intensity rating** is associated with regional BOLD responses around verbalization, after modeling sentence/speech events and prespecified nuisance signals.

The dataset labels this rating `emotional intensity` and scores it from −4 (very negative) to +4 (very positive), with neutral content near zero. Because the scale is signed, the protocol preserves the dataset's terminology and treats it analytically as a **signed, valence-like affective-content score**. It is not described as a direct measurement of the participant's subjective emotional state.

## Research question

**Within participants, is sentence-level affective content associated with regional BOLD activity during verbalized spontaneous thought, beyond the modeled effects of overt speech, head motion, and other prespecified nuisance factors?**

The primary predictor is the dataset-defined emotional-intensity rating, centered within participant. Sadness and anxiety ratings are secondary exploratory variables, not co-primary hypotheses.

## Why this dataset?

The dataset includes 118 healthy adults who continuously verbalized spontaneous thoughts during a 10-minute fMRI session. The extended release provides BIDS-organized MRI data, fMRIPrep/FreeSurfer derivatives, word- and sentence-level timestamps, sentence-level GPT-5 Nano ratings across 14 psychological dimensions, and some post-scan questionnaires. Human ratings by four independent raters are available for 18 transcripts selected from the lower-than-median transcript-length group; this subset is useful for sensitivity checks but is not a representative re-rating of the full sample.

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

## Completed protocol deliverables

| Deliverable | Description |
| --- | --- |
| Research question and scope | Defined primary question, aims, and exploratory questions |
| Focused literature review | Positioned the proposal against dataset-specific and adjacent prior work |
| Dataset description and QC plan | Documented source versions, variables, provisional QC, and sample-size uncertainty |
| Methodological framework | Specified the proposed event-related fMRI and ROI workflow |
| Statistical analysis plan | Documented first-level and group-level modeling, inference, and robustness checks |
| Limitations and data governance | Defined interpretation boundaries and privacy safeguards |
| Reproducibility plan | Specified planned code organization, versioning, and reporting requirements |

## Repository contents

| Path | Purpose |
|---|---|
| [Research protocol](docs/research_protocol.md) | Full proposal, objectives, questions, and hypotheses |
| [Literature review](docs/literature_review.md) | Focused review and positioning |
| [Dataset and QC plan](docs/dataset_and_qc.md) | Data sources, annotation definitions, sample/QC considerations |
| [Methodology](docs/methodology.md) | Proposed fMRI workflow and event model |
| [Statistical analysis plan](docs/statistical_analysis_plan.md) | First-level, group-level, and sensitivity analyses |
| [Limitations and ethics](docs/limitations_and_ethics.md) | Interpretation, ethics, and data governance |
| [Reproducibility plan](docs/reproducibility_plan.md) | Planned implementation and reproducibility requirements |
| [BIDS inventory utility](src/audit_bids_dataset.py) | Preliminary file-inventory script; not an fMRI QC or analysis pipeline |
| [Project status](PROJECT_STATUS.md) | Explicit separation of completed protocol work and pending empirical analysis |
| [CV entry](CV_ENTRY.md) | Accurate wording for describing the completed protocol deliverable |

## Limitations and interpretation

- The dataset participants are healthy adults; this protocol does not support claims about MDD patients or clinical diagnosis.
- GPT-generated affective ratings describe transcript content, not a direct measure of internal emotional state.
- Sentence timestamps mark verbalization, not the onset of the underlying thought.
- Speech-related motion and physiological effects may confound BOLD estimates.
- Observational associations do not establish causality.
- The final usable sample is unknown until the data audit and quality-control procedure are completed.
- The literature review is focused but not systematic; novelty has not been established.

## Current status

**Completed:** research design and documentation package (version 0.2.0).  
**Not started:** participant-level data audit, fMRI quality control, event alignment, GLM fitting, group inference, and empirical interpretation.

This repository is suitable for presenting a completed research-design and protocol-development project. It must not be described as a completed empirical fMRI study until the analysis has actually been performed and validated.
