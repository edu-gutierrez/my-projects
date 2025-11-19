def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True                
                yield arr.copy(), j, j+1
        if not swapped:
            break

def cocktail_sort(arr):
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        
        new_left = right
        for i in range(right, left, -1):
            if arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                new_left = i
                yield arr.copy(), i, i-1
        left = new_left

        new_right = left
        for i in range(left, right):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                new_right = i
                yield arr.copy(), i, i+1
        right = new_right

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        yield arr.copy(), i , j
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            yield arr.copy(), j, j+1
            j-=1
        arr[j+1] = key
        yield arr.copy(), j+1, i

def merge_sort(arr):
    arr = list(arr)
    yield from _merge_sort(arr, 0, len(arr) - 1)
    return

def _merge_sort(arr, left, right):
    if left >= right:
        return
    mid = (left + right) // 2

    yield from _merge_sort(arr, left, mid)
    yield from _merge_sort(arr, mid + 1, right)
    yield from _merge(arr, left, mid, right)

def _merge(arr, left, mid, right):
    temp = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        yield arr.copy(), i, j
        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= mid:
        yield arr.copy(), i, i
        temp.append(arr[i])
        i += 1
    while j <= right:
        yield arr.copy(), j, j
        temp.append(arr[j])
        j += 1

    for k, val in enumerate(temp):
        arr[left + k] = val
        yield arr.copy(), left + k, left + k

def gnome_sort(arr):
    n = len(arr)
    i = 1
    while i < n:
        if arr[i-1] <= arr[i]:
            yield arr.copy(), i-1, i
            i += 1
            
        else:
            arr[i-1], arr[i] = arr[i], arr[i-1]
            yield arr.copy(), i-1, i
            i -= 1
            if i == 0:
                i = 1
