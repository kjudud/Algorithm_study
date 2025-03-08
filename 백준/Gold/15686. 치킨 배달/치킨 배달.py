## 치킨집의 거리를 구할때 BFS로 구하면 한 집당 O(N**2)의 시간이 걸릴 수 있음, 맨해튼거리로 구하면 O((최소값 비교)*치킨집의 개수)
from itertools import combinations

def get_chk_dist(chickens_comb):
    chk_dist = 0
    for house in houses:
        temp_dist = 2 * N
        # chickens_comb는 조합 tuple iterator
        for chicken in chickens_comb:
            temp_dist = min(temp_dist, (abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])))
        chk_dist += temp_dist
    return chk_dist

N, M = map(int, input().split())
city_map = [list(map(int, input().split())) for _ in range(N)]
houses = []
chickens = []
answer = float('inf')
for i in range(N):
    for j in range(N):
        what = city_map[i][j]
        if what == 1:
            houses.append((i, j))
        elif what == 2:
            chickens.append((i, j))

for chickens_comb in combinations(chickens, M):
    answer = min(answer, get_chk_dist(chickens_comb))
print(answer)