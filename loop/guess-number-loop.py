import random

num1 = random.randint(1,5)
num2 = random.randint(1,5)
print(num2,num1)

guess = int(input("Enter the first number randomly generated"))

while guess != num1:
    print("your guess is wrong")
    guess = int(input("Enter the first number randomly generated"))

guess2 = int(input("Enter the second number randomly generated"))

while guess2 != num2:
    print("your guess is wrong")
    guess2 = int(input("Enter the second number randomly generated"))

print("good you guessed both number correctly")
