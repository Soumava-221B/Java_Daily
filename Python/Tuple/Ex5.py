# Write a Python program to add an item to a tuple.

tuplex = (4,6,2,8,3,1)
print(tuplex)
tuplex = tuplex + (9,)
print(tuplex)
listx = list(tuplex)
listx.append(30)
tuplex = tuple(listx)
print(tuplex)