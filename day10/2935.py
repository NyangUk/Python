import collections

al = input()
l = input()
bl = input()

ali =list(al)
bli =list(bl)
a =0
b=0
for i in ali:
    if i=='0':
        a +=1
for j in bli:
    if j =='0':
        b+=1

if l=='*':
    print('1',end ='')
    print('0'*(a+b))
else:
    print(int(al)+int(bl))

