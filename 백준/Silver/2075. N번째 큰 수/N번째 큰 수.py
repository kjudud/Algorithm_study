import heapq

N = int(input())
result_hq = []
for n in range(N):
    temp_hq = [-1*int(i) for i in input().split(' ')]
    heapq.heapify(temp_hq)
    for m in range(n+1):
        heapq.heappush(result_hq, -1*heapq.heappop(temp_hq))
        if m > 0:
            heapq.heappop(result_hq)

result = heapq.heappop(result_hq)
    
print(result)