#list
#start with [] and seperations of elements are with comma

print(["hello","apple","orange","banana"])
list1 = ["hello","apple","orange","banana"]
print(list1)
print(type(list1))



list2 = [22,33,44,77,88,99]
print(*list2)
print(type(list2))
print(list2, sep=" ")

list3 = ["string","integer","boolean","float",22,3.5,True]

print(list3)
print(type(list3))
print(len(list3))

print(list3[-2])

#slicing
print(list3[1:5])    #print(variable[starting Index : ending index but it will not include end value])

print(list3[::-1])   #reverse your sequence 

a = "string"

print(a[::-1])

print(a[2:6])




list3.append("python")    #add by default in last value
print(list3)
list3.pop()
print(list3)
list3.extend([1,2,3])
print(list3)
list3.index()

age = [19,26,22]

print(age)

print(type(age))
print(len(age))

#how can i print 26 from  age list

print(age[1])
print(age[-2])

language = ["Python","C++","Java"]
print(language)
print(len(language))
print(type(language))
print(language[-1])
print(language[0])

numbers = [22,31,54,12]
print("Before Append",numbers)
#to add method is called append
#varriable dot method
numbers.append(42)
numbers.append(65)
print("After Append",numbers)

#pop method use to delete element

numbers.pop(-2)       # in pop method inside bracket you have to define index  number
print("after pop",numbers)

#Extend to add all the items at the end of the lis
num = [1,3,4]

even_number = [4,6,8]

num.extend(even_number)

print("List after extend", num)

#insert    # insert any where in the list                    
num.insert(2,20)
print("updated insert", num)


#modify the element  list is mutable means editable datatype
#you can replace element by index with the help of = operator 
#change list items
num[1] = 99
print("change",num)


#delete any element by index
del num[1]
print("After delete",num)

#remove define direct value
num.remove(20)
print("After remove",num)


for x in list3:
    print(x)



#create any data list apply slicing , print individual value ,print middle values, append value and pop any value , apply len and check datatype , reverse print and apply iteration that is loop
