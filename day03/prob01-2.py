file_name = "prob1-1.txt"

print("Your inputs are below..")


with open(file_name, "r") as f:
    for line in f:
        print(line.strip())

print("\nProcess finished with exit code 0")
