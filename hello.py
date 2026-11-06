"""
number = int(input("write number: "))
rest = number % 2
if rest >= 1:
    print("odd")
else:
    print("even")
"""


"""
number = int(input("write number: "))
if number > 0:
    print("positive")
elif number < 0:
    print("negative")
else:
    print("zero")
"""

"""
number1 = int(input("write number 1: "))
number2 = int(input("write number 2: "))
x = number1
y = number2
if x > y:
    print("x is bigger")
elif x < y:
    print("y is bigger")
else:
    print("equal")
"""

"""
x = int(input("Age: "))
if x < 6:
    print("free")
elif x >= 18:
    print("adult")
else:
    print("child")
"""


"""
for i in range(3):
    print(i)
"""

"""
for i in range(1, 4):
    print(i)
"""

"""
total = 0
for i in range(1, 4):
    total = total + i
print(total)
"""

"""
n = int(input("add number: "))
total = 0
for i in range(1, n + 1):
    total = total + i
print(total)
"""


"""
for x in range(1, 6):
    print(x)
"""


"""
x = 0
for y in range(1, 6):
    x = x + y
print(x)
"""


"""
x = int(input("add number: "))
remainder = x % 3
print(remainder)
"""


"""
x = int(input("add number"))
if x > 100:
    print("big")
else:
    print("small")
"""


"""
x = 17 // 5
print(x)
"""


"""
x = int(input("add number: "))
y = x * x
print(y)
"""


"""
x = int(input("add number: "))
z = 0
if x >= 20:
    print("too big")
else:
    for y in range(1, x + 1):
        z = z + y
    print(z)
"""


"""
x = int(input("add number 1: "))
y = int(input("add number 2: "))
if x > y:
    print(x)
else:
    print(y)
"""



x = int(input("add number: "))
y = 0
for x in range (0, x + 1):
    y = x // 2
    print(y)