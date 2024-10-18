def solution(n):
    answer = []
    # 첫번째 봉(start)에서 두번째 봉(middle)을 사용해 세번째 봉(end)에 n층의 탑을 세우기
    def hanoi(start, middle, end, n): 
        if n == 1:
            answer.append([start, end])
        else:
            # 첫번째 봉(start)에서 세번째 봉을 사용해(end) 두번째 봉(middle)에 n-1층의 탑을 세우기
            hanoi(start,end,middle,n-1) 
            # 첫번째 봉에서 세번째 봉으로 마지막 n층을 옮기기
            hanoi(start,middle,end,1) 
            # 두번째 봉에서(middle) 첫번째 봉을 사용해(start) 세번째 봉(end)으로 n-1층의 탑을 세우기
            hanoi(middle,start,end,n-1) 
            
    hanoi(1,2,3,n)
    
    return answer

# def solution(n):
#     answer = []
    
#     def func(n):
#         # n층의 결과값 만드는 함수
#         # n-1층
#         h = len(floor[n-1])//2
#         # n-1층의 절반
#         h1 = floor[n-1][:h]
#         h1 = [h1[0][::-1]]+h1[1:] # 첫번째 원소 반전
#         # 나머지 절반
#         h2 = floor[n-1][h:]
#         h2 = [h2[0][::-1]]+h2[1:] # 첫번째 원소 반전
#         n1 = h1+h2
#         # n-2층
#         n2 = floor[n-2]
#         # n층 결과
#         res = n2+n1+n2
#         return res
    
#     floor = [[] for _ in range(16)]
#     if n%2==0:
#         floor[1] = [[1,2]]
#         floor[2] = [[1,3],[2,3]]
        
#     else:
#         floor[1] = [[1,3]]
#         floor[2] = [[1,2],[3,2]]
#     for i in range(3,n+1):
#         floor[i] = func(i)
    
#     for i in range(n+1):
#         answer+=floor[i]
    
#     return answer