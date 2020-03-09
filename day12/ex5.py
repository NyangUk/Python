strs =['llll','llrt','lloo']
     # 012345  012345  0123
     #   0       1       2
strs =sorted(strs)
re = ''
index =0
flag=1
for i in strs[0]:
    for j in range(1,len(strs)):
        if i == strs[j][index]:
            pass
        else:
            flag =0
            break
    if flag ==1:
        re+=i
    else:
        break
    index+=1

print(re)
