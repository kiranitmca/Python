class Student:
    def __init__(self):
        self.name = None
        self.age = None
        self.marks = None
        self.sex = None
    def display(self):    
        print(f"Name: {self.name}")        
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Sex: {self.sex}")

s1= Student()

s1.name = "Alice"
s1.age = 20
s1.marks = 85
s1.sex = "Female"

s1.display()
