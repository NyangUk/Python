import sys

sys.path.append("/home/jaeuk/JaeUk/Python/day6")

# 절대 경로를 통해 import 하고자 하는 상위디렉토리를 알려주고 
# sys.path.append를 통해 절대경로안에 import 하고자하는 파일이 있음을 알려준다.

import moddule6_8 as mo

mo.show("김재욱",22)
mo.math1(1,8)

# from 모듈이름 import 모듈함수1, 모듈함수2
# from 모듈이름 import* 를 하면 모든 함수를 불러올 수있다. 

# 바이트코드 형태의 .pyc형태로 불러오기
# 파이썬에서는 모듈을 불러올때 좀더 빠르게 처리 할수 있도록 pyc확장자를 가지는 바이트 코드를 사용한다.

