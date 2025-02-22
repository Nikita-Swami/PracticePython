class Person:
    #Attribute
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    phone_no = None
    address = None


    #Behaviour
    def talk(self):
        print("I can talk")

    def sleep(self,name):#Argument with return type
        print("I am a method!!")
        print("Sleep",name)

    def sleep2(self,name):#Argument with no return type
        print("I am a method!!")
        return None

#Create object of class

nikita =Person()
nikita.name = "Nikita"
print(nikita.name)
nikita.talk()





