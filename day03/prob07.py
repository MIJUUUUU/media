a =[input() for _ in range(5)]

longest = max(a, key=len)
shortest= min(a, key=len)

print("longest :", longest)
print("shortest :", shortest)
