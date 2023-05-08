def solution(n):
    answer = 0
    
    def binary(num):
        cnt = 0
        while True:
            if num%2==1:
                cnt+=1
            num = num//2
            if num==0:
                break
        return cnt
    
    before = binary(n)
    for i in range(n+1, 1000001):
        after = binary(i)
        if before == after:
            answer = i
            break
            
    return answer