def solution(sticker):
    answer = 0
    # dp(점화식)
    if len(sticker)<=2:
        return max(sticker)
    # 0부터 시작
    dp = [0]*(len(sticker)-1)
    for i,v in enumerate(sticker[:-1]):
        dp[i]=max(dp[i-2]+v, dp[i-1])
    answer = max(answer, dp[-1])
    # 1부터 시작
    dp = [0]*(len(sticker)-1)
    for i,v in enumerate(sticker[1:]):
        dp[i]=max(dp[i-2]+v, dp[i-1])
    answer = max(answer, dp[-1])
    
        
    return answer