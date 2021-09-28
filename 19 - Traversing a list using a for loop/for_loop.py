"""
An example of traversing a list using
the "for" loop. Copying items from one
list to another without repeating.
"""

Some_list = [5, 4, 'f', 3, 1, 2, 4, 6, 43, 'f']  # original list
Empty_list = []  # empty list
for i in Some_list:  # 'i' single element of the list 'Some_list', first the first, then the second, and so on
    if i not in Empty_list:  # if i absent in "Empty_List"
        Empty_list.append(i)  # then append i in "Empty_List"
# The cycle will repeat until it has walked through all the elements of the "Some_List"

print(Some_list, "- Original list")  # print Original List
print(Empty_list, "- Copy with out repeat") # print a not-so-empty new list
