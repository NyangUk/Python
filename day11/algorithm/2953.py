re =[]
for _ in range(5):
    li =sum(list(map(int,input().split())))
    re.append(li)
print(re)
print(re.index(max(re))+1,max(re))