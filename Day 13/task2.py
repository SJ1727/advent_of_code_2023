def mirrow_pos(map_):
    val = True
    for i in range(len(map_) - 1):
        diff = 0
        for j in range(len(map_)):
            val = True
            if (2 * i) - j + 1 in range(len(map_)):
                if map_[j] != map_[2 * i - j + 1]:
                    for x, y in zip(map_[j], map_[2 * i - j + 1]):
                        if x != y:
                            diff += 1

        if val and diff == 2:
            return i
        
    return None

maps = []

total = 0
with open("Day 13\\data.txt", "r") as file:
    text = file.read().split("\n\n")
    maps = [["".join(list(t)) for t in x.split("\n")] for x in text]
    maps = [["".join(s) for s in map_] for map_ in maps]
    
    for map_ in maps:
        if (row := mirrow_pos(map_)) is not None:
            total += (row + 1) * 100
            continue
        if (col := mirrow_pos(list(map(lambda x: list(x), zip(*map_))))) is not None:
            total += (col + 1)

print(total)