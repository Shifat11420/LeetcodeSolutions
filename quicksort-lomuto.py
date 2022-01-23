def swap(a, b, arr):
    if a!=b:
        temp = arr[a]
        arr[a] = arr[b]
        arr[b] = temp


def partition(start, end, elements):
    pivot = elements[end]
    pi = start

    for i in range(start,end):
        if elements[i]<= pivot:
            swap(pi, i, elements) 
            pi += 1    
    swap(pi, end, elements) 

    return pi
    
    

def quick_sort_lomuto(start, end,elements):
    if len(elements) == 1:
        return
    if start < end:
        pi = partition(start, end,elements)
        quick_sort_lomuto(start, pi-1 ,elements)
        quick_sort_lomuto(pi+1, end, elements)


if __name__ == '__main__':
    tests = [
        [11,9,29,7,2,15,28],
        [3, 7, 9, 11],
        [25, 22, 21, 10],
        [29, 15, 28],
        [],
        [6]
    ]
    # elements = ["mona", "dhaval", "aamir", "tina", "chang"]

    for elements in tests:
        quick_sort_lomuto(0, len(elements)-1, elements)
        print(f'sorted array: {elements}')

