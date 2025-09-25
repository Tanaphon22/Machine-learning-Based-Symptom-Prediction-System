# Machine-learning-Based-Symptom-Prediction-System

## Dataset Overview
- **1000 rows and 4 columns :** Each row represents a user, and columns include personal and symptoms data
- **Gender :** Gender of user
- **Age :** User's age
- **Summary :** User's symptom information (JSON)
- **Search_term :** Result from symptoms entered

## Solution

1. **Data Understanding**
   **
   <img width="1525" height="212" alt="image" src="https://github.com/user-attachments/assets/c5ce1c89-d227-4aee-abb5-c359bc060573" />
   -in gender factor, we can use onehotencoder with it for ML and age just leave it. the main problem is Summary and Search_term colums. in Summary i can see symptom data locate after 'yes_symptoms' and text. so i use code for tranfrom from json to python dict and i got list of symptoms
   <img width="316" height="319" alt="image" src="https://github.com/user-attachments/assets/72016e9e-c3d3-4482-9d07-0f8cb503c9c0" />
   -as you can see we got some word is not cotain


## Deployment Steps

1. **Upload Data to S3**
   - Create an S3 bucket and upload your data files.

2. **Set Up AWS Glue Crawler**
   - Configure AWS Glue to crawl the S3 data and create a catalog.

3. **Query Data Using Athena**
   - Use Amazon Athena to analyze the data stored in S3.

4. **Transform Data with AWS Glue**
   - Set up ETL jobs to clean and transform data.

5. **Load Data into Redshift**
   - Create a Redshift cluster and load data from S3.

6. **Connect BI Tools**
   - Integrate Redshift with Power BI for visualization.

## Prerequisites

- AWS Account with necessary permissions
- S3 bucket and IAM roles
- AWS Glue, Athena, and Redshift setup

## Tools Used
- **AWS Services:**
  - Amazon S3
  - AWS Glue
  - Amazon Athena
  - Amazon Redshift
- **BI Tools:**
  - Power BI

## Dashboard
![image](https://github.com/user-attachments/assets/d63c2773-ae42-4746-baf0-ca27eb5456a1)
