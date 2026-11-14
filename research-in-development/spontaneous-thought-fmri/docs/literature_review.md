# Literature Review and Positioning

**Review date:** 14 November 2026  
**Purpose:** Establish the current context for a secondary analysis of affective content in verbalized spontaneous thought using OpenNeuro ds006067.

## 1. The dataset and its existing research record

### Zhang et al. (2026): dataset descriptor

Zhang and colleagues describe an extended think-aloud fMRI dataset with 118 healthy adults. Participants verbalized spontaneous thoughts continuously during 10-minute scanning sessions. The extended release adds preprocessed MRI derivatives, word-level timestamps aligned to fMRI acquisition, sentence-level GPT-5 Nano ratings across 14 affective and sensory dimensions, and post-scan self-report measures. The dataset is available across OpenNeuro (MRI) and OSF (behavioral annotations and code).

**Relevance:** This is the direct data source for the proposed work. The current proposal uses its sentence-level affective annotations and time-aligned MRI derivatives.

**Important details:** Emotional intensity is scored from −4 to +4, with negative and positive anchors and neutral values around zero. The other emotion and sensory ratings use 1–4 scales. Four human raters evaluated 18 transcripts; GPT-human agreement was comparable to human-human agreement for most dimensions, with weaker agreement for joy, fear, and anxiety. The rating system is an annotation of sentence content, not a direct self-report of the participant's internal state. The dataset descriptor also reports fMRI validation analyses for sensory annotations (notably vision and audition); this is distinct from the proposed primary analysis of the signed emotional-intensity annotation.

### Su et al. (2025): thought transitions and semantic structure

Su and colleagues used the same ds006067 think-aloud dataset to study transitions between spontaneous thoughts, thought categories, topic changes, and neural responses in default-mode and control networks. The work also examined functional connectivity and the semantic structure of thought trajectories.

**Relevance:** The proposed project must not simply repeat thought-boundary, topic-transition, or broad default/control-network analyses. It should use the newer sentence-level affective annotations as the central predictor and explicitly account for thought transitions or topic changes when the annotations permit.

### Zhao et al. (2026): internal/external thought transitions

A September 2026 bioRxiv preprint reanalyzes ds006067 to study neural signatures preceding transitions between internally and externally oriented thoughts. It reports transition-related activity in the salience/ventral-attention system, including the right temporoparietal junction.

**Relevance:** This reinforces the need to avoid a transition-classification project and to model transition-related activity as a potential nuisance/sensitivity factor where the labels can be joined reliably. The work is a preprint, not a peer-reviewed journal article as of the review date.

## 2. Related work beyond ds006067

### Yu et al. (2025): latent brain states and moment-to-moment thought content

Yu and colleagues used a think-aloud fMRI paradigm with two 7-minute think-aloud runs and one resting-state run to relate latent brain states to the internal–external orientation and novelty of verbalized thoughts. The study used a distinct sample and experimental dataset from OpenNeuro ds006067. It found that default-mode and attention/control-related states tracked different aspects and temporal phases of verbalized thought.

**Relevance:** This is important adjacent work showing that neural-state dynamics can be related to moment-to-moment thought content in a think-aloud paradigm. It does not use the ds006067 sentence-level GPT-5 emotional-intensity annotations, and its main content variables are internal–external orientation and novelty. It should therefore be treated as related methodological and conceptual work, not as a direct analysis of the same dataset.

### Kim et al. (2024): decoding self-relevance and valence

Kim and colleagues developed fMRI-based predictive models of self-relevance and valence using personal narratives. They reported that brain patterns could predict dimensions of thought-related content across story-reading and resting-state data. This is a distinct dataset and paradigm from ds006067, but it is directly relevant conceptually because it links affective/self-related content to brain activity.

**Implication:** The proposed project cannot claim that relating valence to brain activity is a new idea. Its contribution, if supported, would be a transparent secondary analysis using continuous naturalistic think-aloud speech, sentence-level LLM annotations, explicit speech/motion modeling, and an independently defined ROI/group-level inferential plan.

### Fox et al. (2018): affective neuroscience of self-generated thought

