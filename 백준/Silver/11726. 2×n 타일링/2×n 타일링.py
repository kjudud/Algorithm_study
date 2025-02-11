import sys

sys.setrecursionlimit(10**6)
INF = 987654321
cache = [0] * 1001
cache[1] = 1
cache[2] = 2
N = int(input())

def dp(x):
    if cache[x] != 0:
        return cache[x]
    if x > 2:
        cache[x] = (dp(x-1) + dp(x-2)) % 10007
    
    return cache[x]

print(dp(N))