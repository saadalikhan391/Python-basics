class Engine:
    
    def start_engine(self):
        print("Engine Started")

    @staticmethod
    def stop_engine():
        print("Engine Stopped")

#Create Object 
obj = Engine()
obj.start_engine()
obj.stop_engine()
print("********")
Engine().start_engine()
Engine().stop_engine()

#default constructor

# class Calculator:
#     def __init__(self):
#         print("I am default constructor")

#     def add_number(self, a,b):
#         add = a + b
#         return add
    
# obj = Calculator()
# print("object is created")
# addition = obj.add_number(10,10)
# print("addition is", addition)


#parameterized constructor
class Calculator:
    #class_variable = 15  #class variable 
    def __init__(self,a,b):
        self.a = a        #self -->instance variable it is also local variable it is very important to use  now u can pass value to your object calculator()
        self.b = b         #this is instacne variable u can't use this variable outside this function local variable 

    # def add_number(self, a,b):
    #     add = a + b
    #     return add
    def add_number(self):
        return self.a + self.b #+ self.class_variable

obj = Calculator(20,13)
print(obj.add_number())

#if you un0comment class_variable it will add into it   u can also call this self.class_varaibale intead of that Calculator.class_varraible  that is difference between class variable and instance variable 
#inheritance in cartest.py