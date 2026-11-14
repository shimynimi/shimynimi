# Dataset Description and Quality-Control Plan

## 1. Data sources

### Neuroimaging

- Repository: OpenNeuro
- Accession: [ds006067, version 2.0.0](https://openneuro.org/datasets/ds006067/versions/2.0.0)
- Organization: BIDS
- Public MRI/transcript sample: 118 healthy adults
- Task: continuous think-aloud verbalization during a 10-minute fMRI session
- Scanner: 3T Philips Ingenia Elition, 32-channel head coil
- Functional acquisition: multiband T2*-weighted EPI; TR = 1.5 s; TE = 30 ms; 2 × 2 × 2 mm voxels

### Behavioral annotations

- Repository: [OSF — Think Aloud Behavioral Data](https://osf.io/a56rm)
- Word-level timestamps: word, onset, and offset
- Sentence-level timestamps: sentence text, onset, and offset
- Sentence-level GPT-5 Nano ratings: 14 psychological dimensions
- Human validation: four independent raters evaluated 18 transcripts; these were selected from transcripts below the median sentence count and are not a representative re-rating of the full sample
- Post-scan questionnaires: 69 of 126 recruited participants completed surveys

Transcript timestamps are reported in seconds relative to acquisition of the first functional volume. The OSF project also contains code used by the dataset authors; the project will inspect and cite that material rather than silently reproducing it.

## 2. Variables

| Variable | Source / level | Scale | Planned role |
|---|---|---|---|
| Emotional intensity | GPT-5 Nano sentence rating | −4 very negative to +4 very positive | Primary predictor; signed, valence-like content annotation |
| Sadness | GPT-5 Nano sentence rating | 1–4 | Exploratory predictor |
| Anxiety | GPT-5 Nano sentence rating | 1–4 | Exploratory predictor; agreement with human ratings was weaker |
| Sentence onset/offset | Sentence transcript | Seconds from first functional volume | Event timing |
| Word onset/offset | Word timestamp file | Seconds from first functional volume | Speech-density and alignment checks |
| Motion confounds | MRI derivatives | Time series | Nuisance modeling / censoring |
| BOLD image | MRI derivatives | 4D NIfTI | Neural outcome |
| Human ratings | 18 transcripts, 4 raters | Dimension-specific scales | Limited sensitivity analysis |

The 14 dimensions consist of eight affective ratings (emotional intensity, joy, sadness, fear, anger, disgust, surprise, anxiety) and six sensory ratings (vision, audition, olfaction, gustation, somatosensation, interoception). Emotional intensity uses a signed −4 to +4 scale; the other dimensions use 1–4 scales.

## 3. Sample and quality context

The dataset descriptor reports 126 recruited participants and 118 retained for the public MRI/transcript dataset. Mean framewise displacement (FD) across the 118 was 0.43 mm (SD 0.18; range 0.17–1.20 mm), with a negative association between mean FD and median tSNR. The final usable sample for this project is unknown until its own inclusion and QC rules are applied.

The descriptor's speech-versus-silence validation used 73 participants after additional exclusions, including excessive motion and data-quality problems. That sample is specific to that validation analysis and is not an expected or guaranteed sample size for this project.

## 4. Imaging derivatives

The dataset provides fMRIPrep-preprocessed functional images and a further smoothed/denoised/z-scored derivative. The descriptor reports fMRIPrep 23.2.1 and FreeSurfer 7.3.2; slice-timing correction was not applied. The secondary derivative regressed six motion parameters, CSF and white-matter signals, and second-order polynomial trends, then smoothed and temporally z-scored the residual series.

**Primary plan:** begin with fMRIPrep-preprocessed BOLD data and explicitly document the nuisance regressors used in the first-level model.

**Sensitivity plan:** compare with the dataset-provided denoised derivative only if its provenance is confirmed; do not regress the same nuisance terms a second time.

## 5. Provisional inclusion and exclusion rules

1. A readable BOLD image and matching confounds file are available.
2. Sentence timestamps and primary affective ratings can be joined using validated identifiers or a verified join procedure.
3. Required event timing is valid and falls within the usable fMRI run.
4. Mean FD > 0.5 mm is a provisional exclusion threshold motivated by the dataset authors' analyses; implementation must be verified and frozen before inspecting primary ROI effects.
5. FD ≥ 1 mm volumes and the two preceding and following TRs are provisionally considered for censoring, following the dataset descriptor's validation approach. This policy must be checked against the derivative and pre-specified before outcome inspection.
6. Anatomical anomalies, acquisition problems, and missingness will be documented rather than silently excluded.

These are provisional rules, not a fixed sample-size promise. Sensitivity analyses will assess the impact of plausible alternative motion policies.

## 6. Audit checklist

- [ ] Confirm OpenNeuro version 2.0.0 and record download metadata.
- [ ] Record OSF revision/date and file inventory.
- [ ] Verify participant-ID mapping across MRI, transcript, ratings, and confounds.
- [ ] Validate sentence/rating joins; count unmatched and duplicate rows.
- [ ] Inspect within-participant emotional-intensity distributions and variability.
- [ ] Quantify missing or invalid timestamps.
- [ ] Verify TR, volume count, affine, template space, and derivative provenance.
- [ ] Summarize mean FD, high-motion volumes, tSNR where available, and missing volumes.
- [ ] Check event timing against acquisition time.
- [ ] Produce a participant flow table and final usable sample count.

## 7. Data governance

Do not copy raw MRI images, audio, full transcripts, questionnaire item-level data, or potentially identifying information into this public repository. Store working data outside the repository in access-controlled storage. Publish only code, documentation, and aggregate outputs that are appropriate to share under the source repositories' terms and applicable ethics/privacy requirements.
