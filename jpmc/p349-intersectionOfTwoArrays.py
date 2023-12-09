# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]

# Example 2:
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=set(nums1)
        n2=set(nums2)
        l1,l2 = len(n1),len(n2)
        if l2<l1:
            l1,l2 = l2,l1
        res = []
        for n in n1:
            if n in n2:
                res.append(n)   
        return res         
        
        # Alternative answers
        # return list(n1&n2)
        # return list(n1.intersection(n2))