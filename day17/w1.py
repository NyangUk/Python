i = int(input())

for _ in range(i):
    cnt =0
    n,m =map(int,input().split())
    re =[]
    for k in range(n):
        li =list(map(int,input().split()))
        cnt+=sum(li)
        re.append(li)
    if cnt ==0:
        print('YES')
        break
    elif cnt<4:
        print('NO')
        break
    for r in range(n-1):
        for j in range(m-1):
            # print(re)
            if re[r][j]==1 and re[r][j+1]==1 and re[r+1][j]==1 and re[r+1][j+1]==1:
                re[r][j]='.'
                re[r][j+1]='.'
                re[r+1][j]='.'
                re[r+1][j+1]='.'
            elif re[r][j]=='.' and re[r][j+1]==1 and re[r+1][j]=='.' and re[r+1][j+1]==1:
                re[r][j+1]='.'
                re[r+1][j+1]='.'
            elif re[r][j]=='.' and re[r][j+1]=='.' and re[r+1][j]==1 and re[r+1][j+1]==1:
                # print(3)
                re[r+1][j]='.'
                re[r+1][j+1] ='.'
                print(re)
            
    ans =0
    for i in range(n):
        for j in range(m):
            if re[i][j] =='.':
                ans+=1
    print(ans)
    if ans ==cnt:
        print('YES')
    else:
        print('NO')


