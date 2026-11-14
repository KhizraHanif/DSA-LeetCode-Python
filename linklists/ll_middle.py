# MIDDLE OF A LINKED LIST — REVIEW HINTS
#
# Two-pass approach:
# 1. Count all nodes.
# 2. Restart at head and move count // 2 steps.
#
# One-pass approach:
# 1. Start slow and fast at head.
# 2. Slow moves 1 step; fast moves 2.
# 3. Before moving, check that fast AND fast.next exist.
# 4. When fast cannot continue, slow is at the middle.
#
# Why it works: slow travels half as far as fast.
# Even length: this setup returns the SECOND middle.
# Move pointer variables; don't change the list's links.
#
# Trace: empty, 1 node, 2 nodes, odd length, even length.
# Both approaches: O(n) time, O(1) extra space.


class Solution(object):
    def middleNode(self, head):
        # First pass: count the nodes
        count = 0
        curr = head

        while curr is not None:
            count += 1
            curr = curr.next

        # Second pass: move halfway through the list
        curr = head

        for _ in range(count // 2):
            curr = curr.next

        return curr



# fast and slow pointer 
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (head is None or head.next is None):
            return head

        fast = head 
        slow = head
        while (fast is not None and fast.next is not None):
            
            slow = slow.next 
            fast = fast.next.next 

        
        return slow 
