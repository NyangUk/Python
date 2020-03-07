score = []
for i in range(5):
    score.append(int(input()))

sums = 0

for k in score:
    if k>40:
        sums += k
    else:
        sums +=40

print('%d' %(sums/5))
    
