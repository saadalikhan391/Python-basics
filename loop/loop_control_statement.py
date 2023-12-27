# loop control statements
#Break  : terminates the loop if specific condition is met
#continue :skips one iteration of the loop if specified condition is met
# and continue with the next iteration
#pass: when you don't want any command or code to execute

#break

names =["Bill Gates","Steve Jobs","Mark Zukerberg","Billie","Ball"]

for name in names:
    if name == "Mark Zukerberg" :
        print("loop exit here.")
        break     #end this loop if condition is true
    print(name)

# continue
for name in names:
    if name == "Mark Zukerberg":
        print("Skipping this iteration.")
        continue  #skip iteration if true
    print(name)

# pass
for name in names:
    if name == "Mark Zukerberg":
        print("just passing by...")
        pass # move on with this iteration
    print(name)

#else clause
# for 'for' loops

# for i in <collection>:
#     <loop body>
# else:
#     <code block> will run loop halts

# while <conditions>:
#     <loop body>
# else:
#     <code block> will run when loop halts

# print("Else won't run here.")

# for name in names:
#     if name == "Mark Zukerberg":
#         print("loop halted due to break")
#         break #halt this loop
#     print(name)
# else: #this won't work because 'break' was used
#     print("loop has finished")

# print("/n Else statement will run here")
# for name in names:
#     print(name)
# else:   # will work because of no 'break' statement
#     print("second loop has finished")



fruits_vegetables = ['apple', 'banana', 'carrot', 'kiwi', 'broccoli', 'orange', 'cucumber', 'grape', 'spinach']

for item in fruits_vegetables:

    if item == 'carrot':
        break
    print(item)

    if item == 'broccoli':
        continue
    print(item)

    if item == 'kiwi':
        pass
    print(item)

else:
    print(item)
