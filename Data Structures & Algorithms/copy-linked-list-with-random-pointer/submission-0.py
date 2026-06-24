"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # using a hash map to link all the new copies (values) with the old nodes (keys)

        # initalize hashma, edge case: what if points to null? Initalize in hash map first
        oldToCopy = { None : None }

        # first pass, create all the nodes and fill up the hash map
        cur = head
        while cur:
            oldToCopy[cur] = Node(cur.val)
            cur = cur.next

        # second pass, link all copy nodes by using hashmap
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]