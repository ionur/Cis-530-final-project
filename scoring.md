
__Evaluation Metrics:__

1. Entity recognition on the data:
For this task evaluation will be entity-based. This task will require to compare the system output
with the beginning and end locations of each PHI entity tag, as well as detecting correctly the
annotation type.

2. Detect sensitive spans:
For this task evaluation will be span-based, by just evaluating whether spans belonging to
sensitive phrases are detected correctly. This boils down to a classification of spans, where
systems try to obfuscate spans that contain sensitive PHI expressions.

For both sub-tasks, the metric used will be micro-averaged precision, recall, and balanced F-score:
1. Precision (P) = true positives/(true positives + false positives)
2. Recall (R) = true positives/(true positives + false negatives)
3. F-score (F1) = 2*((P*R)/(P+R))

Higher F-scores are better for the above tasks.

Task 2 is a subsequent task after NER (Task 1). Task 2 can be taken up only after successful completion of Task 1.

For more detailed information on evaluation, please refer to the following link:
https://github.com/PlanTL-SANIDAD/MEDDOCAN-Evaluation-Script


