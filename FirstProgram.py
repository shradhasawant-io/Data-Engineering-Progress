from math import *
'''
print("Hello World")

print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "John"
# character_name = 'John'
print(type(character_name))


# print(type(character_name))
character_age = 35
isMale = True
print("There once a man named " + character_name + ",")
print("he was " + str(character_age) + " years old")
print("he was",character_age,"years old")


phrase = "Hello"
print(phrase + " All")
print(phrase.lower())
print(phrase.upper())


def function_yes() : 
    print("Yes")
    return "Hello"
    
print(function_yes())


print("============== String Practice ================")
# phrase = ["Hello", "Everyone"]
phrase = "Hello Everyone"

# print(phrase.upper().isupper())
# print(phrase.islower())
# print(len(phrase))
# print(phrase[1])
# print(phrase.index("l"))
# print(phrase.index("Everyone"))
# print(phrase+ "!!")
# print(phrase.index("q"))


print(phrase.replace("Hello", "Hiii"))


print("============== Working With Numbers ================")
print(2)
print(2.555)
print(10%3)

my_num = 9
print(str(my_num))
print("My number is " + str(my_num))

my_num = -1
print(abs(my_num))
print(pow(3,2))
print("Maximum = "+ str(max(4,6)))
print("Minimum = "+ str(min(4,6)))
print(round(3.256))
'''

# Multi-line comment
'''
shhsgsgshgshgsh
ddgagddsfs
dfdshfdsjh
dfhdsjhf

'''

# print("Hello\nAll")
# print("Hello\All")
# print("Hello\"All")

# print('''
    #   sshhdjsd
    #   dsdhsdsjd
    #   akja       ksisj              jkjk
    #   ''')

'''
print()
print(floor(3.2))
print(ceil(3.2))
print(sqrt(36))

name = input("Enter your name: ")
age = input("Enter your age: Sh")
print("Hello " + name + "! Your age is " + age)
'''

'''
print("============== Building a Basic Calculator ================")
#output = 12 not 3, because python will think it is a string not a number
num1 = input("Enter first number: ")
print(type(num1))

num2 = input("Enter second number: ")
print(type(num2))

# result = num1 + num2
# print("Answer = "+result)

ans = int(num1) + int(num2)
print(type(ans))

v = "Answerr = "+str(ans)
print(type(v)) #str

v = "Answerr = ",str(ans)
print(type(v)) #tuple
print(v[1])
print(type(v[1]))

# v = "Answerr = ",ans
# print(type(v)) #tuple



print(v[1])
'''
a='''
phrase = "Hello"


fun = lambda x : 1  
print(fun)  
    
print(phrase.lower)
print(phrase.lower)
print(phrase.lower)
print(phrase.lower)
print(phrase.upper)
'''

'''
phrase = "Hello Everyone@#$5^&)}]:;,<_-+="
print(len(phrase))
'''

phrase = "Hello Everyone"
# print(phrase[1])
# print(phrase.index("l"))
# print(phrase.index("Everyone"))
# print(phrase,"!!")
# print(phrase.index("q"))
# print(phrase.capitalize()) #Hello everyone
# print(phrase.casefold()) #hello everyone
# print(phrase.center(16)) # _HELLO Everyone_ 

# phrase = "Hello Everyone"
# print(phrase.count("e",-1,-3))

phrase = "Hello Everyone"

# Starts at -1 (index 13) and stops before -6 (index 8)
# Converted, this is equivalent to phrase.count("o", 13, 8)
# print(phrase.count("o", -6, -1)) 
# Output: 0
# print(phrase.encode("UTF-8"))
# print(phrase.encode("ASCII"))
# print(phrase.encode("UTF-16"))
# print(phrase.encode("UTF-32"))
# print(phrase.endswith("E", 1, 7))
# print(phrase.expandtabs(3))
# print(phrase.find("Every")) ---> 6


# print("My name is {name} and my age is {age}".format(name="Shraddha", age=23))

# name = "Shraddha"
# age = 23

# print("My age is {1} and my name is {0}".format(name, age))
# print("{0} {0} {1}".format("Hello", "Python")) #Hello Hello Python

# message = "My name is {} and my age is {}".format(name, age)
# print(message)
 
# print(phrase.isalnum()) #for string Hello0Everyone output is True
# print(phrase.isalpha())
# print(phrase.isascii())
value1=16.89
value="567"
value2=56
print(value.isdecimal())
print(type(value))
print(type(value1))
print(type(value2))

print(phrase[3:9])

print(phrase[-8: -3])
print(phrase[:8])
print(phrase[2:])

print("abc"*2)
print(True+False)
print(True*2)
print(True+34)

# print("abc"*"cba")
print("abc")
print(type(type(True)))
# print("asd"-56)
print(True/67894539)

print("hello python".title())
print("  hello python  ".strip())
print(int(False))
print("Hello python".startswith("ello"))
print("programming".index("g"))
print("programming".count("m"))
print(len("programming"))