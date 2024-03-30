def solution(n, left, right):
    answer = []
    # left, right가 각각 몇행 몇열인지 예측해서 만들기
    left_r = left//n+1
    left_c = left%n+1
    right_r = right//n+1
    right_c = right%n+1
    
    for i in range(left_r, right_r+1):
        tmp = list(range(1,n+1))
        for j in range(i):
            tmp[j]=i
            
        if (i==left_r)&(i==right_r):
            answer+=tmp[left_c-1:right_c]
        elif i==left_r:
            answer+=tmp[left_c-1:]
        elif i==right_r:
            answer+=tmp[:right_c]
        else:
            answer+=tmp
    
    # for i in range(left_r,right_r+1):
    #     if i ==left_r:
    #         # 행의 수 만큼 반복되는 수
    #         answer+=[left_r for _ in range(left_r-left_c+1)]
    #         # 그 뒤에 1씩 증가되어 N까지 가는 수
    #         answer+=[j for j in range(max(left_r+1,left_c),n+1)]
    #     elif i==right_r:
    #         # 행의 수 만큼 반복되는 수
    #         answer+=[right_r for _ in range(min(right_r, right_c))]
    #         # 그 뒤에 1씩 증가되어 right_c까지
    #         answer+=[j for j in range(right_r+1,right_c+1)]
    #     else:
    #         answer+=[i for _ in range(i)]
    #         answer+=[j for j in range(i+1,n+1)]
            
    return answer