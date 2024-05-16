def solution(record):
    answer = []
    id_nick = dict()
    for i in record:
        lst = i.split()
        act = lst[0]
        if act=='Enter':
            user_id, nickname = lst[1:]
            # answer.append(f"{user_id}님이 들어왔습니다.")
            id_nick[user_id] = nickname
        elif act=='Leave':
            user_id = lst[-1]
            # answer.append(f"{user_id}님이 나갔습니다.")
        else:
            user_id, nickname = lst[1:]
            id_nick[user_id] = nickname
            
    for i in record:
        lst = i.split()
        if lst[0]=='Enter':
            answer.append(f"{id_nick[lst[1]]}님이 들어왔습니다.")
        elif lst[0]=='Leave':
            answer.append(f"{id_nick[lst[1]]}님이 나갔습니다.")
        
    
    return answer