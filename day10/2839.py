ham =[]
be =[]
for i in range(3):
    ham.append(int(input()))
for i in range(2):
    be.append(int(input()))
ham.sort()
be.sort()

print(ham[0]+be[0]-50)