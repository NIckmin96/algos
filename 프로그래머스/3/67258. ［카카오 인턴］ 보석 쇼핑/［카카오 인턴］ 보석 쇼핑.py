def solution(gems):
    answer = [0,1e9]
    start,end = 0,0
    gem_dict = dict()
    nunique = len(set(gems))
    while start<len(gems) and end<len(gems):
        gem = gems[end]
        gem_dict[gem] = gem_dict.get(gem,0)+1
        # print(gem_dict)
        if len(gem_dict)==nunique:
            if end-start<answer[1]-answer[0]:
                answer = [start+1, end+1]
            elif start<answer[0]:
                answer = [start+1, end+1]
            # print(answer)
                
            for i in range(start,end+1):
                gem = gems[i]
                gem_dict[gem]-=1
                
                if gem_dict[gem]==0:
                    del gem_dict[gem]
                    start=i+1
                    break
                else:
                    
                    if end-(i+1)<answer[1]-answer[0]:
                        answer = [i+2, end+1]
                    elif i+1<answer[0]:
                        answer = [i+2, end+1]
                    # print(answer)
            
        end+=1
        
    return answer