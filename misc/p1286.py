# Design the CombinationIterator class:
# CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
# next() Returns the next combination of length combinationLength in lexicographical order.
# hasNext() Returns true if and only if there exists a next combination.

# Example 1:
# Input
# ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
# [["abc", 2], [], [], [], [], [], []]
# Output
# [null, "ab", true, "ac", true, "bc", false]

# Explanation
# CombinationIterator itr = new CombinationIterator("abc", 2);
# itr.next();    // return "ab"
# itr.hasNext(); // return True
# itr.next();    // return "ac"
# itr.hasNext(); // return True
# itr.next();    // return "bc"
# itr.hasNext(); // return False

class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.combMap = defaultdict(list)
        self.combMap[self.characters] = self.comb(self.characters, self.combinationLength)

    def next(self) -> str:
        nextE = self.combMap[self.characters][0]
        self.combMap[self.characters].pop(0)
        return nextE

    def hasNext(self) -> bool:
        return True if len(self.combMap[self.characters])>0 else False
        
    def comb(self, s, length):
        res = []
        def backtrack(i,cur):
            if len(cur)==length:
                res.append(cur)
                return
            
            for j in range(i, len(s)):
                cur = cur+s[j]
                backtrack(j+1, cur)
                cur = cur[:-1]
        backtrack(0,"")
        return res    

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()