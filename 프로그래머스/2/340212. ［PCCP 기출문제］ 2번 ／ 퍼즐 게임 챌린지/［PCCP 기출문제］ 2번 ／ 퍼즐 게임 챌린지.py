def solution(diffs, times, limit):
    answer = 1e9
    left=1; right=max(diffs)
    while left<=right:
        time = 0
        level = (right+left)//2
        for i,diff in enumerate(diffs):
            
            if diff<=level:
                time+=times[i]
            else:
                time+=times[i]*(diff-level) # 틀린 퍼즐
                if i>0:
                    time+=times[i-1]*(diff-level)# 이전 퍼즐
                time+=times[i]# 다시 풀기
        # print(time)
        if time<=limit:
            answer = min(answer,level)
            right = level-1
        else:
            left = level+1
        
                
        
    return answer