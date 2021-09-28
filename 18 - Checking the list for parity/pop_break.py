"""
This program checks the list
items for odd parity. If all
elements are even, then the list
will be empty. Because the "pop ()"
method cuts out the last item from the list.
"""

List = list(map(int, input("Enter your digit values ").split()))  # Entering list items separated by a space
while len(List) > 0:  # Execute as long as the length of the list is greater than zero
    last = List.pop()  # Cuts last element of List, and record in variable "last"
    if last % 2 != 0:  # if variable "last" is not even
        print("Number", last, "is not even")  # print this value
        break  # Exit the loop
else:
    print("All numbers are even")  # else print message
    print(List)  # and empty list
