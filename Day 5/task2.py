import re

seeds = [222541566, 218404460, 670428364, 432472902, 2728902838, 12147727, 3962570697, 52031641, 2849288350, 113747257, 3648852659, 73423293, 4036058422, 190602154, 1931540843, 584314999, 3344622241, 180428346, 1301166628, 310966761]

r = "(\\w|\\s|-)+:"

f = False
found_smallest = False

smallest = 0
t_prime = smallest

with open("day 5\\moddata.txt", "r") as file:
    sets = file.read().split("\n\n")
    maps = [x.split("\n")[1:] for x in sets]
    maps = maps[::-1]
    maps = [[list(map(lambda x: int(x), map_.split())) for map_ in set_] for set_ in maps]

    while not found_smallest:
        for set_ in maps:
            for map_ in set_:
                a, b, c = map_
                
                if t_prime >= a and t_prime < a + c:
                    t_prime = t_prime - a + b
                    break
        
        for i in range(len(seeds) // 2):
            if t_prime >= seeds[2 * i] and t_prime < seeds[2 * i] + seeds[2 * i + 1]:
                found_smallest = True
                break
        
        if not found_smallest:
            smallest += 1
            t_prime = smallest
            if smallest % 10_000 == 0:
                print(smallest)

print(smallest)