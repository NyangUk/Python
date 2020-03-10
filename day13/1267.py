n =int(input())
li =list(map(int,input().split()))
re =[]
cnt =0
#영식 30초마다 10
for i in li:
    if i%30 == 0:
        cnt= cnt+(i//30)+1
    else:
        cnt=cnt+1+i//30
re.append([cnt*10,'Y'])
cnt=0
#민식 60 초마나 15
for i in li:
    if i%60 == 0:
        cnt= cnt+(i//60)+1
    else:
        cnt=cnt+1+i//60
re.append([cnt*15,'M'])
re.sort()
if re[0][0]==re[1][0]:
    print('Y M %d' %re[0][0])
else:
    print(re[0][1],re[0][0])