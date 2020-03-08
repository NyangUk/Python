ch =[]
for _ in range(8):
    li =list(input())
    ch.append(li)
cnt= 0
now =-1
for i in ch:
    for j in i:
        now+=1
        if now%2 ==0:
            if j =='F':
                # print(now)
                cnt+=1
    now+=1

print(cnt)