n =int(input())
li = list(map(int, input().split()))
c =int(input())
cnt=0
for i in range(len(li)):
    if li[i] ==0:
        pass
    else:
        if li[i]%c ==0:
            cnt+=li[i]//c
        else:
            cnt+=li[i]//c+1

print(cnt*c)

