def solution(n, k):
    from math import factorial
    from itertools import permutations
    answer = []
    nums = list(range(1,n+1))
    # n-1명을 세우는 경우의 수
    f = n
    while k>1 and f>0:
        if k >= factorial(f):
            # print("factorial num :", f)
            # print("facotrial res :", factorial(f))
            div, k = divmod(k,factorial(f))
            # print(div,k)
            nums = sorted(list(set(nums)-set(answer)))
            # 고정 자리수 추가
            tmp = len(nums)-(f+1)
            if tmp<0:
                a = []
            else:
                a = nums[:tmp]
            answer += a
            # print(answer)
            nums = sorted(list(set(nums)-set(answer)))
            # div,k에 따라 변화하는 숫자 추가
            if nums:
                if k>0:
                    answer.append(nums[div])
                else:
                    answer.append(nums[div-1])
                nums = sorted(list(set(nums)-set(answer)))
            else:
                break
                    
            # print(answer)
            
        f-=1
        
    perms = list(permutations(nums,len(nums)))
    answer+=perms[k-1]
    
    return answer