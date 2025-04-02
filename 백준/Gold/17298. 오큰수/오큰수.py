# 풀이 방법
# A[i] > A[i+1]이라면, A[i-1] > A[i] > A[i+1]이다. 
# 그러므로 i스탭에서는 A[i+1]만 비교하고 A[i] < A[i+1]면 수를 찾은것이고, 이전에 못찾았던 A[x]도 비교해본다.
# A[i] > A[i+1]라면 스택에 넣어서 다음에 A[i] < A[i+1]인 경우에 다시 비교한다.
# 스택에는 큰수가 먼저 들어가 있으므로 나중에 들어간 것 부터 순차적으로 비교한다.

N = int(input())
permut = list(map(int, input().split()))
ans = [-1] * N
stk = []

for i in range(N-1):
    if permut[i] >= permut[i+1]:
        stk.append((permut[i], i))
    else:
        ans[i] = permut[i+1]
        while True:
            if stk:
                if stk[-1][0] >= permut[i+1]:
                    break
                else:
                    ans[stk[-1][1]] = permut[i+1]
                    stk.pop()
            else:
                break

print(*ans)