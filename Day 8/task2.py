import re

class Node:
    def __init__(self, label, l, r):
        self.label = label
        self.l = l
        self.r = r
        
stru = "LLLRRRLLRLRLLRRRLRLRRLRRLRRRLRRLLLRLRRLLRLRRRLRRRLLLRLLLLRLRRLLLRRRLRRRLRLRRRLLLLRLRLLRRLLRRRLRRLRLRRRLRRRLLLRLRRRLRRRLRRLLRRLRRRLLRLRLRLRLRLRRRLRLRRLRLRLRLRRLRRLRLRLRRLLRRLRRRLRRLRRLRRRLRRLRLLRLRLLRRLRRRLRLRLRRLLRRLRRRLRRLRRRLRLRRRLRRLRLRRLRLRRLLLRRLRRLRRRLRLRRLRRRLRLRLRRLRLLRRRR"
n_reg = r"([A-Z]+)\s*=\s*\(([A-Z]+),\s*([A-Z]+)\)"
nodes = []
a_nodes = []
a_nodes_times = []

with open("day 8\\data.txt", "r") as file:
    for line in file.readlines():
        d = re.search(n_reg, line)
        if d is not None:
            nodes.append(Node(d.group(1), d.group(2), d.group(3)))

turns = 0

for i, node in enumerate(nodes):
    if node.label[2] == "A":
        a_nodes.append(i)

a_nodes_times = [None for _ in a_nodes]

while None in a_nodes_times:
    instru = stru[turns % len(stru)]
    
    for index, a_node in enumerate(a_nodes):
        
        if a_nodes_times[index] is not None: 
            continue

        if nodes[a_node].label[2] == "Z":
            a_nodes_times[index] = turns

        if instru == "R":
            target = nodes[a_node].r
            for i, node in enumerate(nodes):
                if node.label == target:
                    a_nodes[index] = i
                    break

        if instru == "L":
            target = nodes[a_node].l
            for i, node in enumerate(nodes):
                if node.label == target:
                    a_nodes[index] = i
                    break
            
    turns += 1

# Use wolfram alpha to find lowest common multiple of output numbers
# https://www.wolframalpha.com/input?i=lowest+common+multiple+of+%2816579%2C+18827%2C+19951%2C+12083%2C+22199%2C+17141%29
print(a_nodes_times)