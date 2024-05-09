def solution(land):
    answer = 0
    # dp
    dp = [[0]*4 for _ in range(len(land))]
    dp[0] = land[0]
    for i in range(1,len(land)):
        for j in range(4):
            tmp = [dp[i-1][k]+land[i][j] for k in range(4) if k!=j]
            dp[i][j] = max(tmp)
    # print(dp)
    answer = max(dp[-1])
    return answer