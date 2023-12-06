# Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.

# Example 1:
# Input: arr = [5,5,4], k = 1
# Output: 1
# Explanation: Remove the single 4, only 5 is left.

# Example 2:
# Input: arr = [4,3,1,1,3,3,2], k = 3
# Output: 2
# Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
 

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
      n = len(arr)
      count = Counter(arr)
      res = 0
      
      freq = [[] for i in range(n+1)]
      for key, v in count.items():
        freq[v].append(key)

      for i,v in enumerate(freq):
        if len(v)>0:
          for val in v:
            if count[val]>k:
              break
            else:
              k -= count[val]
              count.pop(val)
              if k==0:
                break
      return len(count.keys())