# problem description
# file:///home/shifat/Pictures/Screenshot%20from%202022-02-17%2014-48-28.png

## two pointers

"""
#Definition of interval
class Interval(object):
    def __init__(self,start,end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self,intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        s,e =0,0
        res, count = 0, 0
        
        while s<len(intervals):    ## iterate through all of the start times
            if start[s]<end[e]:
                s+=1
                count+=1
            else: 
                e+=1
                count-=1
            res = max (res,count)  
            
        return res      

#input
intervals = [(0,30),(5,10),(15,20)]