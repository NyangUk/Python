#solution 1
def true_or_false():
    n = list((input("숫자를 입력하시오")))
    m = n
    n.reverse() # 뒤집었은것 
    # 문자열로 변환
    ns =''.join(n)
    ms =''.join(m)
    if ns ==ms:
        print("True")
    else:
        print("False") 

#solution 2
def str_true_false(num):
    n =str(num)
    flag =1 # 문자열을 뒤집을때랑 같은지 T,F 문자열의길이가 1인경우 for 문을 돌지 않으므로 시작 플래그를 1로 둬야한다.
    # 문자열길이가 홀수 일때 1 n, 2 n-1,... 정가운데는 확인 안해도된다.
    # 문자열의길이가 짝수일때 1 n ,2 n-1... 모두 인해야한다.
    for i in range(len(n)//2):
        print(n[i],n[len(n)-i-1])
        if n[i] ==n[len(n)-i-1]:
            pass
        else:
            flag =0
            break
    print(flag)

# 0 1 2 3 4 5 6 7 

# true_or_false()
str_true_false(1)


