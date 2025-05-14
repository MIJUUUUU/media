answer = int(input(""))
i = 1

while i <=10:
    num = int(input(""))
    
    if num < answer:
        print("Up")

    elif num > answer:
        print("Down")

    elif num == answer:
        print("Correct")
        break
    i +=1

if i > 10:
    print("End")



