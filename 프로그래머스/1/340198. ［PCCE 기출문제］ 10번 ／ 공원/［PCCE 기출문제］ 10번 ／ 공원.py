def solution(mats, park):
    answer = -1
    n,m = len(park), len(park[0])
    for mat in sorted(mats, reverse=True):
        for i in range(n):
            for j in range(m):
                if park[i][j]=='-1':
                    cnt = 0
                    for k1 in range(i,min(n,i+mat)):
                        for k2 in range(j,min(m,j+mat)):
                            if park[k1][k2]=='-1':
                                cnt+=1
                            else:
                                break
                    if cnt==mat**2:
                        answer = mat
                        return answer
    return answer