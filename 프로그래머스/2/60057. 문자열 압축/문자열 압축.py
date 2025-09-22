def solution(s):
    len_s = len(s)
    len_list = [len_s]
    for window_size in range(1, (len_s//2)+1):
        i_len = check(s, window_size, len_s)
        len_list.append(i_len)
    answer = min(len_list)
    return answer

def check(s, window_size, len_s):
    count = 0
    count_chk = []
    for i in range((len_s//window_size) - 1):
        if s[i*window_size:(i+1)*window_size] == s[(i+1)*window_size:(i+2)*window_size]:
            count += 1
        else:
            if count != 0:
                count_chk.append(count)
                count = 0

    if count != 0:
        count_chk.append(count)
                   
    minus_num = 0
    for count_i in count_chk:  
        if count_i >= 9: #count_i == 9면 10개가 겹쳐있음
            minus_num += (len(str(count_i+1))-1)
        
    return len_s - (sum(count_chk)*window_size) + len(count_chk) + minus_num


