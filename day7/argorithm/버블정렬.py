# def bubble_sort(arr):
#     leng = len(arr) 
#     for re in range(leng):# 수열만큼 버블 정렬 반복
#         leng -=1
#         for i in range(0,leng):
#             for j in range(1,leng+1):
#                 if arr[i] > arr[j]:
#                     arr[i],arr[j] = arr[j],arr[i]
#         for g in arr:
#             print(g,end =' ')
#         print('')    
        
def bubble(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
        for g in arr:
            print(g,end = ' ')
        print('')




n =int(input())

list1 = map(int,input().split())
list1 = list(list1)

bubble(list1)