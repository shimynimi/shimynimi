# Data directory

The raw MRI, transcript, timestamp, rating, and questionnaire data are **not stored in this Git repository**.

Download the relevant files directly from:

- [OpenNeuro ds006067, version 2.0.0](https://openneuro.org/datasets/ds006067/versions/2.0.0) — BIDS-organized MRI data and derivatives.
- [OSF Think Aloud Behavioral Data](https://osf.io/a56rm) — transcripts, timestamps, sentence-level ratings, questionnaires, and associated documentation/code.

Keep local copies under `data/raw/` and do not commit them. The project-level `.gitignore` excludes `data/raw/`, `data/processed/`, and common neuroimaging files. Follow the source repositories' licenses and data-use requirements.