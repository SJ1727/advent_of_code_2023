times = [59, 70, 78, 78]
dists = [430, 1218, 1213, 1276]

total = 1
running_total = 0

for time, dist in zip(times, dists):
    running_total = 0
    for i in range(time):
        if i * (time - i) > dist:
            running_total += 1
            
    total *= running_total
    
print(total)