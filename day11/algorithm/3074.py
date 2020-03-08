num = list(map(int, input().split()))
w = list(input())
num.sort()
w[w.index('A')] =num[0]
w[w.index('B')] =num[1]
w[w.index('C')] =num[2]

for i in w:
    print(i,end =' ')

