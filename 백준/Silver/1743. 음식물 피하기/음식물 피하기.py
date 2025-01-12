from collections import deque
from array import array
import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline 
N, M, K = map(int, input().split())
grid = [array('b', [0] * M) for _ in range(N)]
chk = [array('b', [0] * M) for _ in range(N)]

for _ in range(K):
    y, x = map(int, input().split())
    grid[y-1][x-1] = 1

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
result = 0
cnt = 0

def is_valid_coord(y, x):
    return 0 <= y < N and 0 <= x < M

def dfs(y, x):
    global cnt
    chk[y][x] = True
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_valid_coord(ny, nx) and not chk[ny][nx] and grid[ny][nx]:
            cnt += 1
            dfs(ny, nx)
            

for y in range(N):
    for x in range(M):
        if grid[y][x] and not chk[y][x]:
            cnt = 1
            dfs(y, x)
            result = max(result, cnt)

print(result)