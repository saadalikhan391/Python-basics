# Recursion solution

# find_factorial_ecusive(5)
# 5 * factorial(4)
# 5 * (4 * factorial(3))
# 5 * (4 *(3 * factorial(2)))
# 5 * (4 *(3 *(2 * factorial(1))))
# 5 * (4 *(3 *(2 * (1 * factorial(0)))))
# 5 * (4 *(3 *(2 * (1 * 1))))
# 5 * (4 *(3 *(2 * 1)))
# 5 * (4 *(3 * 2))
# 5 * (4 * 6)
# 5 * 24
# 120

def find_factorial_recusive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recusive(n -1)
    
print(find_factorial_recusive(5))




# Recursive function for Tower of Hanoi
def hanoi(disks, source, helper, destination):
    # Base Condition
    if (disks == 1):
        print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
        return

    # Recursive calls in which function calls itself
    hanoi(disks - 1, source, destination, helper)
    print('Disk {} moves from tower {} to tower {}.'.format(disks, source, destination))
    hanoi(disks - 1, helper, source, destination)

# Driver code
disks = int(input('Number of disks to be displaced: '))
'''
Tower names passed as arguments:
Source: A
Helper: B
Destination: C
'''
# Actual function call
hanoi(disks, 'A', 'B', 'C')

#3



# Explanation
# If you can imagine the disks in question as displayed in the image, you can understand how the code successfully displaces the three disks from tower A to C, following the expected rules. 

# Note how the variable disk initially takes the number of disks as the input and later is read or understood as the disk number in question inside the code.

# In the block of code, the first section is the base condition that that you apply when using disk 1. Once executed, it returns to the rest of the execution flow out of the if condition.

# The remaining disks are moved by passing the values from source to helper with destination as helper. The remaining disk is moved from source to destination. The remaining n-1 disks on the helper are moved from helper to destination with source as the helper.

# In the last section, the driver code takes the input for the number of disks I want to move. In accordance, I pass the values of A, B and C as the tower names and give the function call.

# You will notice that it took 2^3 - 1 = 7 steps to complete the transfer, which meets my expectations.

# The Tower of Hanoi and recursion, in general, can be confusing, even for an avid Python programmer. As such, the best way to understand recursion is by inserting the values and running a dry code using a pen and paper to see how the values change and which function gets called in the code at what point.


#String_name[startparameter:stopparameter:stepparameter] 
#The order of the parameters is always start, stop and step. The start and stopparameters are the indices between which the function manipulates the string. The stepparameter are the hops or jumps the function makes while it traverses a given string.  

def string_reverse(str):
    if len(str) == 0:
        return str
    else:
        return string_reverse(str[1:]) + str[0]
    
    
str = "reversal"
reverse = string_reverse(str)
print(reverse)