### Question: What happens when a user enters "hello" instead of a number? Handle the error.
# value = int(input("Enter any number = "))
# print(value)

try:
    age = int("hello")
    print("Age:",age)
except ValueError:
    print("Please enter a valid number.")