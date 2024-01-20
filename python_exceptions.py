def divid_by(a,b):
    return a / b

# print(divid_by(40,0))

try:
     ans= divid_by(40, 0)
# except:
#      print("something went wrong! with code ask learn with khan to fix!!!")
# except Exception as e:
#      print("something went wrong! with code ask learn with khan to fix!!!",e)
#      print(e.__class__)

except ZeroDivisionError as e:
    print(e,"we cannot divide by zero contact learn with khan page to solve")
except Exception as e:
    print(e, "something went wrong")



# # IndexError
items = [1,2,3,4,5]
# item = items[6]
# print(item)

try:
     item = items[6]
     print(item)
except: 
     print("The index does not exist in the list.")

# #ZeroDivisionError
# def divide_by(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 0
#     except Exception as e:
#         print(e, 'Something went wrong!')

# ans = divide_by(10,0)
# print(ans)


# #FileNotFoundError

try:
     with open('file_does_not_exist.txt', 'r') as file:
         print(file.read())
except:
     print("Unable to locate file")  