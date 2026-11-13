# Research Proposal

## Title

**Affective and Sensory Dimensions of Spontaneous Thought: An NLP-Informed fMRI Study**

**Status:** Proposal in preparation; data analysis has not started.

## 1. Background and motivation

Spontaneous thought is a continuous component of human cognition. Naturalistic think-aloud paradigms provide time-stamped verbal reports during fMRI acquisition, creating an opportunity to relate the content of ongoing thought to neural activity. The extended Think Aloud dataset makes this opportunity more accessible by adding preprocessed MRI derivatives, word-level timestamps, sentence-level LLM-generated ratings across psychological dimensions, and self-report measures.

The researcher's prior work has focused on NLP, computational modeling of thought patterns, and language-based approaches to mental health. This proposed secondary analysis would extend that computational background to direct analysis of functional neuroimaging data.

## 2. Research question

**Do sentence-level affective characteristics of spontaneously verbalized thoughts explain within-participant variation in BOLD activity beyond effects associated with speech production, head motion, and thought transitions?**

A secondary question is whether sensory-content annotations explain additional variance after accounting for affective annotations and speech-related factors.

## 3. Aims

1. Audit the availability, structure, timing, and quality of the MRI, transcript, rating, and questionnaire data.
2. Characterize the distribution, coverage, and inter-dimension relationships of the sentence-level affective and sensory ratings.
3. Estimate the association between selected affective-content regressors and BOLD activity using participant-level fMRI models.
4. Evaluate the robustness of associations to motion, speech-related nuisance effects, timing choices, missingness, and annotation uncertainty.

## 4. Dataset

The proposed sources are OpenNeuro `ds006067` (version 2.0.0) for MRI data and the associated OSF project, “Think Aloud Behavioral Data,” for transcripts, timestamps, sentence-level ratings, and questionnaire data.

The 2026 data descriptor reports 118 participants who verbalized spontaneous thoughts during 10-minute fMRI sessions. It describes word-level timestamps and sentence-level annotations over 14 psychological dimensions. The behavioral/annotation data and imaging data are stored in separate repositories and linked using subject identifiers. The exact number of usable participants for imaging analyses will be determined only after checking the current release, missingness, and quality-control metadata.

### Annotation dimensions reported by the dataset descriptor

- **Affective:** emotional intensity, joy, sadness, fear, anger, disgust, surprise, and anxiety.
- **Sensory:** vision, audition, olfaction, gustation, somatosensation, and interoception.

The descriptor reports emotional-intensity ratings on a signed scale from -4 (very negative) to +4 (very positive), with neutral content near zero. The other affective and sensory dimensions are rated from 1 to 4. These definitions and coding details must be checked against the actual annotation files and documentation before analysis.

The LLM-generated ratings were produced at sentence level. Human ratings are available for a validation subset of 18 transcripts, with four independent human raters. This subset can support sensitivity analyses of annotation agreement, but it is not a substitute for a direct measure of participants' internal emotional states.

## 5. Preliminary hypotheses

The hypotheses below are provisional and will be finalized only after the literature review and data audit.

- **H1 (primary, provisional):** Sentence-level affective-content ratings will show a systematic association with BOLD activity in a literature-defined set of affective/cognitive ROIs after accounting for speech-related activity, motion, and thought structure.
- **H2 (secondary, exploratory):** Sensory-content ratings will explain additional BOLD variation in sensory-related regions beyond the affective-content model.
- **H3 (robustness):** The direction and magnitude of primary associations will be evaluated for sensitivity to annotation coverage, motion thresholds, alternative timing specifications, and model covariates.

No specific effect direction or positive result is assumed at this proposal stage. ROI selection and the primary annotation dimension must be justified by an independent literature review before confirmatory tests.

## 6. Proposed methods

### 6.1 Data audit and quality control

