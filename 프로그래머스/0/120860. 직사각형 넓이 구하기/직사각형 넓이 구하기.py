def solution(dots):
    answer = 1
    dic = {}
    for x,y in dots:
        if x in dic.keys():
            dic[x].append(y)
        else:
            dic[x] = [y]
            
    h1,h2 = list(dic.values())[0]
    height = abs(h1-h2)
    w1,w2 = dic.keys()
    width = abs(w1-w2)
    
    answer*=height
    answer*=width
    
    return answer