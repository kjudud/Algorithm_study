from collections import deque

N, M = map(int, input().split())
adj_mat = [[False] * N for i in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    adj_mat[a-1][b-1] = True
    adj_mat[b-1][a-1] = True

dist = [[0] * N for _ in range(N)]
ans_dist = float('inf')
ans = 0

def bfs(main, target):
    dq = deque()
    dq.append((main , 0))
    check = [False] * N
    check[main] = True
    while dq:
        now, hop_num = dq.popleft()
        if now == target:
            return hop_num
        for i in range(N):
            if adj_mat[now][i] and not check[i]:
                check[i] = True
                dq.append((i, hop_num+1))

for i in range(N):
    for j in range(N):
        if i != j:
            if dist[i][j] == 0:
                hop_num = bfs(i, j)
                dist[i][j] = hop_num
                dist[j][i] = hop_num

for i in range(N):
    dist_sum = sum(dist[i])
    if dist_sum < ans_dist:
        ans_dist = dist_sum
        ans = i

print(ans + 1)