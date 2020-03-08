sv = list(map(float,input().split()))
n =int(input())
k = []
re =[]
for i in range(n):
    li = list(map(float,input().split()))
    k.append(li)

x=1000/sv[1]
re.append(x*sv[0])

for i in range(n):
    x =1000/k[i][1]
    re.append(x*k[i][0])

print('%0.2f' %min(re))

