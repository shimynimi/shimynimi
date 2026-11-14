# Methodology

This document specifies the planned analysis. It is not evidence that any step has been executed.

## 1. Overview

The analysis links sentence-level affective annotations to continuous BOLD time series during a naturalistic think-aloud task. The main predictor is the dataset-defined emotional-intensity rating on a signed −4 to +4 scale. The project will estimate within-participant associations between that rating and BOLD responses, while explicitly modeling the speech event itself and relevant nuisance signals.

## 2. Data preparation

### 2.1 Participant-level joins

For each participant, load:

- sentence-level transcript and sentence start/end times;
- sentence-level GPT-generated ratings;
- word-level timestamps (for timing and speech descriptors);
- fMRIPrep-preprocessed BOLD image;
- fMRIPrep confounds time series.

Use explicit participant IDs and validated row keys. If a direct sentence ID is unavailable, match using an exact/normalized text and timing strategy, then manually inspect mismatches. Do not assume that spreadsheet row order is identical across folders.

### 2.2 Rating checks

Preserve the original emotional-intensity score. Confirm its numeric range and inspect missingness, within-person variance, floor/ceiling effects, and participant-level distributions. Center the predictor within participant. Standardize within participant only if the distribution and interpretability justify it. Do not transform the signed score into an arousal or absolute-intensity measure without a separate hypothesis.

### 2.3 Event construction

Each sentence is represented by onset and duration using the dataset's sentence-level timestamps. The primary event duration is `sentence_end - sentence_start`, checked against word-level timestamps. Exclude or flag negative durations, zero-duration events where inappropriate, out-of-run events, and failed joins. Use the same timing reference as the BOLD data: seconds relative to the first functional volume.

## 3. fMRI signal and preprocessing choice

The primary signal will be the fMRIPrep-preprocessed BOLD image in the appropriate standard space, not the dataset's already smoothed/denoised/z-scored image. The fMRIPrep confounds time series will be reviewed and selected nuisance columns documented. This makes the primary GLM's nuisance regression auditable and avoids double-regressing the dataset's prior denoising terms.

The dataset-provided further-denoised derivative may be used as a sensitivity analysis. If used, do not apply the same nuisance regression again. Report that derivative's preprocessing, smoothing, and z-scoring history.

Before modeling, verify:

- TR and number of volumes;
- BOLD spatial dimensions and affine;
- template space and compatibility with ROI masks;
- run timing relative to transcripts;
- confound column definitions and missingness;
- whether the initial volumes require exclusion based on the acquisition metadata and prior-analysis convention.

## 4. First-level event-related GLM

For participant *s*, a simplified model is:

\[
 y_s(t) = \beta_{0s} + \beta_{speech,s}X_{speech,s}(t)
 + \beta_{affect,s}X_{affect,s}(t)
 + \boldsymbol{\gamma}_s^\top\mathbf{C}_s(t) + \epsilon_s(t)
\]

where:

- `y_s(t)` is the BOLD time series in a voxel or ROI;
- `X_speech` is the unmodulated sentence/speech event regressor;
- `X_affect` is the sentence event regressor modulated by the within-participant centered emotional-intensity rating;
- `C_s(t)` contains prespecified nuisance regressors;
- `epsilon` is residual error.

Both sentence-level event regressors will be convolved with the same prespecified HRF (canonical double-gamma / SPM-style HRF, with a temporal derivative as a planned sensitivity if stable). The affect modulator will not be serially orthogonalized against arbitrary regressors. Its coding and scaling will be specified explicitly.

The unmodulated speech regressor controls the average BOLD response associated with sentence-level speech events. The affect modulator tests whether variation in the signed affective-content score explains additional BOLD variation during those events.

### 4.1 Nuisance regressors

The initial nuisance set will be based on available fMRIPrep outputs and the dataset's processing record. Candidate terms include:

- six rigid-body motion parameters and, if stable, their temporal derivatives;
- CSF and white-matter signals where available and justified;
- low-frequency drift terms / high-pass components;
- motion-outlier spike regressors or censoring;
- speech-duration/word-count/speech-rate descriptors where they can be estimated without severe collinearity;
- thought-boundary/topic-change terms only if annotations are joinable and the design remains identifiable.

The final nuisance set will be fixed before outcome analysis. It will not be expanded post hoc to obtain a preferred result.

### 4.2 Temporal alignment and HRF

Sentence timestamps are relative to the first functional volume. In the GLM, use those event times and convolve with the HRF. Do not both manually shift events by a fixed 4.5-second delay and convolve the events with the HRF. A fixed-shift event-average analysis used in some prior dataset validation work is not identical to an event-related GLM.

The underlying thought may begin before it is verbalized. The dataset records speech timing, not the true moment of thought formation. Therefore the project estimates associations around verbalized content and cannot infer the exact neural onset of the thought itself.

## 5. ROI definition

The primary ROI family is provisionally specified from independent affective-neuroscience literature as three bilateral/combined regions: (1) medial frontal cortex as the operational medial-prefrontal ROI, (2) insular cortex, and (3) amygdala. The initial atlas plan is the Harvard–Oxford maximum-probability atlas at the 25% threshold: cortical atlas labels `Frontal Medial Cortex` and `Insular Cortex`, plus left and right `Amygdala` labels from the subcortical atlas. Left/right amygdala masks will be combined into one bilateral ROI; the cortical atlas labels will be used as provided and their laterality/coverage documented.

Before confirmatory analysis, verify that these exact labels exist in the installed atlas release, inspect their anatomical coverage, and resample label maps to the BOLD reference image using nearest-neighbor interpolation. Record atlas name/version, labels, threshold, resampling, voxel counts, and image-space compatibility in `config/analysis-plan.yaml`. If a label is absent or has inadequate coverage, document the reason and revise the ROI family before viewing primary effect estimates. Do not select a hemisphere or subregion after viewing statistical maps. Whole-brain or network-based results will be secondary/exploratory.

## 6. Group-level analysis

For each participant, estimate the affect-modulator beta in each ROI. At the group level, test whether the mean participant-level effect differs from zero using a random-effects one-sample model. Report:

- mean beta and standard error;
- 95% confidence interval;
- standardized effect size where appropriate;
- two-sided p-value;
- FDR-adjusted q-value across the primary ROI family;
- final participant count and exclusion flow.

The participant, not the individual sentence, is the unit of group-level inference. This avoids treating thousands of sentences as independent participants.

## 7. Sensitivity and exploratory analyses

- Alternative motion policy (e.g., stricter threshold and continuous motion adjustment).
- Alternative plausible HRF specification.
- Comparison with the dataset-provided denoised derivative without duplicate nuisance regression.
- Human-rating sensitivity analysis in the 18 available transcripts only.
- Sadness and anxiety ratings, labeled exploratory.
- Optional whole-brain/parcel-level exploratory analysis with appropriate multiplicity correction.

## 8. Implementation tools

- Python, NumPy, Pandas, SciPy
- NiBabel for NIfTI data inspection
- Nilearn for first-level and second-level GLM tools, ROI extraction, and visualization
- statsmodels for supplementary regression/statistical summaries
- Jupyter for exploratory, documented workflows

Exact package versions will be frozen after an environment is installed and tested. No code in this document has yet been validated against the dataset.