n =int(input())

words =[]

for i in range(n):
    m = input()
    words.append(m)

remove = list(set(words))

result = []
for k in remove:
    result.append([len(k),k])
result.sort()

for i, j in result:
    print(j)