- Verify dataset version, BIDS metadata, MRI acquisition parameters, TR, number of volumes, and available derivatives.
- Inspect fMRIPrep quality-control outputs, motion parameters, missing scans, and participant-level coverage.
- Inspect sentence- and word-level transcript files, rating files, subject-ID linkage, missing annotations, and timing conventions.
- Document inclusion/exclusion criteria before inspecting outcome maps.

### 6.2 Linguistic and annotation features

- Use the dataset-provided sentence-level ratings as the primary source of psychological annotations.
- Verify rating scales and operational definitions from the descriptor, OSF documentation, and file contents.
- Examine missingness, floor/ceiling effects, distributions, inter-dimension correlations, and annotation coverage.
- Use human ratings for the subset with available independent assessments to characterize agreement and conduct sensitivity analyses.
- Treat LLM ratings as annotations of transcript content, not as ground-truth labels of subjective affect.

### 6.3 Temporal alignment

- Use sentence onset and end times as the initial event intervals if the supplied files confirm these fields and their relationship to the fMRI acquisition clock.
- Cross-check sentence timing against word-level timestamps and scan start time.
- Read TR from the BIDS JSON metadata rather than hard-coding it.
- Convolve event regressors with an appropriate HRF as part of the first-level GLM.
- Document how pauses, overlapping/uncertain speech, and sentences outside the scan interval are handled.

### 6.4 fMRI modeling

The preliminary plan is a participant-level event-related GLM using preprocessed BOLD time series. The model will include:

- a speech/prompt interval term or other speech-related regressors where supported by the data;
- sentence-level affective-content regressors, with an explicit choice of scale and centering;
- relevant thought-category or thought-transition regressors if reliable annotations are available;
- motion-related nuisance regressors and censoring/quality-control decisions;
- drift/high-pass terms and other standard nuisance terms justified by the acquisition and preprocessing.

The main contrast will estimate the participant-level association between the selected affective annotation and BOLD activity. A small number of a priori ROIs or networks will be selected from an independent literature review and a documented atlas. Whole-brain maps, if conducted, will be secondary and appropriately corrected for multiple comparisons.

### 6.5 Group-level inference

Participant-level estimates will be brought to a group-level model. The analysis will report effect sizes, confidence intervals, sample size after exclusions, and uncertainty. Covariates and weighting will be selected based on the data structure and a pre-specified rationale. The analysis will not treat individual sentences as independent participants.

### 6.6 Robustness checks

- Alternative reasonable motion thresholds and censoring specifications.
- Models with and without thought category/transition controls.
- Alternative event timing choices where supported by annotations.
- Sensitivity to missing transcript/rating segments.
- Comparisons between LLM-derived scores and human-rated scores in the validation subset.
- Multiple-comparison correction across the planned ROI and secondary-dimension families.

## 7. Expected outputs (planned, not yet produced)

- Dataset audit and data dictionary.
- Reproducible preprocessing/analysis notebooks and scripts.
- Participant-level and group-level statistical summaries.
- Clearly labeled figures and quality-control reports.
- A research report; a poster or manuscript draft only if the completed analyses support it.

## 8. Limitations

- The dataset consists of healthy adults; it cannot directly answer questions about MDD patients or validate diagnostic biomarkers.
- Speaking in the scanner can introduce head motion and speech-related artifacts.
- LLM-generated ratings reflect transcript content and may contain annotation error or model bias.
- Sentence-level annotations and fMRI BOLD responses have different temporal scales; temporal alignment and HRF assumptions require justification.
- Observational associations do not establish causal effects.
- Prior studies have already investigated thought transitions and neural dynamics in this dataset; the proposed affective/sensory analysis requires a careful literature review before any novelty claim.

## 9. Research integrity

This repository is a proposal and reproducibility scaffold. No dataset has been analyzed for this project, no GLM has been fitted, and no results are claimed. The proposal may be refined after feasibility checks. Any exclusions, deviations, null findings, and limitations will be documented.