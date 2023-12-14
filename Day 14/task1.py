import re

def rot(arr):
    arr = [[x for x in r] for r in arr]
    return ["".join(x[::-1]) for x in list(map(list, zip(*arr)))]



total = 0
with open("Day 14\\test.txt") as file:
    text = file.read()
    map_ = text.split("\n")
    map_ = rot(map_)
    map_ = rot(map_)
    map_ = rot(map_)
    
    for col in map_:
        rock_min_pos = 0
        for i, obj in enumerate(col):
            if obj == "O":
                total += (len(col) - rock_min_pos)
                rock_min_pos += 1
            if obj == "#":
                rock_min_pos = i + 1

    print(total)
