def solution(m, n, puddles):
    answer = 0
    dp = [[0]*m for _ in range(n)]
    dp[n-1][m-1]=1
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if dp[i][j] or [j+1,i+1] in puddles:
                # print(i,j)
                continue
            if i+1<n and j+1<m:
                dp[i][j]=dp[i+1][j]+dp[i][j+1]
            elif i+1<n and j+1>=m:
                dp[i][j]=dp[i+1][j]
            elif j+1<m and i+1>=n:
                dp[i][j]=dp[i][j+1]
    answer = dp[0][0]%1000000007
    print(dp)
    
    return answer