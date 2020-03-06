import collections

n = int(input())
li = []
mem = collections.Counter()
for i in range(n):
    name=list(input())
    li.append(name[0])
    # print(name)

mem.update(li)
ch =[]
# print(mem)
ox = 0
for item,cnt in mem.items():
    if cnt>4:
        ch.append(item) 
        ox +=1
ch.sort()
for i in ch:
    print(i,end='')

if ox == 0:
    print("PREDAJA")