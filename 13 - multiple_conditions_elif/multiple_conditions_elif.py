"""
multiple conditions elif
first use "if", then "elif"
and in the end "else" if needed
"""

Number = int(input("Write number < 10000 "))  # variable for the number
if Number < 10:  # first condition
    print(Number, "<10")
elif Number < 100:  # second condition
    print(Number, "<100")
elif Number < 1000:  # thirst condition
    print(Number, "<1000")
elif Number < 10000:  # four condition
    print(Number, "<10000")
else:  # last condition if other condition not fulfilled
    print("ERROR", Number, "> or = 100000 ")
