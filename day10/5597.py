s =[]
re =[]
for _ in range(28):
    s.append(int(input()))
s.sort()

for i in range(1,31):
    if i in s:
        continue
    else:
        print(i)

