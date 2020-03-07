s =[]
a = ['D','A','B','C','E']
for i in range(3):
    li = list(map(int,input().split()))
    s.append(sum(li))
for i in s:
    print(a[i])
