#dfs로 찾아보고, 보고있는 item 순서에서 어떤 경로로 왔든 같은 a,b의 흔적을 가지고 있으면 더 찾아볼 필요 없음

def solution(info, n, m):
    global answer
    answer = float('inf')
    # 중복 비교를 해야돼서 set. 사용, list로 in 연산시 사용시 시간초과
    # set in 연산 O(1), list in 연산 O(n)
    history = set()
    
    dfs(-1, 0, 0, history, n, m, info)
    
    if answer == float('inf'):
        answer = -1
        
    return answer

def dfs(idx, a_trace, b_trace, history, n, m, info):
    global answer
    
    idx += 1
    if a_trace >= n or b_trace >= m:
        return
    
    # 같은 a,b의 흔적을 가진 idx의 경우 탐색을 이미 한것이니까 스킵
    if (idx, a_trace, b_trace) in history:
        return
    else:
        history.add((idx, a_trace, b_trace))
    
    if idx >= len(info):
        answer = min(answer, a_trace)
        return
    
    # A 선택
    n_a_trace = a_trace + info[idx][0] 
    dfs(idx, n_a_trace, b_trace, history, n, m, info)
    
    # B 선택
    n_b_trace = b_trace + info[idx][1]
    dfs(idx, a_trace, n_b_trace, history, n, m, info)