# 잃어버린 괄호
exp = input()
operators = []
minus_idx = []
for v in exp:
    if v in ['-','+']:
        operators.append(v)
exp = exp.replace('-',' ')
exp = exp.replace('+',' ')
nums = exp.split(' ')
# 음의 연산자 인덱스 구하기
for i,v in enumerate(operators):
    if v=='-':
        minus_idx.append(i)
lst = []
minus_res = []
# 음의 연산자 사이를 묶기
if len(minus_idx)==1:
    minus_res.append(list(map(int, nums[minus_idx[0]+1:])))
elif len(minus_idx)>1:
    for i,v in enumerate(minus_idx[:-1]):
        minus_res.append(list(map(int, nums[minus_idx[i]+1:minus_idx[i+1]+1])))
    minus_res.append(list(map(int,nums[minus_idx[-1]+1:])))
total_sum = sum(list(map(int, nums)))
minus_sum = sum(list(map(sum, minus_res)))
print(total_sum-minus_sum*2)