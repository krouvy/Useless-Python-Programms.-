"""
Euclidean Algorithm is
an efficient algorithm
for finding the greatest
divisor of two integers
"""

num1 = int(input("First value\n"))
num2 = int(input("Second value\n"))
while num1 != num2:  # Do until number 1 is equal to number 2
    if num1 > num2:
        num1 = num1 - num2
    else:
        num2 = num2 - num1
print(num1, num2)
