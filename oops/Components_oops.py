#The first one is inheritance, which is the creation of a new class by deriving from an existing one. The original is called the parent or superclass, or any derivatives are referred to as the subclass or child class. The next concept is called polymorphism. It's a word that means having many forms. In the context of Python, polymorphism means that a single function can act differently depending on the object or the causes. For example, the built-in plus operator works differently for different datatypes. In the case of integer data types, the built-in plus operator performs addition operations such as 3 plus 5 equals 8. On the other hand, in the case of string datatype, the built-in plus operator performs a concatenation or combining two strings together. This ability of modifying functionality is called polymorphism. The third concept is encapsulation. Broadly, this means that Python can bind methods and variables from direct access by wrapping them within a single unit of scope, such as a class. Encapsulation helps prevent unwanted modifications, in effect, reducing the occurrence of errors and outputs. Finally, there is a concept of abstraction. This refers to the ability to hide implementation details to make data safer and more secure. Note that Python does not support abstraction directly and uses inheritance to achieve it.
#object is a blueprint of class 
#class attributes are variables and behaviors are functions

#component in oops
#class
#a class is like a blueprint or template that defines the characteristics (attributes) and behaviors (methods) of an object.
#example, consider a "dog" class that defines how a dog should behave and what it can do.
#think of a "dog" class as a blueprint for different dog breeds each breeds of (e.g. Labrador Retriever,poodle.etc.)
#can be represented as an object of the "Dog" class

#class ClassName:
#     statement

#some point on python class:
#1) classes are created by keyword class.
#2) Attributes are the variables that belong to a class
#3) Attributes are always public and can be accessed using the dot(.) operator.E.g.: My class.Myattributes

# the class keyword indicates that you are creating a class followed by the name of the class(dog in this case)

class Dog:
    sound = 'bark'




#object
#an object is an instance of a class it represent a specific entity that has its own unique set of attributes and can perform action
#Eample a specific dog like "my_dog" is an object of the "Dog" class.
#"my_dog" can be an object representing an actual dog, such as "Bravo" shich has its own attributes (e.g. bark,eat,fetch)


#syntax Object definition
#obj =  ClassName()
#print(obj.atrr)

#An object consist of:

# State: it is represented by the attributes of an object. it also reflects the properties of an object
# Behavior: it is represented by the method of an object . it also reflects the response of an object to other object
# Identity: it gives a unique name to an object and enables one object to interact with other object 


#identity
#Name of dog

#state /attributes
#breed
#Age
#color

#behavior
#bark 
#sleep
#eat

#method  
# A method is a function associated with an object that defines the actions  or object it can perfom
#example  a dog object can have methods like "bark()" or "eat()". A do object can hae methods such as "bark()" to make a sound or "eat()" to consume food


class Dog:
    #attributes
    attr1 = "mammal"
    attr2 = "dog"

    #A sample method
    def fun(self):
        print("i'm a", self.attr1)
        print("i'm a", self.attr2)

#object instantiation
Rodger = Dog()

#accessing class attributes
#and method through objects
print(Rodger.attr1)
Rodger.fun()


class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def show(self):
        print("hello my name is "+ self.name +" and I "+"work in "+self.company)


obj = GFG("Mark", "facebook")
obj.show()


