# True / False  Boolean

#logical operators
#and
#or
#not


#1) "and"   check for both conditions to be true
#a = 6   true
#c = 8   true
# a>5 and c<10

#2) "or" check atleast one condition to be true
#a = 6   true
#b = 8   false

# a>5 or b>10


#3) "not"  return false if the  result is true 

#not(a>5)


a = False
b = False

if not(a) and not(b):
    print("using not logical operator!")


a = True
b = True

if a or b:
    print("one condition is true")

a = True
b = True

if a and b:
    print("both conditions are true")
    print("hello")
else:
    print("both conditions are not true")


#control flow
#if
#else
#elif    (else if)