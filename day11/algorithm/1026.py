n = int(input())
a= list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
sum =0
for i in a:
    sum =sum+i*max(b)
    del b[b.index(max(b))]
print(sum)
