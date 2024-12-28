from collections import deque

for _ in range(int(input())):
    pw_deque = deque()
    temp_stack = []
    for pw_char in input():
        if pw_char == '<':
            if len(pw_deque):        
                temp_stack.append(pw_deque.pop())
        elif pw_char == '>':
            if len(temp_stack):
                pw_deque.append(temp_stack.pop())
        elif pw_char == '-':
            if len(pw_deque):
                pw_deque.pop()
        else:
            pw_deque.append(pw_char)

    result = ''.join(pw_deque)
    temp_stack.reverse()
    result += ''.join(temp_stack)
    print(result)