answer = []
for _ in range(int(input())):
    count = 0
    ans = 'NO\n'
    for g_s in input():
        if g_s == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                break
    if count == 0:
        ans = 'YES\n'
    answer.append(ans)
    
print(''.join(answer))
    