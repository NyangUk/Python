import collections

n = int(input())


re =[]

result =collections.Counter()
for f in range(1,n+1):
    # print(f)
    result.update(str(f))
    
for i in range(10):
    re.append(0)

# print(result)

for k,v in result.items():
    re[int(k)] = v

for i in re:
    print(i,end=' ')
    

