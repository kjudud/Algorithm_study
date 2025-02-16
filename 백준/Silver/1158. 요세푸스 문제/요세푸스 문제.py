from collections import deque

N, K = map(int, input().split())
dq = deque([i+1 for i in range(N)])
result = []
for i in range(N):
    for j in range(K):
        if j == K-1:
            result.append(dq.popleft())
        else:
            dq.append(dq.popleft())

print(f'<{", ".join(map(str,result))}>')