# main.py
# Day 21 - Piano keys, slicing example
"""
This is an example of how to use slicing with lists and tuples.
"""

piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_keys[2:5])  # from 2 to 5 c to e
print(piano_keys[:5])  # from 0 to 5 a to e
print(piano_keys[2:5:2])  # from 2 to 5 counting by 2's [c, e]
print(piano_keys[::])  # from 0 to the end of the list a to g
print(piano_keys[::2])  # from 0 to the end counting by 2's [a, c, e, g]
print(piano_keys[::-1])  # reverse from the end to 0
print(piano_tuple[2:5])
