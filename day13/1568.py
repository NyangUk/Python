n =int(input())
i =1
cnt =0
while n>0:
    n= n-i
    cnt+=1
    i+=1
    if i>n:
        i=1
print(cnt)