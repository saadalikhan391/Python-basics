username = "saadalikhan"
password = "pass123"

user = input("Username: ")
pas = input("Password: ")

if user != username and pas != password:
    print("Username and password Incorrect!")
elif user == username and pas != password:
    print("Password Incorrect! ")
elif user != username and pas == password:
    print("Username Incorrect! ")
else:
    print("Successful Login!")

import random

rand_num = random.randrange(333,6666)
print("OTP, ", rand_num)

OTP = int(input("Enter your OTP: "))

if OTP == rand_num:
    print("OTP confirmed! ")
    print("welcome back!")
else:
    print("Wrong OTP!")