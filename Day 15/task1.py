import re

def hash_(s):
    s_hash = 0
    for c in s:
        s_hash += ord(c)
        s_hash *= 17
        s_hash %= 256
    return s_hash

tot = 0

with open("Day 15\\data.txt") as file:
    strings = ",".join(file.read().split("\n")).split(",")

    for string in strings:
        # print(string)
        # print(hash_(string))
        tot += hash_(string)
        
print(tot)