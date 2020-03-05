# n = int(input())

# c =[]
# nc=[]
# for a in range(n):
#     li = map(int,input().split())
#     arr = list(li)
#     c.append(arr)


# for i in range(len(li)):
#     for j in range(i+1):
#         if c[i][0]>c[j][0] and c[i][1]>c[j][1]:
#         el


num_student = int(input())
student_list = []

for _ in range(num_student):
    weight, height = map(int, input().split())
    student_list.append((weight, height))

for i in student_list:
    rank = 1
    for j in student_list:
        if i[0] < j[0] and i[1] < j[1]:
                rank += 1
    print(rank, end = " ")