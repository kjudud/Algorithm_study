import heapq

T = int(input())
ans1 = []
ans2 = []

for _ in range(T):
    M = int(input())
    ans = []
    num_list = []
    for _ in range(int(M//10 + 1)):
        num_list = num_list + (list(map(int, input().split())))
    
    hq_low = []
    hq_high = []
    # 1, 2 번째 숫자 넣어서 초기화
    if M != 1:
        num1 = num_list.pop(0)
        num2 = num_list.pop(0)
        ans.append(num1)
        if num1 < num2:
            heapq.heappush(hq_low, -1*num1)
            heapq.heappush(hq_high, num2)
        else:
            heapq.heappush(hq_low, -1*num2)
            heapq.heappush(hq_high, num1)
        
        for i, num in enumerate(num_list):
            num_high = heapq.heappop(hq_high)
            if num >= num_high:
                heapq.heappush(hq_high, num)
                heapq.heappush(hq_low, -1*num_high)
            else:
                heapq.heappush(hq_low, -1*num)
                heapq.heappush(hq_high, num_high)

            if len(hq_low) > len(hq_high)+1:
                heapq.heappush(hq_high, -1*heapq.heappop(hq_low))

            if len(hq_low) < len(hq_high):
                heapq.heappush(hq_low, -1*heapq.heappop(hq_high))

            if i%2 == 0:
                low_num = -1*heapq.heappop(hq_low)
                ans.append(low_num)
                heapq.heappush(hq_low, -1*low_num)
    else:
        ans.append(num_list.pop(0))
        
    ans1.append(ans)
    ans2.append(M//2 + 1)

for i in range(T):
    print(ans2[i])
    for j in range(len(ans1[i]) // 10 + 1):      
        print(*ans1[i][j * 10:(j+1)*10])