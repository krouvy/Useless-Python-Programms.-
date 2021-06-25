"""
Using nested conditions and cycle for the example of finding the length of a string.
"""
var_1 = input("Write string ")  # variable to write string
len_num_1 = len(var_1)  # function len() return length, now b is int variable which contain length variable var_1
print("len_num_1 is object ", type(len_num_1), "which contain quantity symbols of variable", var_1, "-", len_num_1,
      "symbols")
if var_1.isdigit():  # example usually condition
    x = int(var_1)  # if the line var_1 contains only numbers,then make the variable var_1 int.
    print(var_1, "is number is len", len_num_1)  # print var_1 is number and length var_1
else:
    print(var_1, "no number", len_num_1)  # else print var_1 no number and length var_1
print()

# Same example, but with out function len(), but only for a numbers.
# It's was my first using cycle, so it's looks strange, my bad.
var_2 = int(input("Write number "))  # variable to write number
i = 1  # first number to cycle
end = True  # bool variable to stop cycle

if (var_2 > 0):  # condition to find length of positive number
    while (end):  # while end = True
        if var_2 < 10 ** i:  # a condition nested in a loop
            print("Length", var_2, "is len", i)
            print("Positive number")
            end = False  # stop cycle
        else:  # this condition will happened while 10^i less that var_2
            i += 1
else:  # condition to find length of negative number
    var_2 *= -1 # same, but var_2 was changed
    while (end):
        if var_2 < 10 ** i:
            var_2 *= -1
            print("Length", var_2, "is len", i)
            end = False
        else:
            i += 1
    print("Negative number")
