# Affective and Sensory Dimensions of Spontaneous Thought: An NLP-Informed fMRI Study

**Research status:** Proposed independent research project — analysis not yet started  
**Fields:** Computational Neuroscience · Cognitive Neuroscience · NLP · Neuroimaging  
**Proposed data sources:** OpenNeuro `ds006067` (version 2.0.0) and the associated OSF behavioral/annotation data

> **Status and integrity note:** This page describes a proposed secondary analysis. No participant-level analyses have been run, no statistical models have been fitted, and no results or scientific conclusions are claimed. The research question and analysis plan will be refined after a detailed literature review and feasibility audit.

## Proposed research question

**Do sentence-level affective characteristics of spontaneously verbalized thoughts explain within-participant variation in BOLD activity beyond effects associated with speech production, head motion, and thought transitions?**

The project proposes integrating sentence-level LLM-generated affective/sensory annotations with naturalistic think-aloud fMRI data. The exact primary annotation dimension, ROI definitions, inclusion criteria, and statistical model remain provisional until the data audit and literature review are complete.

## Data sources

- [OpenNeuro ds006067, version 2.0.0](https://openneuro.org/datasets/ds006067/versions/2.0.0)
- [Think Aloud Behavioral Data (OSF)](https://osf.io/a56rm)
- [2026 dataset descriptor — Scientific Data](https://doi.org/10.1038/s41597-026-08414-6)
- [Prior 2025 analysis of spontaneous thought transitions — Nature Communications](https://doi.org/10.1038/s41467-025-61807-w)

The extended data descriptor reports 118 participants, word-level timestamps, sentence-level ratings across 14 affective and sensory dimensions, preprocessed MRI derivatives, and self-report measures. The usable fMRI sample for this project must be determined independently after quality control; the behavioral sample size must not be treated as the guaranteed imaging sample.

The dataset contains healthy adults, not an MDD patient cohort. This project therefore does not test MDD diagnosis or claim to identify clinical biomarkers.

## Expanded project documentation

The complete proposal and analysis scaffold are organized in the project folder:

- [Project README and overview](spontaneous-thought-fmri/README.md)
- [Research proposal](spontaneous-thought-fmri/docs/research-proposal.md)
- [Preliminary analysis plan](spontaneous-thought-fmri/docs/analysis-plan.md)
- [Literature review notes](spontaneous-thought-fmri/docs/literature-review.md)
- [Data governance and ethics](spontaneous-thought-fmri/docs/data-governance.md)
- [Project status tracker](spontaneous-thought-fmri/PROJECT_STATUS.md)
- [Initial BIDS audit utility](spontaneous-thought-fmri/src/audit_bids_dataset.py)

## Proposed methods

The planned workflow includes BIDS and annotation audits, verification of sentence-level rating scales, temporal alignment of transcripts with fMRI acquisition, first-level GLMs with an appropriate HRF and nuisance regressors, literature-defined ROI analysis, group-level inference, and robustness checks.

A prior 2025 publication using this dataset examined thought transitions and neural dynamics. The proposed affective/sensory analysis is a direction for further investigation, not a verified novelty claim. A focused literature review is required before confirmatory hypotheses are fixed.

**Current status:** Proposal and feasibility planning only. No data analysis, GLM results, or neuroimaging findings have yet been produced.