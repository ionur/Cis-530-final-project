Sample evaluation for Extension 2 model.

################# EVALUATION #################
Go to finalSubmission/code/

Evaluation will use the script 'evaluate.py' under the code directory. Please make sure 'classes.py' and 'tags.py'
exist in the same folder.

1) Training evaluation:
  python evaluate.py brat ner ../data/train/gold ../data/train/system
2) Dev evaluation:
  python evaluate.py brat ner ../data/dev/gold ../data/dev/system
  
3)Test evaluation:
  python evaluate.py brat ner ../data/test/gold ../output/test/system
Report (SYSTEM: system):
------------------------------------------------------------
SubTrack 1 [NER]                   Measure        Micro
------------------------------------------------------------
Total (156 docs)                   Precision      0.9573
                                   Recall         0.9133
                                   F1             0.9348
------------------------------------------------------------
