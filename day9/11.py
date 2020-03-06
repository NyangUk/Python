#queue

# put() ,get()으로 넣고 빼고 한다.
import queue

#선입선출 
q = queue.Queue()

for i in range(3):
    # 큐에 집어 넣기
    q.put(i)

while not q.empty(): # 큐가 비어있으면 반복문 나오기
    print(q.get(), end =' ')



#후입선출 큐
lq = queue.LifoQueue()


for i in range(3):
    # 큐에 집어 넣기
    lq.put(i)

while not lq.empty(): # 큐가 비어있으면 반복문 나오기
    print(lq.get(), end =' ')

#우선 순위 큐
# queue.PriorityQueue()를 이용하여 생성가능

