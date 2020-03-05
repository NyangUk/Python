a= input()
b= input()
c= input()

num =int(a)*int(b)*int(c)
num=str(num)
for i in range(0,10):
    print(num.count(str(i)))

    #문자열중 해당 문자의 개수를 세고 싶을때 count를 쓴