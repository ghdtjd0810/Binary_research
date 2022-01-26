'''
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
'''



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

# 위에 알고리즘이랑 똑같은거임.

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end )//2
        if array[mid] == target:
            return mid
        elif array[mid] <= target:
            start = mid + 1
        else:
            end = mid -1 

            
n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0 , n-1)

if result == None:
    print('nothing')
else:
    print(result +1)


## 내가 한번 해보자. 정렬이 되어 있는 상태이다. 지금
# 그러니까 꼭 스토리대로 흘러가지 않더라도 알고리즘의 이점을 살리면 충분히 짧고 간단한 문장이 나올 수 있다.
'''
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end )//2
        if array[mid] == target:
            return mid
        elif: array[mid] <= target:
            start = mid + 1
        else:
            start = start +1
'''
