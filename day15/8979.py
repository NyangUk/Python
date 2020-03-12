n,m =map(int, input().split())
re =[]
for _ in range(n):
    li= list(map(int,input().split()))
    if li[0] == m:
        k= li[:]
    else:
        re.append(li)
ans =1
for i in range(n-1):
    if k[1]<re[i][1]:
        ans+=1
    elif k[1]==re[i][1]:
        if k[2]<re[i][2]:
            ans+=1
        elif k[2]==re[i][2]:
            if k[3]<re[i][3]:
                ans+=1

print(ans)