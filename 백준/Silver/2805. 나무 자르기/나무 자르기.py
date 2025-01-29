N, M = map(int, input().split(' '))
trees = list(map(int, input().split(' ')))
lower_b = 0
upper_b = max(trees)
H = (lower_b + upper_b) // 2

def cut_calculator(trees, H):
    cut = 0
    for tree in trees:
        cut += max(0, (tree - H))
    return cut

while lower_b <= upper_b:
    cut = cut_calculator(trees, H)
    if cut >= M:
        result = H
        lower_b = H + 1
    else:
        upper_b = H - 1

    H = (lower_b + upper_b) // 2

print(result)