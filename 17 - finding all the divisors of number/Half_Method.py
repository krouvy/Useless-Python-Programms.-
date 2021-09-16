"""
Finding all the divisors of a number.
This method checks half
of all the numbers in the number to
increase the calculation speed.
"""

Num = int(input("Write value "))
i = 1
while i <= Num // 2:  # We do not check all the digits,
    if Num % i == 0:  # but only half of the number, it's enough to find all values
        print(i)  # if the number is divisible by 'i' without a remainder, then print the number
    i += 1
print(Num)  # output the number itself
