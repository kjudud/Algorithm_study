from collections import deque

n = int(input())

dx = [+2, +1, -1, -2, -2, -1, +1, +2]
dy = [+1, +2, +2, +1, -1, -2, -2, -1]


def bfs(a, b, c, d):
    dq = deque()
    dq.append((a, b))

    while dq:
        cx, cy = dq.popleft()
        if cx == c and cy== d:
            print(visited[cx][cy] - 1)
            return True

        for i in range(8):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if visited[nx][ny] == 0:
                visited[nx][ny] = visited[cx][cy] + 1
                dq.append((nx, ny))

    return False

for i in range(n):
    l = int(input())
    visited = [[0] * l for _ in range(l)]
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    visited[a][b] = 1
    bfs(a, b, c, d)
