a = [1, 2, 3]
b = a          # b points to the SAME list

b.append(99)
print(a)       # [1, 2, 3, 99]
print(b)       # [1, 2, 3, 99]
print(a is b)  # True
