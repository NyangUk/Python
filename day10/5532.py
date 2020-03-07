l =int(input())
a =int(input())
b =int(input())
c =int(input())
d =int(input())

# aday = a//c
# bday = b//d 
if a%c ==0:
    aday = a//c
else:
    aday = (a//c) +1
if a%c ==0:
    bday = b//d 
else:
    bday = (b//d) +1

print(l-max(aday,bday))