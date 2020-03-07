n,m = map(int,input().split())
info = []

for i in range(n):
    info.append(list(input()))

go =0

for i in range(n):
    for j in range(m):
        if go > 0:
            if info[i][j] =='c':
                info[i][j] =0
                go =1
            else:
                info[i][j] =go
                go +=1
        else:
            if info[i][j] =='c':
                info[i][j] =0
                go=1
            else:
                info[i][j] =-1
    go = 0

for i in info:
    for j in i:
        print(j,end=' ')
    print('')