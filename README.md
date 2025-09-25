# Machine-learning-Based-Symptom-Prediction-System

## Dataset Overview
- **1000 rows and 4 columns :** Each row represents a user, and columns include personal and symptoms data
- **Gender**
- **age**
- **summary**
- **search_term**


## Architecture and Data modeling
![image](https://github.com/user-attachments/assets/caf012ff-75c9-43e2-bce0-a1110d3fbbcc)

![image](https://github.com/user-attachments/assets/e069d965-0ef6-42e6-bf8f-14ac69706d6e)

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
