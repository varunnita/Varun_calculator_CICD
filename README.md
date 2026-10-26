a = [[1, 2], [3, 4]]
b = a.copy()

b[0].append(99)

print(a)   # [[1, 2, 99], [3, 4]]   <- a changed too!
