# You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
# Return the maximum number of events you can attend.

# Example 1:
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.

# Example 2:
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4

# Worst-case Time Complexity: O(nlogn)
# Worst-case Space Complexity: O(n)

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort()

        started = []
        count = 0
        i = 0
        curr_day = events[0][0]

        while i<n:
            while i<n and events[i][0]==curr_day:
                heapq.heappush(started, events[i][1])
                i += 1

            heapq.heappop(started)
            count += 1
            curr_day += 1

            while started and started[0]<curr_day:
                heapq.heappop(started)

            if i<n and not started:
                curr_day = events[i][0]   
 

        while started:
            if heapq.heappop(started)>=curr_day:
                curr_day += 1
                count += 1

        return count                    
                    

