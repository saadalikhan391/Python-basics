#TODO: create a basic class
class Book:
    def __init__(self,title):  #Init is one of python special function for working with class, Initializinf function
        self.title = title
#


#TODO: create instance of the class

book1 = Book("Brave New world")
book2 = Book("war and peace")


#TODO: print the class and property
print(book1)           #object
print(book1.title)     #title
print(book2.title)


