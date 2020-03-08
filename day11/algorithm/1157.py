import collections
n = input()

n=n.upper()

dic = collections.Counter(n)
re = []
# 문자열중 중복되는 문자의 개수를 세고 리스트에 추가
for key,value in dic.items():
    re.append([value,key])

print(dic)

# 만약에 리스트에 추가된 것이 1개라면 
# z, bbbb,ccccccccc 등등 
if len(re) == 1:
    print(re[1][0])
else:
    re.sort()
    re.reverse() # 내림차순으로 정렬한다.
    if re[0][0]==re[1][0]: # 내림차순으로 정리해서 알파벳 개수가 동일하면 ? 출력
        print('?')
    else:           #그렇지 않으면 멕시멈 값 출력
        print(re[0][1])

    
