def solution(n):
    answer = 0
    lst = [1]*(n+1)
    lst[1]=1
    for i in range(2,n+1):
        lst[i]=lst[i-2]+lst[i-1]
    answer=lst[n]%1234567
    return answer