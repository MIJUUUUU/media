
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old and I major in {self.major}."


students = [
    Student("Alice", 21, "Computer Engineering"),
    Student("Bob", 22, "Cyber Security"),
    Student("Charlie", 23, "Game Engineering"),
    Student("David", 24, "IT Operations Management"),
    Student("Eve", 25, "Computer Software")
]


num = int(input(""))


if 1 <= num <= 5:
    print(students[num - 1].introduce()) 
else:
    print("Invalid input. Please enter a number between 1 and 5.")
