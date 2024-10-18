def solution(sides):
    answer = 0
    # 1. 배열외의 변이 가장 길 경우
    answer+=(sum(sides)-max(sides))
    # 2. 배열 안의 가장 긴 변이 가장 길 경우
    answer+=(max(sides)-(max(sides)-min(sides))-1)
    return answer