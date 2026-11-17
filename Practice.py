#  ================================TYPES OF VARIABLES===================================
# sher = "Harsh Bhaiya"

# SheryiansSchool = "Harsh Bhaiya" #Pascal case
# sheryiansSchool = "Harsh Bhaiya" #Camel case
# sheryians_school = "Harsh Bhaiya" #Snake case

# a = -12
# print(type(a))

# b = 12.3
# print(type(b))

# c = 12/3
# print(type(c)) #Float

# d = 32j
# print(type(d)) #Complex

# st = 'uhwh 12344 @#$%^&'
# print(type(st)) #String

# e = True
# print(type(e)) #Boolean

# f = "A"
# print(ord(f)) #To see unicode of A = 65

# # =====================STRING INDEXING===========================
# g = "Hello"
# # print(g[-1],g[5]) # Gives Error
# print(g[-1],g[3])

#  =============================STRING SLICING=======================
# h = "Hello All"
# print(h[0:4:1]) #Hell
# print(h[0:5:1]) #Hello
# print(h[0::]) #Hello All
# print(h[::]) #Hello All

# =========================TYPE CONVERTION========================
# a = 12
# a = str(a)
# a = "dgs"
# a = int(a) 
# print(type(a))

# a = "12"
# a = int(a)
# print(type(a))

# a = "abc"
# a = int(a)
# print(type(a))

# a = 12
# print(bool(a)) #True

# a = "12"
# print(bool(a)) #True

# a = "hello"
# print(bool(a)) #True

# a = ""
# print(bool(a)) #False

# a
# print(bool(a)) #True

# a = "#$$%^"
# print(bool(a)) #True

# a = 0
# print(bool(a)) #False

# print(12/3) #4.0 ----> Implicit Conversion ----> Python automatically converts division into float

# name = "Shweta"
# age = 23
# print("Shweta",age)
# print(name,age)
# print(name,23)
# print("Hello my name is",name,". I'm",age,"years old.")
# print(f"Hello, My name is {name} and my age is {age}") #Fomatted String

# age = input("Enter your age = ")
# print(age)

# =================== ARITHMETIC OPERATORS ========================
# a = 5
# b = 2
# print(a+b) #25
# print(a-b) #-15
# print(a*b) #100
# print(a%b) #5
# print(a/b) #0.25
# print(b/a) #4.0
# print(b//a) #4
# print(a**b) #25 ----> Power Operation
# print(5**100) #7888609052210118054117285652827862296732064351090230047702789306640625
# print(32%5) #Gives Remainder -----> 2
# print(12+4/2) #14.0 -----> Follows BODMAS

# =================== ASSIGNMENT OPERATORS ========================
# a = 20

# =================== COMPOUND ASSIGNMENT OPERATIONS ==================
# a = 20
# a = 40 # Value Reassign
# print(a)

# a = 20
# a = a + 20
# a = a + 40
# a = a + 60
# print(a)

# Compound Assignment Operator
# a = 20
# a += 20
# a += 40
# a += 60 # 140
# a -= 10 # 10
# a /= 10 #2.0
# a *= 10 #200
# a //= 10 #2
# a **= 10 #10240000000000
# print(a)

# =================== COMPARISON OPERATOR ==================
# a = 12.1
# b = 12
# print(a>b) #TRUE
# print(a<b) #FALSE
# print(a<=b) #FALSE
# print(23<=23) #TRUE
# print(a>=b) #TRUE
# print(23>=23) #TRUE
# print(23<23) #FALSE

# ========== comparing strings =============
# print(ord("A")) #65
# print(ord("B")) #66
# print("A" > "B") #FALSE 
# print("ABC" > "BCD") #FALSE
# print("ABC" > "ACD") #FALSE
# print("A" < "66") #FALSE
# print("A" > 34) #TYPE ERROR

# =================== BITWISE OPERATOR ==================
# print(123 > 100, 34 == 34) #True True
# print(123 > 100 and 34 == 34 and 45 < 90 and 12 > 20) #FALSE
# print(12 != 12 or 23 == 45 or 67 == 56 or 10 > 5) #TRUE
# print(not 12 == 12) #FALSE

# ================== CONDITIONAL STATEMENT ====================
# a = 6
# if a > 10:
#     print("I'll do task A")
    
# else:
#     print("I'll do task B")

# money = int(input("Please provide me the money :- "))
# if money == 10:
#     print("I'll have a mini ice cream")
    
# elif money == 20:
#     print("I'll have a chocolate ice cream")
    
# else:
#     print("I'll have a cone ice cream")

# ==================QUESTIONS ON CONDITIONAL====================
# Q1: ========================================
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))

# if num1 > num2:
#     print(f"{num1} is greater than {num2}")
    
# elif num2 > num1:
#     print(f"{num2} is greater than {num1}")
    
# else:
#     print("Both the numbers are same")


# Q2: =====================================
# gen = input("Please tell your gender as character (M or F) : ")
# if gen == "M" or gen == 'm':
#     print("Good Morning Sir")
    
# elif gen == "F" or gen == 'f':
#     print("Good Morning Ma'am")
    
# else:
#     print("Unidentified Gender")


#Q3: ==========================================
# num = int(input("Enter a number : "))

# if num%2 == 0:
#     print("It is an even number")
    
# else:
#     print("It is an odd number")


# Q4: ===========================================
# name = input("Enter your name : ")
# age = int(input("Enter your age : "))

# if age >= 18:
#     print(f"Hello {name} you are a valid voter")
    
# else:
#     print(f"Hello {name} you are not a valid voter")
#     age2 = 18 - age
#     print(f"You will be eligible after {age2} years")


# Q5:
# A leap year is a year that is divisible by 4
# Check century by diving the year with 100 
# year = int(input("Enter your year : "))
# if year%100 == 0 and year%400 == 0:
#     print("It is a leap year")
# elif year%100 != 0 and year%4 == 0:
#     print("It is a leap year")
# else:
#     print("It is a normal year")


# Q6:
# t = int(input("Enter the temperature : "))
# if t < 0:
#     print("Freezing Cold")
# elif t >= 0 and t < 10:
#     print("Very Cold")
# elif t >= 10 and t < 20:
#     print("Cold")
# elif t >= 20 and t < 30:
#     print("Plesent")
# elif t >= 30 and t < 40:
#     print("Hot")
# else:
#     print("Temperature is very hot")