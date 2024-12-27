import sys

input = sys.stdin.readline
result_set = set()
for _ in range(int(input())):
    tag = input()[:-1].split(' ')
    if tag[1] == 'enter':
        result_set.add(tag[0])
    else:
        result_set.discard(tag[0])

for name in sorted(result_set, reverse=True):
    print(name)