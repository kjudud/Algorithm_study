N = int(input())

def dfs(x_list):
    global result
    stage = len(x_list)
    if stage == N:
        result += 1
        return
    del_set_list = []
    for x in x_list:        
        del_set_list += [x-stage, x, x+stage]
        stage -= 1
    
    rest_set = start_set - set(del_set_list)
    for r in rest_set:
        n_x_list = x_list + [r]
        dfs(n_x_list)

result = 0
start_set = set([i for i in range(N)])
# 대칭이니까 절반만 dfs
n = N//2
for i in range(n):
    dfs([i])
result *= 2
# N이 홀수인 경우 중간만 dfs 한번더
if N%2:
    dfs([n])

print(result)
