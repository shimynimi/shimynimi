# Reproducibility and Implementation Plan

## Current reproducibility status

This repository documents the research question, data provenance, proposed analysis design, and statistical safeguards. It does not yet contain an executable fMRI analysis pipeline or empirical results. The existing BIDS inventory utility is a preliminary file-inventory aid only; it does not perform preprocessing, imaging QC, event alignment, or statistical analysis.

## Planned implementation structure

After implementation, the project may grow to include:

- notebooks for dataset audit, transcript/rating validation, fMRI QC, first-level GLM, and group-level analysis;
- source modules for data loading, annotation validation, event construction, QC, design-matrix generation, ROI analysis, and group inference;
- tests for transcript joins, event timing, design-matrix rank, and QC rules;
- a configuration file documenting all analysis choices;
- aggregate result tables and figures.

Raw source data must remain outside the public repository.

## Environment and versioning

The initial dependency list is a planning aid and is not yet version-pinned or tested. After the pipeline runs, record exact versions of Python, NumPy, Pandas, SciPy, NiBabel, Nilearn, statsmodels, and other tools, together with operating-system and execution details. Prefer a lock file or exported environment specification.

## Requirements before reporting results

- Fixed OpenNeuro version and recorded OSF revision/download date.
- Participant inclusion/exclusion table and reasons for exclusions.
- Exact imaging derivative and preprocessing provenance.
- Versioned ROI atlas, exact labels, thresholds, and image-space mapping.
- Dated analysis plan and change log.
- Deterministic seeds for any stochastic procedures.
- Tests for annotation joins, timing, design-matrix rank, and QC.
- Software versions and execution settings.
- Aggregate outputs only; no raw participant-level data in Git.
- A clean-environment run from documented instructions.

## Reporting rule

An analysis step may be described as completed in README, CV, or reports only after the code has run successfully, its outputs have been inspected, and the result can be reproduced from documented inputs and environment settings.
