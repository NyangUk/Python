n=int(input()) #테스트 케이스
for _ in range(n):
    re =[]
    ans1 =0
    ans2 =0
    m=int(input()) 
    for _ in range(m):
        li =list(map(float,input().split()))
        re.append(li)
    for i,j in re:
        ans1 +=i
        ans2 =ans2+ i*j

    print('%d %0.1f' %(ans1,(ans2/ans1)))