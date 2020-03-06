#unpacking


# unpacking을 하려면 각요소에 대입!
pa = (1,2)
a,b = pa

print(a,b)

li = ['a','b',3,('서울',8)]
a,s,d,f = li

# 리스트안에있는 튜플을 풀어낼 수있음
a,s,d,(i,j) = li
print(a,s,d,f,i,j )

st = "Hello"
a,s,d,f,g =st
print(a)

# 특정값을 무시하거나 *을 이용하여 여러개를 언패킹하기

li = ('a','s','d','f')

#언더바를 이용하여 특정값 무시 
a,_,d,_ = li
print(a,d)

li = [[1,2],[3,4],[5,6],[7,8]]

#언패킹을통한 리스트 요소접근

for i, j in li:
    print(i+j)