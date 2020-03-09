n =int(input())
for _ in range(n):
    re =0
    i,j = map(int,input().split())
    li = map(int,input().split())
    for k in li:
        re =re+k//j
    print(re)