# collections 모듈
# deque(양쪽으로 열려있는 큐구조)
# defaltdict,counter,ordereddict

# array 모듈 동일한 데이터 타입 메모리 효율적 사용 o list 여러가지 데이터 타입 메모리 효율적 사용 x

# heapq (힙 생성 힙 내부자료 접근)모듈
# 오버헤드를 줄일수 있다 이미 sort가 되어있음

# bisect모듈 (정렬된 상태로 요소를 추가, 중복값처리)
# queue
# struct
# copy


# collections
# counter 컨테이너에 동일한 값의 자료가 몇개인지 파악할때 사용하는 객체ㅕ엠

import collections

print(collections.Counter(['aa','ss','dd','aa','ff','ss']))
# 딕션어리 형태로 저장된다.
print(collections.Counter({'가':1,'나':4}))
print(collections.Counter(a=2,f= 6,g=5))

con = collections.Counter()
print(con)

# 요소 추가하기
con.update('aassddfggeehh')
print(con)

con.update({'c':2,'f':3})
print(con)

#counter 객체에 접근하기
# []를 이용해서 값 인자를 가져다.
for n in "adfeo":
    print("%s %d" %(n,con[n]))

ct =collections.Counter("hello jaeuk")
ct['x'] = 0
print(ct)

# list1 = list(ct.elements())
# print(list1)

# most_common(n) 상위 n개를 시퀀스


ct2 = collections.Counter()
with open('text.txt','rt') as f :
    for li in f:
        ct2.update(li.rstrip().lower())

for i ,j in ct2.most_common(2):
    print("%s %2d" %(i,j))


print(ct.most_common(3))

for item,cnt in ct.most_common(4):
    print("{0}인 개수{1}".format(item ,cnt))