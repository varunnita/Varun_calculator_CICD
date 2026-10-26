python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
Way 1: + (makes a new list)
python
result = list1 + list2
print(result)   # [1, 2, 3, 4, 5, 6]
print(list1)    # [1, 2, 3]   <- original untouched
Way 2: extend() (adds into the existing list)
python
list1.extend(list2)
print(list1)    # [1, 2, 3, 4, 5, 6]   <- list1 itself changed
Way 3: * unpacking (new list, handy for many lists)
python
result = [*list1, *list2]
print(result)   # [1, 2, 3, 4, 5, 6]
