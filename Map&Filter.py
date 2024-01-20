menu =["expresso","mocha","latte","cappuccino","cortado","amercino"]

def  find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

map_coffee = map(find_coffee,menu)
print(map_coffee)
for x in map_coffee:
    print(x)

# filter_coffee = filter(find_coffee,menu)
# print(filter_coffee)
# for x in filter_coffee:
#     print(x)


# Return a map object  == iterable
#syntax: map(function, Iterables)

#example 1
new_list = [10,20,30,40,50]

def addition(n):
    return n+2

my_list = map(addition,new_list)
print(my_list)

for item in my_list:
    print(item)


#example 2
def adding(x,y):
    return x+y

my_list =map(adding,('apple','watermelon'),('banana','fig'))
print(tuple(my_list))


#example 3

#function to square a number

def square(x):
    return x**2

#list of numbers
numbers=[1,2,3,4,5]

#Use map to square each number

squared_numbers =map(square,numbers)

#convert the result to a list and print
print(list(squared_numbers))


#Filter
#example 1 filtering even numbers from a list

#function to check if number is even
def is_even(x):
    return x % 2 == 0

#list of numbers
numbers = [1,2,3,4,5,6,7,8,9,10]

#use filter to get even numbers
even_numbers=filter(is_even,numbers)

#convert the result to the list and print
print(list(even_numbers))


#Example 2
#filtering name that start with A
#function to check if a name start with "A"
def start_with_a(name):
    return name[0].lower() == 'a'

#list of name
names = ['Ali','Babar','Chand','Daniel',"Anna","Alice"]

#use filter o et names starting with 'A'
a_name = filter(start_with_a, names)

#convert the result into list and print
print(list(a_name))