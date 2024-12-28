N = int(input())
expr = input()
operand_st = []
operand_dict = {}
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(N):
    operand_dict[alphabet[i]] = int(input())

for exp in expr:
    if exp == '+':
        operand_1 = operand_st.pop()
        operand_2 = operand_st.pop()
        operand_st.append(operand_2 + operand_1)
    elif exp == '-':
        operand_1 = operand_st.pop()
        operand_2 = operand_st.pop()
        operand_st.append(operand_2 - operand_1) 
    elif exp == '*':
        operand_1 = operand_st.pop()
        operand_2 = operand_st.pop()
        operand_st.append(operand_2 * operand_1)
    elif exp == '/':
        operand_1 = operand_st.pop()
        operand_2 = operand_st.pop()
        operand_st.append(operand_2 / operand_1)
    else:
        operand_st.append(operand_dict[exp])

print(f'{operand_st[0]:.2f}')    
