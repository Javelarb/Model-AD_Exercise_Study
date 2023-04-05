# Model-AD Exercise Study

This repository includes the R and Python code for the analysis of the microbiomes obtained from mice using shotgun metagenomic sequencing.
The mice were either male or female, sedentary or active, and wild-type vs. 5xFAD (Alzheimer's Disease).
There was a total of 24 mice.

The following files are included:
* mAD_exercise_analysis.py - Python code used to filter and format the initial species-count matrix.
* mAD_exercise_metadata.txt - The biological metadata associated with each sample.
* mAD_exercise_taxonomy_table.txt - The original species-count matrix produced from metaphlan3.
* ModelAD_exercise_diversity_taxonomy.Rmd - R code used for the ecological analysis of the species-count matrix.
* ModelAD_exercise_diversity_taxonomy_no_virus.Rmd - Similar to the previous file, with virus removed.
* QF_read_counts.txt - The number of quality filtered reads produced after removing and trimming low quality read.
