def merge_two_sorted_arrays(arr1,arr2, arr):
    i = j = k = 0

    len_arr1 = len(arr1)
    len_arr2 = len(arr2)

    while i < len_arr1 and j < len_arr2:
        if arr1[i]<arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1 
        k += 1    
            
            
    while i < len_arr1:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len_arr2:
        arr[k] = arr2[j]
        j += 1
        k += 1
   

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid :]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_arrays(left,right, arr)


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9,8,7,2],
        [1,2,3,4,5]
    ]

    for arr in test_cases:
        merge_sort(arr)
        print(arr)
