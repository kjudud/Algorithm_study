from itertools import combinations

sum_result = []
result = []
T_n = [int(i*(i+1)/2) for i in range(1, 46)]*3

for i in combinations(T_n, 3):
    sum_result.append(sum(i))

for _ in range(int(input())):
    result.append(1 if int(input()) in sum_result else 0)

for i in result:
    print(i)
