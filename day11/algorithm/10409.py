n,m = map(int,input().split())
time = list(map(int,input().split()))
sum = 0
re =0
print(time)
for i in time:
    sum+=i
    if sum>m:
        continue
    else:
        re+=1
print(re)

