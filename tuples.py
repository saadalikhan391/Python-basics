a = "saad"
b = "khan"

print(a + b)    #concatenation

list = ['USA',"Pakistan","UAE",2,4,5.5,True]      #it always inside the square bracket that is list mutable

List2 = ['Ireland','India']

print(list[::-1])  # reverse list
print(list)

list[0] = 'Palistine'
print(list[0])  
print(list)

print(list + List2)   #concatenation one line add with other line called concatenation

print(type(list))
print(type(a))


#Tuples imutable value inside tuples can't be modify and change for practice use circle bracket but it is optional 

tuple = ("ab","azz",11,2.4,True)

tuple1 = "ax", 12, 5.6
print(tuple)
print(tuple1)
print(type(tuple))

print(tuple[1])

print(tuple + tuple1)      #concatenation one line add with other line called concatenation

print(type(tuple1))

#different typews of tuples
#Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple haing integer

int_tuple = (1,2,3)
print(int_tuple)

#tuple with mixed datatype

mix_tuple =  (1,"hello",True,8.7)

print(mix_tuple)

var1 = ("hello")  #strings

var2 = ("hello",)  # tuple

# var2[0] = 'saad'


print(type(var1))
print(type(var2))

print(var1*4)     #Repetition
print(list*4)
print(mix_tuple*4)