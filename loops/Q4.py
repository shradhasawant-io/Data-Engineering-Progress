# Take a number as input and print its table
# n = int(input("Enter a number :- "))

# for i in range(n,(n*10)+1,n):
#     print(i)

# ====================== OR ============================
n = int(input("Which table you want :- "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
