# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
# If the fractional part is repeating, enclose the repeating part in parentheses.
# If multiple answers are possible, return any of them.
# It is guaranteed that the length of the answer string is less than 104 for all the given inputs.

# Example 1:
# Input: numerator = 1, denominator = 2
# Output: "0.5"

# Example 2:
# Input: numerator = 2, denominator = 1
# Output: "2"

# Example 3:
# Input: numerator = 4, denominator = 333
# Output: "0.(012)"

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        n = numerator
        d = denominator

        sol = ""

        if n == 0:
            return "0"
        if (n > 0 and d < 0) or (n < 0 and d > 0):
            sign = "-"
        else:
            sign = ""
        n, d = abs(n), abs(d)

        sol = str(n//d)
        dec = ""

        if n % d:
            sol += "."
            nums = {}
            n = n % d

            while n:
                if n in nums:
                    dec += ")"
                    pos = nums[n]
                    dec = dec[:pos]+"("+dec[pos:]
                    break

                nums[n] = len(dec)

                n = n * 10
                dec += str(n//d)
                n = n % d
        return sign+sol+dec
