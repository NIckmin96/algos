def solution(begin, target, words):
    answer = 1e9
    limit=10
    def bfs(start,target,visited,cnt):
        nonlocal answer
        if start==target:
            answer=min(answer,cnt)
            return 
        
        for word in words:
            diff = 0
            for i in range(len(word)):
                if start[i]!=word[i]:
                    diff+=1
            if diff==1 and not visited[word]:
                visited[word]=True
                bfs(word,target,visited,cnt+1)
                visited[word]=False

    visited = {word:False for word in words}
    if target not in words:
        answer=0
    else:
        bfs(begin,target,visited,0)
        
    return answer