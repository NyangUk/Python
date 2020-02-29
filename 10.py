#if 문

# if <조건>:
#     ...
# else :
#     ...

# 연산자별 사용 방식

# 연산자 x

if True :
    print("True")
else :
    print("False")

#논리연산자
# and, or not 
# x and y , x or y, not x
x = 1
y = 0

if x and y:
    print("True")
else :
    print("False")

if x or y:
    print("True")
else :
    print("False")

if not x: #x=0이 이여야 참임 
    print("True")
else :
    print("False")

if x is y:
    print("True")
else:
    print("False")

#in 연산자 
#리스트 튜플 문자열 등에 해당 문자가 들어가있는지 확인후 참 거짓 리턴
# x in 리스트, x in 튜플, x in 문자열
# x not in 리스트, x not in 튜플, x not in 문자열

x =['a','b','c']

if 'a' in x:
    print("True")
else:
    print("False")

#다중 if 문 (else if = elif )

# if <조건1>:
#     ...
# elif <조건2>:
#     ...
# else:
#     ...


#pass 아무 코드도 실행하지않고 다음 코드로 넘어가기 위한 예약어 


