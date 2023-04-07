### Supplementary Material for: 
# "Connected-Components-based Post-processing for Retinal Vessels Deep-Learning Segmentation"

 
## data/
The six normalized datasets.

## pred/
The predicted segmentations.  
For each image of each dataset, three independent trainings and inferences have been performed  
-> in folders: 0/, 1/ and 2/  
Training was performed for 100 epochs with full sized provided images using a batch size of 1 and Adam optimizer with a learning rate of 1e-3


## stats/
Method statistics for known and unknown data

## metricStats.py
To perform the method and evaluate the results for known and unknown data.  
-> Comment/Uncomment the code for desired behaviour.


```
In this study, we propose a Connected-Components-based post-processing procedure to remove artifacts while preserving the most possible amount of disconnected branches.

We performed the procedure over 615 predicted segmentations from six datasets. 
The procedure removed on average 57% of the CC (37/64) and kept 96% of the TP. 

The procedure improved the CC=1 mean dice by a substantial 0.069 leading from 0.782 to 0.851 (also being higher than the original predictions mean dice with no removal).

We demonstrated the procedure efficiency on unknown data by ignoring our data distribution knowledge to set a threshold value. 
It led to good results considering that we were able to keep 56% of the TP and to improve the CC=1 mean dice by a substantial 0.062 leading from 0.782 to 0.844.

The results on unknown data are lower compared to that using known data but we have to keep in mind that we set a very high threshold value i.e. the maximum threshold value amongst the best predictions: 0.0103. 
This threshold has removed 95% of the CC (61/64).

These differences show the strong importance of the knowledge of the data distribution.
To enhance the results on new unknown data, we encourage annotating a small number of images to get a knowledge of the data distribution, thus being able to set a threshold in a more favorable way.
```

