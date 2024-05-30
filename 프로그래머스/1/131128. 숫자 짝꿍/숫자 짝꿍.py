def solution(X, Y):
    xy = set(X)&(set(Y))
    if not xy:
        return "-1"
    elif xy==set("0"):
        return "0"
    else:
        lst = [i*min(X.count(i), Y.count(i)) for i in xy]
        return ('').join(sorted(lst,reverse=True))
    
#     inter = set(X).intersection(set(Y))
#     if not inter:
#         return "-1"
    
#     lst = [i*min(X.count(i), Y.count(i)) for i in inter]
#     return str(int(('').join(sorted(lst,reverse=True))))