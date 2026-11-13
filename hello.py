"""
print("hello")
"""


"""
print("x")
print("y")
"""


"""
print(15 + 27)
print(6 * 7)
"""


"""
print("8 + 1")
print(8 + 1)
print("8" + "1")
"""


"""
x = 5
print(x)
print("x")
"""


"""
x = 4
y = 6
print(x * y)
print(x + y)
"""


"""
x = 2
y = 7
x = 10
print(x)
print(y)
"""


"""
x = 3
x = x * 2
x = x + 4
print(x)
"""


"""
x = "ab"
y = "cd"
print(x + y)
print(x)
"""


"""
print("5" + 3)
"""


"""
print(3 + "5")
"""


"""
x = "5"
y = "3"
print(x + y)
print(int(x) + int(y))
"""


"""
x = input()
print(x + x)
"""


"""
x = int(input())
print(x + x)
"""


"""
x = int(input("Number: "))
print(x + x)
"""


"""
x = 7
y = 2
print("sum is", x + y)
"""


"""
x = 10
if x > 10:
    print("A")
elif x > 5:
    print("B")
else:
    print("C")
"""


"""
print(9 / 3)
print(9 / 2)
print(9 - 2)
"""


"""
print(9 // 2)
print(9 % 2)
print(10 // 5)
print(10 % 5)
"""


"""
print(3 ** 2)
print(2 + 3 ** 2)
print((2 + 3) ** 2)
print(10 - 2 * 3)
"""


"""
x = 4
print(x == 4)
print(x > 10)
print(x != 4)
"""


"""
x = 7
if x > 5:
    print("big")
print("done")
"""


"""
x = 9
if x > 5:
    print("big")
else:
    print("small")
print("done")
"""


"""
x = 10
if x > 8:
    print("high")
elif x > 3:
    print("middle")
else:
    print("low")
"""


"""
x = 7
print( x > 5 and x < 10)
print(x > 5 and x < 6)
print(x > 100 or x < 8)
"""


"""
x = 2
while x < 6:
    print(x)
    x = x + 2
print("end")
"""


"""
for i in range (4):
    print(i * 2)
print("end")
"""


"""
for i in range(1, 4):
    print(i * i)
print("end")
"""


"""
x = 0
for i in range(1, 5):
    x = x + i
print(x)
"""


"""
for i in range (1, 5):
    print("round", i)
    if i % 2 == 0:
        print(i)
print("end")
"""


"""
x = int(input("number: "))
for i in range(1, x + 1):
    if i % 2 == 0:
        print(i)
"""


"""
def hello():
    print("hi")

hello()
hello()
"""


"""
def hello():
    print("hi")

print("start")
hello()
print("end")
"""


"""
def show(x):
    print(x * 2)

show(5)
show(7)
"""


"""
def show(x):
    print(x + 1)

show(3)
show(10)
"""


"""
def double(x):
    return x * 2

print(double(5))
"""


"""
def add_one(x):
    return x + 1

y = add_one(4)
print(y)
print(add_one(10))
"""


"""
def triple(x):
    return x * 3
    
y = triple(4)
print(triple(4))
print(triple(10))
"""


"""
nums = [4, 7, 9]
print(nums)
print(nums[0])
"""


"""
nums = [4, 7, 9]
print(nums[1])
print(nums[2])
"""


"""
nums = [4, 7, 9]
for n in nums:
    print(n + 1)
"""


"""
nums = [2, 5, 8, 1]
for n in nums:
    print(n * 2)
print("end")
"""


"""
nums = [4, 7]
nums.append(9)
print(nums)
"""


"""
nums = []
for i in range(3):
    nums.append(i * 10)
print(nums)
"""


"""
nums = []
for i in range(1, 5):
    nums.append(i * i)
print(nums)
"""


"""
nums = [4, 7, 9]
print(len(nums))
"""


"""
nums = [5, 8, 2, 6, 1]
print(len(nums))
print(len(nums) * 2)
print(nums[len(nums) - 1])
"""


"""
def show_all(nums):
    for n in nums:
        print(n + 1)

show_all([4, 7, 9])
"""


"""
def show_all(nums):
    for n in nums:
        print(n * 2)

show_all([1, 5])
show_all([10, 20, 30])
"""


"""
nums = [3, 8, 5, 10, 6]
count_even = []
for x in nums:
    if x % 2 == 0:
        count_even.append(x)

print(len(count_even))
"""


"""
def count_even(x):
    return x % 2 == 0

nums = [3, 8, 5, 10, 6]
collected = []

for x in nums:
    if count_even(x):
        collected.append(nums)

print(len(collected))
"""



def count_even(nums):
    collected = []
    for x in nums:
        if x % 2 == 0:
            collected.append(x)
    print(len(collected))
    print(collected)
    return collected

result = count_even([3, 8, 5, 10, 6])

print(len(result))
print(result)