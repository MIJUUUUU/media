weight= int(input(""))
height = int(input(""))

height2= height * 0.01
bmi = weight/height2 **2

if bmi <20:
    print("Underweight")

elif 20<=bmi<25:
    print("Normal")

elif 25<= bmi<30:
    print("Overweight")


elif 30<= bmi<40:
    print("Obesity")

elif bmi >=40:
    print("Extremely overweight")