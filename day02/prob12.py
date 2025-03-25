age = int(input())
height = int(input())
weight = int(input())

for _ in range(6):  # 6년간 출력
    print(f"{age} {height} {weight}")
    age += 1
    height += 6
    weight += 2
