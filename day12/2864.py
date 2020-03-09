n,m= map(str,input().split())
i,j =n,m
#min
# replace는 원래 문자열이 바뀌는게 아니므로 
#변수에 할당해줘야 값이 개애신된다.
i= i.replace('6','5')
j= j.replace('6','5')
print(int(i)+int(j),end =' ')
# max
n =n.replace('5','6')
m= m.replace('5','6')
print(int(n)+int(m))
# 