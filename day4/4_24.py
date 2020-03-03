

# 딕션어리 함수

# 항목이 없는 빈 딕션어리 생성 
aa =dict()
print(aa)

# keylist 를 만드는 함수 
#.keys()

bb = {"name" : "김재욱" ,"age":"22","major":"전자공학과"}
keylist1 = bb.keys() # 반환값 dict_keys ([...]) 이라는 객체 
print(keylist1)

keylist2 = list(bb.keys()) #list로 형변환을 해주면 dict_keys은 출력되지 않음 객체를 리스트로 변환
print(keylist2)

for key in keylist2:
   print(key) # 객체요소 각 키값을 출력하기


# valuelist 를 만드는 함수
# values()

valuelist1 = bb.values() # 반환값 dict_values ([...]) 이라는 객체 
print(valuelist1)

valuelist2 = list(bb.values()) #list로 형변환을 해주면 dict_keys은 출력되지 않음 객체를 리스트로 변환
print(valuelist2)

for value in valuelist2:
   print(value) # 객체요소 각 벨류값을 출력하기

# item(key:value)을 얻는 함수

itemlist = bb.items()  # 반환값 dict_itmes ([...]) 이라는 객체 
print(itemlist)

# key:value 를 모두 삭제하기
# bb.clear()
# print(bb)

# key value 얻어오기
# .get(), [] ,.pop()


age = bb.get('age')  # key가 존재하지 않을경우 None 값을 반환한다 
print(age)

gender = bb.get('gender' ,'디폴트값') #key가 존재 하지 않을때 출력할 디폴트 값을 설정해줄수 있음 
print(gender)

major = bb.pop("major") # 딕션어리의 항목을 없앤뒤 가져오는 함수 
print(major)
print("pop을 한뒤의 bb" ,bb)

#pop에 매개변수로 디폴트 값이 전달되지 않을 경우 없는 키를 pop하면 에러가뜨므로 꼭 디폴트 값을 전달한다.
major = bb.pop("major","없음") # 딕션어리에 major가 없어졌기 때문에 디폴트값이 출력된다.

print(major)

age = bb['age'] # key가 존재하지 않을경우 error가 난다
print(age)

# 딕션어리에 해당키가 존재하는지 알아보기 
confirm_bb = 'gender' in bb
print(confirm_bb)  #False 출력

confirm_bb ='name' in bb
print(confirm_bb) #True 출력 


# 딕션어리의 항목의 개수를 알수있는 함수

length =len(bb)
print(length)