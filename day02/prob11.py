answer = int(input(""))
i = 1
while i <=10:

    if i>10:
        print("End")
   
    else:
     num = int(input(""))
     if num < answer:
        print("Up")
     elif num > answer:
        print("Down")

     elif num == answer:
        print("Correct")

i +=1