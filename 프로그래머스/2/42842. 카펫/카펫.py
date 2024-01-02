def solution(brown, yellow):
    answer = []
    total = brown+yellow
    weak_nums = []
    for i in range(2,int(total**0.5)+1):
        if total%i==0:
            weak_nums.append([total//i, i])
    # print(weak_nums)
    
    for nums in weak_nums:
        x,y = nums
        if (x-2)*(y-2)==yellow:
            break
            
    answer.append(x)
    answer.append(y)
        
        
    return answer