# Example 1: Combining two lists
# l1 = [1,2,3,4]
# l2 = ['a','b','c','d']
# l = list(zip(l1,l2))
# print(l)


# Example 2: zip() with three lists
# l1 = [1,2,3,4]
# l2 = ['a','b','c','d']
# l3 = [11,12,13,14]

# result = list(zip(l1,l2,l3))

# print(result)


# Example 3: lists with different lengths
# a = [10, 20, 30, 40]
# b = ["A", "B"]
# print(list(zip(a, b)))


# Example 4: Using zip() in a for loop
# l1 = ["Rahul", "Preeti", "Amit"]
# marks = [85, 90, 78]

# for i, j in zip(l1, marks):
#     # print(i,j)
#     result = [i,j]
#     print(result)


# Example 4: Using zip() in a for loop and printing result in same list
# l1 = ["Rahul", "Preeti", "Amit"]
# marks = [85, 90, 78]

# result = [[i,j] for i,j in zip(l1,marks)]
# print(result)

