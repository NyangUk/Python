s = input()
# 50-10+10-20-10+100+100
re =[]
if '-' not in s:
    re=list(map(int,s.split('+')))
    print(re)
    print(sum(re))
else:
    li =s.split('-')
    for i in li:
        if '+' in i:
            l =i.split('+')
            for j in l:
                re.append(j)
        else:
            re.append(i)
    re =list(map(int,re))
    result = re[0]
    for i in range(1,len(re)):
        result= result -re[i]
    print(result)
