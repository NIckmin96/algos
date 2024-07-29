def solution(user_id, banned_id):
    # 똑같은 ban id가 여러개 있는 경우
    # ban id는 다른데 똑같은 id가 걸리는 경우
        # [**o*o, ***do] -> [[frodo, crodo],[frodo,crodo]]
    answer=0
    import re
    from itertools import permutations
    # 모든 조합 구하기
    answers = []
    for p in permutations(user_id, len(banned_id)):
        cnt = 0
        for i in range(len(p)):
            ban = banned_id[i].replace('*','.')
            if re.match(ban,p[i]) and len(ban)==len(p[i]):
                cnt+=1
        if cnt==len(banned_id):
            p = sorted(p)
            if p not in answers:
                answers.append(p)
                
    answer = len(answers)
    
    return answer