def solution(park, routes):
    # 시작점 찾기
    for row,i in enumerate(park):
        for col,j in enumerate(i):
            if j=='S':
                start = [row,col]
                
    # 2차원 배열 생성
    graph = [[i for i in row] for row in park]
    h,w = len(park), len(park[0])
    
    # 규칙 수행
    for route in routes:
        op,n = route.split()
        
        if op=='E':
            if (start[1]+int(n) > w-1) | ('X' in graph[start[0]][start[1]:start[1]+int(n)+1]):
                continue
            start[1] = start[1]+int(n) 
            
        elif op=='W':
            if (start[1]-int(n) < 0) | ('X' in graph[start[0]][start[1]-int(n):start[1]+1]):
                continue
            start[1] = start[1]-int(n)
            
        elif op=='N':
            
            up = []
            i = 1
            while start[0]-i >= 0:
                if i > int(n):
                    break
                up.append(graph[start[0]-i][start[1]])
                i+=1
                
            if (start[0]-int(n) < 0) | ('X' in up):
                continue
            start[0] = start[0]-int(n)
            
        elif op=='S':
            
            down = []
            i = 1
            while start[0]+i <= h-1:
                if i > int(n):
                    break
                down.append(graph[start[0]+i][start[1]])
                i+=1
            # down = [graph[start[0]+i][start[1]] for i in range(int(n)+2)]
            if (start[0]+int(n) > h-1) | ('X' in down):
                continue
            start[0] = start[0]+int(n)
        
    answer = start
    return answer