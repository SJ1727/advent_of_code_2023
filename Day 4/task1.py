import re

total = 0

with open(r"day 4\datat.txt", "r") as file:
    for line in file.readlines():
        line = re.sub("Card \d+: ", "", line)
        w, m = line.split("|")
        w = w.split()
        m = m.split()

        t = len(set(w).intersection(m)) - 1

        if t >= 0:
            total += 2 ** t

print(total)