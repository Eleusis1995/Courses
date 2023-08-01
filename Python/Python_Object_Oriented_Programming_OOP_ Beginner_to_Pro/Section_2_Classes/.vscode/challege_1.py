import random
class Student:
    educational_platform = "Udemy"
    def __init__(self, name, age = 16):
        self.name = name
        self.age = age

    def greet(self):
        list_of_greets = ["Hello {0} it is a pleassure"
                            "Hey I´m {0}, how are you doing",
                            "Hi, my name is {0}, nice to meet you",
                            "My name is {0}, what is yours?"]
        
        return random.choice(list_of_greets).format(self.name)

student_one = Student(name="Pedro")

print(student_one.greet())
print(student_one.greet())
print(student_one.greet())
print(student_one.greet())