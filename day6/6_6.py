# 상속
# 재사용의 한가지 방법 

class Circle:
    def __init__(self,radius,name):
        self.radius =radius
        self.name = name
        print("객체 초기화 {}".format(self.name) )

    def get(self):
        print("{0} 반지름 {1}".format(self.name,self.radius))

# Circle클래스를 상속받는 pizza클래스는 Pizza(Circle) 이라고 표시하며
# 부모 클래스(상위)를 슈퍼클래스라고 하며 자식클래스를 서브클래스라고 한다.

class Pizza(Circle):
    def __init__(self,name,radius,loaction):
        Circle.__init__(self,radius,name)
        self.loaction =loaction
        print("{} 피자를 만들었습니다.".format(self.name))

    def get(self):
        Circle.get(self)
        print("{}지점으로 배달 예정입니다.".format(self.loaction))

c1 = Circle(5,"도넛")
p1 = Pizza(10,"포테이토","인하대")

member = [c1,p1]
for i in member:
    i.get()
    