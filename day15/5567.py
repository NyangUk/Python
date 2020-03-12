n =int(input())
m =int(input())
f =[]
for _  in range(m):
    f.append(list(map(int, input().split())))

re =[]
for i,j in f:
    if i ==1:
        re.append(j)
    if j ==1:
        re.append(i)
re2=[]
for i,j in f:
    for k in re:
        if i ==k:
            re2.append(j)
        if j ==k:
            re2.append(i)
ans =re+re2

print(len(set(ans))-1)

