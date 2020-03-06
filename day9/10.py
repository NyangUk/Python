# bisect 모듈 : 정렬된 상태로 아이템을 추가 할수 있는 모듈
# 데이타가 많은 리스트를 사용할경우 힙방식보가 시간을 절약 할 수있다.
import bisect
import random
random.seed()
for i in range(5):
    print('%d' %random.random(),end = ' ')

print('new list')
li1 = []
li2 = []
li3 = []
for i in range(1,15):
    num =random.randint(1,10) # 1 부너 100의 정수를 랜덤으로 출력한다.
    # 밑에 두개가 짝꿍이야 오름차순으로 정렬된다.
    pos = bisect.bisect(li1,num) #아이템이 추가될때 인덱스값을 리턴하게 되어있음
    bisect.insort(li1,num) #리스트를 정렬상태로 유지 이걸 실햀켜야 정렬된다.
    print('%3d %3d  ' %(num,pos),li1)


    # 중복된 값이 나올때 중복값을 오른쪽에 둘지 왼쪽에 둘지!
    pos = bisect.bisect_left(li2,num)
    bisect.insort_left(li2,num)
    print('%3d %3d  ' %(num,pos),li3)
    pos = bisect.bisect_right(li3,num)
    bisect.insort_right(li3,num)
    print('%3d %3d  ' %(num,pos),li2)
