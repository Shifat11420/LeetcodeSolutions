
def validPalindrome(s):
    l = 0 
    r = len(s)-1

    while l < r:
        if s[l]==s[r]:
            l += 1
            r -= 1
        else: 
            return check_palindrome_with_skip(s,l) or check_palindrome_with_skip(s,r)                      
        return True
    
    
    def check_palindrome_with_skip(s,int2skip):
        l =0
        r =len(s)-1
   
        while l<r:
            if int2skip ==l:
                l += 1
            if int2skip ==r:
                r-= 1  
            if s[l] != s[r]:
                return False    
            else:
                l +=1
                r -= 1
                
        return True              
     
     
     
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(validPalindrome(s))
