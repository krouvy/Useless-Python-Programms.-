"""
Finding all the divisors of a number.
This method repeats the numbers until the
i squared is greater than the number itself.
This is much faster than going through half
of all the numbers in the number.
"""

Num = int(input("Write value "))
i = 1
List = []  # list to record all divisors
while i ** 2 <= Num:  # until the squared i less than number
    if Num % i == 0:  # check i is divisors of number
        print(i)
        List.append(i)  # add i to list
        if i != Num // i:  # if i isn't the smallest divisor
            print(Num // i)  # then print
            List.append(Num // i)  # and add to list
    i += 1  # next number
List.sort()  # then sort list
print(List)  # and print
