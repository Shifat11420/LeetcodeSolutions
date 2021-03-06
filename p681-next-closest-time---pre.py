# https://leetcode.com/problems/next-closest-time/description/
# 
#Given a time represented in the format "HH:MM", from the next closest time by reusing the current digits. There is no limit on how many times a digit can be reused.
# You may assume the given input string is always valid. For example, “01:34”, “12:09” are all valid. “1:34”, “12:9” are all invalid.

# Example 1:
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, 
# which occurs 5 minutes later.  
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. 
# It may be assumed that the returned time is next day's time since it is smaller 
# than the input time numerically.


def nextClosestTime(time):        
    s = set(time)
    hour = int(time[0:2])
    minute = int(time[3:5])

    while True:
        minute += 1    
        if minute == 60:
            minute = 0
            hour = 0 if hour == 23 else hour + 1
        time = "%02d:%02d" % (hour, minute)    
       
        if set(time) <= s:   ## <= includes
            return time
    return time    
 
 
time = "13:33"    
print(nextClosestTime(time))
