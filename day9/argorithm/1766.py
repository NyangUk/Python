# 16:00 
# 13
n,m =map(int,input().split())
good = []

for i in range(m):
    fi,la = map(int,input().split())
    good.append([fi,la])

good.sort()

for i,j in good:
    print(i,j,end=' ')