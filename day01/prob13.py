n = int(input(""))

if n>=150000:
    print("15%")
    dis = n * 0.15
    print(f"{n-dis:.0f}")

elif n>=100000:
    print("10%")
    dis = n * 0.1
    print(f"{n-dis:.0f}")

elif n>=50000:
    print("5%")
    dis = n * 0.05
    print(f"{n-dis:.0f}")

else:
    print("-1")



