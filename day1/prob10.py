a,b,c = map(int, input("Input 3 integer values>> ").split())


if a+b<=c or b+c<=a or a+c<=b:
    print("No, this is NOT a triangle")

else:
    print("Yes, this is a triangle")
