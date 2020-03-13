def solution(n, words):
    li =words #리스트형태 
    ch =li[0]
    dic = set()
    dic.add(ch)
    cnt=1 #등수 1 2 3 4 5 6 7 8 9 
    # 0 1 2 3 4 5 6 7 8 9
    f =1
    a =[]
    for i in range(1,len(li)):
        cnt+=1
        print(cnt)
        if cnt%n==0:
            a.append(1)
    
        if li[i] not in dic:
            re = li[i]
            if ch[len(ch)-1] == re[0]:
                ch= li[i]
                dic.add(li[i])
                print(li[i])
        else:
            print(ch)
            f= 0
            break

    if f ==0:
        if cnt%n ==0:
            return [n,sum(a)]
        else:
            return [cnt%n,sum(a)]
    else:
        return [0,0]

        
    return answer
# li =['tank', 'kick', 'kiw', 'wheek', 'kifcd', 'dream', 'mother', 'robot', 'tank']
li2 =['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']
print(solution(5,li2))