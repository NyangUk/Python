# 모듈의 name 속성
# 모든 모듈은 이름을 가지고 있다. 
# 모듈의 name 속성을 이용하면 외부로 불러들여 졌을때 곧바도 실행되지 않게 할 수있다.


def sum(i,j):
    return i+j

def mul(i,j):
    return i*j

if __name__ == "__main__":
    print(sum(1,5))
    print(mul(1,5))
# 모듈로 가져왔을땐 sum ,mul을 출력할 필요가 없다.

# 해당 파일을 실행하면 if문이 참이 되어 출력되지만
# 다른 파일에서 import될때 실행되지 않는다.