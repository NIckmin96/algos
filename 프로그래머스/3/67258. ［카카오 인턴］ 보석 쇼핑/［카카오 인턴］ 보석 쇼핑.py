def solution(gems):
    gem_dict = dict()
    nunique = len(set(gems))
    answer = [1,1e9]
    start, end = 1,len(gems)
    for idx,gem in enumerate(gems):
        gem_dict[gem] = idx+1
        if gem==gems[start-1]:
            start = min(gem_dict.values())
        
        if len(gem_dict)==nunique:
            end = idx+1
            if end-start<answer[1]-answer[0]:
                answer = [start, end]
            elif start<answer[0]:
                answer = [start, end]
        
            

    return answer