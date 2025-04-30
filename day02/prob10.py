a,b,c = map(int, input("").split())


if a+b<=c or b+c<=a or a+c<=b:
    print("Input 3 integer values>> No, this is NOT a triangle.")

else:
    print("Input 3 integer values>> Yes, this is a triangle.")
