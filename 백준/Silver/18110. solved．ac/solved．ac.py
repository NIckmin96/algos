# solved.ac
import sys

def new_round(num):
    if num-int(num) >= 0.5:
        return int(num)+1
    else : 
        return int(num)

input = sys.stdin.readline
n = int(input())
lst = [int(input().strip()) for _ in range(n)]
if n == 0 : 
    res = 0
else : 
    # num_cut = int(round(n*0.15,0))
    num_cut = int(new_round(n*0.15))
    if num_cut > 0:
        new_lst = sorted(lst)[num_cut:-num_cut]
        # res = int(round(sum(new_lst)/len(new_lst),0))
        res = int(new_round(sum(new_lst)/len(new_lst)))
    else : 
        # res = int(round(sum(lst)/len(lst),0))
        res = int(new_round(sum(lst)/len(lst)))
print(res)