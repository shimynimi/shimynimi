# Preliminary Analysis Plan

**Status:** Draft; to be finalized after the dataset audit and literature review. No analyses have been run.

## Phase 0 — Verify source versions and files

1. Record the OpenNeuro accession and exact version downloaded.
2. Record the OSF project version/date and file inventory.
3. Confirm the subject-ID mapping between MRI, transcript, ratings, and questionnaires.
4. Record the dataset's license/data-use conditions and any restrictions on redistribution.

## Phase 1 — BIDS and imaging audit

- Confirm `dataset_description.json`, `participants.tsv`, subject directories, functional/anatomical images, JSON sidecars, field maps, and derivatives.
- Extract TR, number of volumes, acquisition labels, and preprocessing provenance from metadata.
- Review fMRIPrep confounds and quality-control outputs.
- Summarize mean framewise displacement and other relevant motion metrics per run.
- Establish a transparent imaging inclusion/exclusion table. Do not assume that the full behavioral sample is also the usable fMRI sample.

## Phase 2 — Transcript and rating audit

- Inventory sentence-level transcript files, word-level timestamp files, LLM rating files, and human validation files.
- Check required columns, subject identifiers, row counts, duplicate sentences, missing values, and timing bounds.
- Verify the exact rating scales using the dataset descriptor and OSF documentation.
- Summarize per-subject and overall annotation coverage.
- Quantify correlations between dimensions to identify collinearity and avoid fitting all dimensions indiscriminately.

## Phase 3 — Define the primary predictor and event model

The dataset descriptor reports 14 sentence-level psychological dimensions. The provisional primary predictor is the dataset's signed emotional-intensity rating. Its scale is reported as -4 (very negative) to +4 (very positive); it should not be silently relabeled or transformed into an absolute intensity score. The exact primary variable will be verified in the source files before selection.

Initial event table fields (subject to confirmation):

- `onset`: sentence start time relative to acquisition of the first functional volume;
- `duration`: sentence end time minus sentence start time;
- `trial_type`: speech/thought event label;
- `emotional_intensity`: dataset-provided sentence-level score;
- secondary affective/sensory ratings where coverage supports analysis;
- available thought-category or thought-transition labels.

The precise event construction must respect the dataset's timestamp definitions and avoid using any event outside the valid scan interval.

## Phase 4 — First-level fMRI model

Provisional components:

1. Baseline task/speech interval and relevant thought-structure regressors.
2. Primary affective annotation regressor, centered/scaled according to a pre-specified rule.
3. Motion nuisance regressors and documented censoring decisions.
4. Drift/high-pass terms and additional nuisance terms supported by the acquisition and preprocessing.
5. An HRF model appropriate to the event durations and timing precision.

Model the primary annotation as a parametric/event-level predictor. Compare a baseline model with an expanded model containing the primary affective predictor as a secondary model comparison, if the design and sample size support it. Inspect design-matrix correlations and condition numbers before model fitting.

## Phase 5 — ROI and group-level analysis

- Define ROIs/networks from independent literature and a documented atlas before confirmatory model fitting.
- Extract participant-level estimates/contrasts.
- Perform group-level inference using the participant as the unit of analysis.
- Report effect sizes, uncertainty intervals, sample sizes, and correction method.
- Treat whole-brain inference as secondary and apply suitable correction.

## Phase 6 — Secondary dimensions and robustness

- Explore joy, sadness, fear, anger, disgust, surprise, anxiety, and sensory dimensions only after the primary model is fixed.
- Correct for multiplicity across the planned family of secondary tests.
- Compare LLM-derived annotations with human ratings in the available validation subset.
- Test sensitivity to motion thresholds, event timing, missing data, thought category/transition controls, and alternative nuisance specifications.

## Decision gates

The project should not advance to confirmatory modeling until:

- the exact dataset version and data structure are recorded;
- transcript-to-MRI ID linkage and timing are verified;
- annotation columns and scales are confirmed;
- imaging QC/inclusion criteria are documented;
- the prior-work review supports a clearly differentiated question;
- ROIs, primary predictor, nuisance terms, and correction family are specified.