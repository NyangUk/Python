n= int(input())
box =0

while True:    
    if (n%5) == 0:
        box= box+(n/5)
        print(box)
        break
    n-= 3
    box += 1
    if n <0:
        print("-1")
        break


# inp = int(input())
# Box = 0
# while True:
#     if (inp % 5) == 0:
#         Box = Box + (inp//5)
#         print(Box)
#         break
#     inp = inp-3
#     Box += 1
#     if inp < 0:
#         print("-1")
#         break