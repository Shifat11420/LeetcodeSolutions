# Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

# Example 1:
# Input: date = "2019-01-09"
# Output: 9
# Explanation: Given date is the 9th day of the year in 2019.

# Example 2:
# Input: date = "2019-02-10"
# Output: 41

# Time: O(1), Space: O(1)
class Solution:
    def dayOfYear(self, date: str) -> int:
        month = {"1":31, "2":28, "3":31, "4":30, "5":31, "6":30, "7":31, "8":31, "9":30, "10":31, "11":30, "12":31}
        year, mon, day = map(int, date.split("-"))
        
        res = 0
        for i in range(1, mon):
            res += month[str(i)]
        res += day
        if (year%400==0 or (year%100 and year%4==0)) and mon>2:
           res += 1
        return res

        