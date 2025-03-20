N = int(input(""))

five = N//500
N %=500

hund=N//100
N %=100


fif=N//50
N %=50


ten=N//10
N %=10

print(five, hund, fif, ten)
    

