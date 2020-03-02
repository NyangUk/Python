# 파일 입출력 

# 파일 객체 = open(파일 이름 ,파일열기모드)

# r : 읽기모드 파일을 읽기 용도로 시용 
# w : 쓰기모드 파일에 내용을 쓸때 이미 파일이 존재할경우 파일내용 초기화 그렇지 않은 경우 새로운 파일 생성
# a : 추가모드 파일에 새로운 내용을 추가할때  

file1= open("test.txt",'w')
# 경로를 다로 설정을 하지 않을 경우 해당 코드파일이 존재하는 디렉토리에 저장
file1.close()
# close를 꼭 사용 하여 파일을 닫아준다.

file1= open("test.txt",'w')

for i in range(1,5):
    content = "%d 번째줄...\n" %i
    file1.write(content)

#파일의 한줄만 읽어오는 방법 
#.readline()

file1 = open("test.txt",'r')
data = file1.readline() #읽어온 라인을 리턴한다.
print(data)
file1.close()


#파일 전체를 읽어오는 방법 1
file1 = open("test.txt",'r')

while True :
    data = file1.readline()  #더이상 읽을 값이 없을 경우 null 을 리턴한다.
    if not data :
        break
    print(data, end= '')

file1.close()

# 파일 전체를 읽어오는 방법 2
#.readlines()

file1 = open("test.txt",'r')
datas = file1.readlines() # 리턴값이 리스트이다.
for i in range(len(datas)) :
    print(datas[i],end ='')

file1.close()

# 파일 전체를 읽어오는 방법 3
# .read()

file1 = open("test.txt",'r')
datass = file1.read() # 리턴 값이 문자열이다.
print(datass)
file1.close()

# a모드를 이영하여 파일에 내용을 추가하기 

file1 = open("test.txt" ,'a')

for i in range(5,8):
    content = '%d번째줄--- \n' %i
    file1.write(content)

file1.close()

# with 문을 이용해 파일객체 다루기 
file1 = open("test.txt" ,'w')
file1.write("파일 입출력 테스트 2번째 ")
file1.close()

#open을 사용하면 close를 무조건 해줘야하는 번거로움을 with를 이용하면 편리함
with open("test.txt","w") as file1 :
    file1.write("with문을 이용한 파일 입출력 테스트 3번째")

# 해당 범위를 벗어나게 될경우 자동으로 close 된다.


#여러 파일을 출력하기 위한 모듈 
# 도스 명령중에 type이라는 기능을 구현하기 위해 모듈을 가져옴

import sys

# 저장후 명령프롬포트에서 실행해야함 type이용
args = sys.argv[1:]
for i in args :
    print (i) 