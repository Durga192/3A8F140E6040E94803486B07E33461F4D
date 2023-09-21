class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

# Create a list of student objects
students = [
    Student("John", "A001", 3.8),
    Student("Jane", "A002", 3.9),
    Student("Alice", "A003", 3.7),
    Student("Bob", "A004", 3.5),
]

# Sort the list of students based on CGPA
sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(student.name, student.roll_number, student.cgpa)