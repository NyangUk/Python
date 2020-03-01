# 사용자 정의 함수 

# def 함수명(매개변수):
#     실행문...


# 매개변수와 리턴값이 존재
# 리턴이 실행되는 순간 함수를 빠져나옴
def sum(x ,y):
    return x+y

print("합 : %d" %sum(5,9))

# 매개변수만 존재

def compare(x,y):
    if x<y:
        print("{0}(이)가 {1}보다 작습니다.".format(x,y))
    elif x>y:
        print("{0}(이)가 {1}보다 큽니다.".format(x,y))
    else:
        print("두수가 같습니다.")

compare(1,2)
compare(4,2)
compare(7,7)

#리턴값만 존재

def line():
    print("{0:-^20}".format("오늘은 여기서 끝낼까요?"))

line()


# 매개변수의 초기값 설정

def who(name ,age,gender="M"):
    gender =gender.upper()
    print("이름 : {0}".format(name))
    print("나이 : {0}".format(age))

    if gender == 'M' :
        print("인 남자입니다.")
    elif gender == 'W':
        print("인 여자입니다.")


# def who(name ,gender="M",age):
#     gender =gender.upper()
#     print("이름 : {0}".format(name))
#     print("나이 : {0}".format(age))

#     if gender == 'M' :
#         print("인 남자입니다.")
#     elif gender == 'W':
#         print("인 여자입니다.")


who("김재욱" ,22,"w")
who("김성운" ,24)

# 초기화 하고자 하는 매개변수들은 마지막에 적어줄것 


