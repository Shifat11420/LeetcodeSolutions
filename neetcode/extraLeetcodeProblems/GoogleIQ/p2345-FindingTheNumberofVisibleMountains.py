# You are given a 0-indexed 2D integer array peaks where peaks[i] = [xi, yi] states that mountain i has a peak at coordinates (xi, yi). A mountain can be described as a right-angled isosceles triangle, with its base along the x-axis and a right angle at its peak. More formally, the gradients of ascending and descending the mountain are 1 and -1 respectively.
# A mountain is considered visible if its peak does not lie within another mountain (including the border of other mountains).
# Return the number of visible mountains.

# Example 1:
# Input: peaks = [[2,2],[6,3],[5,4]]
# Output: 2
# Explanation: The diagram above shows the mountains.
# - Mountain 0 is visible since its peak does not lie within another mountain or its sides.
# - Mountain 1 is not visible since its peak lies within the side of mountain 2.
# - Mountain 2 is visible since its peak does not lie within another mountain or its sides.
# There are 2 mountains that are visible.

# Example 2:
# Input: peaks = [[1,3],[1,3]]
# Output: 0
# Explanation: The diagram above shows the mountains (they completely overlap).
# Both mountains are not visible since their peaks lie within each other.

# class Solution:
# does not work for [[2,2],[2,2],[3,1]]
#     def visibleMountains(self, peaks: List[List[int]]) -> int:
#         count = Counter((x,y) for x,y in peaks)
#         peaks = sorted([k for k, v in count.items() if v==1])
#         stack = []

#         def isHidden(peak1, peak2):
#             x1, y1 = peak1
#             x2, y2 = peak2
#             return x2-y2<=x1-y1 and x1+y1<=x2+y2


#         for i, peak in enumerate(peaks):
#             while stack and isHidden(peaks[stack[-1]], peak):
#                 stack.pop()
#             if stack and isHidden(peak, peaks[stack[-1]]):
#                 continue
#             stack.append(i)

#         return len(stack)

class Solution:
    # Time: O(nlogn), Space: O(n)
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        stack = [-inf]
        curMax = 0
        for x, y in sorted(peaks):
            # find triangle x boundaries
            pos, neg = x-y, x+y

            # remove previous mountain that got overlapped
            while stack[-1] >= pos:
                stack.pop()

                # will not get overlapped by previous mountain
            if neg > curMax:
                curMax = neg
                stack.append(pos)
        return len(stack) - 1
