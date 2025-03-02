N, M = map(int, input().split())
board = [input() for _ in range(N)]

def chk(y, x, pattern):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2:
                if board[y+i][x+j] != pattern:
                    cnt += 1
            else:
                if board[y+i][x+j] == pattern:
                    cnt += 1
    
    return cnt

answer = 64

for y in range(N-7):
    for x in range(M-7):
        cnt = chk(y, x, 'B')
        answer = min(answer, cnt)
        cnt = chk(y, x, 'W')
        answer = min(answer, cnt)

print(answer)