n ,a,b =map(int,input().split())
s = []

ml =a*a+b*b
for _ in range(n):
    s.append(int(input()))

for l in s:
    if ml>=l*l:
        print('DA')
    else:
        print('NE')

