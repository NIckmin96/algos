def check(uid, bid):
    if len(uid)!=len(bid):
        return False
    
    for i in range(len(bid)):
        if uid[i]!=bid[i] and bid[i]!='*':
            return False
        
    return True

def dfs(idx=0,lst=[]):
    if len(lst)==len(bannable):
        res.add(tuple(sorted(lst)))
        return 
    elif idx>=len(bannable):
        return
    
    for _id in bannable[idx]:
        if _id not in lst:
            dfs(idx+1,lst+[_id])

def solution(user_id, banned_id):
    global res, bannable
    answer = 0
    bannable = []
    for bid in banned_id:
        lst = []
        for uid in user_id:
            if check(uid, bid):
                lst.append(uid)
        bannable.append(lst)
    # print(bannable)
    res = set()
    dfs()
    answer = len(res)
                
    return answer