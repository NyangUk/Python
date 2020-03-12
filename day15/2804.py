n,m = list(input().split())
re =[]
for _ in range(len(m)):
    li =['.']*len(n)
    re.append(li)
a=0
b=0
cnt=0

for i in range(len(n)):
    for j in range(len(m)):
        if n[i] == m[j]:
            a,b =i,j
            cnt=1
            break
    if cnt ==1:
        break
for i in range(len(n)):
    re[b][i] =n[i]

for j in range(len(m)):
    re[j][a] =m[j]

for i in re:
    for j in i :
        print(j,end='')
    print()


    
