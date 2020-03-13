n= int(input())
c=[0,1,2,3,4,5,6,7,8,9]
re=[]
dic ={}
for i in range(n):
    s =list(input())
    re.append([len(s),s])
re.sort()
ans =[]
for i in range(n):
    s= re.pop()
    for j in range(len(s[1])):
        if s[1][j] in dic:
            s[1][j] =dic[s[1][j]]
        else:
            dic[s[1][j]] = c.pop()
            s[1][j] =dic[s[1][j]]
    print(s)
    ans.append(s[1])
    
print(ans)
print(dic)

