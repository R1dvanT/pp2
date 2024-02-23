#Task1
def square(n):
    for x in range(1,n+1):
        return x**2
n = int(input())
square_num = square(n)
print(square_num)

#Task2:
n = int(input())
def even(n):
    for x in range(n+1):
        if x%2==0:
            yield x
for y in even(n):
    print(y, end = ' ')

#Task3: 
n = int(input())
def div(n):
    for x in range(n+1):
        if x%3==0 and x%4==0:
            yield x
for y in div(n):
    print(y)

#Task4:
a = int(input())
b = int(input())
def square(a, b):
    for x in range(a, b+1):
        yield x**2

for y in square(a, b):
    print(y)

#Task5:
n = int(input())
def reverse(n):
    for x in range(n, -1, -1):
        yield x
for y in reverse(n):
    print(y)
    