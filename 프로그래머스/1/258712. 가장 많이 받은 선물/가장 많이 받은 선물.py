def solution(friends, gifts):
    answer = 0
    dic = {}
    res = {}
    gift_idx = {}
    for f in friends:
        dic[f] = dict()
        res[f] = res.get(f,0)
        gift_idx[f] = gift_idx.get(f,0)
    # key : 준사람 / value : {받은 사람 : 받은 개수}
    for gift in gifts:
        a,b = gift.split()
        dic[a][b] = dic[a].get(b,0)+1
    # print("dic :", dic)
    # 선물지수 구하기
    for give, get in dic.items():
        # 준만큼 더하기
        gift_idx[give]+=sum(get.values())
        # 받은만큼 빼기
        for k,v in get.items():
            gift_idx[k]-=v
    # print("gift idx :", gift_idx)
    
    for i in range(len(friends)):
        f1 = friends[i]
        for j in range(i+1,len(friends)):
            f2 = friends[j]
            # print(f1, f2)
            # 주고 받은 기록이 있는 경우
            if (f2 in dic[f1].keys()) or (f1 in dic[f2].keys()):
                # 두사람 사이에 선물을 준 개수 확인
                f1_give = dic[f1].get(f2,0)
                f2_give = dic[f2].get(f1,0)
                if f1_give>f2_give:
                    res[f1]+=1
                elif f1_give<f2_give:
                    res[f2]+=1
                # 개수가 같은 경우 지수 비교
                else:
                    if gift_idx[f1]>gift_idx[f2]:
                        res[f1]+=1
                    elif gift_idx[f1]<gift_idx[f2]:
                        res[f2]+=1
            # 기록 없는 경우
            else:
                # 지수 비교
                if gift_idx[f1]>gift_idx[f2]:
                        res[f1]+=1
                elif gift_idx[f1]<gift_idx[f2]:
                    res[f2]+=1
            # print(res)
    answer = max(res.values())
    
    return answer