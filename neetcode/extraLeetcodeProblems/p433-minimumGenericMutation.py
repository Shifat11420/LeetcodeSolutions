# A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.
# Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.
# For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
# There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.
# Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.
# Note that the starting point is assumed to be valid, so it might not be included in the bank.

# Example 1:
# Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
# Output: 1

# Example 2:
# Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
# Output: 2

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        lookup = {}
        for b in bank:
            lookup[b] = False

        q = deque([(startGene, 0)])

        while q:
            cur, level = q.popleft()
            if cur == endGene:
                return level

            for i in range(len(cur)):
                for c in ['A', 'C', 'T', 'G']:
                    if cur[i] == c:
                        continue
                    newGene = cur[:i]+c+cur[i+1:]
                    if newGene in lookup and lookup[newGene] == False:
                        q.append((newGene, level+1))
                        lookup[newGene] = True
        return -1
