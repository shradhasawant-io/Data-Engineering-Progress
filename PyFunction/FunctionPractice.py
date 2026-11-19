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
# hello('Aman')
    
# def argsss(*args) : 
#     print(args)

# print(argsss(1,2))
# *args 
# *kwars 

# ===============Keyword Arguement=====================
# def hello(name,age,address):
#     print(f"My name is {name}, i'm {age} years old and i live in {address}")
# hello(address='Indore', name='Shivam', age=16)

# =============== *args =====================
# def add(*nums):
#     total = 0
#     for i in nums:
#         total += i
#     return total

# print(add(12,23))
# print(add(54,77,100,19,272))

# =============== *args =====================
# def show_profile(**details): 
#     for key, value in details.items(): 
#         print(key, value)
        
# show_profile(name="Aman", age=21, 
# course="Python")