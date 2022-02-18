# https://leetcode.com/problems/add-strings/

def addString(num1,num2):
    num1 = list(num1)
    num2 = list(num2)
    car = 0
    res = ""
    
    while num1 or num2 or car:
        if num1:
            car += int(num1.pop())  
        if num2:
            car += int(num2.pop())  
        res += str(car%10)
        car = car//10
    return res[::-1]        
            
num1 = "456"
num2 = "77"                    
print(addString(num1,num2))    