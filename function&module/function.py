# def  name (parameter):     return     it execute when you call the function
#when ever you get return value inside function so you have to asign variable to fuction for print/output result

def function1():                           
    print("hmmmmmmmm")
    print("hmmmmmmmmmmm22222222")

function1()              #call function when it use print 
function1()
function1()

def hello(name):
    print("hello "+ name + "!!!!")

hello("Saad Ali Khan")
hello("Python Trainer")
hello("khan")

def hello1(name="Python function"):
    print("hello "+ name + "!!!!")

hello1()
hello1()
hello1()


def hello2(name,age):
    print("hello "+ name + " you are "+str(age)+ " year old!")


hello2("python",20)

def change(value):
    value = 2

val = 1
change(val)
print(val) 

hello2("python",20)


# A function can return a value, using the return statement. For example in
# this case we return the name parameter name:
def hello3(name):
    print('Hello ' + name + '!')
    return name

h = hello3('khan11')
print(h)
# When the function meets the return statement, the function ends.
# We can omit the value:
def hello4(name):
    print('Hello ' + name + '!')
    return
i =hello4("python11")
print(i)

# We can have the return statement inside a conditional, which is a common
# way to end a function if a starting condition is not met:

def hello5(name):
    if not name:
        return
    print('Hello ' + name + '!')

j = hello5("session7")
print(j)
# If we call the function passing a value that evaluates to False , like an empty
# string, the function is terminated before reaching the print() statement.
# You can return multiple values by using comma separated values:

def hello6(name):
    print('Hello ' + name + '!')
    return name, 'khan', 8

k =hello6("learnwith")
print(k)
# In this case calling hello('Syd') the return value is a tuple containing those
# 3 values: ('Syd', 'khan', 8) 

def function2(x):    #parameter fill return value 
    return 2*x        #return is output of fuction


a = function2(6)      #input or argument to get output
print(a)


def function3(x):
    return x - 2

b= function3(10)

print(b)

def addition(a , b):
    return a + b


f =addition(15,4)
print(f)


