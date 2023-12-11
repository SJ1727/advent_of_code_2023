class Galaxy:
    def __init__(self, pos):
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

gals = []
col_exp = []
row_exp = []
lem = 0

def gt_c(arr, num):
    c = 0
    
    for ele in arr:
        if ele < num:
            c += 1

    return c

tot_dis = 0

DIST = 1_000_000 - 1

with open("Day 11\\data.txt" , "r") as file:
    
    re = file.read()
    rel = re.split("\n")
    
    for i, line in enumerate(rel):
        if "#" not in line:
            row_exp.append(i)
    lem = len(rel)

    for i in range(len(rel[0])):
        cg = False
        for j in range(lem):
            if rel[j][i] == "#":
                cg = True
                break
            
        if not cg:
            col_exp.append(i)

    for i, line in enumerate(rel):
        for j, char in enumerate(line):
            if char == "#":
                gals.append(Galaxy((i + gt_c(row_exp, i)*DIST, j + gt_c(col_exp, j)*DIST)))
                
    for i in range(len(gals)):
        for j in range(i+1, len(gals)):
            tot_dis += abs(gals[i].x - gals[j].x) + abs(gals[i].y - gals[j].y)
            
print(tot_dis) 
