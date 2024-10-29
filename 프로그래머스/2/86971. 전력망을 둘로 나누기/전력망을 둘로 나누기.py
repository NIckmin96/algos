def solution(n, wires):
    from collections import deque
    
    answer = 1e9
    wires = deque(wires)
    for _ in range(n-1):
        wire = wires.popleft()# 연결 끊을 부분
        # print(wire)
        tower_a = set()
        visited = set()
        # 겹치는 부분끼리 묶기(bfs)
        q = deque([wires[0]])
        visited.add(tuple(wires[0]))
        tower_a = tower_a.union(set(wires[0]))
        # print(tower_a)
        while q:
            v1,v2 = q.popleft()
            v1_lst,v2_lst = [tuple(w) for w in wires if v1 in w], [tuple(w) for w in wires if v2 in w]
            for w in v1_lst+v2_lst:
                if w not in visited:
                    q.append(w)
                    visited.add(w)
                    tower_a = tower_a.union(set(w))
                    
            # print(tower_a)
        
            
        
        wires.append(wire)
        tower_b = set(range(1,n+1))-tower_a
        # print(tower_a)
        # print(tower_b)
        answer = min(abs(len(tower_a)-len(tower_b)), answer)
    
    return answer