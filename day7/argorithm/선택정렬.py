n =int(input())


list1 = map(int,input().split())
list1 = list(list1)


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)): # 가장작은 값의 인덱스를 찾는 
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        for g in list1:
            print(g,end=' ')
        print('')
        

    
        
        

selection_sort(list1)
# print(list1)

# 2 6 3 1 5
# 0 1 2 3 4 