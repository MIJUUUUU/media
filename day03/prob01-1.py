
file_name = "prob1-1.txt"


n = []

print("Input your string...")
while True:
    enter = input(">> ")
    if enter == "Q":
        break
    n.append(enter)

# 파일에 저장
with open(file_name, "w") as f:
    for line in f:
        f.write(line + "\n")

print("Write process has been finished")
