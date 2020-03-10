n =int(input())
re =[]
li = list(map(int,input().split()))
re.append(len(li))
li.pop()
#  2 1 1 0
for i in range(len(li)-1,-1,-1):
    if li[i] ==len(re):
        re.append(i+1)
        li.pop()
    else:
        re.insert(li[i],i+1)
for k in re:
    print(k,end=' ')
