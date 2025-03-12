score = int(input(""))

if score<0 or score>100:
    print("-1")

else:
    if score>=80:
     print("A")


    elif score>=60 and score<80:
     print("B")

    elif score>0:
     print("C")