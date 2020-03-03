# #사용자 입력

# # input() 괄호 안에는 입력을 받음과 동시에 출력하고자 하는 문구 넣기 
# a = input("이름을 입력하세요")
# print(a)

# #여러개의 변수에 입력을 받을때 
# # input().split() 두번째 괄호안에 어떤기호를 기준으로 나눌 것인지를 알기위함 

# b, c = input('문자열 두 개를 입력하세요: ').split()    # 입력받은 값을 공백을 기준으로 분리
 
# print(b)
# print(c)
# print(b+c) # 문자열 이기 때문에 셈을 할수 없음

# 입력받은 데이터의 자료형 변환 
# map(변환하고자 하는 자료형 ,input().split)
d,e = map(int,input().split(','))
print(d+e)

