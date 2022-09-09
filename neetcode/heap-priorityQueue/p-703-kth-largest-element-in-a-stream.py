# Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

# Implement KthLargest class:

# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

# Example 1:

# Input
# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
# Output
# [null, 4, 5, 5, 8, 8]

# Explanation
# KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
# kthLargest.add(3);   // return 4
# kthLargest.add(5);   // return 5
# kthLargest.add(10);  // return 5
# kthLargest.add(9);   // return 8
# kthLargest.add(4);   // return 8
 
# Use min heap because we will only add elements, and we are finding largest elements nd minimum of them
# min heap: add/pop------> logn, find min value------>O(1)
# Complexity : time O(nlogn) worst case
import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # minheap with k largest integers
        self.minheap, self.k = nums, k
        heapq.heapify(self.minheap)
        while len(self.minheap)> self.k:
            heapq.heappop(self.minheap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap)> self.k:
            heapq.heappop(self.minheap)
        return self.minheap[0]         # always minimum element


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)