# namedtuple

import collections

person =collections.namedtuple("person",'name age gender')
# collections.namedtuple('만들 객체의 이름 ,'튜플안에 들어갈 '

aa = person(name ="김재욱" ,age ='22',gender="여")
bb = person(name = "김성운" ,age = "24",gender= "남")

for n in [aa,bb]:
    print("%s은 %s세의 %s성 입니다." %n)

#orderedDict  자료의 순서를 기억하는 사전형 클래스
dic= {}
# 표준 딕션어리는 아무렇게 나 아이템을 정렬하여 출력
dic["a"] ="가"
dic["b"] ="나"
dic["c"] ="다"

for i,j in dic.items():
    print(i,j)

print("-"*10)

# orderedDict 는 아이템이 들어간 순서를 기억해서 출력한다.
dic1 = collections.OrderedDict()

dic1["a"] ="가"
dic1["b"] ="나"
dic1["c"] ="다"

for i,j in dic1.items():
    print(i,j)

# 표준과 ordered는 ㄱ아이템이 모두 같아도 순서가 다르면 False값을 출려한다.
# 표준과 표준은 아이템만 같으면 상관 없다.