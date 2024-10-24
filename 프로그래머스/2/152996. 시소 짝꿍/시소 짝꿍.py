def solution(weights):
    from collections import deque
    answer = 0
    
    pair = [2/2, 2/3, 3/2, 2/4, 4/2, 3/4, 4/3]
    count_dic = dict(zip(range(100, 1000+1), [0]*len(range(100, 1000+1))))
    for num in weights:
        count_dic[num]+=1
        
    weights = deque(weights)
    while weights:
        w = weights.popleft()
        count_dic[w]-=1
        tmp = list(map(lambda x:x*w, pair))
        for i in tmp:
            if 100<=i<=1000 and int(i)==i:
                answer+=count_dic[int(i)]
    
    return answer