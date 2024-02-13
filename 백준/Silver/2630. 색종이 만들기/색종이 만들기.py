# 색종이 만들기
import sys
input = sys.stdin.readline
n = int(input().strip())
paper = [input().strip().split() for _ in range(n)]
white, blue = 0,0

def divide_n_count(paper):
    global white, blue
    n = len(paper)
    tmp = []
    for row in paper:
        for i in row:
            tmp.append(i)
    if len(set(tmp))==1:
        if tmp[0]=='0':
            white+=1
        elif tmp[0]=='1':
            blue+=1
        return None
    a,b,c,d = [],[],[],[]
    a2,b2,c2,d2 = [],[],[],[]
    for row in paper[:n//2]:
        # 1사분면
        tmp = [row[i] for i in range(n//2)]
        a.append(tmp) # 2dim list
        a2 = a2+tmp # set
        # 2사분면
        tmp = [row[i] for i in range(n//2,n)]
        b.append(tmp) # 2dim list
        b2 = b2+tmp # set

    for row in paper[n//2:]:
        # 3사분면
        tmp = [row[i] for i in range(n//2)]
        c.append(tmp) # 2dim list
        c2 = c2+tmp # set
        # 4사분면
        tmp = [row[i] for i in range(n//2,n)]
        d.append(tmp) # 2dim list
        d2 = d2+tmp # set
    # print(set(a2),set(b2),set(c2),set(d2))
            
    for j,i in [(a,a2), (b,b2), (c,c2), (d,d2)]:
        if (len(i)==1)&(i[0]=='0'):
            white+=1
        elif (len(i)==1)&(i[0]=='1'):
            blue+=1
        elif (len(set(i))==1)&(i[0]=='0'):
            white+=1
        elif (len(set(i))==1)&(i[0]=='1'):
            blue+=1
        else:
            # print(j)
            divide_n_count(j)

divide_n_count(paper)
print(white)
print(blue)