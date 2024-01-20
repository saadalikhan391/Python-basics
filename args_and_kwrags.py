# kwrags = key words aguments  dictionary
# Args = non key word arguments  any number of arguments  tuple

# def sum_of (a,b):
#      return a + b

# print(sum_of(4,5,6))


# *args (Non-Keyword Arguments)

def sum_of(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print(sum_of(4,5,6,4,5,6))


def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)


# def myFun(arg1, *argv):
#     print("First argument :", arg1)
#     for arg in argv:
#         print("Next argument through *argv :", arg)
 
 
# myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')

# **kwargs (Keyword Arguments)

def calculate_total(**kwargs):
    total_sum = 0
    for item, price in kwargs.items():
        total_sum += price
    return round(total_sum, 2)

print(calculate_total(coffee=2.99, cake=4.55, juice=2.99))


def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="ali", Lastname="khan", Age=26, Phone=1234567890)
intro(Firstname="saad", Lastname="khan", Email="saadalikhan43@nomail.com", Country="USA", Age=27, Phone=9876543210)



# def myFun(arg1, **kwargs):
#     for key, value in kwargs.items():
#         print("%s == %s" % (key, value))
 
 
# # Driver code
# myFun("Hi", first='Geeks', mid='for', last='Geeks')






# def myFun(arg1, arg2, arg3):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
 
 
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks")
# myFun(*args)
 
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks"}
# myFun(**kwargs)






# def myFun(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
 
 
# # Now we can use both *args ,**kwargs
# # to pass arguments to this function :
# myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")



# # defining car class
# class car():
#     # args receives unlimited no. of arguments as an array
#     def __init__(self, *args):
#         # access args index like array does
#         self.speed = args[0]
#         self.color = args[1]
 
 
# # creating objects of car class
# audi = car(200, 'red')
# bmw = car(250, 'black')
# mb = car(190, 'white')
 
# # printing the color and speed of the cars
# print(audi.color)
# print(bmw.speed)





# # defining car class
# class car():
#     # args receives unlimited no. of arguments as an array
#     def __init__(self, **kwargs):
#         # access args index like array does
#         self.speed = kwargs['s']
#         self.color = kwargs['c']
 
 
# # creating objects of car class
# audi = car(s=200, c='red')
# bmw = car(s=250, c='black')
# mb = car(s=190, c='white')
 
# # printing the color and speed of cars
# print(audi.color)
# print(bmw.speed)



