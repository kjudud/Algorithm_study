from collections import deque

N = int(input())
dq = deque([i for i in range(1,N+1)])

for _ in range(N-1):
    pop_value = dq.popleft()
    pop_value = dq.popleft()
    dq.append(pop_value)

print(dq.popleft())