from itertools import combinations

nanjanges = []
for _ in range(9):
    nanjanges.append(int(input()))

for i in combinations(nanjanges, 7):
    if sum(i) == 100:
        for i in sorted(i):
            print(i)
        break