# 학생 정보를 저장하는 Student 클래스
class Student:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major

    def introduce(self):
        return f"Hello, my name is {self.name}. I am {self.age} years old and I major in {self.major}."

# 학생 정보 리스트 (1~5번 학생)
students = [
    Student("Alice", 21, "Computer Engineering"),
    Student("Bob", 22, "Cyber Security"),
    Student("Charlie", 23, "Game Engineering"),
    Student("David", 24, "IT Operations Management"),
    Student("Eve", 25, "Computer Software")
]

# 사용자 입력 받기
num = int(input("Enter a number (1-5): "))

# 입력값이 1~5 사이일 경우 출력
if 1 <= num <= 5:
    print(students[num - 1].introduce())  # 리스트는 0부터 시작하므로 num-1 사용
else:
    print("Invalid input. Please enter a number between 1 and 5.")
