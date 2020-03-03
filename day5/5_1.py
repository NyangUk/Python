# 절차지향 프로그래밍

# C언어 

# 책읽듯이 순차적인 처리를 중요시 하며 프로그램 전체가 유기적으로 연결되도록 만드는 프로그래밍 기법

# 단점
#  1. 재사용 불가
#  2. 확장성이 떨어짐 (코드를 재사용하므로써 다른 코드로 구현하는것.)
#  3. 유지보수가 어렵다. (코드하나가 잘못되면 그 코드 전체를 파악해야함)

# 객체지향 프로그래밍

# C++.Python

# 구조적 프로그래밍과 다르게 작은 문제들을 해결할수 있는 객체를 만들고 이 객체들을 조합하여 큰문제를 해결한다.
# 객체의 독립성 신뢰성을 높게 만들어 놓으면 그 객체를 수정 할 필요없이 재사용이 가능해 개발 비용 시간을 줄일 수 있다.





# 절차지향
# 남자 여자를 구분하려면 또 다른 함수를 만들어 줘야한다.(재사용 불가능)
show_info = ""

def person(name,age):
    global show_info
    show_info += "이름 : %s 나이 : %d \n" %(name,age)


w_show_info = ""

def w_person(name,age):
    global w_show_info
    w_show_info += "이름 : %s 나이 : %d \n" %(name,age)
    

person("김재욱",22)
person("김성운",24)
print(show_info)

w_person("김재욱",22)
print(w_show_info)

# 객체지향
# 남자 여자를 구분하려면 다른 객체를 만들어주면된다.(재사용 가능)
# 여러 사람을 출력하려면 객체지향이 매우 유리하다.


class Person:
    def __init__(slef):
        slef.info = ""
    
    def showinfo(self ,name,age):
        self.info += "이름 : %s 나이 : %d \n" %(name,age)
        print(self.info)

man =Person()
woman = Person()

man.showinfo("김성운",24)
woman.showinfo("김재욱",22)

