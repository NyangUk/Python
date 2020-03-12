re =[]

for i in range(5):
    li = list(input())
    li = li+['']*(15-len(li))
    re.append(li)

for i in range(15):
    for j in range(5):
        print(re[j][i],end='')

    
