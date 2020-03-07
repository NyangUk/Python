#75.876%
# 0 1 2 3 4 5 6 7
score =[]
for i in range(8):
    score.append(int(input()))
re=[]
sum=0

for i in range(5):
    sum +=max(score)
    cnt=score.index(max(score))
    score[cnt] =0
    re.append(cnt+1)
re.sort()
print(sum)
for k in re:
    print(k,end=' ')


    
