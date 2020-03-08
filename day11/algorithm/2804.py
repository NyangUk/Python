n,m =list(input().split())

re = []
for _ in range(len(m)):
    li = list('.'*len(n))
    re.append(li)
naf =n.find('A') #1  0
nbf =n.find('B') #0  1
maf =m.find('A') #4  -1
mbf =m.find('B') #-1  2

# print(naf,maf,nbf,mbf)

if naf > -1 and maf>-1:
    for j in range(len(n)):
        re[maf][j] = n[j]
    for i in range(len(m)):
        re[i][naf] = m[i]
        # a 결합
else: # b가 결합해야대
    for j in range(len(n)):
        re[mbf][j] = n[j]
    for i in range(len(m)):
        re[i][nbf] = m[i]

for i in re:
    for j in i:
        print(j,end='')
    print()

# [['.', 'P', '.', '.', '.', '.'], 
# ['.', 'I', '.', '.', '.', '.'], 
# ['.', 'D', '.', '.', '.', '.'],
# ['.', 'Z', '.', '.', '.', '.'], 
# ['B', 'A', 'N', 'A', 'N', 'A'], 
# ['.', 'M', '.', '.', '.', '.'], 
# ['.', 'A', '.', '.', '.', '.']]



# [['.', 'C', '.', '.'],
#  ['.', 'C', '.', '.'],
#  ['A', 'B', 'B', 'A'],
#   ['.', 'B', '.', '.']]
