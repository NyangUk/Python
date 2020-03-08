n,m=map(int,input().split())
l =[]
for _ in range(n):
    l.append(int(input()))
cnt = []
sum =0
for i in l:
    re = 0
    while re<m:
        if re in cnt:
            re +=i
        else:
            sum +=1           
            re +=i


n,c=map(int,input().split())
t=[0]*(c+1)
for _ in range(n):
    i=int(input())
    for j in range(i,c+1,i):t[j]=1
print(sum(t))

