a, b, op = input().split()  
a, b = int(a), int(b) 

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:  
        print("It cannot be divided by zero.")
    else:
        print(a / b)
else:
    print("No corresponding operation exists.")
