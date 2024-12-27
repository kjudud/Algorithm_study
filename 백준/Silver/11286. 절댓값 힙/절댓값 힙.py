import heapq
import sys

input = sys.stdin.readline
N = int(input())
plus_hq = []
minus_hq = []
# answer = []
for _ in range(N):
    inp = int(input())
    if not inp:
        plus_len = len(plus_hq)
        minus_len = len(minus_hq)
        if not (plus_len + minus_len):
            # answer.append('0')
            print(0)
        else:
            if plus_len:
                plus_min = heapq.heappop(plus_hq)
                if not minus_len:
                    # answer.append(str(plus_min))
                    print(plus_min)
                    continue
            if minus_len:
                minus_min = heapq.heappop(minus_hq)
                if not plus_len:
                    #answer.append(str(minus_min))
                    print(-1*minus_min)
                    continue
                    
            if plus_min < minus_min:
                # answer.append(str(plus_min))
                print(plus_min)
                if minus_len:
                    heapq.heappush(minus_hq, minus_min)    
            else:
                # answer.append(str(-1*minus_min))
                print(-1*minus_min)
                if plus_len:
                    heapq.heappush(plus_hq, plus_min)
    else:
        if inp > 0:
            heapq.heappush(plus_hq, inp)
        else:
            heapq.heappush(minus_hq, -1*inp)

# print('\n'.join(answer))