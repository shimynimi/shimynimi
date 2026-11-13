# Literature Review Notes

**Status:** Starting bibliography; this is not a systematic review. The review must be expanded before final hypotheses or novelty claims are made.

## Core dataset papers

### Zhang et al. (2026) — Extended dataset descriptor

Zhang, M., Liu, P. R., Su, H., Zhao, M., Li, X., Born, S., Lee, Y., Honey, C. J., Chen, J., & Lee, H. (2026). *An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures.* Scientific Data. [https://doi.org/10.1038/s41597-026-08414-6](https://doi.org/10.1038/s41597-026-08414-6)

Why it matters: describes 118 think-aloud fMRI participants, preprocessed MRI outputs, word-level timestamps, sentence-level LLM-generated ratings across 14 affective/sensory dimensions, and self-report measures. It is the primary source for the extended data release and annotation definitions.

### Su et al. (2025) — Prior analysis of thought transitions

Su, H., Li, X., Born, S., et al. (2025). *Neural dynamics of spontaneous memory recall and future thinking in the continuous flow of thoughts.* Nature Communications, 16, 6433. [https://doi.org/10.1038/s41467-025-61807-w](https://doi.org/10.1038/s41467-025-61807-w)

Why it matters: analyzes neural correlates of thought boundaries/transitions, semantic content, and interactions within/between default and control networks using the earlier release of the dataset. The present proposal should not simply repeat thought-boundary analyses.

## Methods and standards

- **Nilearn first-level models:** [Documentation](https://nilearn.github.io/stable/glm/first_level_model.html). Provides the GLM framework in which voxel time series are modeled against predicted BOLD responses formed by convolving event predictors with an HRF; design matrices can include nuisance regressors.
- **BIDS:** [Specification](https://bids-specification.readthedocs.io/en/stable/). Use for organizing and validating neuroimaging files and metadata.
- **fMRIPrep:** [Documentation](https://fmriprep.org/en/stable/). Consult to understand preprocessing provenance and derivatives; the project should use the released derivatives where appropriate and document any further preprocessing.

## Literature questions to resolve

1. Which affective dimensions are most strongly grounded in spontaneous thought and have a defensible neural hypothesis?
2. Which networks/ROIs are justified independently of the observed results?
3. How have prior studies controlled for speech production, speech-related head motion, pauses, and thought transitions during naturalistic think-aloud fMRI?
4. What are the implications of using LLM-generated ratings instead of direct participant ratings?
5. Does any recent paper already analyze the same affective/sensory dimensions in this release?
6. What group-level model best respects repeated sentence observations nested within participants?

## Novelty boundary

The project must be presented as a proposed secondary analysis of an existing public dataset. Novelty is not established by selecting a feature that was newly included in a data descriptor. A focused literature review is required to identify the exact unresolved question and avoid overlap with existing or in-progress analyses.