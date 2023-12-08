import re

class Node:
    def __init__(self, label, l, r):
        self.label = label
        self.l = l
        self.r = r
        
stru = "LLLRRRLLRLRLLRRRLRLRRLRRLRRRLRRLLLRLRRLLRLRRRLRRRLLLRLLLLRLRRLLLRRRLRRRLRLRRRLLLLRLRLLRRLLRRRLRRLRLRRRLRRRLLLRLRRRLRRRLRRLLRRLRRRLLRLRLRLRLRLRRRLRLRRLRLRLRLRRLRRLRLRLRRLLRRLRRRLRRLRRLRRRLRRLRLLRLRLLRRLRRRLRLRLRRLLRRLRRRLRRLRRRLRLRRRLRRLRLRRLRLRRLLLRRLRRLRRRLRLRRLRRRLRLRLRRLRLLRRRR"
n_reg = r"([A-Z]+)\s*=\s*\(([A-Z]+),\s*([A-Z]+)\)"
nodes = []

with open("day 8\\data.txt", "r") as file:
    for line in file.readlines():
        d = re.search(n_reg, line)
        if d is not None:
            nodes.append(Node(d.group(1), d.group(2), d.group(3)))
            

curr_n_i = 0
turns = 0

for i, node in enumerate(nodes):
    if node.label == "A":
        curr_n_i = i
        break

while nodes[curr_n_i] != "ZZZ":
    instru = stru[turns % len(stru)]

    if nodes[curr_n_i].label == "ZZZ":
        break

    if instru == "R":
        target = nodes[curr_n_i].r
        for i, node in enumerate(nodes):
            if node.label == target:
                curr_n_i = i
                break

    if instru == "L":
        target = nodes[curr_n_i].l
        for i, node in enumerate(nodes):
            if node.label == target:
                curr_n_i = i
                break
            
    turns += 1
    
print(turns)