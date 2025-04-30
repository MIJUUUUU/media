list_a = list(map(int, input(""). split()))


print(list_a)

list_a.insert(2,50)
list_b = list_a[:]

del list_a[3]
list_c = list_a[:]

print(list_b)
print(list_c)