

# maxheap allows to find which ones are most frequent in O(log n) time, in this case it's O(log 26)=O(1) ##26 letters
# overall complexity O(n*m) for count the occurances of each task from input, and poping every value from max heap and adding to it
# m is the idle time

# done using max heap, actually making all the values negative and doing min heap
# inside maxheap, the values are occurances of tasks

# solution source : https://www.youtube.com/watch?v=s8p8ukTyA2I 

from collections import Counter, deque
import heapq


def leastInterval(tasks, n):  
    time = 0
    q = deque() #[-cnt, time]
    
    count = Counter(tasks)
    maxHeap = []
    for val, freq in count.items():
        heapq.heappush(maxHeap, -freq)
    
    while maxHeap or q:
        time +=1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            if cnt:
                q.append([cnt, time+n])
            
        if q and q[0][1]==time:
            heapq.heappush(maxHeap, q.popleft()[0])           
    return time        
 
# O(n) complexity, using dictionary, O(1) space
#need good explanation
def leastInterval(tasks, n):
    counter = Counter(tasks)
    items = list(counter.items())
    items.sort(key = lambda x: x[1], reverse = True)
    maxFeq = items[0][1] -1
    idles = maxFeq * n

    for i in range(1, len(items)):
        idles -= min(items[i][1], maxFeq)
    return max(len(tasks), len(tasks) + idles)                

tasks = ["A","A","A","B","B","B"]
n = 2

print(leastInterval(tasks, n))
#leastInterval(tasks, n)