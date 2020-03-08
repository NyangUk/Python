re = []
for _ in range(10):
    re.append(int(input()))
li=[]
for k in re:
    li.append(k%42)
re.clear()
result =set(li)
print(len(result))


