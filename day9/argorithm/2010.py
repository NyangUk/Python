n = int(input())

multi = []
for i in range(n):
    multi.append(int(input()))

remove = n-1
# print(multi)
# if remove == 0:
#     print(sum(multi))
# else:
result = sum(multi)-remove
print(result)