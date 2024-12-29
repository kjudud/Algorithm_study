from itertools import combinations

sum_result = []
result = []
T_n = [int(i*(i+1)/2) for i in range(1, 46)]

def check(l):
    for i in range(45):
        for j in range(i,45):
            for k in range(j,45):
                if (T_n[i] + T_n[j] + T_n[k]) == l:
                    return 1
    return 0

for _ in range(int(input())):
    print(check(int(input())))

