# Given a string s containing an out-of-order English representation of digits 0-9, return the digits in ascending order.

# Example 1:
# Input: s = "owoztneoer"
# Output: "012"

# Example 2:
# Input: s = "fviefuro"
# Output: "45"
 
from collections import Counter, OrderedDict


class Solution:
    def originalDigits(self, s: str) -> str:
      countS = Counter(s)
      check = OrderedDict()
      check["z"] = ["0","zero"]
      check["w"] = ["2","two"]
      check["u"] = ["4","four"]
      check["x"] = ["6","six"]
      check["g"] = ["8","eight"]
      check["o"] = ["1","one"]
      check["t"] = ["3","three"]
      check["f"] = ["5","five"]
      check["s"] = ["7","seven"]
      check["i"] = ["9","nine"]

      output = []
      while sum(countS.values()) != 0:
        for key in check.keys():
          if key in countS and countS[key] != 0:
            val = countS[key]
            for c in check[key][1]:
              countS[c] -= val
            output.extend([check[key][0] for i in range(val)])
          else:
            continue
      output.sort()
      return "".join(output)      