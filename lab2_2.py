#แก้ไข เขียนโปรแกรมให้สามารถรับค่าอายุของผู้ใช้และแสดงข้อความตามช่วงอายุที่กำหนด

age = int(input("Enter your age: "))

if age < 5:
    print("You're too young for movies! Enjoy cartoons.")
elif age <= 12:
    print("You can watch G-rated movies.")
elif age <= 17:
    print("You can watch PG-13 movies.")
else:
    print("You can watch anything rated movies.")

like = input("Do you like action movies? (yes/no): ").strip().lower()
if like == "yes":
    print("good boy!")
else:
    print("Go away!")

#Choose Your Own Adventure    
#คุณเป็นคนที่ติดโทษประหารชีวิต มีข้อเสนอเข้ามาว่าถ้าเล่นเกมเอาตัวรอดนี้ชนะจะได้รับอถัยโทษ
#ให้เลือกว่าตลงหรือยอมโดนโทษประหาร 
#ถ้าเลือกว่าจะเล่นเกม ต่อมาโดนจับเข้าไปในเกาะทุกคนจะได้ระเบิดติดตัวไม่เหมือนกัน 
# และแต่ละคนจะถูกกระจายไปทั้วเกาะ
# คุณถูกเริ่มที่ชายหาดและมีระเบิดติดตัวอยู่ 6 ลูก เป็นแบบคุณจะทำอย่างไร


