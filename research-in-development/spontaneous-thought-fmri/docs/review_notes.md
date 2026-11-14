# Review Notes — Version 0.2.0

**Review date:** 14 November 2026  
**Review scope:** README, research protocol, dataset/QC plan, methodology, statistical analysis plan, literature review, CV wording, and package consistency.

## Overall assessment

The project is suitable to present publicly as a **proposed secondary-analysis project** once the researcher is comfortable with the scope and wording. It is not a completed study, an executable pipeline, or a preregistered protocol.

## Changes made in version 0.2.0

1. **Title precision:** The title now explicitly refers to sentence-level affective content and regional BOLD activity during *verbalized* spontaneous thought. The timestamps identify speech, not the private onset of a thought.
2. **Primary variable:** The dataset calls the variable `emotional intensity`, but it is scored from −4 (very negative) to +4 (very positive). The proposal retains the dataset's variable name and describes it as a signed, valence-like annotation of transcript content—not arousal and not a direct self-report of felt emotion. Ratings were generated with GPT-5 Nano.
3. **Sample-size discipline:** The dataset contains 118 released participants. The 73-person sample in the data descriptor came from a particular speech-versus-silence validation with additional exclusions; it is not the sample size for this project. The final analytical sample must be determined from the proposed analysis' own QC rules.
4. **Human ratings:** Four raters assessed 18 transcripts, selected from transcripts with fewer sentences than the median. This is useful for a limited sensitivity analysis, not a representative human re-annotation of all participants.
5. **Model identifiability:** Sentence-level events may be dense and closely spaced during near-continuous speech. The affect-modulator model must pass design-matrix rank, collinearity, and within-participant variation checks before confirmatory inference. If it does not, revise the estimand rather than force the model.
6. **ROI scope:** mPFC, insula, and amygdala are provisional candidates. Exact atlas labels and spatial coverage must be checked and frozen before inspecting primary effect estimates.
7. **Novelty:** The project is positioned as a dataset-specific secondary analysis, not the first study connecting affective thought and neural activity. Prior work includes valence-related fMRI prediction using personal narratives, latent brain-state analyses of think-aloud thought in a separate sample, and thought-transition analyses using ds006067.
8. **CV placement:** Use the proposed entry only under `Research Projects in Development` or `Ongoing Research Proposals`. Do not put it among completed research experience, completed projects, or publications until the relevant work has been done.

## Items that remain open before preregistration or empirical analysis

- Verify the exact OpenNeuro release and OSF file layout at the time of download.
- Confirm annotation-to-transcript joins using stable IDs or a validated matching procedure; never rely on row order alone.
- Confirm whether the emotional-intensity rating has sufficient within-participant variation and whether the sentence-event design is identifiable.
- Freeze the primary motion exclusion and censoring policy before inspecting primary ROI outcome estimates. The mean-FD > 0.5 mm rule is provisional and motivated by the dataset authors' prior analyses, not a universal threshold.
- Verify the exact Harvard–Oxford atlas version, labels, laterality, voxel coverage, and resampling. The `Frontal Medial Cortex` label is an operational atlas ROI, not the entirety of medial prefrontal cortex.
- Confirm dataset and OSF reuse conditions before redistribution of any derivative or data-derived material. Do not publish raw MRI, audio, full transcripts, or participant-level questionnaire data.
- Conduct an updated search before making a novelty or publication claim. The literature review is focused and preliminary, not systematic.

## Source checks used in this review

- Zhang et al. (2026), *Scientific Data*, dataset descriptor: https://doi.org/10.1038/s41597-026-08414-6
- Su et al. (2025), *Nature Communications*: https://doi.org/10.1038/s41467-025-61807-w
- Zhao et al. (2026), bioRxiv preprint: https://doi.org/10.64898/2026.08.27.747628
- Yu et al. (2025), *iScience*: https://doi.org/10.1016/j.isci.2025.113755
- Kim et al. (2024), *PNAS*: https://doi.org/10.1073/pnas.2401959121
- Fox et al. (2018), *Annals of the New York Academy of Sciences*: https://doi.org/10.1111/nyas.13740
- fMRIPrep confounds documentation: https://fmriprep.org/en/stable/outputs.html
- Nilearn fMRI GLM documentation: https://nilearn.github.io/stable/glm/index.html

No GitHub repository, CV file, or user profile was modified during this review.