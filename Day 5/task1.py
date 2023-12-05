import re

class Seed:
    def __init__(self, seedn):
        self.t = seedn
        self.changed = False

r1 = "seeds:"

t = "map:"

f = False

with open("day 5\\data.txt", "r") as file:
    seeds = []
    for linenum, line in enumerate(file.readlines(), start=1):
        if line == "\n":
            for seed in seeds:
                seed.changed = False
            continue


        if re.search(r1, line):
            line = re.sub(r1, "", line)
            seeds = [Seed(int(x)) for x in line.split()]
            continue
        
        if re.search(t, line):
            continue
        
        a, b, c = line.split() 
        for seed in seeds:
            if seed.changed:
                continue
            
            if seed.t >= int(b) and seed.t < int(b) + int(c):
                seed.t = int(a) + seed.t - int(b)
                seed.changed = True

current_min = 10e12

for i, seed in enumerate(seeds):
    current_min = min(current_min, seed.t)

print(current_min)