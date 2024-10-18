def solution(dots):
    # 기울기 구하기(점 한번씩만 사용할 수 있음)
    lst = []
    x0,y0 = dots[0]
    for i in range(1,4):
        x1,y1 = dots[i]
        slope1 = (y1-y0)/(x1-x0)
        
        lst = list(range(1,4))
        lst.remove(i)
        x2,y2 = dots[lst[0]]
        x3,y3 = dots[lst[1]]
        slope2 = (y3-y2)/(x3-x2)
        
        if slope1==slope2:
            return 1
    return 0
        
        