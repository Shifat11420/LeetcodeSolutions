#https://leetcode.com/problems/lru-cache/
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

# Implement the LRUCache class:

# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.




class Node:
    def __init__(self, key, val):
        self.key , self.val = key, val
        self.prev, self.next = None      #pointers for previous node and next node


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}    #hashmap, map key to node
        
        # left = LRU, right = most recent
        self.left, self.right = Node(0,0), Node(0,0)   #dummy pointers for least recently used(LRU), and most recently used 
        self.left.next, self.right.prev = self.right, self.left  #link the nodes, put a new node in the middle

    # remove node from list (linked list), helper function
    def remove(self, node):  
        prev, nxt = node.prev, node.nxt
        prev.next, nxt.prev = nxt, prev          # removing from the middle of the linked list

    # insert node at right of the node in the linked list, helper function
    def insert(self, node):        
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            #TODO: update the most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1    
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)   #include in the hashmap and pointer to node    
        self.insert(self.cache[key])         # include in the right of the double linked list

        if len(self.cache)> self.cap:
            # remove from list and delete the LRU from the hash map
            lru = self.left.next     #least recently used from the linked list
            self.remove(lru)             # remove from list
            del self.cache[lru.key]      # remove from cache
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)