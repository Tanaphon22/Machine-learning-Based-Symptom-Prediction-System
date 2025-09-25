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
  ตัวแปรที่จะเป็น target ของโมเดล Machine Learning ปัญหาคือข้อมูลบางแถวมีมากกว่า 1 ค่า และเมื่อใช้คำสั่ง Counter พบว่าข้อมูลไม่สมดุลกันอย่างมากยกตัวอย่างอาการ "ไอ" มีทั้งหมด 173 ตัว แต่ "เลือดกำเดาไหล" มี 1 ตัว การที่ข้อมูลมีจำนวณที่แตกต่างกันมากขนาดทำให้โมเดลของ   เราที่ได้มาเกิด bias ได้ เนื่องจากโมเดลไม่มีข้อมูลเพียงพอจะเรียนรู้ว่าอาการเลือดกำเดาไหลคือเลือดกำเดาไหลแต่โมเดลจะคิดว่าเลือดกำเดาไหลคืออาการไอนั้นเอง จึงต้องพิจารณาวิธีการจัดการกับปัญหาทัั้ง 2 ให้เหมาะสม



   
2. **Data Preprocessing & Cleaning**

   ก่อนนำข้อมูลไปใช้กับ Machine Learning จำเป็นต้องทำการเตรียมและปรับแต่งข้อมูลให้พร้อมก่อนได้แก่

   - **Gender**  
   ตัวแปรประเภท categorical ที่ยังไม่สามารถนำเข้า Machine Learning ได้ จำเป็นต้องแปลงจากตัวอักษรเป็นตัวเลขด้วย OneHotEncoder เพื่อให้สามารถใช้กับ ML ได้

   - **Age**  
  ตัวแปร numerical สามารถใช้กับ ML ได้ทันทีโดยไม่ต้องแปลงค่า

   - **Summary**  
  ตัวแปรนี้อยู่ในรูปแบบ JSON ซึ่งภายในเก็บข้อมูลเกี่ยวกับอาการป่วย เมื่อดึงข้อมูลออกมา พบว่าข้อมูลส่วนใหญ่เป็นภาษาไทย แต่มีบางส่วนเป็นภาษาอังกฤษ เช่น 'Fever' รวมถึงบางคำที่ไม่เกี่ยวข้องกับอาการป่วย เช่น 'การรักษาก่อนหน้า' จึงต้องทำความสะอาดด้วยการลบออกไป

   **ก่อน**

   <img width="301" height="321" alt="image" src="https://github.com/user-attachments/assets/ec25fe74-dedd-4acf-84cf-90534b28bae2" />
   
   **หลัง**

   <img width="244" height="323" alt="image" src="https://github.com/user-attachments/assets/4d2bc65c-b44b-4b75-b139-5d38bfc4bce8" />

   - **Search_term**  
  ตัวแปรในรูปแบบ list ถูกกำหนดให้เป็น target ของโมเดล แต่เนื่องจากบางแถวมีค่ามากกว่าหนึ่งค่า จึงใช้คำสั่ง df.explode เพื่อแยกค่าภายในคอลัมน์ search_term ออกมาเป็นหลายแถว การแยกนี้จำเป็นเพื่อให้โมเดลมองแต่ละค่าเป็นอิสระ หากไม่แยก โมเดลจะมองเห็นค่าทั้งหมดเป็นก้อนเดียว เช่น 'เสมหะ, ไอ' ในขณะที่รูปแบบที่ต้องการให้โมเดลเห็นคือ 'เสมหะ' และ 'ไอ' แยกออกจากกัน

   **ก่อน**

   
   <img width="108" height="325" alt="image" src="https://github.com/user-attachments/assets/f837a9b4-70af-416a-927e-f489e824f264" />

   **หลัง**

   
   <img width="96" height="329" alt="image" src="https://github.com/user-attachments/assets/7c1100bd-93b6-42ce-b711-5ab26e79e391" />


   ปัญหาคลาสไม่สมดุลจะแก้ไขโดยการทำ Duplicate data เพื่อเพิ่มจำนวนของคลาสที่มีตัวอย่างน้อย และเมื่อแบ่งข้อมูลเป็น train และ test ใช้พารามิเตอร์ stratify=y เพื่อให้สัดส่วนของแต่ละคลาสยังคงเหมือนเดิมในการแบ่งชุดข้อมูล หมายความว่า แม้ว่าสัดส่วนของคลาสจะไม่เท่ากัน แต่เราจะมั่นใจได้ว่าทุกคลาสจะปรากฏทั้งใน train และ test ต่อไปจะใช้ sample weight เพื่อช่วยให้โมเดลให้ความสำคัญกับคลาสที่มีจำนวนตัวอย่างน้อยกว่าได้มากขึ้น





  
   




