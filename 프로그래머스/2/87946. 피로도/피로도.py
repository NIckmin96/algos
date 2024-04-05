def solution(k, dungeons):
    answer = []
    dungeons = [d for d in dungeons if d[0]<=k]
    # 완전 탐색 접근(최대 : 8*7*6*8)
    from itertools import permutations
    for i in permutations(dungeons, len(dungeons)):
        k_cp = k
        cnt = 0
        for a,b in i:
            if a<=k_cp:
                k_cp-=b
                cnt+=1
            else:
                continue
        answer.append(cnt)
    # print(answer)
    
    return max(answer)