# assignment operator
# arithmetic operators
# comparison operators
# logical operators
# bitwise operators
# plus some interesting ones like is and in .



# #math operator
# # +
# # -
# # /
# # *
# # **
## //
## %

#1)Additiion
print(22 + 5)
print(44.5+23.4)


# #2) Substraction
print(44-7)
print(66.4 -6.5)

# #3) Division
print(20/2)

print(55.2/5.2)


# #4) Multiply
print(20 * 2)

print(50.3 * 5.6)

# #power of number
print(5.4**2.2)
print(4**2)    # 4x4


#implicit

a = 22
b =  10.5

print(type(a))
print(type(b))

print(a + b)

#do practice here



#numeric
#integer is a whole number like 10, 2 , 7 , -2 , -5
# float decimal number 1.1 , 5.6 , -2.2, 7.8
# complex number  a + 2ab (-b)2


age = 9

anotherage = age

print(age)
print(anotherage)

#combine the assigning operators

age = 10
age += 3
print(age)

age1 = 10
age1 -= 3
print(age1)


#use more here * , / and so on



# Python defines a few comparison operators:
# ==
# !=
# >
# <
# >=
# <=

c = 2

d = 4

if c <= d: 
    print("True")
else:
    print("false")



#logical operator
# condition1 = True
# condition2 = False
# not condition1 #False
# condition1 and condition2 #False
# condition1 or condition2 #True


# Bitwise operators
# Some operators are used to work on bits and binary numbers:
# & performs binary AND
# | performs binary OR
# ^ performs a binary XOR operation
# ~ performs a binary NOT operation
# << shift left operation
# >> shift right operation
# 31
    

# Bitwise operators are rarely used, only in very specific situations, but they
# are worth mentioning.
    


# is and in
# is is called the identity operator. It is used to compare two objects and
# returns true if both are the same object. More on objects later.
# in is called the membership operator. Is used to tell if a value is
# contained in a list, or another sequence. More on lists and other sequences
# later
    


# The Ternary Operator
# The ternary operator in Python allows you to quickly define a conditional.
# Let's say you have a function that compares an age variable to the 18
# value, and return True or False depending on the result.
# Instead of writing:
def is_adult(age):
    if age > 18:
        return True
    else:
        return False

# You can implement it with the ternary operator in this way:
def is_adult(age):
 return True if age > 18 else False
# First you define the result if the condition is True, then you evaluate the
# condition, then you define the result if the condition is false:
# <result_if_true> if <condition> else <result_if_false