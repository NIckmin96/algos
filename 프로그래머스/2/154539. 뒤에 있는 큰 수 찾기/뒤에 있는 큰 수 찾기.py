def solution(numbers):
    answer = [-1] * len(numbers)
    # 1. stack을 이용한 풀이
    # list구조에 append를 하게 되면 새로 들어온 데이터가 뒤에 쌓일 수 밖에 없기 때문에, LIFO구조의 stack을 사용하는 것이 옳은 접근으로 보임
    stack = []
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer