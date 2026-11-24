# number = int("abc")
# print(number)

# try:
#     number = int("abc")
# except ValueError:
#     print("Invalid Number")
    
    
### We can store exception object using as
try:
    number = int("abc")
except ValueError as error:
    print(error)