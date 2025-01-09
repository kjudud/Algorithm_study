from collections import deque

R, C = map(int, input().split())
grid = [input() for _ in range(R)]
chk = [[set() for _ in range(C)] for _ in range(R)]
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
ans = 0

def is_valid_coord(y, x):
    return 0 <= y < R and 0 <= x < C

dq = deque()
chk[0][0].add(grid[0][0])
dq.append((0, 0, grid[0][0]))
while dq:
    y, x, alp_str = dq.popleft()
    ans = max(ans, len(alp_str))

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if is_valid_coord(ny, nx) and grid[ny][nx] not in alp_str:
            n_alp_str = alp_str + grid[ny][nx]
            if n_alp_str not in chk[ny][nx]:
                chk[ny][nx].add(n_alp_str)
                dq.append((ny, nx, n_alp_str))


print(ans)