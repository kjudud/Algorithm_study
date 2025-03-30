alphabet_str = input()

def OkCheck(alphabet_dict):
    isok = True
    cnt = 0
    for alphabet in alphabet_dict.values():
        cnt += alphabet % 2
        if cnt > 1:
            isok = False
            break

    return isok

alphabet_dict = {}
for alphabet in alphabet_str:
    if alphabet in alphabet_dict:
        alphabet_dict[alphabet] += 1
    else:
        alphabet_dict[alphabet] = 1

if not OkCheck(alphabet_dict):
    print("I'm Sorry Hansoo")
else:
    half = []
    mid = []
    for alphabet, alphabet_cnt in alphabet_dict.items():
        half.append(alphabet * (alphabet_cnt // 2))
    
    half = sorted(half)

    for alphabet, alphabet_cnt in alphabet_dict.items():
        if alphabet_cnt % 2:
            mid.append(alphabet)
            break
        
    ans = half + mid + half[::-1]

    print(''.join(ans))