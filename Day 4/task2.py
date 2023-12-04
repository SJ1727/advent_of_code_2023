import re

with open(r"day 4\data.txt", "r") as file:
    l = [1 for _ in range(len(file.readlines()))]

with open(r"day 4\data.txt", "r") as file:
    for i, line in enumerate(file.readlines()):
        line = re.sub("Card \d+: ", "", line)
        w, m = line.split("|")
        w = w.split()
        m = m.split()

        t = len(set(w).intersection(m))

        for j in range(t):
            l[i + j + 1] += l[i]

print(sum(l))
