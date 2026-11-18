#Example 1 - Without enumerate()
# list = ['a', 'b', 'c', 'd']
# index = 0
# for i in list:
#     print(index,i)
#     index += 1


# Example 2: Using enumerate()
# list = ['a', 'b', 'c', 'd']
# for index,i in enumerate(list):
#     print(index,i)


# Example 3: enumerate() with start - used to start indexing from 1 in instead of 0(Default)
# list = ['a', 'b', 'c', 'd']
# for index,i in enumerate(list, start = 1):
#     print(index,i)

# Example 4: enumerate() with a string
# word = 'Python'
# for s,i in enumerate(word):
#     print(s,i)