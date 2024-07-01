def solution(number, k):
    from collections import deque
    # stack의 마지막값이 push할 값보다 작은 경우에 Pop
    stack = []
    number = deque(list(number))
    while number:
        num = number.popleft()
        while stack and stack[-1]<num and k:
            stack.pop()
            k-=1
        stack.append(num)
    number = stack
    if k:
        number = number[:-k]
    # 앞에서부터 순회하면서, 뒤의수보다 작으면 빼기
    # n = len(number)
    # while k:
    #     for i in range(n-1):
    #         if number[i]<number[i+1]:
    #             del number[i]
    #             k-=1
    #             n-=1
    #             break
    #         # 끝까지 갔을때
    #         elif i==n-2:
    #             del number[n-1]
    #             k-=1
    #             n-=1

    return ''.join(number)