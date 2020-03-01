# 변수의 범위(scope)



b =  0 #전역변수

def change(b): # 함수내에서의 b이므로 함수내에서만 존재함
    b = b+1 #지역변수 
    print(b)

change(b) #함수내의 b의 값만 바뀜 (함수인자를 복사해서 가져오기때문에)
print(b) # 함수내에서의 변화이므로 원래 b에서는 값이 바뀌지않음





# global을 사용할 경우 본래 값을 가져다가 함수내에서실행하기 때문에
# 함수의 내용에 따라 값이 직접적으로 바뀐다.

a = 10
c = 124
def exchange():
    global a # 직접 사용하고자 할때 global사용 
    global c
    print(a,c)
    tmp = a
    a = c
    c = tmp
    print(a,c)

exchange()
print(a,c)

#위의 방법보다는 return을 사용하는 것이 바람직 하다.