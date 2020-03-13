n,m =map(int,input().split())
li = []
for _ in range(n):
    li.append(int(input()))

ans =0
for i in range(len(li)-1,-1,-1):
    if m //li[i] >0:
        ans +=m//li[i]
        m = m - (m//li[i])*li[i]
    if n ==0:
        break
print(ans)
