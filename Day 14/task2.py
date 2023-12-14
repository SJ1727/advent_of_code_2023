import re

def push_n(arr):
    for i, line in enumerate(arr):
        for j, ele in enumerate(line):
            if ele != "O":
                continue

            di = i
            while di > 0 and arr[di - 1][j] == ".":
                di -= 1
            if di == i:
                continue
            
            arr[i][j] = "."
            arr[di][j] = "O"
    return arr

def push_s(arr):
    arr = arr[::-1]
    for i, line in enumerate(arr):
        for j, ele in enumerate(line):
            if ele != "O":
                continue

            di = i
            while di > 0 and arr[di - 1][j] == ".":
                di -= 1
            if di == i:
                continue
            
            arr[i][j] = "."
            arr[di][j] = "O"

    return arr[::-1]

def push_w(arr):
    for i, line in enumerate(arr):
        for j, ele in enumerate(line):
            if ele != "O":
                continue

            dj = j
            while dj > 0 and arr[i][dj - 1] == ".":
                dj -= 1
            if dj == j:
                continue
            
            arr[i][j] = "."
            arr[i][dj] = "O"

    return arr

def push_e(arr):
    arr = [x[::-1] for x in arr]
    for i, line in enumerate(arr):
        for j, ele in enumerate(line):
            if ele != "O":
                continue

            dj = j
            while dj > 0 and arr[i][dj - 1] == ".":
                dj -= 1
            if dj == j:
                continue

            arr[i][j] = "."
            arr[i][dj] = "O"

    return [x[::-1] for x in arr]

total = 0
with open("Day 14\\data.txt") as file:
    text = file.read()
    map_ = text.split("\n")
    map_ = [[x for x in t] for t in map_]
    
    CYCLES = 10 ** 9

    cycle_s = dict()

    for i in range(CYCLES):
        map_ = push_n(map_)
        map_ = push_w(map_)
        map_ = push_s(map_)
        map_ = push_e(map_)

        tup_ = tuple(tuple(x) for x in map_)
        if tup_ in cycle_s:
            diff = i - cycle_s[tup_]
            r_cycles = (CYCLES - i) % diff - 1
            break

        cycle_s[tup_] = i

    for _ in range(r_cycles):
        map_ = push_n(map_)
        map_ = push_w(map_)
        map_ = push_s(map_)
        map_ = push_e(map_)

    print(sum([(len(map_) - i) for i in range(len(map_)) for j in range(len(map_[0])) if map_[i][j] == 'O']))