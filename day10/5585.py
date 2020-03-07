n =int(input())
re = 1000-n
cnt =0
li = [500,100,50,10,5,1]
while re>0:
    for i in li:
        h =re//i
        if h>0:
            re= re-i*h
            cnt =cnt+h*1
        else:
            continue
    
print(cnt) 