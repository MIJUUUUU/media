import pickle 

dict = {
    "dictionary": "사전",
    "python": "파이썬",
    "Zoo": "동물원",
    "School": "학교",
    "University": "대학교"
}

with open("prob2-1.bat", "wb") as f:
    pickle.dump(dict, f)

with open("prob2-1.bat", "rb") as f:
    my_dict = pickle.load(f)

for key, value in my_dict.items():
    print(f"{key}: {value}")

