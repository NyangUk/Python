# init 메소드

# 객체를 생성하고 초기화 작업을 할때 유용하게 사용가능
# 클래스가 인스턴스화 될때 호출된다.

class Circle :
    def __init__(self,radius):
        self.radius = radius
    def get(self):
        print("반지름은" ,self.radius)

circle1 = Circle(5)
circle1.get()
print(circle1)

# namespace 
# 변수와 필드의 가장큰 차이점은 namespace 필드는 객체 내에서만 의미가 있다.

# 필드에는 객체 변수와 클래스 변수가 있다.

# 클래스 변수는 공유된다. 클래스로 부터 생성된 모든 인스턴스들이 접근 할 수 있다.

# 객체 변수(인스턴스 변수)는 클래스로 부터 생성된 각각의 객체에 속해 있는 변수  
# 객체별로 객체 변수를 하나씩 따로 가지고 있다 즉 공유하지 않고 있다.

class Player:
    # 클래스 변수
    count = 0

    def __init__(self,name): # C++ 에서의 생성자와 비슷함
        self.name = name  #객체 변수 
        print("준비중...{0}".format(self.name))

        Player.count += 1 # 클래스가 만들어짐과 동시에 클래스변수 count에 1을 더한다.
    
    def gameover(self):
        print("플레이어 {0}가 죽었습니다.".format(self.name))

        Player.count -=1

        if Player.count ==0 :
            print("최후의 플레이어 {0}".format(self.name))
        else:
            print("남은 플레이어수 : {0}".format(Player.count))
    
    def get(self):
        print("플레이어 이름 : {0}".format(self.name))

#@classmethod (장식자)()   check_player = classmethod(check_player)
    @classmethod
    def check_player(how):
        print("현재 {0}이 남았습니다.".format(Player.count))


yiri = Player("yiri")
hong = Player("hong")
kakao = Player("kakao")

hong.gameover()
yiri.gameover()
Player.check_player() # 클래스 메소드 호출 방법 : 클래스명,메소드 명



