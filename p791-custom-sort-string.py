# https://leetcode.com/problems/custom-sort-string/

# You are given two strings order and s. All the words of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

import collections


order = "cbafg"
s = "xyfzg"

### using list
def customSortString(order, s):
        o = list(order)
        s = list(s)
        res = []
        rest = []
        
        for i in range(len(o)):
            if o[i] in s:
                count= s.count(o[i])
                for j in range(count):
                    res.append(o[i])
                    
        for k in range(len(s)):
            if s[k] not in o:
                rest.append(s[k])
        
        final = res+rest
        return "".join(final)
    
print(customSortString(order, s))  


### using hashmap  
def customSortStringH(order, s):
    order_map = collections.defaultdict(lambda: -1)

    for i, c in enumerate(order):
        order_map[c] = i

    sorting = sorted(s, key=lambda x: order_map[x])
    return "".join(sorting)

print(customSortStringH(order, s))  
    