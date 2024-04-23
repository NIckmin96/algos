def solution(topping):
    from collections import Counter
    answer = 0
    a = set()
    b = set(topping)
    counter = Counter(topping)
    while topping:
        if len(a)==len(b):
            answer+=1
        p = topping.pop()
        
        a.add(p)
        if counter[p]:
            counter[p]-=1
            if counter[p]<1:
                b.discard(p)
        # print(a,b)
    
    return answer