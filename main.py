import numpy as np

# Zad 1

# a = np.arange(1, 4)
# b = np.array([4, 5, 6])
# print(a)
# print(b)
# c = a * b
# print(c)

# Zad 2

# a = np.arange(9).reshape(3, 3)
# b = np.arange(10,26).reshape(4, 4)
# print(a)
# print(b)
# print(a.min(axis=1))
# print(a.min(axis=0))
# print(b.min(axis=1))
# print(b.min(axis=0))

# Zad 3

# a = np.arange(1, 4)
# b = np.array([4, 5, 6])
# print(a)
# print(b)
# print(a.dot(b))
# print(np.dot(a, b))

# Zad 4

# a = np.arange(1, 4)
# b = np.array([np.pi, np.e, np.sqrt(2)])
# print(np.dot(a, b))

# Zad 5

# x = np.arange(1, 7).reshape(2, 3)
# print(x)
# a = np.sin(x)
# print(a)

# Zad 6

# y = np.arange(1, 7).reshape(2, 3)
# b = np.cos(y)
# print(b)

# Zad 7

# print(np.add(a, b))

# Zad 8

# a = np.arange(9).reshape(3,3)
# print(a)
# for b in a:
#     print(b)
#     print("")

# Zad 9

# a = np.arange(9).reshape(3,3)
# print(a)
# for b in a.flat:
#     print(b)

# Zad 10

# a = np.arange(81).reshape(9, 9)
# print(a)
# print(a.reshape(1, 81))
# print(a.reshape(81, 1))
# print(a.reshape(3, 27))
# print(a.reshape(27, 3))
#
# # oba parametry macierzy musza byc dzielnikami liczby skladnikow macierzy, stad tylko takie opcje

# Zad 11

# a = np.arange(12).reshape(3,4)
# print(a)
# b = np.arange(12).reshape(4,3)
# print(b)
# c = np.arange(12).reshape(2,6)
# print(c)
# print(a.ravel())
# print(b.ravel())
# print(c.ravel())