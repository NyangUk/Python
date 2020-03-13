a =list(input())
b =list(input())
re =[]
cnt =0
for i in a:
    for j in range(len(b)):
        if i==b[j]:
            cnt+=1
            b[j] =1
            break
        else:
            pass

print(len(a)+len(b)-2*cnt)