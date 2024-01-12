# An array arr is a mountain if the following properties hold:
# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

# You must solve it in O(log(arr.length)) time complexity.

# Example 1:
# Input: arr = [0,1,0]
# Output: 1

# Example 2:
# Input: arr = [0,2,1,0]
# Output: 1

# Example 3:
# Input: arr = [0,10,5,2]
# Output: 1

# Time: O(logn), Space: O(1)
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        l, r = 0, n-1
        while l<=r:
            if r-l+1 == 2:
                if arr[l]>arr[r]:
                    return l
                else:
                    return r    
            mid = (l+r)//2
            if mid-1>=0 and arr[mid-1]<arr[mid]<arr[mid+1]:
                l = mid+1
            elif mid+1<n and arr[mid-1]>arr[mid]>arr[mid+1]:
                r = mid-1
            elif mid-1>=0 and mid+1<n and arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]:
                return mid       
