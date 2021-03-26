a = input("Enter the value")  # Default object type str.
print(type(a))  # type str(string)
print(a)

b, c, d = map(int, input("Enter 3 values").split())  # This hard, but I'll Try explain.

# function map get function and container
# function input() create string type str, for example "1 3 5"
# Then method split() cut this string with "spaces" between numbers
# And we get container with variables 1, 3 ,5
# Then function int() inside map() applies to every elements of container
# And all values become type int, instead str.
# Then with help multi assignment send these values in variables b,c,d


print(b + c + d)  # Now, when all variables type int, we can sum those variables

print("enter values of list")
f = list(map(int, input().split()))  # Other sample. Here we use function list(), to create list with these variables.
print(f[2])  # Then we print element of list with index 2(it's 3'st element, 0,1,2)
