"""
This program describes the use of several methods
and functions for working with strings, and a small
example of how to swap variables in one step.
"""

a = input("Write string... ")  # the input() function will return the written string with the type - string
print("type a -", type(a))  # function type() return object type

if a.isdigit():  # if the string contains only numbers, then method isdigit() return True
    a = int(a)  # and function int() will change the object type from "str" to "int"
    print("new type a -", type(a))  # after function int() class str changed to int

    if a > 100:  # now that type has been changed to int math comparison operations can be used
        print(a, "> 100")  # if a > 100
    else:
        print(a, "< 100")  # if a < 100
    print("Okay\n")

b = type(a)  # write in B type A
print("type b - ", type(b))  # type B  is  class 'type'
b = str(b)  # change type b with "type" to "str"
print("new type b -", type(b), b)  # now B it is string which contains the entry - "<class 'x'>"

b = b.replace("<", "")  # now when b is string, can be used string's method replace
b = b.replace(">", "")  # to change '<' and '>' symbols to ''
b = b.replace("s", "o")  # and change all 's' to 'o'
print("Now b don't have < > symbols -", b, a, "\n")  # result

# and a small example of how you can compare objects of the same type
c = input("Write c... ")
d = input("Write d... ")
if c > d:
    c, d = d, c  # and to swap a few variables
print(c, d)
