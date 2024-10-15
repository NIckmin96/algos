def solution(num, total):
    answer = []
    if total%num==0:
        middle = total//num
        for i in range(middle-num//2, middle+num//2+1):
            answer.append(i)
    else:
        middle = total/num
        left = int(middle-0.5)
        right = int(middle+0.5)
        for i in range(left-num//2+1, right+num//2):
            answer.append(i)
    return answer