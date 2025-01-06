# 격자칸에서 상하좌우로 움직이며 경로를 찾는 문제를 위한 DFS, BFS 코드 형태 익히기
from collections import deque

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
N = int(input())
check = [[false] * N for _ in range(N)]

def valid_coord_check(y, x):
  return 0 <= y < N and 0<= x < N

def dfs(y, x):
  if adj_mat[y][x] = ans:
    return

for k in range(4):
  ny = y + dy[k]
  nx = x + dx[k]
  if valid_coord_check(ny, nx) and not check[ny][nx]:
    check[ny][nx] =True
    dfs(ny, nx)

def bfs(sy, sx):
  q = dequeu()
  check[sy][sx] = True
  q.append((sy, sx))
  while len(q):
    y,x = q.popleft()
    if adj[y][x] == ans:
      return
  for k in range(4):
    ny = y + dy[k]
    nx = x + dx[k]
    if valid_coord_check(ny, nx) and not check[ny][nx]:
      check[ny][nx] = True
      q.append(ny, nx)


