a = [1, 2, 3]
b = a
a[1] = 4

print(id(a))

print(id(b))

print(a is b)