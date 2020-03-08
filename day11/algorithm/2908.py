a ,b=map(list,input().split())
a.reverse()
b.reverse()

re= []
re.append(int(''.join(a)))
re.append(int(''.join(b)))
print(max(re))