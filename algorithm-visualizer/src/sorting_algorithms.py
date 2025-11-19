def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True                
                yield arr.copy(), j, j + 1
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
                yield arr.copy(), i, i - 1
        left = new_left

        new_right = left
        for i in range(left, right):
            if(arr[i] > arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                new_right = i
                yield arr.copy(), i, i + 1
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
