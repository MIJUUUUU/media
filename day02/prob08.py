list_a= list(map(int, input().split()))
list_b=[]

for i in list_a:
    if i%2 ==0:
        list_b.append(i)

    
print(list_b)