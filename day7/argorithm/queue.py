import collections
n= int(input())

queue = collections.deque()

for i in range(n):
    cmd = input()    
    cmd = cmd.split()
    con =len(queue)

    if 'i' in cmd:
        queue.append(cmd[1])
    elif 'c' in cmd:
        print(con)
    elif 'o' in cmd:
        if con ==0:
            print("empty")
        else:
            print(queue.popleft())


