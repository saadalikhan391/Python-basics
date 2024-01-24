#TODO: create a basic class
class Book:
    #the init function is called when the instance is created and ready to be initialized
    def __init__(self,title,author,pages,price):  
        self.title = title
        #TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price 
    #TODO:create instance methods
    def getprice(self):
        if hasattr(self,"_discount"):     #hasattr is buit in function in python  check to see if an attribute exists 
            return self.price - (self.price*self._discount)
        else:
            return self.price
    def setdiscount(self,amount):      
        self._discount = amount     #its a hint for developer  that this attribute is considered internal to the class and is not for basic consumption



#TODO: create some book instance
b1 = Book("war and peace","khan",1225,39.95)
b2 = Book("the catcher","JD",234,29.95)



#TODO: print the price of book1
print(b1.getprice())
print(b1.pages)
print(b1.author)
print(b1.title)
print(b1.price)

#TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())