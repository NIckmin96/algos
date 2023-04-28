def solution(wallpaper):
    # graph = []
    answer = []
    # # 2d-array
    # for row in wallpaper:
    #     tmp = []
    #     for i in row:
    #         if i=='.':
    #             tmp.append(0)
    #         elif i=='#':
    #             tmp.append(1)
    #     graph.append(tmp)
        
    # 가장 바깥쪽 파일 찾기
    top = len(wallpaper)+1
    bottom = 0
    left = len(wallpaper[0])+1
    right = 0
    for i,row in enumerate(wallpaper):
        for j,col in enumerate(row):
            if wallpaper[i][j]=="#":
                top = min(top,i)
                bottom = max(bottom,i)
                left = min(left,j)
                right = max(right,j)
                
    # print(top)
    # print(left)
    # print(bottom)
    # print(right)
    
    answer.append(top)
    answer.append(left)
    answer.append(bottom+1)
    answer.append(right+1)
        
    return answer