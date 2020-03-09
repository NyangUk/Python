s =input()
re =0
stack =[]
for i in range(len(s)):
    if s[i] =='(':
        re+=1
    elif s[i] ==')':
        if s[i-1] =='(':

        else:
            re +=1
