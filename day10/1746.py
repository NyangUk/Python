n,m = map(int,input().split())
hear = []
re= []
cnt =0
for _ in range(n):
    hear.append(input())

for _ in range(m):
    see=input()
    for i in hear:
        if see ==i:
            cnt+=1
            re.append(see)
        else:
            continue
print(cnt)
for k in re:
    print(k)