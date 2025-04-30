import pickle

with open("prob2-1.bat", "rb") as f:
    data = pickle.load(f)

for key, value in data.items():
    print(f"{key}: {value}")

search = input("\nEnter the word to search : ")


if search in data:
    print(f"meaning of '{search}' you searched for is '{data[search]}'")
else:
    print(f"'{search}' is a word that does not exist")
