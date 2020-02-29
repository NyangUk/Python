# 변수의 자료형
# long 형 , char 형  따로 없음.. python 에서는 필요가 없다.

a = 10.0
b = 120
# 문자열은 작은따옴표와 큰따옴표에따른 구분이 없다.
c = "JAEUk" 
d = 'JAEUK'

# 연산자
# ** 거듭제곱
# // 소수점을 버림
# % 나머지반환 

print(a-b) # print 하고 나서는 무조건 줄바꿈이 일어남
print(a+b)
print(a*b ,"\n",b/2) # 여러개 출력하고자 할때 , 으로 구분가능

print(a**3)
print(a/3) # 소수점까지 모두출력
print(a//3) # 소수점 버림 
print(a%3)

# 이스케이프 코드
# \n \r \t \" \' \000 \\ 
print ("\nhello world")
print ("\rhello world")
print ("\thello world")
print ("\' hello world! \'")
print ("\" hello world! \"")
print ("\\ hello world \\")
