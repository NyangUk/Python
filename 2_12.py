#for문 


#for 문 유형 1
list1 = ['a','b','c']

for i in list1 :
    print(i)

list2 = [90,39,53,28,64,77]


#리스트 
number = 0
for i in list2:
    number = number+1
    if i>50 :
        print("%d번째 학생 %d점수로 합격되었습니다." %(number,i))
    else :
        print("%d번째 학생 %d 점수로 불합격되었습니다." %(number,i))

#튜플
list3 = [('a','b'),('c','d'),('e','f')]
for (i,j) in list3 :
    print (i+j)


#문자열 
str1= "asdfghjkl"

for i in str1:
    if i == 'g':
        print("g 를 찾았습니다.")