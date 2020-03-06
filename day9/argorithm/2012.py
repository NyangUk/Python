# 17:18
# 17:24
import math
n =int(input())
per = []

for i in range(n):
    per.append(int(input()))
rank =1
ang =0
per.sort()
print(per)
for k in per:
    ang = ang + abs(k-rank)
    rank +=1
print(ang)
