def merge_sort(array, left, right):
    if left < right:
        mid = left + int((right - left) / 2)

        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

def merge(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = []
    R = []

    for i in range(n1):
        L.append(array[left + i])

    for j in range(n2):
        R.append(array[mid + 1 + j])

    i = 0
    j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1

        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1
