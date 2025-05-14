a = int(input(""))
b = int(input(""))

answer = sum(range(a, b + 1))
if a <= 0 or b <= 0:  
    print(-1)
elif a > b:  
    print(-1)
else:
    print(answer) 

