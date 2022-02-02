# Joe Kwan Portfolio
Some work from Master of Data Science and my leisure time.

# [Project 1 - AirBnb Data Analysis](AirBnb Data Analysis Project.pdf)

## Overview
To analyze Airbnb data from 2019 to 2020, investigate which factors affect the price and the booking schedule. Also, generating a prediction model to suggest what facility and which location can help boost up the price and booking inquiries.


<details>
  
  **<summary>Click for more detail</summary>**

## Task
- Use R to do data cleaning and manipulation, clustering, and correlation test to isolate necessary feature.
- Use NLP and SVM to build a regression model, identify what feature affects the renting price, and build a prediction model.
- Use Tableau and R markdown for reporting.

## Notes
As the only one in the team who has 10 years of coding experience, I handle a bit more coding than others.
The whole team design what features we need for analysis/prediction, and I help with coding. 
Each of us involved all the K-mean clustering, Regression model, analysis, and visualization. 
I work a bit more on NLP/SVM.

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

<br /><br />
## Data Engineering
Using the same Airbnb dataset, applied a basic data pipeline using AWS glue/athena/quicksight. <br />
Generated a simple visual similar as PowerBI dashboard below.<br />
This is to demonstrate my skills of working on cloud data ETL tools.<br />
Didn't choose Redis/Snowflake because this data is in a relatively simple structure and small volume. 


Pipeline flow:<br />
S3(CSV) > Glue Crawler(Data/Column transformation) > S3(parquet) > Glue Job <> Glue DataBrew(Data Preparation and Scheme update) > Athena > Quicksight

<br /><br />
<a href="https://ap-southeast-1.quicksight.aws.amazon.com/sn/accounts/031268667119/dashboards/327300b3-61bb-48eb-b2b8-83ceb2dc4e79" target="_blank"> > Airbnb QuickSight Dashboard</a>
<br /><br />
***Below are the temporary Quicksight account setup for viewing the dashboard.
<br /><br />
Quicksight Accout: airbnb-quicksight-demo
<br />
Email: byzjoe@gmail.com
<br />
Password: QQwe@123

<br /><br />
<a href="images/Glue1.png" target="_blank"><img src="images/Glue1.png" alt="AWS" width="480"/></a>
<a href="images/Glue2.png" target="_blank"><img src="images/Glue2.png" alt="AWS" width="480"/></a>
<a href="images/Glue3.png" target="_blank"><img src="images/Glue3.png" alt="AWS" width="480"/></a>
<a href="images/Glue4.png" target="_blank"><img src="images/Glue4.png" alt="AWS" width="480"/></a>
<a href="images/Glue5.png" target="_blank"><img src="images/Glue5.png" alt="AWS" width="480"/></a>
<a href="images/Glue6.png" target="_blank"><img src="images/Glue6.png" alt="AWS" width="480"/></a>

<br />
<br /><br />


## Power BI Visual
A simple visual only to demonstrate my PowerBI skills, not as fancy as in the report.
Quick EDA of the AirBnb data.

<a href="https://drive.google.com/file/d/1o4JyFWo128lpGd-4jVszbJQN6Owd8KI3/view?usp=sharing" target="_blank"> > PowerBI: AirBnb EDA</a>

<br />
<img src="images/powerBI1.png" alt="PowerBI" width="640"/>
<img src="images/powerBI2.png" alt="PowerBI" width="640"/>
<img src="images/powerBI3.png" alt="PowerBI" width="640"/>
<img src="images/powerBI4.png" alt="PowerBI" width="640"/>
<br />
<br /><br />














# [Project 2 - Creativity Assessment Automation](Creativity Assessment Automation.pdf)

## Overview
This project is to help our client to evaluate people’s creativity levels. Since our client doesn’t have a systematic method to do that, our goal is to develop an AI model that can base on an image, and the text response of that image from test subjects to evaluate their creativity level.

<details>
  <summary>Click for more detail</summary>
  
  
## Task
- Use GCP Vision to analyze images and identify necessary information.
- Use R, NLP to analyze images and text data for establishing data features to train prediction models.
- Use Bayesian Network to build DAG for understanding cause and effect and the probabilities of data features.
- Build prediction model using Bayesian Network.
- Use Tableau and R markdown for reporting.

## Notes
There are only 2 people with coding experience including me in this team, hence we handle most of the heavy coding tasks.
The other coder handles research of neural networks and provides some help for other teammates.
I mainly develop API for image analysis and also decide features using Bayesian network. 
In the end, I come up with various valuable features using Bayesian network and create a useful prediction model which brings a HD to the team. 

## Preview
<img src="images/bar.png" alt="creativity lvel" width="400"/>
<img src="images/feat corr.png" alt="features" width="400"/>
<img src="images/cloud_p2.png" alt="word cloud" width="400"/>
<img src="images/dag.png" alt="dag" width="400"/>
<img src="images/model_comparison.png" alt="model comparasion" width="600"/>

## Code
- [R - Bayesian Network Analysis.Rmd](code/R - Bayesian Network Analysis.Rmd)
- [Python - image_analysis.py](code/Python - image_analysis.py)
- [Python - calculate_similarity.py](code/Python - calculate_similarity.py)
  
</details>
