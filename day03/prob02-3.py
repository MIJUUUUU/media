import pickle

print("Change the value of the key 'python'")


with open("prob2-1.bat", "rb") as f:
    data = pickle.load(f)


data["python"] = "자바"

with open("prob2-1.bat", "wb") as f:
    pickle.dump(data, f)

for key, value in data.items():
    print(f"{key}: {value}")


