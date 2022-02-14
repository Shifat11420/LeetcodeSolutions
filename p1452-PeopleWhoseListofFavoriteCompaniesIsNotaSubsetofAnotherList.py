# https://leetcode.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list/
# Given the array favoriteCompanies where favoriteCompanies[i] is the list of favorites companies for the ith person (indexed from 0).

# Return the indices of people whose list of favorite companies is not a subset of any other list of favorites companies. You must return the indices in increasing order.

def peopleIndexes(favoriteCompanies):
    new, d, cnt = [], {}, 1
    for i in favoriteCompanies:
        for j in i:
            if j not in d:
                d[j] = cnt
                cnt += 1
            print("j : ",j,"d[j] : ", d[j])
    
        new += set([d[j] for j in i]),
        print("new now: ", new)

    res = []
    for i in range(len(new)):
        print([new[i] <= j for j in new])   #set of boolians
        if sum([new[i] <= j for j in new]) == 1:   # <= is subset of, sum() summation of set elements
            res += i,
            print(res)

    

    return res             
    


favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
print(peopleIndexes(favoriteCompanies))