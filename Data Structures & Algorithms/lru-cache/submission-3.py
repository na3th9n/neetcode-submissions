class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}
        
    def _remove(self, node):
        # update the doubly-linked list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def _insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self._remove(node)
            self._insert(node)

            return self.cache[key].val

        return -1
        
    def put(self, key: int, value: int) -> None:
        # insert the new node
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        
        node = Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.capacity:
            to_be_deleted = self.head.next
            del self.cache[to_be_deleted.key]
            self._remove(to_be_deleted)





        
