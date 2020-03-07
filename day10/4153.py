li =[]

for i in range(30000):
    l =list(map(int,input().split()))
    l.sort()
    l.reverse()
    if sum(l)==0:
        break
    li.append(l)

print(li)
for c,a,b in li:
    if c*c == a*a+b*b:
        print('right')
    else:
        print('wrong')