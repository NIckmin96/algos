def solution(numbers):
    answer = []
    for num in numbers:
        # 짝수 -> 홀수 : 바로 다음 수
        if num%2==0:
            answer.append(num+1)
        # 홀수 -> 짝수
        else:
            cnt=1
            div = num
            while div:
                div,mod = divmod(div,2)
                if mod==0:
                    break
                cnt+=1
                # print(div,mod,cnt)
            # 011 -> 101 / 0111 -> 1011 / 01111 -> 10111 ... 
            cnt = max(2,cnt)
            answer.append(num+2**(cnt-2))
    
    return answer