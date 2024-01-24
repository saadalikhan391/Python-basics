class P:
    def __init__(self):
        self.a = 7

class C(P):
    pass

c = C() # instance of child class

print(c.a)


#Employment

class Employees:
    def __init__(self, name, last):
        self.name = name
        self.last = last

class Supervisorrs(Employees):
    def __init__(self, name, last, password):
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + "days"
    

saad = Supervisorrs("Saad","Khan","apple")

ali = Chefs("Ali", "A")
khan = Chefs("Khan","K")


print(ali.leave_request(3))
print(saad.password)
print(khan.name)

# Multiple inheritance
# class A:
#    a = 1
   
# class B:
#    b = 2
   
# class C(A, B):
#    pass

# c = C()
# print(c.a, c.b)


#Multi-level inheritance
class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)  #The output is 2 because C derives from the immediate super class of C, and that's B.


# Built-in functions
# There are two built-in functions that can come in handy when trying to find the relationship between different classes and objects: issubclass() and isinstance().

# The first one, issubclass () is demonstrated below. 

# issubclass(class A, class B)
print(issubclass(A,B))
print(issubclass(B,A))  #Is B subclass of A?“ You can see the result is "True"

class Y:
	pass
class Z(Y):
	pass

z = Z()
print(isinstance(z,Z))
print(isinstance(z,Z))


# Now that you know how classes can be extended from other classes, let's look at another useful built-in function called the super() function.

# The super() function is a built-in function that can be called inside the derived class and gives access to the methods and variables of the parent classes or sibling classes. Sibling classes are the classes that share the same parent class. When you call the super() function, you get an object that represents the parent class in return.

# The super() function plays an important role in multiple inheritance and helps drive the flow of the code execution. It helps in managing or determining the control of from where I can draw the values of my desired functions and variables.

# If you change anything inside the parent class, there is a direct retrieval of changes inside the derived class. This is mainly used in places where you need to initialize the functional

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour()