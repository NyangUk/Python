n = list(map(int,input().split()))
m = list(map(int,input().split()))
ns =sum(n)
ms =sum(m)
if ns == ms:
    print(ns)
elif ns>ms:
    print(ns)
else:
    print(ms)