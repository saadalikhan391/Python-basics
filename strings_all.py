print("string")

lastname = "khan"
firstname = "saad"

code_number = "0312"
number = "8417151"
#operator to join one string to another concatenate

print(firstname + lastname)

print(code_number + number)

#how can i print khan 10 times with the help * operator

print(lastname * 10)

#You can append to a string using += :
pharse = "saad"
pharse += " is teaching python"

print(pharse)

#function called type() tells you about datatype
type(pharse)
print(type(pharse))


#tell the difference between string and integer

var1 = 8
var2 = "8"



# print(var1 + var2) #this is not going to work because datatype is not same 

print(type(var1),type(var2))

#only the one way to add with eachother convert other datatype into same data type 
#function called to change 0r conversion datatpe is called explicit
#typecasting function is str(), int(), float(), bool(), etc
# print(var1,var2)


print(str(var1) + var2)

print("this is my number:" + str(var1))

print("Roger is " + str(8) + " years old") #Roger is 8 years old

print(''' python
      by
      khan''')


#methods of strings

st1 = "STRING"

print(st1.lower())

#count string alphabet with the help of len()

print(len(st1))

#The in operator lets you check if a string contains a substring

print("STR" in st1)


#calling character with the help of index number either its positive or negative

print(st1[0])
print(st1[1])
print(st1[2])
print(st1[-1])
print(st1[-2])

#slicing it provide you the range [index_number:item_number]

print(st1[1:3])
print(st1[2:6])
print(st1[1:])

print(st1[::-1]) #to reverse the items 