n =int(input())
f = int(input())
s =n//100
for i in range(0,100):
    k = s*100+i
    if k%f ==0:
        print('%02d' %i)
        break

