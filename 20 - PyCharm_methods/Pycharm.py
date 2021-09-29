"""
Starting with this program,
programs are written in Pycharm.
If press control, and click on
__abs__() or another function
a file opens where these
 functions are described.
"""

st2 = int(input("Write a negative number "))
st2 = st2.__abs__()  # method abs
print("Positive number", st2)  # positive number

# some about methods, I remember,
# that methods in C++ can change object.
# In Python it's happening not always.

str1 = "aaa"  # str "aaa"
str2 = str1.upper()  # apply method upper and save result in str2
print(str1)  # but str1 wasn't change
print(str2)
