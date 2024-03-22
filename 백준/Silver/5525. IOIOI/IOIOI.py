# IOIOI
n = int(input())
m = int(input())
s = input()
# p = ('O').join(['I']*(n+1))
# p와 일치하는지 확인
cnt=0
# for i,v in enumerate(s):
#     if v=='I':
#         if i+(2*n+1)<m:
#             if s[i:i+(2*n+1)]==p:
#                 cnt+=1
# 슬라이싱 없이
cnt_lst = [0]*m
for i,v in enumerate(s):
    if v=='I':
        if cnt_lst[i-1]:
            if s[i-1]=='O':
                cnt_lst[i]=cnt_lst[i-1]+1    
            else:
                cnt_lst[i]=1
        else:
            cnt_lst[i]=1
    else:
        if cnt_lst[i-1]:
            if s[i-1]=='I':
                cnt_lst[i]=cnt_lst[i-1]+1

for i in cnt_lst:
    if (i>=2*n+1)&(i%2==1):
        cnt+=1
            
print(cnt)