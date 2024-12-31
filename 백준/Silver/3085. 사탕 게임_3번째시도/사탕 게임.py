# def search_max_concord(candy_matrix):
#     # 행에서 오른쪽으로 연속된 길이 찾기
#     concord_len_list = []
#     max_concord_len = 0
#     for i in range(2, N+2):
#         j = 2
#         while j < N+2:
#             concord_len = 0
#             for k in range(1, N+2-j):
#                 if candy_matrix[i][j] == candy_matrix[i][j+k]:
#                     concord_len += 1
#                 else:
#                     # 행 방향에서 일치 길이 찾기인 경우 concord_len_list[?][3] = 0, 
#                     # 열방향인 경우 concord_len_list[?][3] = 1
#                     concord_len_list.append([concord_len, i, j, 0])
#                     break
#             if concord_len > max_concord_len:
#                 max_concord_len = concord_len
#             j += (concord_len+1)
            
#     for j in range(2, N+2):
#         i = 2
#         while i < N+2:
#             concord_len = 0
#             for k in range(1, N+2-i):
#                 if candy_matrix[i][j] == candy_matrix[i+k][j]:
#                     concord_len += 1
#                 else:
#                     # 행 방향에서 일치 길이 찾기인 경우 concord_len_list[?][3] = 0, 
#                     # 열방향인 경우 concord_len_list[?][3] = 1
#                     concord_len_list.append([concord_len, i, j, 1])
#                     break
#             if concord_len > max_concord_len:
#                 max_concord_len = concord_len
#             i += (concord_len+1)
#     return concord_len_list, max_concord_len


# N = int(input())
# candy_matrix = []
# candy_matrix.append(['X' for _ in range(N+4)])
# candy_matrix.append(['X' for _ in range(N+4)])
# for _ in range(N):
#     candy_matrix.append(['X', 'X'] + list(input()) + ['X', 'X'])
# candy_matrix.append(['X' for _ in range(N+4)])
# candy_matrix.append(['X' for _ in range(N+4)])

# concord_len_list, max_concord_len = search_max_concord(candy_matrix)

# result = max_concord_len
# for conc in concord_len_list:
#     conc_len = conc[0]
#     i = conc[1]
#     j = conc[2]
#     if conc_len == max_concord_len:
#         if conc[3] == 0:
#             row_conc = (candy_matrix[i][j] == candy_matrix[i][j+conc_len+2])
#             col_conc_1 = (candy_matrix[i][j] == candy_matrix[i+conc_len-1][j+1])
#             col_conc_2 = (candy_matrix[i][j] == candy_matrix[i+conc_len+1][j+1])
#             if row_conc and (col_conc_1 or col_conc_2):
#                 result = max_concord_len + 2
#                 break
#             elif row_conc or col_conc_1 or col_conc_2:
#                 result = max_concord_len + 1
#         else:
#             col_conc = (candy_matrix[i][j] == candy_matrix[i+conc_len+2][j])
#             row_conc_1 = (candy_matrix[i][j] == candy_matrix[i+conc_len+1][j-1])
#             row_conc_2 = (candy_matrix[i][j] == candy_matrix[i+conc_len+1][j+1])
#             if col_conc and (row_conc_1 or row_conc_2):
#                 result = max_concord_len + 2
#                 break
#             elif col_conc or row_conc_1 or row_conc_2:
#                 result = max_concord_len + 1
#     if result == max_concord_len + 1:
#         break
#     elif conc_len == max_concord_len-1:
#         if conc[3] == 0:
#             row_conc = (candy_matrix[i][j] == candy_matrix[i][j+conc_len+2])
#             col_conc_1 = (candy_matrix[i][j] == candy_matrix[i+conc_len-1][j+1])
#             col_conc_2 = (candy_matrix[i][j] == candy_matrix[i+conc_len+1][j+1])
#             if row_conc and (col_conc_1 or col_conc_2):
#                 result = max_concord_len + 1
#                 break
#         else:
#             col_conc = (candy_matrix[i][j] == candy_matrix[i+conc_len+2][j])
#             row_conc_1 = (candy_matrix[i][j] == candy_matrix[i+conc_len+1][j-1])
#             row_conc_2 = (candy_matrix[i][j] == candy_matrix[i+conc_len+1][j+1])
#             if col_conc and (row_conc_1 or row_conc_2):
#                 result = max_concord_len + 1
#                 break

# print(result+1)

N = int(input())
candy_matrix = [list(input()) for _ in range(N)]
result = 1

def confirm(candy_matrix):
    output = 0
    for i in range(N):
        concord = 1
        for j in range(1,N):
            if candy_matrix[i][j-1] == candy_matrix[i][j]:
                concord += 1
                if concord > output:
                    output = concord
            else:
                concord = 1
    for j in range(N):
        concord = 1
        for i in range(1, N):
            if candy_matrix[i-1][j] == candy_matrix[i][j]:
                concord += 1
                if concord > output:
                    output = concord
            else:
                concord = 1
    return output

for i in range(N):
    for j in range(N):
        if j > 0:
            candy_matrix[i][j], candy_matrix[i][j-1] = candy_matrix[i][j-1], candy_matrix[i][j]
            output = confirm(candy_matrix)
            if output > result:
                result = output 
            candy_matrix[i][j], candy_matrix[i][j-1] = candy_matrix[i][j-1], candy_matrix[i][j]

        if i > 0:
            candy_matrix[i][j], candy_matrix[i-1][j] = candy_matrix[i-1][j], candy_matrix[i][j]
            output = confirm(candy_matrix)
            if output > result:
                result = output 
            candy_matrix[i][j], candy_matrix[i-1][j] = candy_matrix[i-1][j], candy_matrix[i][j]

print(result)
