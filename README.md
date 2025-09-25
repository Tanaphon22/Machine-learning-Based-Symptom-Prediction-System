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

   - **Gender**  
  ตัวแปรประเภท categorical ซึ่งบอกถึงเพศของผู้ใช้งาน

   - **Age**  
  ตัวแปร numerical ซึ่งบอกถึงอายุของผู้ใช้งาน

   - **Summary**  
  ตัวแปรอยู่ในรูปแบบ JSON ข้างในมีข้อมูลเกี่ยวกับอาการป่วย จำเป็นต้องดึงข้อมูลเพื่อใช้ในการวิเคราะห์และสร้างโมเดล

   - **Search_term**  
  ตัวแปรที่จะเป็น target ของโมเดล Machine Learning ปัญหาคือข้อมูลบางแถวมีมากกว่า 1 ค่า จึงต้องพิจารณาวิธีการจัดการให้เหมาะสม



   
2. **Data Preprocessing & Cleaning**

   ก่อนนำข้อมูลไปใช้กับ Machine Learning จำเป็นต้องทำการเตรียมและปรับแต่งข้อมูลให้พร้อมก่อนได้แก่

   - **Gender**  
   ตัวแปรประเภท categorical ที่ยังไม่สามารถนำเข้า Machine Learning ได้ จำเป็นต้องแปลงจากตัวอักษรเป็นตัวเลขด้วย OneHotEncoder เพื่อให้สามารถใช้กับ ML ได้

   - **Age**  
  ตัวแปร numerical สามารถใช้กับ ML ได้ทันทีโดยไม่ต้องแปลงค่า

   - **Summary**  
  ตัวแปรอยู่ในรูปแบบ JSON ข้างในมีข้อมูลเกี่ยวกับอาการป่วยอยู่ จึงทำการดึงข้อมูลออกมาซึ่งข้อมูลอาการส่วนใหญ่นั้นเป็นภาษาไทยแต่ว่าข้อมูลที่ดึงออกมามีบางตัวที่เป็นภาษาอังกฤษ
  
   




