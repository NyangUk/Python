c, k = map(int, input().split())
if k == 0:
    print(c)
else:
    s =10**k #상근이가 가진돈 
    re=(c//s)*s
    if c%s>=s/2:
        re=re+s

print(re)
        