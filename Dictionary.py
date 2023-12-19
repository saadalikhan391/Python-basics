# dictionary in python a look-up table where you find key against key you will get value, immutable key mean not changeable but values are mutable 


#look up table
# key     |     value
# 11      |     "Umair"
# 22      |     "zaid"
# 33      |     "Anas"

# dict {key:value,key:value}   dictionary represent with curly bracket 

print({11:"Umair",22:"zaid",33:"Anas"})

dic =  {11:"Umair",22:"zaid",33:"Anas"}

print(dic)
print(type(dic))
print(len(dic))

print(dic[22])


# print(d[33])
# print(d[11])
# print(len(d))

a = {"Umair": 11}
print(a)
print(a["Umair"])

country_capital = {
    "United States": "Washington D.C",
    "England" : "London",
    "Italy" : "Rome"
}

print(country_capital)
print(country_capital["United States"])





print(country_capital["Italy"])       # Value are mutable (changeable)

country_capital["England"] = "Lahore"

print(country_capital)

# add item
country_capital["Germany"] = "Berlin"
print(country_capital)

#delete item  with the help of key 
del country_capital["Italy"]

print(country_capital)

#remove all item 
#country_capital.clear()

#print(country_capital)

#in operator thay key exists or not

print('England' in country_capital)

#pop()     Remove the item with the specified key
#update() Add or change dictionary items
#clear()   Remove all items
#keys()   Return all the dictionary keys
#Values()     Return all the dictionary values
#get()      retrun the value of the specified key
#popitem()  Return the last inserted key and value as a tuple
#copy()    Return a copy of the dictionary


country_capital.pop("United States")
print(country_capital)