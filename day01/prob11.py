arr= list(map(int, input("").split()))

odd = [arr[i] for i in range(0,20,2)]

if odd:
    min = min(odd)
    max = max(odd)
    avg = sum(odd)/len(odd)

    print(min, max, f"{avg:.2f}")