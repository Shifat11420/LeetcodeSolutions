# Given two integer arrays pushed and popped each with distinct values, return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.

# Example 1:
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4),
# pop() -> 4,
# push(5),
# pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

# Example 2:
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.

class Solution:
    # Time:  O(n), Space : O(n)
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #     s = []
    #     i, j = 0, 0 
    #     n, m  = len(pushed), len(popped)

    #     while True:
    #         if i==n or j==m:
    #             break

    #         if s!=[] and s[-1]==popped[j]:
    #             s.pop()
    #             j += 1
    #         else:
    #             s.append(pushed[i])
    #             i += 1

    #     while j<m:
    #         if s[-1]==popped[j]:
    #             s.pop()
    #             j += 1
    #         else:
    #             return False
    #     return True if s==[] else False   
#------------------------------------------
    # Time:  O(n), Space : O(1)
    # def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    #     i, j = 0, 0 
    #     n, m  = len(pushed), len(popped)

    #     while i<len(pushed):
    #         if i>-1 and pushed[i]==popped[j]:
    #             pushed.pop(i)
    #             i -= 1
    #             j += 1
    #         else:    
    #             i += 1

    #     i = len(pushed)-1
    #     while j<m:
    #         if pushed[i]!=popped[j]:
    #             return False          
    #         i -= 1
    #         j += 1
    #     return True          
#------------------------------------------
    # Time:  O(n), Space : O(1)
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        for num in pushed:
            pushed[i] = num
            while i>-1 and popped[j]==pushed[i]:
                i -= 1
                j += 1
            i += 1
        return i == 0  