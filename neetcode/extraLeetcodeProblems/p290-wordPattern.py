# Time: O(n), where n is the length of the pattern or the number of words in the string, whichever is smaller.
# Space : O(m), where mmm is the number of unique characters in the pattern or the number of unique words in the string, whichever is smaller.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split(" ")
        if len(pattern) != len(slist):
            return False

        hashmap = {}
        for i in range(len(slist)):
            if pattern[i] in hashmap:
                if hashmap[pattern[i]] != slist[i]:
                    return False
            elif slist[i] in hashmap.values():
                return False
            else:
                hashmap[pattern[i]] = slist[i]
            print("hashmap = ", hashmap)
        return True
