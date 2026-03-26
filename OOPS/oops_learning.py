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

# class Calculator:
#     def __init__(self):
#         self.a = None
#         self.b = None
#     @staticmethod
#     def add(a, b):
#         return a + b
# c1 = Calculator()
# result = c1.add(5, 10)
# print(f"Addition: {result}")


# Encapsulation in Python

# class Student:
#     def __init__(self,name,age,marks):
#         self.name=name
#         self.age=age
#         self.marks=marks
#     def display(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Marks: {self.marks}")
# s1 = Student("Alice", 20, 85)
# s1.marks = 90
# s1.display()

# class BankAccount:
#     def __init__(self,balanace):
#         self.__balance = balanace
    
#     def get_balance(self):
#         return self.__balance
    
#     def deposit(self,amount):
#         if amount > 10:
#             self.__balance += amount
#             print(f"Deposited: {amount}")
#         else:
#             print("Minimum deposit amount is 10")

#     def withdraw(self,amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -+ amount
#             print(f"Withdrawn: {amount}")
#         else:
#             print("Invalid withdrawal amount or insufficient balance")
# account = BankAccount(500)
# print(f"Initial Balance: {account.get_balance()}") 
# account.deposit(5)
# print(f"Balance after deposit: {account.get_balance()}") 

# Inheritance in Python

# Single Inheritance
# class Animal:
#     def speaks(self):
#         print("Animal makes a sound")
# class Dog(Animal):
#     def speak(self):
#         print("Dog barks")

# d1= Dog()
# d1.speak()
# d1.speaks()

class Animal:
    def __init__(self, name):
        self.name=name
    def eat(self):
        print(f"{self.name} is eating")
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} meows")
d1 = Dog("Buddy")
d1.eat()    
d1.speak()
c1= Cat("Whiskers")
c1.eat()    
c1.speak()

        
        