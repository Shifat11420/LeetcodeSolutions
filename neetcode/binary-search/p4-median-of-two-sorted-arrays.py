# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

## binary search
nums1 = [1,2]
nums2 = [3,4]

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

#NEETCODE
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1)+len(nums2)
        half = total//2

        if len(A)>len(B):
            A, B = B, A

        l, r = 0 , len(A)-1
        while True:
            i = (l+r)//2     # for A
            j = half-i-2     # for B, index, so -2 for 0's in A and B

            Aleft = A[i] if i>=0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity") 
            Bleft = B[j] if j>=0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            if Aleft<=Bright and Bleft<=Aright:
                #odd
                if total % 2:
                   return min(Aright, Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                r= i-1
            else:
                l = i+1

new = Solution
print(new().findMedianSortedArrays(nums1,nums2))

