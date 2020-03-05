# counter 객체는 산술 찝합 연산이 가능하다
import collections

ct1 = collections.Counter(['a','s','d','f','g','a'])
ct2 = collections.Counter('aasd')

print(ct1,ct2)
 
print(ct1+ct2) #두 컨테이너에서의 모든 값을 더함

print(ct1-ct2)

print(ct1&ct2)

print("union", ct1 | ct2) # 두 컨테이너중 공통된 값만을 출력

#defaultdict 컨테이너르 초기화 할때 디폴트값을 지정한다.


def default(): #디폴트 값을 출력하는 함수
    return "a"

dic =collections.defaultdict(default,n1 = "hi")
print(dic)
print(dic['n1'])
print(dic['n2']) # 찾고자 하는 값이 없을때 defalt함수를 호출하여 값을 내놈 



# Deque 양방향 큐 는 컨테이너 양쪽에 아이템을 넣거나 뺄수있음
deq =collections.deque("hello jaeuk")
print(deq)
print(len(deq))
print(deq[0])
print(deq[-1])

deq.remove('o')
print(deq)
deq.append('k')
print(deq)
deq.appendleft('k')
print(deq)
deq.extendleft('l')
print(deq)

#  item 꺼내기
# print("오른쪽에서 부터 꺼내오기")
# while True:
#     try:
#         print(deq.pop(), end = ' ')
#     except IndexError:
#         break

print("왼쪽에서 부터 꺼내오기")
while True:
    try:
        print(deq.popleft(), end = ' ')
    except IndexError:
        print("모두 꺼냈습니다.")
        break