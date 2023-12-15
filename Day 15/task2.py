import re
from copy import deepcopy

def hash_(s):
    s_hash = 0
    for c in s:
        s_hash += ord(c)
        s_hash *= 17
        s_hash %= 256
    return s_hash

class Lens:
    def __init__(self, label, value):
        self.label = label
        self.value = value

tot = 0

boxes = [list() for _ in range(256)]

dec_regex = "(\w+)-"
in_regex = "(\w+)=(\d+)"

type_match = None 

with open("Day 15\\data.txt") as file:
    strings = ",".join(file.read().split("\n")).split(",")

for string in strings:
    if (type_match := re.match(dec_regex, string)) is not None:
        h = hash_(type_match.group(1))
        for item in list(boxes[h]):
            if item.label == type_match.group(1):
                boxes[h].remove(item)
        
    if (type_match := re.match(in_regex, string)) is not None:
        h = hash_(type_match.group(1))
        new_lens = Lens(type_match.group(1), int(type_match.group(2)))
        
        added = False
        for i in range(len(boxes[h])):
            if boxes[h][i].label == new_lens.label:
                boxes[h][i] = new_lens
                added = True
                break
            
        if not added:
            boxes[h].append(new_lens)
total = 0
for j, box in enumerate(boxes, start=1):
    for i, lens in enumerate(box, start=1):
        total += lens.value * i * j

print(total)

 
