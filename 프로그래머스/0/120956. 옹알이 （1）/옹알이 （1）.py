def solution(babbling):
    from collections import deque
    answer = 0
    lst = ['aya','ye','woo','ma']
    for babble in babbling:
        tmp = ''
        babble = deque(list(babble))
        while babble:
            tmp+=babble.popleft()
            if tmp in lst:
                tmp = ''
        if tmp=='':
            answer+=1
    
    return answer