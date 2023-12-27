
#while loop repeats a specific block for unknown number of time until condition is met
#while loop is based upon condition being true once  the condition is no longer true the loop will stop

# while <conditions>:
#     <loop body>
# else:
#     <code block> will run when loop halts

# num = 1

# while num <= 10:
#     print(num)
#     num +=1

#Q2) how do you create a for loop that prints  numbers from 1 to 5?
num = 1

while num <= 5:
    print(num)
    # num = num + 1
    num +=1


# #while loop

n = 0

while n < 10: #while n is less than 10
    print(n)   #print out the value of n
    # n = n + 1
    n += 1

# numbers = [0,5,10,6,3]

# length = len(numbers) # get length of array
# n = 0

# while n < length: #loop condition
#     print(numbers[n])
#     n = n + 1
    

# program to calculate the sum of numbers
# until the user enters zero

total = 0

number = int(input('Enter a number: '))

# add numbers until number is zero
while number != 0:
    total += number    # total = total + number
    
    # take integer input again
    number = int(input('Enter a number: '))
    

print('total =', total)



# Infinite while Loop in Python
# If the condition of a loop is always True, the loop runs for infinite times (until the memory is full). For example

age = 32

# the test condition is always True
while age > 18:
    print('You can vote')


# Python While loop with else
# In Python, a while loop may have an optional else block.

# Here, the else part is executed after the condition of the loop evaluates to False.

counter = 0

while counter < 3:
    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')

# Note: The else block will not execute if the while loop is terminated by a break statement.
counter = 0

while counter < 3:
    # loop ends because of break
    # the else part is not executed 
    if counter == 1:
        break

    print('Inside loop')
    counter = counter + 1
else:
    print('Inside else')



# Python for Vs while loops
# The for loop is usually used when the number of iterations is known. For example,

# this loop is iterated 4 times (0 to 3)
for i in range(4):
    print(i)


# The while loop is usually used when the number of iterations is unknown. For example,

# while condition:
    # run code until the condition evaluates to False