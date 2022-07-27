# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]


#Complexity: 
# time = O(n)    actually O(n)+ O(n) for n length of input array,   len(freq) + len (freq[i])
# Space = O(n)      hashmap

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:

def topKFrequent(nums, k):
    count = {}
    freq = [[] for i in range(len(nums)+1)]  

    for n in nums:
        count[n] = 1 + count.get(n,0)              ## count[number] = occurance, {1:3, 2:2, 3:1, 4:2}

    for n, c in count.items():
        freq[c].append(n)                          ## freq[occurance] = list of numbers,   [1:[3],2:[2,4],3:[1]], sorted
    print(freq)    

    res = []
    for i in range(len(freq)-1, 0, -1):           ## descending loop
        for n in freq[i]:
            res.append(n)

            if len(res) == k:
                return res


nums = [1,1,1,2,2,3,4,4]
k = 2 
print(topKFrequent(nums, k))