def binary_search(array, target, start, end):
    if start> end:
        return None
    mid = (start + end)// 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input.split()))

result = binary_search(array, target,0, n-1)




def binary_search_while(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid +1

    return None




## 내가 한번 해보자 그러니까 꼭 

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target :
            end = mid -1
        else:
            start = mid + 1
