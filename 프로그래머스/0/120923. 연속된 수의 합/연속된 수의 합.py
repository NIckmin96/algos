def solution(num, total):
    # 수식적 풀이
    start = total/num-(num-1)/2
    answer = [start+i for i in range(num)]
        
    
    # answer = []
    # if total%num==0:
    #     middle = total//num
    #     for i in range(middle-num//2, middle+num//2+1):
    #         answer.append(i)
    # else:
    #     middle = total/num
    #     left = int(middle-0.5)
    #     right = int(middle+0.5)
    #     for i in range(left-num//2+1, right+num//2):
    #         answer.append(i)
    return answer