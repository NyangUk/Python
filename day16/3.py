def solution(answers):
    sa =[1,2,3,4,5]*2000
    sb =[2,1,2,3,2,4,2,5]*2000
    sc =[3,3,1,1,2,2,4,4,5,5]*1000
    answer = [] 
    re=[0,0,0]

    for i in range(len(answers)):
        if sa[i]==answers[i]:
            re[0] +=1
        if sb[i]==answers[i]:
            re[1] +=1
        if sc[i]==answers[i]:
            re[2] +=1
    print(re)
    for i in range(3):
        if re[i] ==max(re):
            answer.append(i+1)
   
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))
