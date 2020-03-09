n = int(input())

def T_F():
    s = input()
    li =[]
    for i in s:
        if i =='(':
            li.append(')')
        elif i ==')':
            if len(li)<=0:
                return 'NO'
            else:
                li.pop()
                pass
    if len(li) ==0:
        return 'YES'
    else:
        return 'NO'
            

for k in range(n):
    print(T_F())