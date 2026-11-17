# Sum up to n terms
n = int(input("Enter a number :- "))

sum = 0

for i in range(1,n+1):
    sum = sum + i
    
print(f"Your sum is {sum}")