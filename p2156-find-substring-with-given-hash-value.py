
# import collections

# from string import ascii_lowercase

# LETTERS = {letter:str(index)  for index, letter in enumerate(ascii_lowercase, start = 1)}

# def alphabetic_position(text):
#     text = text.lower()
#     for character in text:
#         if character in LETTERS:
#             return LETTERS[character]


# def hash(s, p, k, m):
#     hashV = 0
#     s = list(s)
#     for i in range(k):
#         hashV += int(alphabetic_position(s[i][0])) *(p**i)

#     return hashV % m 
 

# def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
#     sub_dict = collections.Counter(s[:k-1])
#     start = 0

    
#     for i in range(k-1,len(s)):    
#         sub_dict[s[i]] += 1
#         print(sub_dict)

#         substr = s[start:i+1]
#         print("substr = ", substr)    

#         print("hash = ",hash(substr, power, k, modulo))
#         print("hashvalue = ", hashValue)
#         if hash(substr, power, k, modulo) == hashValue:
#             print("return substr", substr) 
#             return substr

#         sub_dict[s[start]] -= 1  

#         if sub_dict[s[start]] == 0:
#             del sub_dict[s[start]]
#         start += 1    
#         print(sub_dict)  


 

# # s = "fbxzaad"
# # s = "xmmhdakfursinye"
# s = "kfedcbdngvlykqyrbvwbnaassgjifjxtawlafhcpjtpzfnbsqfasohevbbhkwmtnmixolfepkjmcbadqcljmsbonrngsgfqwzqiisbiwiqgtqtqddukgtjymbxzmtxrobuhkdxmdmqccrauzkrjisstznnkhupiandekzcchsrzwintkkzhvqomqmnbasynmvtxwydcvwoukqmgrpmgzqancuzapgncasxnbyznlrdvcbomdptjftgxdzeqzyavfdpseoxpvohpxtikyjfvskxyqbubgnseraxtrcrwjxloxymhqgaxwbbvzhjsbncqrlpdbiuakdjzjrbclhxgnjjyfrqyjchlsdrcwtdoktviqwjctlmzqemumgmjufcbixkfhzkugsvnkrrakccguybwhmuexiemqusltaaqrswsezccqzaputgaabrjdeihmkpzbojnusmhkwjdxvgiexwdkkazhhmlalgzvxgqgncfytrxuhkwhwcxhmlbvkhjcnyztepwnlpthozdqexvhxpvheopjrsjzkqrstczffkhkikelwydcbnghfiibeyabgegdgaqvasujmggltkvokmnsmontjzsmzoeeqenafvurbnbwqbizvaqxfgnoxasctfrwvqmoufvpajdkethlvbhbehxahcpcizocbchwfznhuqtblwepeqdhycrovqosmxxeeqaffjvvclmpcqdugndexexcykyusetuamymszlteobxkestwbzubpstbwrstuovlybycevedzgurqvlgkouvavcukccgixixsrndurvrkfegegnchbhockujlafxexlxhgysraviztkjymiqxrlldcixvfnzrpserrqycbfmesqbltywmandcqtluccbisfqzosbvedqhsxepdjevaasylvjmfpvyxqvclaalgxytiukyarojmzyovmiunkvqhkouhxxhbemavagrhteofpowvlpdunjjpwgcjibagfswrzwkgrwklppchvtukzncvoqorlsskyghkhrazwvyqqjfygmduhsfkrseddgmtdvlqeruxogmyttdqmdpmscspatkoifauivwjtbwisiiqztrllfqnjvbagrfylrpjudjmvwhdkhahyxlsfbkuuyofryfgblllzeacfiqqawridcbtqnroxwuqhyspqmwhxmjztqokofnkfvupcykszthicdgjbrgafpztktrcwtayoulnjaazigkinnpttghhyboiczvtswenshlmqyelnwhzqlswblqssiiynypfcxerlykpiyimkoodimdfdlzbwmlwflylcqwaflivqeonjswvowxgeoafmppodmfbvooodtnzgmhfnchenaaywqevklrpgajbmbxgiopofghlouhjfarjxlclcullsgyzhohowtragbkaebrvbkmxfxughlirtikheojbrrgxtqldfdnqxndzvfgajiltnqnuwavxbrvuiycsizunlglwnivpseyfwmgydmmpzhxkdtpuzpddacjmjhvncdoicedkimdgaqobdfagpggvjemstqbsshynyvhdyslgldvkapqgusmnuroqxcivjifkhrotomxodficktxmcytkbqitrlalpbtphowfgtzgfacabjodvivgykorvmxhzpqvskolkbfpbdgowlighossrlwiomgohfhgklmlnekniqfjmvvqvmimkeddfxnxwzzroospxvndynetghkgrakuslukqsrdtmjkblwrmwhzzojcwwogrjvnftdwwpoqcjqimvjbwgqgpeffjnwlzdyhkhwmvpwpcmjmdqneexqwcrvdxsfsnidwyflwxwngczklprhoazeeqwclrqvnicfvrtbqailbwrqxadxslouwdjycidupemdwhpkqekaxxprtdtmjficrhlvqidvgwkllaowyyajkxugqiztbpzvjqtpuyugkvdfcaczzruskvucsxtvroljnjojuzncatgnypbzwvilbajqqnjovqxcfunwwbxgshrjlajwveaswqegidfnedpxqdreddvawrpbllkcshlafnxyocbmwacytvgtoonlkukqhxwbfxcfnbgmrfcnkvtxmygiyjoyoljd"
# power = 71717
# modulo = 94536
# k = 1149
# hashValue = 39999

# subStrHash(s, power, modulo, k, hashValue)

## time limit exceeded with thin example, logically fine I guess, following is a solution from Leetcode


# https://youtu.be/bmX2_mal8YQ 
s = "fbxzaad"
power = 31
modulo = 100
k = 3
hashValue = 32

def subStrHash(s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
    alf = 'abcdefghijklmnopqrstuvwxyz'
    alf_dct = {alf[i]: i+1 for i in range(len(alf))}

    curr = 0   #prev calculated hash, starts with 0 because of reverse string calculation, starts at end
    p = 1

    for i in range(k-1):
        p = (p * power) % modulo
        print("p = ",p)

    for i in reversed(range(len(s)-k, len(s))):
        print("curr: ",curr, " * power ", power, " + alf_dct[s[i]] ", alf_dct[s[i]], ") % modulo ", modulo, "here s[i] is ", s[i])
        curr = (curr * power + alf_dct[s[i]]) % modulo
        print("curr = ", curr)
        if curr == hashValue:
            result = i
            print("this")
            
    for i in reversed(range(len(s)-k)):
        print("later thing:   curr ",curr," - ( alf_dct[s[i + k]] ", alf_dct[s[i + k]]," * p ", p,") %  modulo, ",modulo, ") * power ",power, "+ alf_dct[s[i]] ",alf_dct[s[i]], " ) % modulo ", modulo, " here s[i] is ", s[i], "here s[i+k] is ", s[i+k])
        curr = ((curr - (alf_dct[s[i + k]] * p) % modulo) * power + alf_dct[s[i]]) % modulo
        print("curr later= ", curr)
        if curr == hashValue:
            result = i
            print("that")
    print("s[",result,":", result+k,"]")        
    return s[result:(result+k)]

print(subStrHash(s, power, modulo, k, hashValue))    