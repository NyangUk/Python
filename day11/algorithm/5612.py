t = int(input())
now = int(input())
car = []
for _ in range(t):
    li = list(map(int,input().split()))
    car.append(li)

result =[]
for i in range(t):
    now = now+car[i][0] -car[i][1]
    result.append(now)

if -1 in result:
    print(0)
else:
    print(max(result))
