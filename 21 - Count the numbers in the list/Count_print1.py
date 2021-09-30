"""
This program counts how
many times certain numbers
appear in the list.
Number range from 0 to 100
"""

Num_list = [4, 2, 4, 1, 2, 2, 3, 1, 1, 2, 3, 2, 0, 0, 0, 0, 4, 2, 5, 3, 6, 67, 54, 34, 23, 6, 4, 3, 5]
Count_list = [0] * 100  # Creation of a list containing 100 zero cells
for i in Num_list:  # the loop goes through all the elements of the Num_list
    Count_list[i] += 1  # and using the Num_list number as index of count_list adds 1
for i in range(len(Count_list)):  # then the loop goes through all index of the Num_list from 0 to 99
    if Count_list[i] > 0:  # and if element of Count_list > 0
        while Count_list[i] > 0:  # while element of Count_list > 0
            print(i, end=" ")  # print index of this element without line break
            Count_list[i] -= 1  # subtracts one from this element
        print(end=" ")  # print space between loops
print("\nEnd")
