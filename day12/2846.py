n=int(input())
li = list(map(int,input().split()))

re =[]
for i in range(len(li)-1):
    k =i
    se =set()
    while k<n:
        if li[k]<li[k+1]:
            se.add(li[k])
            se.add(li[k+1])
            k+=1
        else:
            break
    re.append(se)

result =[]      
for l in re:
    if l ==set():
        continue    
    else:
        r =list(l)
        result.append(max(r)-min(r))
print(max(result))
