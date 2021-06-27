"""
A simple program that
breaks a number into
digits using a loop.
"""
s = int(input("Write number \n"))
while s > 0:
    a = s % 10  # last digit of number
    print(a, end="")  # print digit
    s = s // 10  # divide the number by 10 without a remainder
print("\n")  # as a result, we get the inverse of the original number
