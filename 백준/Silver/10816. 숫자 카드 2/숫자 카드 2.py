def finder_lower_b(num, lower_b, upper_b):
    mid = (lower_b + upper_b) // 2
    idx = lower_b
    while lower_b <= upper_b:
        if cards[mid] >= num:
            idx = mid
            upper_b = mid - 1
        else:
            lower_b = mid + 1
        mid = (lower_b + upper_b) // 2
    return idx

def finder_upper_b(num, lower_b, upper_b):
    mid = (lower_b + upper_b) // 2
    idx = upper_b
    while lower_b <= upper_b:
        if cards[mid] > num:
            upper_b = mid - 1
        else:
            idx = mid
            lower_b = mid + 1
        mid = (lower_b + upper_b) // 2
    return idx

N = int(input())
cards = sorted(map(int, input().split(' ')))
M = int(input())
to_find = list(map(int, input().split(' ')))
result = []
for i in to_find:
    lower_idx = finder_lower_b(i,0,N-1)
    if cards[lower_idx] == i:
        upper_idx = finder_upper_b(i, lower_idx, N-1)
        result.append(str(upper_idx - lower_idx + 1))
    else:
        result.append('0')

print(' '.join(result))