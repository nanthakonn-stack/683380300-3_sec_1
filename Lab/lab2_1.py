#แก้ไขโค้ดนี้ให้ถูกต้อง

num = int(input("Enter a number: ") )
if num < 0:
    text = f"{num} is negative"
elif num > 0:
    text = f"{num} is positive"
else:
    text = f"{num} is zero"

if num == 0:
    print(f"{text} and Even number")
elif num % 2 == 0:
    print(f"{text} and Even number")
else:
    print(f"{text} and Odd number")
#รับค่าตัวเลขเป็้นint นำไปตรวจว่าเป็นบวกลบหรือ0 แต่อย่างพึ่งprintให้ไปprintพรร้อมกับที่เช็คว่าเป็นคู่คี่
