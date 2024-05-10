def solution(n, s):
    answer = []
    if n>s:
        answer.append(-1)
    # n의 배수 중 s와 가장 가까운 수 x를 찾아 x/n을 구한뒤, x/n으로 최대한 채우고 부족한 만큼 추가
    else:
        div,mod = divmod(s,n)
        answer = [div]*n
        for i in range(1,mod+1):
            answer[-i]+=1
    
    return answer