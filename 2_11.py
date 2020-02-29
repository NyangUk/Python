# while문


# while <조건> :
#   ...
#   ...

a =10
#예시

while a<14 :
    a+=1
    print(a) 

# 보조제어문

while True :
    a-=1
    print(a)
    if not a:
        print("a = 0 입니다.")
        break