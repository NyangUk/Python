# 문자열 함수 

#소문자를 대문자로 바꾸는 함수

str1 =  "kimjaeuk"
str2 = str1.upper()

print("{0:^10} {1:^10}".format(str1,str2))

#대문자를 소문자로 바꾸는 함수 
str3 = "HELLO"
str4 = str3.lower()

print("{0:<10} {1:<10}".format(str3,str4))

# 문자열 길이 구하는 함수 
str5 = "nyang uk"
print(len(str5))

# 원하는 문자열 개수 구하는 함수 
print(str5.count("nyang"))

# 문자열의 위치 찾아주는 함수
# 문자, 문자열을 찾은 가장 첫번째 인덱스를 리턴함 업을 경우 -1 리턴 
# .index .find 의 차이점은 해당 문자가 없을 경우 전자는 에러 후자는 -1 을 반환

str6 = "2020년 3월 1일"
print(str6.find("년"))

# print(str6.index("요일")) 


# 공백 지우는 함수 (lstrip rstrip strip) 
# 문자열 사이사이에 있는 공백은 취급하지 않고 가장 왼쪽 가장 오른쪽의 공백만을 지워줌
str7 = "        good   !!!!    "

print(str7.lstrip() +" morning")
print(str7.rstrip() +" morning")
print(str7.strip() + "morning")


# 문자열 대체 함수 
str8 = "my boy friend is ..."
str9 = str8.replace("..." ,"donghyen")
        #str.replace(바뀔 문자,교체할 문자)
print("%s \n%s " %(str8 ,str9))

# 문자열 나누기 함수 

str_split = str9.split()
print(str_split)

#str.split(c) c : 나눌 기준이될 문자 공백,/,? 등 
# 나뉜 문자열들은 리스트로 저장된다.
