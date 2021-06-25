"""
 If we simply equate two lists, then the second
 list will refer to the first one and changes in
 any of them will be reflected on each other.

 So when we copy the list, we do it with a slice. [:]
 and second list will receive content first's list.

 But this will continue to work as long as the list
 contains no nested lists. In such a situation, the
 nested list will refer to the other list and the
 changes will be reflected in both lists.

 To copy list that contains nested list can be used
 function deepcopy from library copy.
 """

print("\nExample without deepcopy\n")
a = [4, 21, 67, 3, 4, [64, 12]]  # list with nested list
print(a, "- original list a")
d = a[:]  # copy the list using a slice
d[5][1] = 'YES'  # change the element of the nested list
d[2] = 'NO'  # change the element of the list
print(a, "- list a")  # only element in nested list changed
print(d, "- list d")  # both elements changed
print("\n_____________________________\n")

from copy import deepcopy

print("Example with deepcopy\n")
h = [1, 2, [3, 4]]
print(h, "- original list h")
k = deepcopy(h)  # all sames, but copy with the help function deepcopy
k[2][0] = 'YES'
k[1] = 'NO'

print(h, "- list h")  # no changed
print(k, "- list k")  # changed
