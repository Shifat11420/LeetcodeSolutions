# https://leetcode.com/problems/verifying-an-alien-dictionary/

# In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

# Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

#using hashmap
def isAlienSorted(words, order):
    mapping = {}
    for i in range(len(order)):
        mapping[order[i]] = i
    
    for i in range(len(words)-1):
        for j in range(len(words[i])):
            if len(words[i])>j and len(words[i+1])>j:
                if mapping[words[i][j]] == mapping[words[i+1][j]]:
                    continue
                elif mapping[words[i][j]] < mapping[words[i+1][j]]:
                    break
                else:
                    return False
            elif len(words[i])> len(words[i+1]):
                return False
            
    return True

words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))