Fox and colleagues review affective dimensions of self-generated thought and summarize evidence implicating regions including orbitofrontal cortex, amygdala, insula, and medial prefrontal cortex. They also emphasize variability in affective experience and the relevance of self-generated thought to mental health.

**Implication:** This review provides broad theoretical motivation for an independently defined affect-relevant ROI family. It does not justify selecting regions based on the results of the proposed dataset analysis.

## 3. Provisional research gap and contribution

The strongest defensible positioning is **not** that affective thought and neural activity have never been studied. Prior work has examined valence-related brain patterns in personal narratives, and the ds006067 dataset has already been used to study thought transitions, semantic content, and internal/external orientation.

The narrower candidate contribution is a transparent secondary analysis of the sentence-level affective annotations in ds006067, testing within-person associations between the dataset-defined signed emotional-intensity rating and regional BOLD activity while explicitly modeling speech events, head motion, and event timing. This is a dataset-specific extension, not a claim that affective content and neural activity have not previously been linked. Whether it adds a publishable scientific contribution depends on the final literature review, feasibility, model identifiability, analysis quality, and findings.

## 4. Questions to resolve before confirmatory analysis

1. Has another paper or preprint published after 29 September 2026 analyzed the emotional-intensity dimension against BOLD responses in ds006067?
2. Which affect-relevant ROI definitions best match the hypotheses and available spatial derivatives?
3. How much variance in the emotional-intensity regressor is shared with sentence duration, word count, thought category, topic changes, and speech rate?
4. Is the primary effect identifiable with a single 10-minute run per participant and the available number of usable events?
5. What is the appropriate treatment of the human-rating subset, given that the 18 transcripts were sampled from those with fewer sentences than the median?

These questions are design gates, not evidence that the project is infeasible.

## 5. References

1. Zhang, M., Liu, P. R., Su, H., Zhao, M., Li, X., Born, S., Lee, Y., Honey, C. J., Chen, J., & Lee, H. (2026). An fMRI dataset of verbalized spontaneous thought with annotated transcripts and self-report trait measures. *Scientific Data*. https://doi.org/10.1038/s41597-026-08414-6
2. Su, H., Li, X., Born, S., Honey, C. J., Chen, J., & Lee, H. (2025). Neural dynamics of spontaneous memory recall and future thinking in the continuous flow of thoughts. *Nature Communications, 16*, 6433. https://doi.org/10.1038/s41467-025-61807-w
3. Zhao, M., Zhang, M., Su, H., Liu, P. R., & Lee, H. (2026). Neural signatures of spontaneous transitions between internal and external thought. *bioRxiv* preprint. https://doi.org/10.64898/2026.08.27.747628
4. Yeo, Y. et al. (2025). Mapping content and dynamics in the stream of consciousness through latent brain state analysis. *iScience, 28*(11), 113755. https://doi.org/10.1016/j.isci.2025.113755
5. Kim, H. J., Lux, B. K., Lee, E., Finn, E. S., & Woo, C.-W. (2024). Brain decoding of spontaneous thought: Predictive modeling of self-relevance and valence using personal narratives. *Proceedings of the National Academy of Sciences, 121*(14), e2401959121. https://doi.org/10.1073/pnas.2401959121
6. Fox, K. C. R., Andrews-Hanna, J. R., Mills, C., Dixon, M. L., Markovic, J., Thompson, E., & Christoff, K. (2018). Affective neuroscience of self-generated thought. *Annals of the New York Academy of Sciences, 1426*(1), 25–51. https://doi.org/10.1111/nyas.13740
7. Poldrack, R. A., Mumford, J. A., & Nichols, T. E. (2011). *Handbook of Functional MRI Data Analysis*. Cambridge University Press.
8. Esteban, O. et al. (2019). fMRIPrep: a robust preprocessing pipeline for functional MRI. *Nature Methods, 16*, 111–116. https://doi.org/10.1038/s41592-018-0235-4
9. Nilearn documentation: Statistical analysis of fMRI data. https://nilearn.github.io/stable/glm/index.html

## 6. Review limitation

This is a focused, initial literature review, not a systematic review. Database-specific searches, citation chaining, and a final update before any preregistration, conference submission, or manuscript submission will be required before making a novelty claim. The proposed work is not preregistered at this stage.