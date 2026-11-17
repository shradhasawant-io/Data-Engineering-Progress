# string = "I am an intern at Kodvix."

# print("hello" in string)

# if "I am an intern at Kodvix." == string:
#     print("yayyy is not present")
# else:
#     print("yayyy is present")


# student = ("Payal", 22, "Jaava")

# name, *age = student
# print(name, age) #Payal [22, 'Jaava']

# print(student) #('Payal', 22, 'Jaava')

# print(list(student)) #['Payal', 22, 'Jaava']

# #variable practice
# #ques1:
# name, age, city, course, percentage = "Payal", 22, "Indore", "Python", "73%"
# print(name, age, city, course, percentage)

# #ques2:
# val1=23
# val2=34

# print(val1, val2)

# val1=23+val2
# val2=val1-val2
# val1=val1-val2
# print(val1, val2)

# #ques3:
# a = b = c = 10
# print(a, b, c)

# #ques4:
# p = 2
# print(type(p))
# p = "Shraddha"
# print(type(p))


# #ques5:
# course = ("Python", 3, "Beginner")
# language, level, course_type = course

# print(language, level, course_type, sep="@")



# age = input("Hey! Enter your age: ")
# print(type(age))
# if int(age) >= 18:
#     print("Eligible to vote", end="!!!")
# else:
#     print("Not-eligible to vote")


# # print(f"My name is {namee : "raam"} and I am {agee = 23} years old")

# nameee, ageee = input("Enter name and age:").split()

# print(nameee, ageee)



#Input/Output practice questions:

#ques1:
# username = input("Enter your good name: ")
# print(f"Hey {username}, welcome to learn python in our community!!")

#ques2:
# name, age, city = input("Enter your name, age and city: ").split()
# print(name, age, city)

#ques3:
# a, b = input("Enter two numbers:").split()
# print(a, b)

# #ques4:
# print("Python", "Java", "C++", sep="|")

# # ques5:
# print("Hello", end=" ")
# print("Heyyy")

#ques 6:
# a = 4
# b = 3
# print(f"Product = {a*b}")

# #ques7:
# fname, lname = input("ENter your full name: ").split()
# print(fname, lname)

#ques8:
# price = 23.458789
# print(f"The price value is {price:.3f}")


# #typecasting practice questions:

# #q1:
# print(int("123"))
# print(type(int("123")))

# #q2:
# print(float("45.67"))
# print(type(float("45.67")))

# #q3:
# print(str(100))
# print(type(str(100)))

# #q4:
# print(int(True))
# print(int(False))

# #q5:
# print(int(99.99))

# #q6:
# print(list("Python"))

# #q7:
# print(set([1, 2, 2, 3, 3, 4]))

# #q8:
# print(bool(0)) #False
# print(bool("")) #False
# print(bool(" ")) #True
# print(bool([])) #False
# print(bool([0])) #True

# #q9:
# a, b = input("Enter two numbers:").split()
# print("Sum of two entered numbers is ", int(a)+int(b))

# #q10:
# age = input("Enter your age: ")
# print(type(age)) #<class 'str'>
# age = int(age)
# print(type(age)) #<class 'int'>

#q11:
#output should be :
#30.5
#<class 'float'>

#q12. Why does int("12.5") fail but int(float("12.5")) work?

# ans: because 12.5 is a float value so we should first convert it to 
# float then convert the produced float output to integer. 
# i think direct conversion is not possible. 


#Comparison operators practice questions:

# # q1:
# a = 23
# b = 45
# print(a == b) #False

# #q2:
# x = 300
# print(x > 100)

# #q3:
# x = 60
# if 50 >= x <= 100:
#     print(x, "Yes")
# else:
#     print(x, "No")
# #this is giving output as No, why?? 60 is in between 50 and 100, still it is printing No, why?

# #q4:
# a = "qwerty"
# b = "qwerty"
# print(a == b) #True
# print(a is b) #True 

# #q5:

# age = input("Enter your age:")
# if int(age) >= 18:
#     print("YES")
# else:
#     print("NO")
    
# #q6:
# marks = input("Enter your marks:")
# if int(marks) >= 40:
#     print("Pass")
# else:
#     print("Fail")
    
# #q7:
# #output should be: 
# #True
# #False
# #True
# #False

# #q8: Find the difference between = and ==

# # = is an assignment operator which is used when we want to store the values into some variable
# # == is comparison operator which is used to compare the values of two variables or objects

# #q9:
# num = input("Enter a number:")
# if int(num) >= 100 and int(num) <= 500:
#     print("YES")
# else:
#     print("NO")
    
#q10: Explain why 10 == 10.0 is true but 10 > "10" raises an error.

# 10 == 10.0 is true because i think python

num = input("enter a num: ") 
num = int(num) 
# print(num)

# print(f"value of num is {num}".format(num))
l = [1,2,3]
print(list())
print(type(l[0])) 


