def isPalindrome(x: int):
    length =  len(str(x))
 
    for i in range(length//2):
        if not str(x)[i] == str(x)[-(i+1)]:
            return False
    return True        
    
    
    
    
print(isPalindrome(66851215666))   