a,sign, b=input("").split()
a = int(a)
b = int(b)

if sign == "-":
    print(a, sign, b, "=", a-b)

elif sign == "+":
    print(a, sign, b, "=", a+b)

elif sign == "*":
    print(a, sign, b, "=", a*b)

elif sign == "/":
    print(a, sign, b, "=", a/b)