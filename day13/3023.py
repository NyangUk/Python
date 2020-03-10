r,c =map(int,input().split())
s =[]
sr=[]
re =[]
for _ in range(r):
    k1= list(input())
    s.append(k1)
    k2 =list(reversed(k1))
    sr.append(k2)

sk=list(reversed(s))
sl =list(reversed(sr))

x,y=map(int,input().split())

for i in range(r):
    l=list(s[i]+sr[i])
    re.append(l)
for i in range(r-1,-1,-1):
    l=list(s[i]+sr[i])
    re.append(l)

print(re)

if re[x-1][y-1] =='.':
    re[x-1][y-1] ='#'
elif re[x-1][y-1] =='#':
    re[x-1][y-1] ='.'

for i in re:
    for j in i:
        print(j,end='')
    print()