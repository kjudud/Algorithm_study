import sys

input = sys.stdin.readline

N, P = map(int, input().split())
answer = 0
finger_status = [[] for _ in range(6)]
for _ in range(N):
    string_num, c_prat = map(int, input().split())
    while len(finger_status[string_num-1]) > 0:
        p_prat = finger_status[string_num-1].pop() 
        if p_prat > c_prat:
            answer += 1
        elif p_prat < c_prat:
            finger_status[string_num-1].append(p_prat)
            finger_status[string_num-1].append(c_prat)
            answer += 1
            break
        else:
            finger_status[string_num-1].append(p_prat)
            break

    if len(finger_status[string_num-1]) == 0:
        finger_status[string_num-1].append(c_prat)
        answer += 1

print(answer)
        