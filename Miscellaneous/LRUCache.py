# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.

# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


# KEY STEP: Implement using a Hashmap and a Doubly LinkedList
# The Doubly LinkedList class has attributes key, value, prev, next
# There are 2 Linked List node markers head(0,0) and tail(0,0) that are permanent.
# We also use two helper functions
# _remove(Node) which removes a particular node from the doubly linkedlist.
# _add(Node) which adds a node behind the tail marker.
 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.hashmap = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        pr = node.prev
        ne = node.next
        pr.next = ne
        ne.prev = pr
    
    def _add(self, node):
        pr = self.tail.prev
        pr.next = node
        node.prev = pr
        node.next = self.tail
        self.tail.prev = node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        node = Node(key, value)
        self._add(node)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.hashmap[node.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)