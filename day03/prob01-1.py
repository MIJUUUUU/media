file_name = "prob1-1.txt"

n = []

print("Input your string...")
while True:
    enter = input(">> ")
    if enter == "Q":
        break
    n.append(enter)

with open(file_name, "w") as f:
    for line in n:
        f.write(line + "\n")

print("Write process has been finished")
