n =int(input())
re =[]
for _ in range(n):
    x,y = map(int,input().split())
    re.append([y,x])
re.sort()
for i in range(n):
    print(re[i][1],re[i][0])
    # print()
