# Class and Object declaration
# class Student:
#     def __init__(self):
#         self.name = None
#         self.age = None
#         self.marks = None
#         self.sex = None
#     def display(self):    
#         print(f"Name: {self.name}")        
#         print(f"Age: {self.age}")
#         print(f"Marks: {self.marks}")
#         print(f"Sex: {self.sex}")

# s1= Student()

# s1.name = "Alice"
# s1.age = 20
# s1.marks = 85
# s1.sex = "Female"

# s1.display()

# class multi:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def display(self):
#         print(f"Multiplication: {self.a * self.b}")
# m1 = multi(5, 10)
# m1.display()

# Class variable and class method

# class Student:
#     school= 'Narayana'
#     def __init__(self):
#         self.name=None
#         self.age=None
#         self.marks=None
#         self.gender=None
#     @classmethod
#     def change_school(cls, new_school):
#         cls.school = new_school
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Marks: {self.marks}")
#         print(f"Gender: {self.gender}")
#         print(f"School: {self.school}")
# s1 = Student()
# Student.change_school("Vignan")
# s1.name = "Alice"
# s1.age = 20
# s1.marks = 85   
# s1.gender = "Female"
# s1.display()    

# @staticmethod declaration and usage 

class Calculator:
    def __init__(self):
        self.a = None
        self.b = None
    @staticmethod
    def add(a, b):
        return a + b
c1 = Calculator()
result = c1.add(5, 10)
print(f"Addition: {result}")