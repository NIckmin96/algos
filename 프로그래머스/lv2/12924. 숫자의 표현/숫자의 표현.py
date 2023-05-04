def solution(n):
    answer = 0
    # 약수 구하기
    odd = []
    root = int(n**0.5)+1
    for i in range(2,root):
        if n%i==0:
            if i%2!=0:
                odd.append(i)
            if (n//i)%2!=0:
                if i==n//i:
                    continue
                else:
                    odd.append(i)
    answer += len(odd)
    
    if n%2!=0:
        answer+=1
    answer+=1
    
    if n==1:
        answer=1
        
    return answer

# 홀수 : 무조건 2개 이상 / 약수 중, 홀수가 존재 -> +1
# 1: 1
# 2: 2
# 3: 1,2 / 3
# 4: 4
# 5: 2,3 / 5
# 6: 1,2,3 / 6
# 7: 3,4 / 7
# 8: 8
# 9: 2,3,4 / 4,5 / 9
# 10: (0,)1,2,3,4 / 10
# 11: 5,6 / 11
# 12: 3,4,5 / 12
# 13: 6,7 / 13