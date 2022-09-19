# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

# Example 2:
# Input: digits = ""
# Output: []

# Example 3:
# Input: digits = "2"
# Output: ["a","b","c"]

# idea: loop inside backtrack
# number of outputs we can have is 4^n, n = length of the input string, 4^n because 4.4.4.4... for each of the place we can have 3 or 4 choices
# length of each output string is length of the input string = n
# Complexity: time = O(n *4^n)

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitTochar = { "2": "abc",
                        "3": "def",
                        "4": "ghi",
                        "5": "jkl",
                        "6": "mno",
                        "7": "pqrs",
                        "8": "tuv",
                        "9": "wxyz"
                        }
        
        # writting inside the function so we need to pass in this parameters everytime we call the function 
        def backtrack(i, curStr):    # i = index of digit we are currently at, curStr = current string  
            # base case 
            if len(curStr) == len(digits):      # all the string would be the size of input
                res.append(curStr)
                return
            
            for c in digitTochar[digits[i]]:       #for "23", c starts with "a","b","c" 
                backtrack(i+1, curStr+c)           # i+1 next level, level 1: "a",.... , level 2: "ad", "ae", "af"
                
        if digits:
            backtrack(0, "")     #since we return [] for empty input
        return res    