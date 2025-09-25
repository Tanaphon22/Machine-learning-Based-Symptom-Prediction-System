# Machine-learning-Based-Symptom-Prediction-System

## Dataset Overview
- **1000 rows and 4 columns :** Each row represents a user, and columns include personal and symptoms data
- **Gender :** Gender of user
- **Age :** User's age
- **Summary :** User's symptom information (JSON)
- **Search_term :** Result from symptoms entered

## Solution

1. **Data Understanding**

   
   <img width="1525" height="212" alt="image" src="https://github.com/user-attachments/assets/c5ce1c89-d227-4aee-abb5-c359bc060573" />

   -จากภาพจะเห็นได้ว่าตัวแปลที่สามารถจัดการก่อนจะมีตัวแปล Gender โดยจะใช้ onehotencoder เพื่อแปลงให้เป็นตัวเลยเพื่อที่เราจะสามารถเอาเข้าไปใน ML ได้ ต่อมาจะเป็นตัวแปล Age ซึ่งเป็นตัวเลขอยู่แล้วจึงสามารถข้ามไปได้ก่อน โดยปัญหาหลักคือตัวแปล Summary และ Search_term ปัญหาของตัวแปล Summary คือยังอยู่ในรูปแบบ json ซึ่งเราจะเห็นได้ว่าข้อมูลข้างในมีข้อมูลของอาการป่วยอยู่ จึงทำการดึงข้อมูลนั้นออกมาจากตัว json และเก็บอยู่ dataframe column

   -From the image, we can see that the variable that can be handled first is Gender, which will be transformed using OneHotEncoder so that it can be fed into the ML model. Next is Age variable, which is already numeric and can be left as is. The main problem lies with Summary and Search_term variables. The issue with Summary is that it is still in JSON format, which contains information about symptoms. Therefore, we extract that information from JSON and store it in the dataframe column


   -จากที่ได้ข้อมูลของอาการป่วยมาแล้วจะเห็นได้ว่ามีคำที่ไม่ได้เกี่ยวข้องกับอาการป่วยและภาษาอังกฤษรวมอยู่ด้วยเช่น "การรักษาก่อนหน้า", "ประวัติอุบัติเหตุ", "Fever" จึงทำการลบพวกมันออกไป

   

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
