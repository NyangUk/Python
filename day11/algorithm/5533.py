n  =int(input())
score =[]
re = []
for i in range(n):
    li = input()
    li = li.split() #f리스트로 반
    score.append(li)
for i in range(3):
    for j in range(n):
        se = score[j][i]
        go=0
        for k in range(j+1,n):
            if score[j][i]==score[k][i]:
                score[k][i] =0
                go =1
        if go ==1:


for i in score:
    sum =0
    for j in i:
        sum +=int(j)
    print(sum)


