# 사용자 정의 모듈 만들기
import sys
def show(name,age):
    print("이름 :{0} 나이: {1}".format(name,age))

def math1(i,j):
    if (i+j) ==0: show("제로",0)
    else: print(i+j)


