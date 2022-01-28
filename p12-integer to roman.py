
def intToRoman(num):
    
    roman=''
    while num >= 1000:
        num = num -1000
        roman += 'M'
    if num >= 900:
        num = num -900
        roman += 'CM'
    while num >= 500:
        num = num - 500
        roman += 'D'
    if num >= 400:
        num = num -400
        roman += 'CD'
    while num >=100:
        num = num -100
        roman += 'C'
    if num >= 90:
        num = num -90
        roman += 'XC'
    while num >= 50:
        num = num - 50
        roman += 'L'
    if num >= 40:
        num = num -40
        roman += 'XL'
    while num >= 10:
        num = num - 10
        roman += 'X'
    if num >= 9:
        num = num -9
        roman += 'IX'
    while num >= 5:
        num = num -5
        roman += 'V'
    if num >= 4:
        num = num -4
        roman += 'IV'
    while num >= 1:
        num = num -1
        roman += 'I'    
    
    print("Roman is : ", roman)    
        

intToRoman(1994)        


# another answer
def intToRoman1(num):
    dic = {
                1:'I',
                4:'IV',
                5:'V',
                9:'IX',
                10:'X',
                40:'XL',
                50:'L',
                90:'XC',
                100:'C',
                400:'CD',
                500:'D',
                900:'CM',
                1000:'M'}
            
            
    numbers = list(dic.keys())[::-1]
    print(numbers)

    ans = []
    for nd in numbers:
        div1, mod1 = divmod(num, nd)
        if div1 > 0:
            ans.append(div1*dic[nd])
        num = mod1
    
    #return ''.join(ans)

    print(''.join(ans))


intToRoman1(1994)  
