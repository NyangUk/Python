n = int(input())
li =[]
re=[]
for _ in range(n):
    li.append(int(input()))

li.sort()
li.reverse()
for i in range(1,n+1):
    re.append(li[i-1]*i)
print(max(re))