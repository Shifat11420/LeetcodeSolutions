# You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
# There are two types of logs:
# Letter-logs: All words (except the identifier) consist of lowercase English letters.
# Digit-logs: All words (except the identifier) consist of digits.
# Reorder these logs so that:
# The letter-logs come before all digit-logs.
# The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
# The digit-logs maintain their relative ordering.
# Return the final order of the logs.

# Example 1:
# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig".
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".

# Example 2:
# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
 
# Constraints:
# 1 <= logs.length <= 100
# 3 <= logs[i].length <= 100
# All the tokens of logs[i] are separated by a single space.
# logs[i] is guaranteed to have an identifier and at least one word after the identifier.

# Time: O(mnlog), Space: O(mlogn)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sortingalgo(log):
            leftside, rightside = log.split(" ", 1)

            if rightside[0].isalpha():
                return (0, rightside, leftside)
            else:
                return (1,)

        return sorted(logs, key = sortingalgo)            


# We split each log into a list with two entries so the following log:
# "dig1 8 1 5 1"
# Turns into the following:
# ["dig1", "8 1 5 1"]

# The log.split(" ", 1) means to only at most one time, from left to right, upon encountering a white-space character, split the string into two strings and store the two strings in a list.

# Then we look at the second string, or the right_side in this case of "8 1 5 1", we can see that the first character of 8, which is from right_side[0] is not an alpha character, with .isalpha() only returning true when a character is any lowercase or uppercase character from "a-z".

# For a log like "let1 art can", right_side[0].isalpha() would be applied to the letter 'a' in this case, and would return true.

# What we are returning from this function informs the sorted() function how sorted() ought to behave. The return of (0, right_side, left_side) tells sorted() to sort this entire log with a priority of 0, which is lower in value than 1, so any log with a right_side that begins with a letter will come before any log with a right_side that begins with a number.

# After ensuring that the logs with letters in the right_side come first, the letter logs are further sorted alpha-numerically by the contents of their entire right side, then if the right_sides still match, they are sorted even further based on the contents of their left_sides, alpha-numerically with the sorted() function.

# The second return statement is missing instructions on how to be sorted with only (1,) passed into it, missing the second argument. The logs with digits in their right_side only know that they must come after the letter logs, and they do not sort because they have no rule to sort by in the second argument.

# We have to write it as (1, ) because this is a tuple, I think of it as just (1), but we cannot write (1) because Python would think of it as just 1, rather than as a tuple with one element. We are specifying the sorting rules for the sort algorithm by returning tuples.

# The logs are then sorted() with the sorting logic provided by sorting_algorithm. The key in sorted() is an optional argument that allows us to attach our own custom function to override the default sorting behaviour.

# The built in sorting algorithm is used, which is TimSort in Python, most relevant sorting algorithms including this one provide a worst case run time of O(nlog(n)) and a space of O(n).


# O(nlogn * m) time complexity where n is the number of strings and m is the max length of the strings. The .split() function operates with O(m) time within each string. The sorting function operates with O(nlogn) time for the strings.

# O(mlogn) space complexity where n is the number of strings and m is the max length of the strings. The built in python sorting algorithm uses log(n) space, holding onto the split logs uses up O(m) space for each sorting step.