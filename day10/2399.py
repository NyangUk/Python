x =[]
n = int (input())
x =list(map(int,input().split()))
result =0
x.sort()
x.reverse()

for i in range(n):
    for j in range(i,n):
        result+=x[i]-x[j]
print(result*2)