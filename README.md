# Joe Kwan Portfolio
Some work from Master of Data Science 

# [Project 1 - AirBnb Data Analysis](AirBnb Data Analysis Project.pdf)

## Overview
To analysis Airbnb data from 2019 to 2020, find out the factors that affect the price and the booking. Also generate a prediction model to suggest what facility and which location can help boost up the price and booking enquiries.

<details>
  <summary>Click for more detail</summary>

## Task
- Use R to do data cleaning and manipulation, clustering, and correlation test to isolate necessary feature
- Use NLP and SVM to build regression model, to identify what feature affects the renting price and build a prediction model.
- Use Tableau and R markdown for reporting.

## Notes
As the only one in the team has 10 years of coding experience, I handle a bit more coding than others than others.
The whole team design what features we need for analysis/prediction, and I help with coding. 
Each of us involved all the K-mean clustering, Regression model, analysis and visualization. 
I only work a bit more on NLP/SVM.

## Preview
<img src="images/cluster.png" alt="k-mean cluster" width="640"/>
<img src="images/map.png" alt="heatmap" width="400"/>
<img src="images/corr.png" alt="correlation matrix" width="400"/>
<img src="images/sentiments.png" alt="nlp sentiment" width="400"/>
<img src="images/cloud.png" alt="word cloud" width="400"/>
<img src="images/svm1.png" alt="svm" width="400"/>
<img src="images/svm2.png" alt="svm" width="400"/>
<img src="images/svm3.png" alt="svm" width="680"/>

</details>



# [Project 2 - Creativity Assessment Automation](Creativity Assessment Automation.pdf)

## Overview
This project is to help our client to evaluate people’s creativity level. Since our client doesn’t have a systematic method to do that, our goal is to develop an AI model that can base on image, and the text response from of that image from test subject to evaluate their creativity level.

<details>
  <summary>Click for more detail</summary>
  
  
## Task
- Use GCP Vision to analysis images.
- Use R, NLP to analysis image and text data and establish data features.
- Use Beayson Network to build DAG for understanding cause and effect and the probabilities of data features.
- Build prediction model using Beayson Network.
- Use Tableau and R markdown for reporting.

## Notes
There are total 2 people with coding experience including me in this team, hence we handle most heavy coding task.
The other coder handles research of neural network and provide some help for other teammates.
I mainly develop API for image analysis and also decide features using Beayson network. 
At the end my selection and decision of using Beauyson network brings a HD to the team. 

## Preview
<img src="images/bar.png" alt="creativity lvel" width="400"/>
<img src="images/feat corr.png" alt="features" width="400"/>
<img src="images/cloud_p2.png" alt="word cloud" width="400"/>
<img src="images/dag.png" alt="dag" width="400"/>
<img src="images/model_comparison.png" alt="model comparasion" width="400"/>

## Code
- [R - Bayesian Network Analysis.Rmd](code/R - Bayesian Network Analysis.Rmd)
- [Python - image_analysis.py](Python - image_analysis.py)
- [Python - calculate_similarity.py](Python - calculate_similarity.py)
  
</details>
