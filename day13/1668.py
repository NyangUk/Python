n = int(input())
li =[]
for _ in range(n):
    li.append(int(input()))

def gogo(li):
    cnt=1
    s =li[0]
    for i in range(1,n):
        if li[i]>=s:
            s= li[i]
            cnt+=1
            if s == max(li):
                break
    print(cnt)

gogo(li)
li.reverse()
gogo(li)
