

def heap_sort(arr):
    def heapfy(arr, i, n):
        root = i
        left = 2*i+1
        right = 2*i+2

        if left < n and arr[left] > arr[i]:
           root = left

        if right < n and arr[right] > arr[root]:
            root = right

        if root != i:
            arr[i], arr[root] = arr[root], arr[i]
            heapfy(arr, root, n)

    n = len(tab)
    start = (n // 2) - 1
    for j in range(n, 0, -1):
        for parent in range(start, -1, -1):
            heapfy(tab, parent, j)
        tab[0], tab[j-1] = tab[j-1], tab[0]


tab = [4, 2, 1, 8, 5, 7, 9]
print(tab)
heap_sort(tab)
print(tab)
