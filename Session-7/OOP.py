import os
os.system('cls' if os.name == 'nt' else 'clear')

#!Everthing in Python is class
# def print_types(data):
#     for i in data:
#         print(i, type(i))

# test = [122, "victor", [1, 2, 3], (1, 2, 3), {1, 2, 3}, True, lambda x:x]

# print_types(test)

# #! defining class

# #"class" keyword for defining

# class Person:
#     name = "adam"
#     age = 33

# person1 = Person()
# person2 = Person()

# print(person1.name) #instances inherites class atributes
# print(person1.age)


# Person.job = "developer"
# print(person1.job)

# #! class attributes vs instance attributes:

# class Person:
#    company = "clarusway"

# person1 = Person() #!instance
# person2 = Person() #!instance

# person1.location = "turkey"

# print(person1.location)
# person1.company= "tesla"

# print(person2.company)
# print(person1.company)

#! SELF keyword and methods

# class Person:
#    company = "clarusway"

#    def test(self):
#        print("test")

#    def set_details(self,name, age):
#        self.name = name
#        self.age = age

#    def get_details(self):
#        print(f"{self.name} - {self.age}")

#    @staticmethod  #! static her instance için aynı sonucu döndürür. 
#    def salute ():
#        print("Hi there!")

# person1 = Person()
# person2 = Person() 

# # person1.test()
# # Person.test(person1)



# person1.name= "adam"
# person1.age = 33
# person1.get_details()

# person2.name= "henry"
# person2.age= 18

# person2.set_details("json",15)
# person2.get_details()

# person1.salute()

#! special methods (dunder methods)

class Person:
    company = "clarusway"

    #automaticaly runs when the instance is created
    def __init__(self,name, age, gender="male"):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        print(f"{self.name} - {self.age} - {self.gender}")

person1 = Person("adam", 33)
person1.get_details()

person2 = Person("Jason", 22)

