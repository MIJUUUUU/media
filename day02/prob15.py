while True:
    try:
        n = int(input())
        break
    except:
        pass  # 숫자 입력될 때까지 반복

lower_count = 0  # 소문자 개수
upper_count = 0  # 대문자 개수

for _ in range(n):
    ch = input()
    if len(ch) == 1:  # 한 글자만 입력된 경우
        if ch.islower():
            lower_count += 1
        elif ch.isupper():
            upper_count += 1

# 결과 출력 (소문자, 대문자 순)
print(lower_count)
print(upper_count)
