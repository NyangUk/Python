def Insertion_sort(arr):
    count =0 
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while i>= 0 and arr[i]>key:
            count+=1
            arr[i+1] =arr[i]
            i= i-1
        arr[i+1] =key
        # for g in arr:
        #     print(g,end=' ')
    return count

n =int(input())

list1 = map(int,input().split())
list1 = list(list1)

print(Insertion_sort(list1))