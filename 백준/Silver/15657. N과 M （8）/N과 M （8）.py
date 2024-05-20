# N과 M (8)
n,m = map(int, input().split())
nums = sorted(list(map(int,input().split())))
def dfs(lst):
    if len(lst)==m:
        print((" ").join(map(str,lst)))
        return 
    else:
        idx = nums.index(lst[-1])
        for i in range(idx,n):
            dfs(lst+[nums[i]])
for i in nums:
    dfs([i])