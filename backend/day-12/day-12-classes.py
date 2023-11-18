class Student:
    def __init__(self, name, age, 
        is_enrolled, classes, offenses):
        self.name = name
        self.age = age
        self.is_enrolled = is_enrolled
        self.classes = classes
        self.offenses = offenses

student1 = Student("Juan Dela Cruz", 20, True, [], [])

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")
print(f"Status: {'Enrolled' if student1.is_enrolled else 'Not Enrolled Yet'}")
print(f"Classes: {student1.classes}")
print(f"Offenses: {student1.offenses}")

