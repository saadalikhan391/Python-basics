# the abstract class is a type of class for which you cannot create an instance. Python also does not support abstraction directly. You need to impose a module just to define an abstract class. Furthermore, methods in an abstract class needs to be defined before they can be implemented.
#The module is known as the abstract base class or ABC, and needs to be imported with some code. After that, you can create a class called SomeAbstractClass and pass in the ABC module so that it inherits that class.
#The next step is to import the abstract method decorator inside the same module. A decorator is a function that takes another function as its arguments and gives a new function as its output.  It's denoted by the add sign
#A decorator is a function that takes another function as its arguments and gives a new function as its output

from abc import ABC, abstractmethod   #import ABC

class SomeAbstractClass(ABC):   #ceate inheiting class
    @abstractmethod             #import abstract method
                                #call abstract method
    def someabstractmethod(self):
        pass

#we can define abstract methods with the help of what we call an abstract method decorator present inside the same module. Any given abstract class can consist of one or more abstract methods. However, a class that has abstract class as its parents cannot be instantiated unless you override all the abstract methods present in at first. 


class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

#create sub class
class Donation(Employee):
    def donate(self):
        a =input("How much would you like to donate: ")        #Implementation
        return a

#create instances
amounts = []

saad = Donation()
s = saad.donate()
amounts.append(s)

khan = Donation()
k = khan.donate()
amounts.append(k)

print(amounts)