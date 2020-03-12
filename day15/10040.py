n,m =map(int,input().split())
i= []
j=[]
re=[0]*n
for _ in range(n) :
    i.append(int(input()))
for _ in range(m) :
    j.append(int(input()))

for k in j:
    for r in range(len(i)):
        if k>=i[r]:
            re[r] +=1
            break

print(re.index(max(re))+1)