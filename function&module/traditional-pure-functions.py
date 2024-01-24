# Let's start by exploring the role of a function, functions take some input, process it and then produce some outputs. There are two types of functions traditional and pure, pure functions will always do the same thing and return the same results no matter how many times they are called. There are several differences between traditional and pure, so let's list them. Traditional functions can access and modify variables on the global state, but pure functions cannot, both traditional functions and pure functions can access variables in the local state. Traditional functions can change our dogs, whereas pure functions cannot, and lastly, the outputs of traditional functions does not depend on inputs. However, the output of pure functions does depend on input, functional programming in essence is a programming paradigm that utilizes functions for clean, consistent and maintainable code. Compared to object orientated programming, which we'll learn about later, functional programming differs by design.
#they can be assigned to a variable, passed as an argument or returned to its caller.

# It's important to understand that there is a clear difference between traditional and pure functions. A pure function is a function that does not change or have any effect on a variable, data, list, or sets beyond its own scope. For example, if you have a list with the global scope, a pure function cannot add something to that list or alter it in any way. 
#pure function  --> no effect beyond its  own scope

#global scope

global_list = [1,2,3]   #global list

def add_to(item):
    return global_list.append(item)
add_to(4)
print(global_list)

#output [1,2,3,4] appended item this is not pure function
#No, it's not a pure function as it changes the global_list by appending the item which is passed as an argument

# A pure function is used in functional programming because it does not change or have any effect on a variable, data, list, or set beyond its own scope. 

# change to a pure function
def add_to_list(lst,item):
    nl = lst.copy()
    nl.append(item)
    return nl

#example1
my_list = [1,2,3]

def add_to_list(item):
    return my_list.append(item)

add_to_list(4)

print(my_list)
#What do you think? Is this a pure function? No, it's not. Because the data has been manipulated at the global scope from inside the scope of the function
#lets change this function to pure function
my_list = [1,2,3]

def add_to_list(lst,item):
    nl= lst.copy()
    nl.append(item)
    return nl

new_list = add_to_list(my_list,4)

print(my_list)
print(new_list)

#This function is now a pure function because it adds value to a list, but it doesn't manipulate the original list outside the function