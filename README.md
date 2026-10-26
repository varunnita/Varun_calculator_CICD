import copy

a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)

b[0].append(99)

print(a)   # [[1, 2], [3, 4]]       <- safe
print(b)   # [[1, 2, 99], [3, 4]]
