# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # using a heap
            # can have k number of lists to merge together 
            # easy way to find the min is to use a heap
            # add all the heads to a heap and the heap will sort by the head.value
            # pop the min and connect it to the dummy node and move tail to begin attaching new nodes to the new list
            # 

        # pointers[i] would be the pointer to lists[i]
        dummy = tail = ListNode()

        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap) # create the heap, O(NlogN) where N is the number of nodes

        while heap: # O(N)
            val, i, node = heapq.heappop(heap) # O(1)

            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next)) # O(logN)

        return dummy.next
        