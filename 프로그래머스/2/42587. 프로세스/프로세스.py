def solution(priorities, location):
    answer = 0
    from collections import deque
    processes = deque(list(zip(range(len(priorities)), priorities)))
    cnt = 1
    tmp = []
    while processes:
        process = processes.popleft()
        if processes:
            if process[1]<max(list(map(lambda x:x[1], list(processes)))):
                    processes.append(process)
            else:
                if process[0]==location:
                    answer=cnt
                    break
                else:
                    cnt+=1          
        else:
            answer=cnt
        
    return answer