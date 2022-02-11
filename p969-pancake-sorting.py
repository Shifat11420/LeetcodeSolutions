# https://leetcode.com/problems/pancake-sorting/

# Given an array of integers arr, sort the array by performing a series of pancake flips.

# In one pancake flip we do the following steps:

# Choose an integer k where 1 <= k <= arr.length.
# Reverse the sub-array arr[0...k-1] (0-indexed).
# For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.



def pancakeSort(arr):
    n = len(arr)
    klist = []

    while n>1:
        if arr == sorted(arr):
            return klist
        maxvalue = max(arr[:n])
        for i in range(len(arr)):
            if arr[i]==maxvalue:
                k = i+1
                
        arr[:k] = arr[:k][::-1]
        #print(arr)
        klist.append(k)
        arr[:n] = arr[:n][::-1]
        #print(arr)
        klist.append(n)
        #print("klist = ",klist)
        n=n-1
    return klist    

arr = [3,2,4,1]
print(pancakeSort(arr))        
            