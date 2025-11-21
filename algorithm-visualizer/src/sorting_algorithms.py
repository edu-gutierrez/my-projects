import random

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
            yield arr.copy(), i, i
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
        yield arr.copy(), left, right

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

def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i

        for j in range(i+1, n):
            yield arr.copy(), min, j
            if arr[j] < arr[min]:
                min = j
        
        arr[i], arr[min] = arr[min], arr[i]
        yield arr.copy(), i, min

def quick_sort(arr):
    arr = list(arr)
    yield from _quick_sort(arr, 0, len(arr) - 1)
    return

def _quick_sort(arr, low, high):
    if low < high:
        pivot, frames = _partition(arr, low, high)

        for frame in frames:
            yield frame
        
        yield from _quick_sort(arr, low, pivot - 1)
        yield from _quick_sort(arr, pivot + 1, high)
        yield arr.copy(), low, high

def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    frames = [] # Hay que usar lista para pasar los yields ya que la funcion devuelve un valor
    
    for j in range(low, high):
        frames.append((arr.copy(), j, high))

        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            frames.append((arr.copy(), i, j))

    arr[i+1], arr[high] = arr[high], arr[i+1]
    frames.append((arr.copy(), i+1, high))

    return i+1, frames

def bogo_sort(arr):
    arr = list(arr)
    while not _is_sorted(arr):
        random.shuffle(arr)
        yield arr.copy()

def _is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def random_sort(arr):
    arr = list(arr)
    n = len(arr)

    while not _is_sorted(arr):
        for i in range(n-1, 0, -1):
            j = random.randint(0, i)
            arr[i], arr[j] = arr[j], arr[i]
            yield arr.copy(), i, j
    yield arr.copy()

def bucket_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    if n < 10: 
        num_buckets = 1
    else:
        num_buckets = n // 10
    buckets = [[] for _ in range(0, num_buckets)]

    max_val = max(arr)
    min_val = min(arr)
    range_val = (max_val - min_val)

    for i, value in enumerate(arr):
        index = min(num_buckets - 1, max(0, int((value - min_val) / range_val * num_buckets)))
        buckets[index].append(value)
        yield ("to_bucket", arr.copy(), i, index)

    index = 0

    for bucket_idx, bucket in enumerate(buckets):
        bucket.sort()
        for value in bucket:
            arr[index] = value
            yield ("rebuild", arr.copy(), index, bucket_idx)
            index += 1 

def counting_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    max_val = max(arr)
    count = [0] * (max_val + 1)

    for i, value in enumerate(arr):
        count[value] += 1
        yield ("to_bucket", arr.copy(), i, value)

    index = 0
    for value in range(max_val + 1):
        while count[value] > 0:
            arr[index] = value
            yield ("rebuild", arr.copy(), index, value)
            index += 1
            count[value] -= 1

def radix_sort(arr):
    n = len(arr)
    if n <= 1:
        return
    max_val = max(arr)
    exp = 1

    while max_val // exp > 0:
        buckets = [[] for _ in range(10)]
        
        for i, value in enumerate(arr):
            index = (value // exp) % 10
            buckets[index].append(value)
            yield("to_bucket", arr.copy(), i, index)
        
        index = 0
        for i, bucket in enumerate(buckets):
            for value in bucket:
                arr[index] = value
                yield("rebuild", arr.copy(), index, i)
                index += 1
        
        exp *= 10
