#print function always give you the output of the result print()
#comment
#single inverted comma double inverrted comma both performing same thing there is no such difference in python
#String data "" or '' only in python it perform same 
#"any alphabet any number"
# cd stand for change directory  backward cd .. cd path name  ls mean list directory
#tab key help you to choose the path 
#run file python and name of file
print('python code')
print("this is my first class")
#shortcut key in windows is F5
print('aaaaaa')
print("saad","Trainer","python")   #for seperation use comma ,

print("ssssssssssssssssssssssssssssssssssssssssssssssssssss\
sssssssssssssssss\
ssssssssssssss")    

print("today is my \n second class\n of the python\n and i am learing\n about print function")

print("karachi","lahore","Islamabad")

print('Karachi \nLahore \nIslamabad' )

#input function always represent with input()
#vaiable is a box where you store data inside it

# name = input("whats your name:")
# print("hello",name)
# print(name)

box = "python"
box1 = "html"
box2 = "java"
box3 = "javascript"
box4 = "php"
box5 = "python"

print(box,box1,box2,box3,box4,box5)
print("programing language is:",box)
print(box1 + box)   #concatenate it mean join one line to another
#multiline variables
a,b,c = 'A','B','C'

print(a,b,c)

#always initialized variable with alphabet or underscore 
_s = "saad"

print(_s)

# = sign asign the value  == sign is comparision operator 
food = input("do you like fruit?")

if food == "yes":
    print("great! good for health")
elif food == "no":
    print("that sad i've something for you")
else:
    print("select yes/no")


#Python String literal

# in single quote
s = 'python by khan'
 
# in double quotes
t = "python by khan"
 
# multi-line String
m = '''python 
           by 
               khan'''
 
print(s)
print(t)
print(m)


#format method print

print('I love {} by "{}!"'.format('python', 'khan'))
print('programming language {}'.format('Java'))
 
# # using format() method and referring a position of the object
print('{0} and {1}'.format('python', 'Java'))
 
print('{1} and {0}'.format('python', 'Java'))
 
print(f"I love {'python'} for \"{'Java'}!\"")
 
# # using format() method and referring a position of the object
print(f"{'python'} and {'java'}")




