def solution(food):
    answer = ''
    for i,v in enumerate(food):
        if i==0:
            continue
        v = v//2
        answer+=(str(i)*v)
    rear = answer[::-1]
    answer+='0'
    answer+=rear
    return answer