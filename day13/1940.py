n = int(input())
m = int(input())
li = list(map(int,input().split()))
cnt=0
for i in range(n):
    if type(li[i]) ==int:
        print(li)
        if m-li[i] in li:
            k =li.index(m-li[i])
            li[k] = '/'
            li[i] = '/'
            cnt+=1
print(cnt)
