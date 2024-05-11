def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        tmp = []
        for i,s in enumerate(skill):
            idx = tree.find(s)
            tmp.append(idx)
        
        while tmp and tmp[-1]==-1:
            tmp.pop()
            
        if not tmp:
            answer+=1
        else:
            if (-1 not in tmp) and(tmp==sorted(tmp)):
                answer+=1
            
    return answer