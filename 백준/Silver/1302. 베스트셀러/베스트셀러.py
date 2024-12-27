import sys

input = sys.stdin.readline
selling_record = {}
for _ in range(int(input())):
    book_name = input()
    if book_name in selling_record:
        selling_record[book_name] += 1
    else:
        selling_record[book_name] = 1
max_value = 0
for k,v in selling_record.items():
    if v > max_value:
        max_value = v
        result = [k]
    elif v == max_value:
        result.append(k)
        
print(sorted(result)[0])

