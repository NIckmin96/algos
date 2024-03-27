def solution(elements):
    answer = 0
    lst = []
    tmp = elements+elements
    for i in range(1,len(elements)+1):
        if i==1:
            lst = lst+elements
        elif i==len(elements):
            lst.append(sum(elements))
        else:
            for j in range(len(elements)):
                lst.append(sum(tmp[j:j+i]))
    answer = len(set(lst))
    
    return answer