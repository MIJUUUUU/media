while True:
    try:
        n = int(input())
        if 1 <= n <= 9:
            break
    except:
        pass

for i in range(1, n + 1):
    numbers = list(range(i, 0, -1)) + list(range(2, i + 1))
    line = " ".join(str(j) for j in numbers)

    # 왼쪽 공백 계산: (n - i) 만큼, 공백 2칸 기준
    space = " " * ((n - i) * 2)
    print(space + line)
