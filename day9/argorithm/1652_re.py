# n = int(input())
# rm = []
# for i in range(n):
#     rm.append(list(input()))

# result1=0
# result2=0
# cnt = 0

# # rm = [['....X'],
# #       ['..XX.'],
# #       ['.....'],
# #       ['.XX..'],
# #       ['X....']]


# print(rm)

# # for i in range(n):
# #     for j in range(n):
# #         if rm[i][j] =='.':
# #             cnt+=1
# #             if cnt==n:
# #                 cnt=0
# #                 result1 +=1
# #         else:
# #             if cnt>=2:
# #                 result1 += 1
# #                 cnt=0
# #             else:
# #                 cnt =0
# cnt =0
# for j in range(n):
#     for i in range(n):
#         print(cnt)
#         if rm[i][j] =='.':
#             cnt+=1
#             if cnt==n:
#                 cnt=0
#                 result2 +=1
#         else:
#             if cnt>=2:
#                 result2 += 1
#                 cnt=0
#             else:
#                 cnt =0


# print(result1,result2)


n = int(input())
s = []
cnt_w = 0
cnt_h = 0
position_w = 0
position_h = 0
for i in range(n):
    s.append(input())
for i in s:
    for j in i:
        if j == '.':
            cnt_w += 1
        else:
            if cnt_w > 1:
                position_w += 1
            cnt_w = 0
    if cnt_w > 1:
        position_w += 1
    cnt_w = 0
for i in range(n):
    for j in range(n):
        if s[j][i] == '.':
            cnt_h += 1
        else:
            if cnt_h > 1:
                position_h += 1
            cnt_h = 0
    if cnt_h > 1:
        position_h += 1
    cnt_h = 0
print(position_w, position_h)