#Take input and create a class in python

class Person:
    def __init__(self):
        self.name = input("Enter the name\n")
        self.age = input("Enter the age\n")
        self.phone = input("Enter the phone\n")
        self.occupation = input("Enter the occupation\n")

    def display_information(self):
        print(f"Name is:{self.name}")
        print(f"age is:{self.age}")
        print(f"phone is:{self.phone}")
        print(f"occupation is:{self.occupation}")

#Create the object of class
person1 = Person()

#Call the function
person1.display_information()