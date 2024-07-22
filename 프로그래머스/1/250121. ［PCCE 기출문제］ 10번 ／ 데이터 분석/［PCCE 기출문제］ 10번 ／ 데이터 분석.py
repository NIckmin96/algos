def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    col_to_idx = {'code':0,
                 'date':1,
                 'maximum':2,
                 'remain':3}
    # ext<val_ext & sort
    answer = sorted([i for i in data if i[col_to_idx[ext]]<val_ext], key=lambda x:x[col_to_idx[sort_by]])
    return answer