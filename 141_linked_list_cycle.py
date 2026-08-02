# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        nodemap = {}
        i = 0
        curr = head

        while curr:

            if curr in nodemap:
                return True

            nodemap[curr] = i
            i+=1
            curr = curr.next
        
        return False