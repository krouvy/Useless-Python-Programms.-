"""
This program is an example of using
a loop and conditions to define a
character in a string
"""

string = "fWAFwaf312f f32f324#$$4321f!#F"  # string with different symbols, letters and digits.
while len(string) > 0:  # loop which will continue until the string is empty
    symbol = string[0]  # get first element from string
    if symbol >= "a" and symbol <= "z":  # symbols have index number, so we can compare them
        print(symbol, " small")  # if symbol belongs to this interval, so it's small letter
    elif symbol >= "A" and symbol <= "Z":  # same but for another interval
        print(symbol, " big")  # if symbol belongs to this interval, so it's big letter
    elif symbol.isdigit():  # other condition, if symbol is digit,
        print(symbol, " digit")  # so print digit
    else:
        print(symbol, "symbol")  # and for other ways, symbol is symbol
    string = string[1:]  # remove first element of string after print
print("\nThe end")
