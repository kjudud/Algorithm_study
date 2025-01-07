from collections import deque

N, M = map(int, input().split())
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
chk = [[False] * M for _ in range(N)]
chk[0][0] = True
dq = deque()

miro = []
for _ in range(N):
    input_string = input()
    miro.append([int(char) for char in input_string])

def is_valid_coord(y , x):
    value = (0 <= y < N and 0 <= x < M)
    return value

dq.append((0, 0, 1))
while len(dq):
    y, x, cnt = dq.popleft()
    if y == (N-1) and x == (M-1):
        print(cnt)
        break

    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        ncnt = cnt + 1
        if is_valid_coord(ny, nx) and miro[ny][nx] and not chk[ny][nx]:
            chk[ny][nx] = True
            dq.append((ny, nx, ncnt))