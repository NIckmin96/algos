def solution(genres, plays):
    answer = []
    genre_idx = {}
    genre_plays = {}
    idx_plays = {}
    for i,v in enumerate(genres):
        # genre-idx
        if v not in genre_idx.keys():
            genre_idx[v] = [i]
        else:
            genre_idx[v].append(i)
        # genre-plays(sum)
        if v not in genre_plays.keys():
            genre_plays[v] = plays[i]
        else:
            genre_plays[v] += plays[i]
        # idx-plays
        idx_plays[i]=plays[i]
        
    for genre,play in sorted(genre_plays.items(), key=lambda x:-x[1]):
        # sort by plays&idx
        answer+=sorted(genre_idx[genre], key=lambda x:[-idx_plays[x],x])[:2]
    
    return answer