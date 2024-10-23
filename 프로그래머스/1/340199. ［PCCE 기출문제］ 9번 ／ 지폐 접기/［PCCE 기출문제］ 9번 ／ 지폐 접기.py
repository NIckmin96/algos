def solution(wallet, bill):
    answer = 0
    max_w, min_w = max(wallet), min(wallet)
    max_b, min_b = max(bill), min(bill)
    while max_b>max_w or min_b>min_w:
        max_b, min_b = max([max_b//2, min_b]), min([max_b//2, min_b])
        answer+=1
        
    return answer