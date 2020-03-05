n,x =map(int,input().split())
num = list(map(int,input().split()))
sorted(num)
for i in num:
    if i<x:
        print(i,end =' ')