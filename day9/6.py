#pprint
# pprint 모듈에 pprint()이용
from pprint import pprint

data =[(1,{'a':'가','s':'나'}),(2,{'q':'다','w':'라 '})]

print(data)

pprint(data)

import array

# array 시퀀스 자료구조를 정의함 고정된 자료형 메모리를 좀더 효율적으로 사용할 수있음
#지원 자료구조

s1 ="asdfghjk"
a1 =array.array('u',s1)  

print(a1)
pprint(a1)

a2 =array.array('i',range(5))
print(a2)

# 요소 추가
a2.extend(range(5))
print(a2)

# 슬라이싱
print(a2[3:6])

# enumerate는 튜플 형태로 시눠스를 메김 꼭 리스트형태로 바꿔줄것
print(list(enumerate(a2)))

li1 =[1,2,(4,5,6)]
print(li1)