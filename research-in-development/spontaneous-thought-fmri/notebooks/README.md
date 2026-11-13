# Planned notebooks

The notebooks below are planned deliverables. They have not yet been run and will be added after the dataset audit confirms the file structure.

1. `01_dataset_audit.ipynb` — inspect BIDS metadata, subject coverage, MRI derivatives, transcript/rating files, and missingness.
2. `02_annotation_audit.ipynb` — verify rating definitions/scales, distributions, coverage, inter-dimension correlations, and human-rating validation data.
3. `03_temporal_alignment.ipynb` — verify sentence timestamps against word timestamps and fMRI acquisition time; construct event tables.
4. `04_first_level_glm.ipynb` — create and inspect participant-level design matrices and fit first-level GLMs.
5. `05_group_roi_analysis.ipynb` — aggregate participant estimates and conduct prespecified ROI/group-level analyses.
6. `06_robustness_checks.ipynb` — examine motion thresholds, missingness, timing, alternative nuisance terms, and multiple-comparison sensitivity.