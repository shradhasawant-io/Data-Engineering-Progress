# l1 = [[1,2,3,4], [5,6,7,8]]
# l2 = l1.copy()
# print(l1)
# print(l2)

# l2[1][0] = 100
# print(l1)
# print(l2)

# l2.append([11,12,13])
# print(l1)
# print(l2)

#### Shallow copy
# l1 = [1,2,3,4]
# l2 = l1
# print(l1)
# print(l2)

# l2[1] = 100
# print(l1)
# print(l2)

#### Deep copy
# l1 = [1,2,3,4]
# l2 = l1.copy()
# print(l1)
# print(l2)

# l2[1] = 100
# print(l1)
# print(l2)

#### Shallow Copy in 2D List(Nested List)
# l1 = [[1,2,3,4],[5,6,7,8]]
# l2 = l1
# print(l1)
# print(l2)
# l2[0] = "c"
# l2[1][0] = 100
# print(l1)
# print(l2)
# print("Append")
# l2.append([11,12,13])
# print(l1)
# print(l2)

#### Deep Copy in 2D List(Nested List)
import copy
# l1 = [[1,2,3,4],[5,6,7,8]]
# l2 = copy.deepcopy(l1)
# print(l1)
# print(l2)
# l2[1][0] = 100
# print(l1)
# print(l2)
# l2.append([9,10,11])
# print(l1)
# print(l2)