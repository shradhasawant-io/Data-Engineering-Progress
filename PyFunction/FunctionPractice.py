# ===============Parameter and Arguement=============== 
# def greet(name):
#     print("Hello", name)
# greet("Rishi")


# ===============Positional Arguement==================
# def hello(name, age):
#     print(f"My name is {name} and my age is {age}")
# hello('Shivani', 22)


# ================Return values========================
# def hello():
#     return 'Hello All'
# hello() #This will not print Hello All because we are calling the function but not printing its returned value.
# print(hello())


# ===============Function without return================
# def hello():
#     print('Hello All')
#     return 1

# result = hello()
# print(result)
# OUTPUT --------------> Hello All , 1
# def hello():
#     print('Hello All')

# result = hello()
# print(result)
# OUTPUT --------------> Hello All , None


# ===============Returning multiple values================
# def hello():
#     return 'Hello', 'All', 25
# print(hello())


# def calculate(a, b): 
#  total = a + b 
#  difference = a - b 
#  return total, difference 
# sum, diff = calculate(20,10)
# print(sum)
# print(diff)


# ===============Default Arguement==================
# def hello(name="Guest"):
#     print('Hello All', name)
# hello()
# hello('Aman')\\
    
def argsss(*args) : 
    print(args)

print(argsss(1,2))
# *args 
# *kwars 
