#loop
#for loop
#while loop


#for loop checks for specific conditions than repeatedly executes a block of code as long as those condition met
#for loop check for last item

# for variable in <collection>:
#  loop body 

str = "looping"

for item in str :    #item variable, str is sequence this for loop will iterate the data
    print(item)  

print(str[1])

#Q1) what is the purpose of for loop
#A) a for loop in python is used to iterrate over sequence of items such as list, string or range
# and perform set of action on each items in sequence 

#Q2) how to you create  a for loop that prints number from 1 to 5?
#A) you can use rangge function and for loop

for num in range(1,6):
    print(num)

my_string = "Hello"

for char in my_string:
    print(char)

c = list(range(1,5))   #ending point is not included
print(c)

for i in range (1,5):
    print(i)

total2 = 0
for a in range(1,6):
    total2 = total2 + a     #a = 1 + 2 +3 +4 +5
    # total2 += a
    print(total2)

#numeric range 

for b in range(10):  #collection of numbers from 0 to 9
    print(b)

for e in range(10): #number from 0 - 9
    if e % 2 == 0: # is divisible by 2 (even)
        print(e) #printing

#looping with list

names = ["Bill Gates","Steve Jobs","Mark Zukerbeg","Billie","Ball"]

print(type(names))
print(len(names))

# for name in names:
#     print(name)

for name in names:
    if "B" in name:
        print(name)

# #List comprehension

# namesWithB = []
# for name in names:
#     if "B" in name:
#         namesWithB.append(name) # add this element to this array
    
#newlist= [expression for loop variable in list(if condition)]

nameWithB = [name for name in names if "B" in name]
print(nameWithB) 

# numbers = [i for i in range(10)]
# print(numbers)