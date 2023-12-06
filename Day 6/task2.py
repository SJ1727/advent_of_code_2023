time = 59707878
dist = 430121812131276

running_total = 0
for i in range(time):
    if i * (time - i) > dist:
        print(time - 2 * i + 1)
        break