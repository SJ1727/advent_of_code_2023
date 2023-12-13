from functools import cache

@cache
def ru_s(f, in_r, r):
	if f == "":
		if in_r is None and len(r) == 0:
			return 1
		if len(r) == 1 and in_r is not None and in_r == r[0]:
			return 1
		return 0

	mp = 0
	for char in f:
		if char == '#' or char == '?':
			mp += 1
	if in_r is not None and (mp + in_r < sum(r) or len(r) == 0):
		return 0
	if in_r is None and mp < sum(r):
		return 0

	p = 0
	if f[0] == '.' and in_r is not None and in_r != r[0]:
		return 0

	if f[0] == '?' or f[0] == '#':
		if in_r is None:
			p += ru_s(f[1:], 1, r)
		else:
			p += ru_s(f[1:], in_r+1, r)

	if (f[0] == '?' or f[0] == '.') and in_r is None:
		p += ru_s(f[1:], None, r)

	if f[0] == '.' and in_r is not None or (f[0] == '?' and in_r is not None and in_r == r[0]):
		p += ru_s(f[1:], None, r[1:])
	return p

tot = 0

with open("day 12\\data.txt", "r") as file:
    for line in file.readlines():
        s, f = line.split(" ")
        f = tuple(map(lambda x: int(x), f.split(",")))
        tot += ru_s((5 * (s + "?"))[:-1], None, f*5)

print(tot)
