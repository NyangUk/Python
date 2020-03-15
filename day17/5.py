def solution(budgets, M):
    s = sum(budgets)//M-1
    while True:
        re =0
        s+=1
        for i in budgets:
            if i>s:
                re +=s
            else:
                re+=i
        if re>M:
            return s-1


def solution(budgets, M):
    b =list(sorted(budgets))
    re =0
    s =0
    for i in range(len(b)):
        if b[i]*len(b)>M:
            re =b[i]
            s=sum(b[:i])
            b =b[i:]
            print(s,b)
            break
    
    while True:
        re-=1
        if re*len(b)<=M-s:
            break
    return re


print(solution([120,110,140,150],485))
