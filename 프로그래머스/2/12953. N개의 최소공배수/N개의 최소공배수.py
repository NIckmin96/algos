def solution(arr):
    answer = 1
    def func(arr, answer):
        for i in range(2,sorted(arr)[-2]+1):
            tmp = [True if num%i==0 else False for num in arr]
            if sum(tmp)>1:
                answer=answer*i
                arr = [int(num/i) if num%i==0 else num for num in arr]
                return func(arr,answer)
        return arr, answer
    
    arr, answer=func(arr,answer)
    for num in arr:
        answer*=num
            
    return answer