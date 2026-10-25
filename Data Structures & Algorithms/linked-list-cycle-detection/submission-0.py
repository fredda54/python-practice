# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        seen = set()
        seen.add(curr)
        while curr:
            curr = curr.next
            if curr in seen:
                return True
            else:
                seen.add(curr)
        return False