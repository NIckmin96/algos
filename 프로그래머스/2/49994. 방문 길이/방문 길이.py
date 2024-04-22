def solution(dirs):
    answer = 0
    x,y = 0,0
    # 출발, 도착 경로 리스트 저장
    lst = []
    for d in dirs:
        if d=='U':
            if (-5<=x<=5)&(-5<=y+1<=5):
                start = (x,y)
                end = (x,y+1)
                x,y = end
                if ([start,end] not in lst)&([end,start] not in lst):
                    lst.append([start,end])
        elif d=='D':
            if (-5<=x<=5)&(-5<=y-1<=5):
                start = (x,y)
                end = (x,y-1)
                x,y = end
                if ([start,end] not in lst)&([end,start] not in lst):
                    lst.append([start,end])
        elif d=='R':
            if (-5<=x+1<=5)&(-5<=y<=5):
                start = (x,y)
                end = (x+1,y)
                x,y = end
                if ([start,end] not in lst)&([end,start] not in lst):
                    lst.append([start,end])
        else:
            if (-5<=x-1<=5)&(-5<=y<=5):
                start = (x,y)
                end = (x-1,y)
                x,y = end
                if ([start,end] not in lst)&([end,start] not in lst):
                    lst.append([start,end])
    # print(lst)
    answer=len(lst)
            
    return answer