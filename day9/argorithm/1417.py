n = int(input())
read = []
for i in range(n):
    read.append(int(input()))

me =read[0]         #5
other = read[1:]    #7 7 8
out = 1

count=0
while out:
    # print(other, me)

    maxv = max(other)
    maxi = other.index(maxv)
    if maxv==0:
        break
    elif me <= maxv:
        other[maxi] = other[maxi]-1
        count+=1
        me = me + 1
    elif me>maxv:
        out = 0

print(count)
        