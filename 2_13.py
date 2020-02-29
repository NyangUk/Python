#for문 


#for 문 유형 2


# range(start,last) = [start,start+1 ... last-1]
# range(start,last,plus) = [start,start+plus ... last-plus]


for i in range(1,10) :
    if i %2 == 0 :
        print('*'*i)
    else:
        print(" "*i)

for i in range(1,20,4) : #[1,5,9,13,17]
    print("@"*i ,i)

# for else
# 반복문에서의 else는 반복문이 실행되고 나서 무조건 실행되는 코드
# break문을 사용했을 경우 수행되지 않는다.

for i in range(4,10) :
    print(i)
else :
    print("반복문 종료")


# 구구단 출력_1
for i in range(2,10):
    print("%d단 :" %i, end = ' ')  #end = "?" print의 자동 줄바꿈을 end 를 이용하여 문자로 바꿔 줄 수 있다
    for j in range(1,10):
        print ("%2d * %d = %2d" %(i,j,(i*j)), end = " ")
    print(' ')


# 구구단 출력_2

list1 =[1,2,3,4,5,6,7,8,9]
gugudan_2 = []
index = 0
for i in list1 :
    
    for j in range(1,10):
        gugudan_2.append(i*j)
    print (gugudan_2[index:])
    index +=9