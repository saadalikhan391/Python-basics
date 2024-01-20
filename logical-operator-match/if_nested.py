http_status = 501
internet_down = 600

if http_status == 200 or http_status == 201:
    print("success")
elif http_status == 404:
    print("not found")
elif http_status == 400:
    print("bad request")
elif http_status == 500 or http_status == 501:
    print("server error")
elif http_status == 601 and internet_down == 600:
    print("nothing working")
else:
    print("unknown")


#syntax
#you can have if statements inside if statements, this is called nested if statement
#the syntax of the nested if elif else :

#if expression1:
#   statement(s)
#   if expression2:
#       statement(s)
#   elif expression3:
#       statement(s)
#   elif expression4:
#       statement(s)
#   else:
#       statement(s)
#else:
#   statement(s)


x = 19

if x > 10:
    print("above ten,")
    if x > 20:
        print("and also above 20")
    else:
        print('but not above 20.')

var = 100

if  var < 200:
    print("Expession value is less than 200")
    if var == 150:
        print("which is 150")
    elif var == 100:
        print("which is 100")
    elif var == 50:
        print("which is 50")
    elif var < 50:
        print("Expession value is less than 50")
else:
    print("could not find true  expression")

print("goodbye")
    
