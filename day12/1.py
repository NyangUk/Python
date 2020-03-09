    #문자열

#문자열을 만드는 4가지 경우
# "" , '' ,""" """ ,''' ''' 

# 3개를 쓸경우 줄바꿈을 효율적으로 쓸수 있음
str1 ="""
my name is....
Jaeuk
"""
print(str1)

#문자열의 덧셈
s2 = "I'm"
s3 = "happy"

print(s2+' '+s3)

#문자열의 곱셈
s4 = ':D'
n = 10
print(s4*n)

# 문자열의 인덱싱 
s5 = "Life is too short ,you need Python"
print(s5[15] ,s5[-1])

for i in range(len(s5)-1,-1,-1):
    # 끝에서 부터 출력하려면 range 의 특성을 잘알아야함
    # range(시작 인덱스,끝인덱스,증감량)
    print(s5[i])

# 문자열 슬라이싱
s6 = "Life is too short ,you need Python"



ss ="aaaaaasdfghjkl"
print(ss.strip('a'))
print(ss.split('s'))
print(ss.split('d'))
 