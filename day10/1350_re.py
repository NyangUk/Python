n =int(input())
fi = list(map(int,input().split()))
size = int(input())

cnt= 0 #핑ㄹ요디스
for i in fi:

    val =0
    if i ==0:
        pass
    else:
        val = i-size
        i = val
        cnt+=1
        while val>0:
            val = i-size
            i = val
            cnt+=1

print(size*cnt,end =' ')

