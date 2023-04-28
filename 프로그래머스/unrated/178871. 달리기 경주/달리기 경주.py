def solution(players, callings):
    
    a = {player:i for i,player in enumerate(players)} # player
    b = {i:player for i,player in enumerate(players)} # rank
    
    for call in callings:
        cur = a[call] # 이름 불린 선수의 등수
        pre = cur-1 # 이름 불린 선수의 앞 등수
        
        cur_player = b[cur]
        pre_player = b[pre]
        
        # 등수 변경(update)
        b[cur] = pre_player
        b[pre] = cur_player
        
        a[cur_player]-=1
        a[pre_player]+=1
    
    
    answer = list(b.values())
    return answer