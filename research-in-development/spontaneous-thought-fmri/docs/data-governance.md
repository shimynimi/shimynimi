# Data Governance and Research Ethics

## Data sources

- MRI data: [OpenNeuro ds006067, version 2.0.0](https://openneuro.org/datasets/ds006067/versions/2.0.0)
- Transcripts, timestamps, ratings, and questionnaires: [OSF Think Aloud Behavioral Data](https://osf.io/a56rm)

## Data handling principles

1. Do not commit raw MRI images, transcripts, audio, questionnaire responses, or participant-level annotation files to this public repository.
2. Download data directly from the original repositories and comply with their license, terms, and any data-use restrictions.
3. Keep all local raw data in a folder excluded by `.gitignore`.
4. Do not publish transcript excerpts or examples that could reveal sensitive personal information.
5. Publish only code, documentation, aggregate summaries, and figures that are appropriate to share and do not expose participant-level sensitive information.
6. Preserve source attribution and dataset version information in every report.

## Interpretation boundaries

- The dataset participants are healthy adults; the project is not a patient study and does not assess MDD diagnosis.
- LLM-generated ratings reflect perceived psychological content in verbalized sentences; they are not direct measurements of participants' subjective experiences.
- Statistical associations in observational fMRI data do not establish causal relationships.
- Results should not be used for clinical decisions or individual mental-health assessment.

## Reporting checklist

- [ ] Dataset version and download date recorded.
- [ ] Inclusion/exclusion rules documented before confirmatory analysis.
- [ ] Subject counts reported for every analysis stage.
- [ ] Motion and other quality-control decisions described.
- [ ] Rating scales and annotation source documented.
- [ ] Human validation subset described where used.
- [ ] Multiple-comparison correction specified.
- [ ] All analysis deviations documented.
- [ ] Raw participant-level data excluded from the repository.