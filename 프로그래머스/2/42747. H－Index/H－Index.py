def solution(citations):
    answer = 0
    h=0
    lst = []
    upper_bound = sorted(citations)[len(citations)//2]
    while h<=upper_bound:
        more = [i for i in citations if i>=h]
        less = [i for i in citations if i<h]
        if (len(more)>=h)&(len(less)<=h):
            lst.append(h)
        h+=1
    answer = max(lst)
        
    return answer