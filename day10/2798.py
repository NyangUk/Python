# n,maxx = map(int,input().split())

# li = list(map(int,input().split()))
# li.sort()

# sum1 =[]
# start = 0
# result =0
# if n==3:
#     result = sum(li)
# else:
#     while start<(n-2):
#         val = li[start]+li[start+1]+li[start+2]
#         sum1.append(val)
#         start+=1

#     for k in range(len(sum1)):
#         result =sum1[k]
#         if sum1[k]>maxx:
#             result =sum1[k-1]
#             break
# print(result)

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = len(a)
sum = 0
for i in range(0, b - 2):
        for j in range(i + 1, b - 1):
                for k in range(j + 1, b):
                        if a[i] + a[j] + a[k] > m:
                                continue
                        else:
                                sum = max(sum, a[i] + a[j] + a[k])
print(sum)