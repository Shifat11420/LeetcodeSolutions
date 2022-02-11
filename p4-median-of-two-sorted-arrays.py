# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).


## 2 pointer solution
nums1 = []
nums2 = [2,3]

def findMedianSortedArrays(nums1, nums2):
    l1,l2 = len(nums1), len(nums2)
    middle = (l1+l2)/2
    
    if middle == 0.5:
        if l1>l2:
            return float(l1[0])
        else:
            return float(l2[0])    
        
    x=y=0
    prev=curr=0
        
    if middle % 1 == 0:
        loops = middle+1
    else:
        loops = middle+0.5
        
    for _ in range(int(loops)):
        prev= curr
        
        if x == l1:
            curr = nums2[y]
            y += 1
        elif y == l2:
            curr = nums1[x]
            x += 1
        elif nums1[x] > nums2[y]:
            curr = nums2[y]
            y +=1
        else:
            curr = nums1[x] 
            x += 1
    if middle % 1 == 0:
        return (prev+curr)/2
    else:
        return float(curr)                         


print(findMedianSortedArrays(nums1, nums2))    