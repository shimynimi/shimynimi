# Affective and Sensory Dimensions of Spontaneous Thought: An NLP-Informed fMRI Study

**Project status:** Research proposal and analysis scaffold — analysis not yet started  
**Project type:** Independent secondary-data research proposal  
**Research areas:** Computational Neuroscience · Cognitive Neuroscience · Natural Language Processing · Cognitive Modeling

> **Research integrity note:** This repository currently documents the research question, data sources, preliminary analysis plan, and reproducibility scaffold. No participant-level data have been analyzed for this project, no statistical models have been fitted, and no findings or performance metrics are claimed. The protocol will be refined after a formal data and literature audit.

## Overview

This project proposes a secondary analysis of publicly available naturalistic think-aloud fMRI data. It will examine whether sentence-level affective and sensory annotations of spontaneously verbalized thoughts are associated with within-participant variation in BOLD activity, after accounting for speech-related activity, head motion, thought structure, and other relevant nuisance effects.

The project is designed to connect computational language analysis with functional neuroimaging. It builds on prior work in NLP and computational modeling of cognition while adding a direct neuroimaging analysis component.

## Primary research question

**Do sentence-level affective characteristics of spontaneously verbalized thoughts explain within-participant variation in BOLD activity beyond effects associated with speech production, head motion, and thought transitions?**

The exact primary annotation dimension, ROI definitions, and model specification will be finalized only after inspecting the dataset documentation, annotation coverage, and relevant literature.

## Data sources

- **Neuroimaging:** [OpenNeuro ds006067, version 2.0.0](https://openneuro.org/datasets/ds006067/versions/2.0.0)
- **Behavioral transcripts and annotations:** [Think Aloud Behavioral Data (OSF)](https://osf.io/a56rm)
- **Dataset descriptor:** Zhang et al. (2026), [Scientific Data](https://doi.org/10.1038/s41597-026-08414-6)
- **Prior analysis of thought transitions:** Su et al. (2025), [Nature Communications](https://doi.org/10.1038/s41467-025-61807-w)

The extended dataset description reports 118 participants with 10-minute think-aloud fMRI sessions, word-level timestamps, sentence-level LLM-generated ratings across 14 affective and sensory dimensions, preprocessed MRI derivatives, and post-scan questionnaires. The usable imaging sample for this project must be established independently through data audit and quality control; 118 must not be treated as the guaranteed fMRI analysis sample.

## Proposed contribution

A prior 2025 study using this dataset examined thought transitions, semantic boundaries, and associated neural dynamics. The proposed analysis is differentiated by focusing on the affective and sensory annotations included in the extended 2026 data release. This is a proposed research direction, not a verified novelty claim; a structured literature review is required before finalizing hypotheses.

## Preliminary workflow

1. **Literature and data audit:** inspect the BIDS layout, fMRI derivatives, transcripts, timestamps, rating files, questionnaires, missingness, and quality-control metadata.
2. **Annotation validation:** verify the operational definitions and scales of the 14 sentence-level dimensions; assess agreement with human ratings for the available validation subset.
3. **Temporal alignment:** align sentence-level ratings and speech intervals to the fMRI acquisition time base, using the timing fields supplied with the dataset.
4. **First-level modeling:** construct participant-level event-related GLMs with an appropriate HRF and relevant nuisance regressors, including motion and speech-related effects where supported by the data.
5. **ROI and group analysis:** define a small set of a priori ROIs or networks from an independent literature review and atlas; estimate participant-level effects and conduct group-level inference.
6. **Robustness and reporting:** assess sensitivity to motion thresholds, missing annotations, timing choices, model specification, and multiple comparisons; report effect sizes and uncertainty.

## Repository structure

```text
.
├── README.md
├── PROJECT_STATUS.md
├── docs/
│   ├── research-proposal.md
│   ├── analysis-plan.md
│   ├── literature-review.md
│   ├── data-governance.md
│   └── data-dictionary-template.csv
├── data/
│   └── README.md
├── notebooks/
│   └── README.md
├── src/
│   ├── README.md
│   └── audit_bids_dataset.py
├── results/
│   └── README.md
├── figures/
│   └── README.md
└── requirements.txt
```

## Getting started

This scaffold does not include the MRI or behavioral data. Download the appropriate files from OpenNeuro and OSF under their stated terms, then keep them outside version control. See [data/README.md](data/README.md).

Create an environment and install the proposed Python dependencies:

```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\\Scripts\\activate
python -m pip install -r requirements.txt
```

Run the initial BIDS structure audit after downloading the MRI dataset:

```bash
python src/audit_bids_dataset.py --bids-dir /path/to/ds006067
```

The audit utility only inventories files and basic BIDS metadata. It does not preprocess MRI data or perform statistical analyses.

## Scientific and ethical boundaries

- The dataset participants are healthy adults; this project does not directly study MDD patients and cannot support clinical or diagnostic claims about depression.
- LLM-generated ratings describe the content of verbalized thoughts. They are not direct measurements of a participant's subjective emotional state.
- Speaking inside the scanner can introduce head motion and speech-related artifacts; quality control and nuisance modeling are essential.
- Associations between transcript features and BOLD activity are observational and do not establish causality.
- Raw speech, transcripts, MRI data, and participant-level sensitive records must not be copied into this repository. Publish only code, documentation, and outputs that are appropriate to share.
- No results are available yet. Null, inconclusive, or non-robust findings will be reported transparently after the analysis is conducted.

## Status

**Current stage:** Proposal, literature positioning, and repository scaffold.  
**Next milestone:** Complete the dataset audit and confirm the exact files, variables, sample coverage, and data-quality criteria before freezing hypotheses and the analysis plan.

## References

1. Zhang, M., Liu, P. R., Su, H., et al. (2026). *An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures.* Scientific Data. [https://doi.org/10.1038/s41597-026-08414-6](https://doi.org/10.1038/s41597-026-08414-6)
2. Su, H., Li, X., Born, S., et al. (2025). *Neural dynamics of spontaneous memory recall and future thinking in the continuous flow of thoughts.* Nature Communications, 16, 6433. [https://doi.org/10.1038/s41467-025-61807-w](https://doi.org/10.1038/s41467-025-61807-w)
3. [Nilearn: First-level fMRI models](https://nilearn.github.io/stable/glm/first_level_model.html)
4. [BIDS Specification](https://bids-specification.readthedocs.io/en/stable/)
5. [fMRIPrep Documentation](https://fmriprep.org/en/stable/)

---

*This is a living research plan. The question, inclusion criteria, regressors, ROIs, and statistical procedures may change after the data audit and literature review. Any changes will be documented before confirmatory analysis.*