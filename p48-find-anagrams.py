import collections

s = "cbaebabacd"
p = "abc"

def findAnagrams(s: str, p: str): 
    # take counter of first n elements in s_dict with n = len(p) - 1
    s_dict = collections.Counter(s[:len(p)-1]) 
    print("s_dict : ",s_dict)
    # counter of p, this should not be changed
    p_dict = collections.Counter(p)
    print("p_dict : ", p_dict)
    start = 0
    # final result list
    res = []
    # We iterate over the string s, and in each step we check if s_dict and p_dict match
    for i in range(len(p)-1, len(s)):
        print("before update, ",s_dict[s[i]])
        # updating the counter & adding the character
        s_dict[s[i]] += 1
        print("i = ",i, "s[i] = ", s[i], "s_dict[s[i]] = ", s_dict[s[i]] )
        print("after update s_dict, ",s_dict)
        # checking if counters match
        if s_dict == p_dict:
            res.append(start)
        # remove the first element from counter
        s_dict[s[start]] -= 1
        print("after removing first element s_dict, ",s_dict)
        #if element count = 0, pop it from the counter
        if s_dict[s[start]] == 0:
            del s_dict[s[start]]
        start += 1
        
    return res
        


print(findAnagrams(s,p))        
