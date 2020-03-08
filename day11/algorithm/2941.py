import collections
cro =['c=','c-','dz=','d-','lj','nj','s=','z=']
rep=['1','2','3','4','5','6','7','8']

n = input()
for i in range(8):
    n = n.replace(cro[i],rep[i])
# print(n)
dic =collections.Counter(n)
# print(dic)
result = 0
for key, value in dic.items():
    result+=value
print(result)

