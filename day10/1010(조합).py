n =int(input())
for _ in range(n):
    w,e =map(int,input().split())
    key= 1
    if w != e:
        for k in range(e,e-w,-1):
            key*=k
        for l in range(w,1,-1):
            key//=l
    print(key)
    
