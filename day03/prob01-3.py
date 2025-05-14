with open("prob1-1.txt", "r") as f:
    lines = f.readlines()

print("Enter the string to append...")
new = input(">>")

lines.append(new +"\n")

with open("prob1-3.txt", "w") as f:
    f.writelines(lines)

print("File append process has been finished")
