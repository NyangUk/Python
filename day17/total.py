# 문자열 주요함수 
# len(str)              #str의 길이를 리턴함
# str.upper() 
# str.lower()   
# str.swapcase()        # 대문자는 소문자로 소문자는 대문자로
# str.title()           # 각 단어나 문자열의 첫글자를 바꿔줌
# str.count('')         # 괄호안의 문자열이 몇개있는지 리턴
# str.find(s1,n2)       # s1 =찾을 문자열 n2=시작할 인덱스 ,인덱스 리턴 없을경우 -1
# str.rfind(s1,n2)      # 뒤에서부터 찾기 , 인덱스 리턴 없을경우 -1
# str.index()           # 인덱스 리턴 없을경우 -1
# str.rindex()          # 뒤에서부터 찾기,인덱스 리턴 없을경우 -1
# str.startswith(s1)    # s1이 문자열 처음부터 시작하는지  T,F리턴
# str.endswith(s1)      # s1이 문자열 끝에서부터 시작하는지  T,F리턴
# str.strip(s1)         #s1 문자를 모두 지운다.
# str.rstrip(s1)        #s1 문자를 문자열 기준 오른쪽으로 모두 지운다.  공백시 함수전달인자 x
# str.lstrip(s1)        #s1 문자를 문자열 기준 왼쪽으로 모두 지운다.  공백시 함수전달인자 x
# str.replace(s1,s2)    # s1을 s2로 모두 바꾼다.
# str.ljust(n1)         # 문자열을 n1 만큼 왼쪽에서 띄어서 출력
# str.rjust(n1)         # 문자열을 n1 만큼 오른쪽에서 띄어서 출력
# str.center(n1)        # n1만큼 빈공간만들고 중앙에 문자열 배치
# str.spilt(s1)         #s1문자를 기준으로 문자열을 분리 리턴타입은 리스트
# str.spiltline(s1)     # 행을 기준으로문자열을 분리 더알아보기 $$$$$$$$$$$$$$$$$
# str.isdigit()         # 숫자인지 리턴 T,F
# str.alpha()           # 알파벳인지 리턴 T,F
# str.isalnum()         #알파벳이랑 숫자인지 리턴 T,F
# str.isspace()         #공백인지 리턴 T,F
# str.islower()         #소문자인지 리턴 T,F
# str.isupper()         #대문자인지  리턴 T,F


# 리스트 주요함수 
# list.append(t1)       #매개변수값을 리스트끝에 추가
# list.pop()            #리스트 가장 마지막에 있는 값 리턴하고 지우기ㅣ
# list.reverse()        # 리스트를 뒤집어준다, 리턴값 x
# reversed(list1)       # 해당 리스트를 뒤집어 리스트로 리턴한다.
# list.sort()           # 리스트를 오름차순 정렬해준다, 리턴값 x
# sorted(list1)         #리스트를 오름차순으로 정렬하여 리스트로 리턴한다.
# list.remove(t1)       #리스트안에 있는 요소 t1을 첫번째 한개만 지운다.
# list.insert(n1,t1)    #리스트 n1자리에 t1을 추가하고 뒤에 인덱스틀은 1칸식 밀리게 됨
# list.extend()         #list1+list2와 같은 리스트 확장개념
# list.count(t1)         # 리스트 내의 t1의 개수를 리턴함
# list.index(t1)        # 리스트 내의 t1의 인덱스를 리턴함
# len(list)             #리스트의 길이를 리턴
# del(list[n1:n2])      # 해당 리스트의 n1-n2까지 없앤다

# 집합 주요함수
# s=set()               # 빈세트 만들기 세트안에 리스트 초기화 할때는 문자열이나 리스트 1개만가능함 리스트 안의 소개수 상관x
# set.add()             # 값을 하나만 추가 할때 리스트안의 요소를 모두 분해하여 추가됨
# set.update()          # 값을 여러개 추가 할때 2차원 리스트는 넣을수 없음
# set.clear()           # 집합을 초기화시켜줌
# s =s1 & s2            # 교집합 집합 객체리턴
# s =set.intersection() #
# s =s1 - s2            # 차집합 집합 객체리턴 s2의 요소가 s1에 있으면 삭
# s =set.difference()
# s =s1 ^ s2            # 대칭차집합 두 집합중 없는 요소만을 집합 객체로 리턴
# s =s1 | s2            # 합집합 집합 객체리턴
# s =set.union()
# len(s)                # 집합의 개수를 출력

# 딕션어리 주요함수
# dict[k] = value        # 항목추가 또는 항목수정
# del(dict[k])           # 항목삭제
# d =dict.keys()         # 딕션어리에 있는 모든 key값을 리스트로 리턴함
# d =dict.values()       #딕션어리에 있는 모든 value 값을 리스트로 리턴함
# d =dict.items()        #딕션어리에 있는 모든 key:value들을 2차원 리스트로 리턴함
# dict.clear()           #딕션어리에있는 모든 것 초기화
# v =dict.get(k)         # k에 해당하는 v값 리턴, 없을 경우 None 리턴
# v =dict.get(k,default) # k에 해당하는 v값 리턴, 없을경우 설정한 디폴트값 리턴
# v =dict.pop(k,default) #k에 해당하는 value값을 리턴하고 없앤다. 디폴트값 설정 필수!
# v =dict[k]             # 딕션어리 안에 k에해당하는 v값 리턴 없을 경우 에러 
# len(dict)              # 딕션어리이의 항목개수 리턴
# T,F = 'key' in dict    #있으면 T 없으면 F
# for key,value :dict.items(): 를 이용하면 모든항목에 접근가능 

# 문자열>숫자
print(int('123')+int('1'))

# 숫자 > 문자열
print(str(123)+str(1))

# 문자열>리스트
print(list("123"))

# 기준을 가지고 문자열 >리스트
s0 = "my name is jaeuk"
li0 = s0.split()
print(li0)
# 리스트 >문자열 숫자일때는 불가능이야!
li1 = ['1','2','3']
print(''.join(li1))

# 숫자>리스트  숫자를 문자열로 바꾼후 리스트로 변환
print(list(str(123)))

# 리스트>숫자   리스트를 문자열로 바꾼후 숫자로 바꿈
li2=['1','2','3','4']
print(int(''.join(li2)))


#문자열에서 해당 문자의 개수세기
s1 = "aassssdddffffff"
print(s1.count('f'))

# if문중 list에서 해당값을 찾을때
li3 = ['1','a',1]
if 1 in li3:
    print("true")