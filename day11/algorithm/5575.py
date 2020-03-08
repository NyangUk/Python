t =[]
for i in range(3):
    li = list(map(int,input().split()))
    t.append(li)
# 0 1 2 3 4 5 
re = []
for i in range(3):
    rs=0
    rm=0
    rh=0
    s =t[i][5]-t[i][2]
    if s >=0:
        rs =s
        m =t[i][4]-t[i][1]
    else:
        rs=s+60
        m =t[i][4]-t[i][1]-1
    if m>=0:
        rm =m
        h =t[i][3]-t[i][0]
    else:
        rm= m+60
        h =t[i][3]-t[i][0]-1
    rh =h
    re.append([rh,rm,rs])
for i in re:
    for j in i:
        print(j,end =' ')
    print()

