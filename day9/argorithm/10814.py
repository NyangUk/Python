n = int(input())

per = []
for i in range(n):
    age,name = map(str,input().split())
    per.append([int(age),i,name])

# print(per)
per.sort()
for i ,j,k in per:
    print(i, k)

