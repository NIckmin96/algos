def solution(n, words):
    answer = []
    res = 0
    for i,word in enumerate(words):
        if i==0:
            continue
        else:
            if (words[i-1][-1] != word[0]) | (word in words[:i]):
                res = i
                break
    
    if res == 0:
        answer = [0,0]
    else:
        num = (i+1)%n
        if num==0:
            num = n
            turn = (i+1)//n
        else:
            turn = (i+1)//n+1
        
        answer = [num,turn]

    return answer