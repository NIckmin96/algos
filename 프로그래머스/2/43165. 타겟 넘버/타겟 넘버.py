def solution(numbers, target):
    answer = 0
    # dfs
    stack = [(0,-1)]
    while stack:
        tmp, idx = stack.pop()
        idx+=1
        if idx<len(numbers):
            stack.append((tmp+numbers[idx],idx))
            stack.append((tmp-numbers[idx],idx))
        else:
            if tmp==target:
                answer+=1
    
    return answer