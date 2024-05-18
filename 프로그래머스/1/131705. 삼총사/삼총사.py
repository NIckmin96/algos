def solution(number):
    answer = 0
    from itertools import combinations
    for comb in combinations(number,3):
        if sum(comb)==0:
            answer+=1
    return answer