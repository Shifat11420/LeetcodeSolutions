# problem : https://github.com/codebasics/data-structures-algorithms-python/blob/master/algorithms/5_MergeSort/merge_sort_exercise.md 


def merge_two_sorted_arrays(left_list,right_list, key, descending = False):
    arr = []

    if descending:
        while len(left_list)>0 and len(right_list)>0:
            if left_list[0][key]>=right_list[0][key]:
                arr.append(left_list.pop(0))               
            else:
                arr.append(right_list.pop(0))
        
    else:
        while len(left_list)>0 and len(right_list)>0:
            if left_list[0][key]<=right_list[0][key]:
                arr.append(left_list.pop(0))              
            else:
                arr.append(right_list.pop(0))
    

    arr.extend(left_list)
    arr.extend(right_list)
    return arr

def merge_sort(elements, key, descending = False):
    if len(elements) == 1:
        return elements

    mid = len(elements)//2

    left = elements[:mid]
    right = elements[mid:]

    left_list = merge_sort(left, key, descending)
    right_list = merge_sort(right, key, descending)

    sorted_list = merge_two_sorted_arrays(left_list,right_list, key, descending)

    return sorted_list


if __name__ == '__main__':
    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]

    sorted_list1 = merge_sort(elements, key='time_hours', descending=True)
    sorted_list2 = merge_sort(elements, key='name')

    print(sorted_list1)
    print(sorted_list2)
