# An integer has sequential digits if and only if each digit in the number is one more than the previous digit.
# Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

# Example 1:
# Input: low = 100, high = 300
# Output: [123,234]

# Example 2:
# Input: low = 1000, high = 13000
# Output: [1234,2345,3456,4567,5678,6789,12345]
 
# Time: O(1), Space: O(1)  # fixed length 10 ~ O(1)
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        c = "123456789"
        res = []
        for i in range(len(c)):
            for j in range(i+1, len(c)+1):
                num = int(c[i:j])
                if low<=num<=high:
                    res.append(num)
        res.sort()            
        return res

