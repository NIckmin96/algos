def solution(triangle):
    answer=0
    h = len(triangle)
    dp = [[0]*h for _ in range(h)]
    # 첫번째 행
    dp[0][0] = triangle[0][0]
    # 2~마지막 행
    for i in range(1,h):
        for j in range(len(triangle[i])):
            if j==0:
                dp[i][j] = dp[i-1][j]+triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])
    answer = max(dp[-1])
    return answer