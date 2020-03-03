a = 100
b = 100

# is 
# Lvalue = Rvalue 일때 참 반대일때 거짓을 리턴한다.
print(a is b)

#변수 선언 및 초기화
c = d =200
e,f = "e" ,"f"

#참조 변수
aa  =[1,2,3]  #aa는 [1,2,3]이라는 리스트를 가르킨다
bb = aa       #bb는 aa를 가르킨다   
aa[2] =5      #aa가가르키는 2번인덱스의 값을 변경한다
print(aa)
print(bb)     #bb또한 aa를 가르키기 때문에 aa 와bb가 같다.

#데이터의 복사

aa = ['a','s','d']
bb = aa[:]    #슬라이싱을 통해 복사했다.
aa[2]='k'     
print(aa)
print(bb)     #bb가 또다른 ['a','s','d']를 가르키기 때문에 aa에의해 값이 변경되지 않는다.
