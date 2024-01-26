def heapify(arr, size, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < size and arr[left] > arr[largest]:
        largest = left

    if right < size and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, size, largest)

def heap_sort(array):
    arr = array.copy()
    for i in range(int(len(arr)/2 - 1), 0, -1):
        heapify(arr, len(arr) , i)

    for i in range (int(len(arr) - 1), 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)



