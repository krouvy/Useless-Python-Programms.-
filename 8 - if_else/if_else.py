# "if" is always the first condition, after "elif" (any number)
# and the last must be "else" (if necessary)

x = int(input("Write X "))
y = int(input("Write Y "))
if x > 0:
    if y > 0:
        print("Zone 1, up-right corner")
    elif y < 0:
        print("Zone 4, down-right corner")
    else:
        print("X-Axis, right side")

elif x < 0:
    if y > 0:
        print("Zone 2, up-left corner")
    elif y < 0:
        print("Zone 3, down-left corner")
    else:
        print("X-Axis, left side")

else:
    if y > 0:
        print("Y-Axis above zero")
    elif y < 0:
        print("Y-Axis below zero")
    else:
        print("center, two zeroes")

# if else conditions
# Nesting example
# Program for determining the position of a point.

