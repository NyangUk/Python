n = int(input())
m = int(input())
li = []
inv = []
for k in range(m):
    i,j = map(int,input().split())
    li.append([i,j])

for i,j in li:
    if i == 1:
        inv.append(j)
        li.remove([i,j])
        for q,p in li:
            if q == j:
                inv.append(p)
                li.remove([q,p])
    if j == 1:
        inv.append(i)
        li.remove([i,j])
        for q,p in li:
            if p == j:
                inv.append(q)
                li.remove([q,p])

print(len(set(inv)))


