# 문자열 함수

# .format()
# {n} 은 자리표시자를 의미하며 format의 지정된 위치 표시

print("you have {0} a friend".format("got"))

str = "{2} {0} {1}".format('a',100 ,300)
print(str,end = '\n\n\n')


number =75
day = "일요일"

# 인덱스만을 사용
print ("우리가 사귄지 {0} 일째되는 {1}이야!".format(number,day))
# 인덱스와 이름을 혼용 
print("100일 까지 {day}일 남았지롱! {0}".format(":D :c ;< ",day=25)) 

#정렬(서식문자가 아닌 .format()사용)
# {n:s m} n : 인덱스, m : 정렬할 크기, s: < > ^
name = "김재욱"
#좌측 정렬 
print("{0:<10}".format(name))
#우측정렬
print("{0:>10}".format(name))
#가운데 정렬
print("{0:^10}".format(name))
# 정렬시 사용할 기호를 설정할 수 있음 
print("{0:+^20}".format(name))

# < > ^ 기호 앞에 공백대신 채워넣을 기호를 넣어주면됨

 