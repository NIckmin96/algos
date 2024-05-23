def solution(dartResult):
    answer = 0
    lst = []
    score=''
    for i in dartResult:
        if i.isdigit():
            score+=i 
        else:
            if i=='*':
                try:
                    lst[-1] = 2*lst[-1]
                    lst[-2] = 2*lst[-2]
                except IndexError:
                    pass
            elif i=='#':
                try:
                    lst[-1] = -1*lst[-1]
                except IndexError:
                    pass
            else:
                lst.append(int(score))
                score=''
                if i=='D':
                    lst[-1]=lst[-1]**2
                elif i=='T':
                    lst[-1]=lst[-1]**3
        # print(lst)
                
    answer = sum(lst)
        
    return answer