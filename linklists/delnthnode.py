# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0 
        curr = head
        while curr:
            count = count +1
            curr = curr.next 
        

        sz = count 

        if (count == n):
            nhead = head.next
            return nhead

        #second pass two delete the node at nth position 
        i = 0
        nthpos = sz - n
        prev = None
        cur = head
        if head.next is None:
            return None

        while cur:
            
            if (i == nthpos):
                prev.next = cur.next

            prev = cur
            cur = cur.next
            i += 1
            
        return  head



    # we can further improve it using two pointers in one pass


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:



        fast = head 
        for nodes in range(n):
            fast = fast.next

        if fast == None:
            return head.next 

        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next 

        
        slow.next = slow.next.next

        return head