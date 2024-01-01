import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print("i have just rolled 2 dice")
print("the number produced are",dice1,"and",dice2)

operation = input("enter add to add 2 number or enter sub to substact 2 numbers")

if operation == "add":
    answer = dice1 + dice2
    print(answer)
elif operation == "sub":
    answer = dice1 - dice2
    print(answer)
else:
    print("i don't understand!!!")