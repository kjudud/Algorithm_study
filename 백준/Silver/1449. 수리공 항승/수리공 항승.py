N, L = map(int, input().split())
holes = list(map(int, input().split()))
holes.sort()
result = 1
start = holes[0]
for hole in holes:
    if (hole - start) > (L - 1):
        result += 1
        start = hole
    else:
        pass

print(result)