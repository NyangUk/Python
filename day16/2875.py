n,m,k = map(int,input().split())
cnt =0
#16 4 2
f =0
while True:
    if cnt>=k:
        break
    if n>m*2:
        f=0
        if n >m*2:
            n=n-1
            cnt+=1
        elif n<=m*2:
            m=m-1
            n=n-2
            cnt+=3
    else:
        f=1
        if n//2<m:
            m=m-1
            cnt+=1
        elif n//2 >=m:
            m=m-1
            n=n-2
            cnt+=3

if f==1:
    print(n//2)
else:
    print(m)
