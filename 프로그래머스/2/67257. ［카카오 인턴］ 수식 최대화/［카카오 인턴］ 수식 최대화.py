def calculate(num1, num2, op):
    if op=='+':
        res = int(num1)+int(num2)
    elif op=='-':
        res = int(num1)-int(num2)
    else:
        res = int(num1)*int(num2)
    return res

def solution(expression):
    from itertools import permutations
    p_lst = list(permutations(['+','-','*'],3))
    answer = 0
    for p in p_lst: # 6
        exp = expression.replace('+', ' + ').replace('-', ' - ')\
        .replace('*',' * ').split(' ')
        # print(exp)
        for op in p:
            while op in exp:
                idx = exp.index(op)
                num1,num2 = exp[idx-1], exp[idx+1]
                res = calculate(num1, num2, op)
                exp = exp[:idx-1] + [str(res)] + exp[idx+2:]
        answer = max(answer, abs(int(exp[0])))
            
                
            
    
    
    return answer