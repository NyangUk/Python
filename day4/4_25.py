# 집합 
# set

# 중복을 허용하지 않으며 숫자 제외 , 인덱스같은 순서가 없다.
#집합과 딕션어리는 인덱싱을 지원하지 않는다.

set1 = set(['a','s','d'])
print(set1)

set2 = set([1,2,3,4])
print(set2)

set3 =set("hello")
print(set3)

# 인덱싱을 하기위해 자료형을 바꿔줘야함

list1 = list(set1)
print(list1[1])


# 교집합 합집합 차집합

set4 = set([1,2,3,4,5,6,7,8,9,10])
set5 = set([3,4,6,7,8,11])

# 교집합 '&'를 사용하거나 .intersection()
print(set4 & set5)
print(set4.intersection(set5))

# 합집합 '|'를 사용하거나 .union()을 사용한다.
print(set4 | set5)
print(set4.union(set5))

# 차집합 '-'를 사용하거나 .difference()를 사용한다.
print(set4 - set5)
print(set4.difference(set5))

 
set6 = set([1,2,3])

#집합의 값을 추가하기
set6.add(100)
print(set6)

#집합의 여러 값 추가하기
set6.update([10,12,64])
print(set6)

# 집합의 값 삭제하기
# .remove() .discard()

set6.remove(10) # 없는 값을 없앨경우 에러 
set6.discard(12) #없는 값을 없앨경우 에러발생 x
print(set6)

# 대칭 차집합 : 두개의 집합이 있을때 두집합 공통으로 가지지 않는 값을 출력함
# '^' 을 사용한다.
set7 =set("good morning")
set8 = set("good night")

print(set7-set8) # 차집합
print(set7^set8) # 대칭 차집합

#집합의 모든 값 제거
set7.clear()

#집합의 개수 구하기
length = len(set8)
print(length)