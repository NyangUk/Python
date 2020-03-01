# 리스트 함수 

# 리스트의 값추가
list1 = ["빨강","파랑","노랑"]
list1.append("초록")
print(list1)

# 리스트 정렬함수
list2 = [1,4,7,2,9,5]
list3 = ['a','l','r','g']
#오름차순
list2.sort() 
list3.sort()
print(list2,list3)

# 리스트 뒤집기 함수
#sort를 한뒤에 reverse를 해주면 내림차순이 된다. 
list2.reverse()
list3.reverse()
print(list2,list3)

# 요소의 위치반환
str1 ="수학의 바이블"
list4 =["수학","영어","미술","체육"]

# 문자열의 요소 위치반환
print(str1.find("바"))
print(str1.index("바"))

# 리스트의 요소 위치 반환  
# 문자열과 마찬가지로 index함수는 찾고자하는 값이 없으면 에러가 뜬다.
print(list4.index("수학"))

# 요소를 삽입하는 함수
#.insert(인덱스,추가요소)
list5 = ["first" ,"thrid",'forth']
list5.insert(1,"seconde")
print(list5)

# 요소를 제거하는 함수
#.remove(삭제하고자 하는 요소)
list5.remove("forth")
print(list5)

# 요소를 pop하는 함수

list6 = [2,3,5,7,10,4,8,1,9,6]
list6.sort()

for i in range(0,10):
    print(list6.pop(),end = " ")
    if i==9:
        print("clear")

#원하는 요소의 개수를 파악하는 함수
list7 = [2,4,3,4,2,2,1,4,5,2,2,3,4]
count = list7.count(2)
print(" 요소개수는? %d" %count)

# 리스트 확장함수 

list8 = [1,2,3]
list9 = list8 +[2,3,6,7,8]
print(list9)
# append 와 +연산(리스트 확장) 의 차이를 알아야함 
list8.append([2,3,6,7,8])
print(list8)
