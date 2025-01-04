import sys
import heapq

input = sys.stdin.readline
meeting_list = []
N = int(input())
count = 0
for _ in range(N):
    start, end = map(int, input().split())
    meeting_list.append((end, start))
heapq.heapify(meeting_list)
end_time = 0
for _ in range(N):
    end ,start = heapq.heappop(meeting_list)
    if start >= end_time :
        count += 1
        end_time = end
print(count)

