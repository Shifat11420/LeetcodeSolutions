# # https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

# You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

# Return a list of groups such that each person i is in a group of size groupSizes[i].

# Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

def groupThePeople(groupSizes):
    listofgroups = []
    group = []
    count = 0
    chunklist = []
    for i in range(len(groupSizes)):
        for j in range(len(groupSizes)):        
            if i+1 == groupSizes[j]:
                count +=1
                group.append(j)
        if count == i+1:        
            listofgroups.append(group)
        elif count > i+1:
            chunklist = list(chunks(group,i+1))
            listofgroups=listofgroups+chunklist   
        group = [] 
        count = 0   
    return listofgroups        
            
groupSizes = [3,3,3,3,3,1,3]      
print(groupThePeople(groupSizes))      