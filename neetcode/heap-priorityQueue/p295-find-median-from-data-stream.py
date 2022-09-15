# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.
# For example, for arr = [2,3,4], the median is 3.
# For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example 1:
# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0
 
import heapq

class MedianFinder:
    # two heaps, large, small, minheap, maxheap
    # heaps should be equal size, that is, size difference should be >1
    def __init__(self):
        self.small, self.large = [], []         #small= maxheap, large=minheap, in python heap can be initialized by list

    # Complexity all heap operations here are O(logn)
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)       # push in the maxheap or minheap with negative values

        # make sure every num in small <= every num in large
        if self.small and self.large and -1 * self.small[0] > self.large[0]:    #small[0] = max value of maxheap and large[0] = smallest value in minheap                
            val = -1 * heapq.heappop(self.small)                                # -1 to get the actual value                           
            heapq.heappush(self.large, val)

        # uneven lengths?
        if len(self.small) > len(self.large)+1 :
            val = -1 * heapq.heappop(self.small)                                 # -1 to get the actual value
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small)+1 : 
            val = heapq.heappop(self.large)                                 # -1 to get the actual value
            heapq.heappush(self.small, -1 * val)  

        

    def findMedian(self) -> float:
        if len(self.small)> len(self.large):
            return -1 * self.small[0]
        if len(self.large)> len(self.small):
            return self.large[0]
        return (-1 * self.small[0] + self.large[0]) / 2  
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()

