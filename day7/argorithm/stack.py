n =int(input())
stack = []

for i in range(n):
    commend = input()
    cmd = commend.split()

    if 'i' in cmd:
        stack.append(cmd[1])

    elif 'o' in cmd:
        if len(stack)==0:
            print("emtpy")        
        else:
            print(stack.pop())


    elif 'c' in cmd :
        print(len(stack))



# s = "hello python!"
# s.split()
# print(s)

# stack= [1,2,3]
# aa = []
# print(stack[1])
# aa.append(stack[1])
# print()