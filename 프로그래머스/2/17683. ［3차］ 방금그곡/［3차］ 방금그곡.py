def solution(m, musicinfos):
    from collections import deque
    answer = '(None)'
    max_len = 0
    
    # m정확히 구하기(# 구분)
    m_cp = deque(list(m).copy())
    m = []
    while m_cp:
        tmp = m_cp.popleft()
        if tmp=='#':
            m[-1] = ''.join([m[-1],tmp])
        else:
            m.append(tmp)
    len_m = len(m)    
    str_m = ''.join(m)
    
    # main
    for music in musicinfos:
        start, end, name, melody = music.split(',')
        _h,_m = start.split(':')
        start = int(_h)*60+int(_m)
        _h,_m = end.split(':')
        if _h=='00' and _m=='00':
            end = 24*60
        else:
            end = int(_h)*60+int(_m)
        t_diff = end-start
        
        # melody길이 정확히 구하기(# 붙은 경우 구분)
        melody_cp = deque(list(melody).copy())
        melody = []
        while melody_cp:
            tmp = melody_cp.popleft()
            if tmp=='#':
                melody[-1] = ''.join([melody[-1],tmp])
            else:
                melody.append(tmp)
        len_melody=len(melody)
        
        # radio에서 들은 멜로디 복원
        if t_diff<=len_melody:
            radio=melody
        else:
            div,mod = divmod(t_diff,len_melody)
            radio=melody*div+melody[:mod]
        print(radio)
        
        # radio에서 들은 멜로디와 기억하는 멜로디가 일치하는지 확인
        for i in range(0,len(radio)-len(m)+1):
            str_radio = ''.join(radio[i:i+len(m)])
            # print(str_m)
            # print(str_radio)
            if str_m==str_radio:
                if answer!='(None)':
                    if max_len<t_diff: # 재생 시간이 긴 경우, update
                        max_len = t_diff
                        answer = name
                    else: # 재생 시간 같거나 짧은 경우 현재 answer 유지
                        pass
                        
                else: # 처음인 경우
                    max_len = t_diff
                    answer = name
                break
        
    return answer