score =[]
sums =[]
re = []
n = int(input())
m= n*(n-1)
dic = {1:0, 2:1 ,3:2 , 4:3 }

for j in range(n):
    sums.append(0)
    # re.append(0)

for i in range(m//2):
    li = list(map(int,input().split()))
    score.append(li)

# print(score)

for a,b,asc,bsc in score:
    if asc > bsc:
        sums[dic[a]] +=3
    elif asc < bsc:
        sums[dic[b]] +=3
    elif asc==bsc:
        sums[dic[a]] +=1
        sums[dic[b]] +=1

# print(sums)

# sums =[10,40,20,30,90,80,80]
# re = []
# 나보다 큰사람이 몇명있는지 보면됨
for i in sums:
    rank = 1
    for k in sums:
        if i<k:
            rank = rank+1
    re.append(rank)

for i in re:
    print(i)
