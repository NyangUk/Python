# 객체 = 인스턴스 
# cat = animal() cat은 animal의 인스턴스다 o 관계위주로 설명할때!!  
#                cat은 인스턴스다 x

# class 기초

# class 선언
class Test:
    str = "클래스 개념잡기" # Test의 요소,멤버(attribute,field)

test1 = Test() #Test 클래스에 의해 만들어진 인스턴스이다.

print(test1.str)



# 클래스의 구성
# class 클래스명:
    # 변수 (클래스에 소속된 변수) 이러한 변수들을 클래스의 필드(field)
    # 함수 (클래스에 소속된 함수) 이러한 함수들을 클래스의 메소드(method)라고 한다.

# 클래스는 필드와 메소드로 구성되어있으며 변수 함수와는 구분짓기위해 다르게 부른다.

# 메소드의 경우 매개변수의 목록에 항상 한개의 변수를 맨앞에 추가해야한다.
# 꼭 self를 사용해야하는것은 아니지만 일반적으로 self를 사용하다.(표준으로 사용)

# 메소드를 호출할때 self 변수에는 직접 값을 넘겨주지 않고 자동으로 값을 전달 한다.
# self는  자신의 객체를 가리킨다 this 와 같은 개념!

class Person:
    def say(self):
        print("안녕하세요")

p1 = Person()
p1.say()

class EX:
    pass

p2 = EX()  # p2가 객체주소를 가르키고있는 참조변수이다.
print(p2)  #<__main__.EX object at 0x7fce46df0d68>    0x7fce46df0d68 : 메모리에 객체가 할당됨!!

