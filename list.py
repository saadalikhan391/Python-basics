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

for x in list3:
    print(x)


#create any data list apply slicing , print individual value ,print middle values, append value and pop any value , apply len and check datatype , reverse print and apply iteration that is loop
