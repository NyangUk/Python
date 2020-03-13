n =int(input())
li =list(map(int,input().split()))
li.sort()
re =[]
ans = 0
for i in li:
    ans=ans+i
    re.append(ans)
print(sum(re))