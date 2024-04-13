def solution(word):
    answer = 0
    lst = []
    for i in ['A','E','I','O','U']:
        tmp = [i]
        while tmp:
            letter = tmp.pop()
            if len(letter)>=5:
                lst.append(letter)
                continue
            else:
                lst.append(letter)
                
            for j in ['A','E','I','O','U','']:
                if j=='':
                    continue
                tmp.append(letter+j)
    
    dic = {v:i for i,v in enumerate(sorted(list(set(lst))))}
    answer=dic[word]+1
                    
    return answer