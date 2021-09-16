"""
Algorithm for finding the
Greatest common divisor and
Least common multiple
"""

num_1, num_2 = map(int, input("Enter 2 numbers ").split())  # get 2 values
num_1x = num_1  # Saving the value
num_2x = num_2  # of variables
while num_2 > 0:
    num_1, num_2 = num_2, num_1 % num_2  # save in num_1 variable num_2
print(num_1, " GCD")  # and remainder of the division in num_2
LCM = num_1x * num_2x / num_1  # multiply first values of num_1 and num_2
print(LCM, "LCM")  # and divide by Greatest common divisor
