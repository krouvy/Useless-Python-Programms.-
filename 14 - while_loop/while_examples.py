"""
This program contains some
examples of using cycles.
It also uses the remove
method to work with the list.
"""

i = 0
while i < 6:  # usually "while" loop which print numbers of 0 to 5
    print(i, end=" ")  # "end" is parameter is responsible for line break, by default end = "\ n"
    i += 1

while i != 0:  # this "while" loop will run until the number entered is 0.
    i = input("\nTo end loop write 0 - ")  # The int() function was not used here to avoid errors
    if i.isdigit():  # if value is digit,
        i = int(i)  # then make value is int. And if value = 0, then end loop
    print("it's not 0")
print("End\n\n")

a = [12, 42, 53, 2, 5, 64, 12, 54, 2, 5, 3, 12, 64, 23, 64] * 4  # if you multiply the list by a number,
print(a, "\n")  # then the list will consist of several repeating list0s
n = int(input("Write value which will be removed from list- "))  # write the number to be removed from the list below
while n in a:  # As long as the entered number is in the list
    a.remove(n)  # apply list's method to remove chosen number from list
print(a, "\n\n\n")  # print changed list

s = "The end program"
while len(s) > 0:  # each loop, this loop
    print(s[0])  # prints the first element of the loop and
    s = s[1:]  # then removes the first element from the list until the list is empty

