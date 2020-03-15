def solution(progresses, speeds):
    p=list(reversed(progresses))
    s=list(reversed(speeds))
    cnt =0
    flag =0
    answer = []
    while len(p)>0:
        cnt+=1
        for i in range(len(p)):
            p[i] +=s[i]
        # print(p)
        for j in range(len(p)):
            if p[len(p)-1]>=100:
                p.pop()
                flag+=1
        if flag >0:
            answer.append(flag)
            flag =0
    # print(answer)
    return answer
