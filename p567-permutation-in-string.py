
from collections import Counter


def checkInclusion(s1, s2):
    # s1l = list(s1)
    # s2l = list(s2)
    # res = []
        
    # for i in range(len(s1l)):
    #     if s1l[i] in s2l:       
    #         for j in range(len(s2l)):
    #             if s1l[i] == s2l[j]:
    #                 res.append(j)                
    #     else:
    #         return False
            
    # res = sorted(res)
    # print("res : ",res) 
    # if len(res) == 1:
    #     return True
    # else:
    #     for k in range(len(s1l)-1):
    #         if res[k+1]-res[k] != 1:
    #             return False           
    #     return True
    if len(s1)>len(s2):
        return False
    window = len(s1)
    s1_c = Counter(s1)
    print(s1_c)
    
    for i in range(len(s2)-window+1):
        s2_c = Counter(s2[i:i+window])
        if s2_c == s1_c:
            return True
        
    return False
        
s1="hello"
s2="ooolleoooleh"  

print(checkInclusion(s1, s2))    
    