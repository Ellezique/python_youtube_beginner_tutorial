#from the file called Student.py import the class called Student
from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Jennifer", "Arts", 4.0, False)

print(student1.name)
print(student1.gpa)
print(student1.on_honor_roll())

print(student2.name)
print(student2.on_honor_roll())