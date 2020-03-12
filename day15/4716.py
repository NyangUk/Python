t,a,b =map(int,input().split())
li =[]
for _ in range(t):
    li.append(list(map(int,input().split())))
tr =map(int,input().split())
ans = 0
re =0
go =[]
for n, As,Bs in li:
    print(a,b)
    if As>Bs:
        re =b-n
        if re<0:
            b=0
            a=a+re
            ans =b*Bs+(abs(re))*As
        else:
            b=b-n
            ans =n*Bs
    elif As<Bs:
        re =a-n
        if re<0:
            a=0
            b =b+re
            ans =a*As+(abs(re))*Bs
        else:
            a=a-n
            ans =n*As
    go.append(ans)
print(sum(go))