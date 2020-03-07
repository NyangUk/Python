x =int(input())
y =int(input())
yp =int(input())
ypp =int(input())
l =int(input())
sum =[]
sum.append(x*l)
f =yp-l
if f>=0:
    sum.append(y)
else:
    pay = y+(abs(f)*ypp)
    sum.append(pay)
print (min(sum))