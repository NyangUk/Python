#   0 1 2 3 4 5 6 7 8 9
c =[6,2,5,5,4,5,6,3,8,7]

n = int(input())
ans =''
# while True:
#     if n ==3:
#         ans+='7'
#         break
#     elif n==0:
#         break
#     n-=2
#     ans+='1'



if n%2 ==0:
    ans +='1'*(n//2)
else:
    ans= '7'+'1'*((n-3)//2)
print(ans)


