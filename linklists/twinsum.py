# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: ListNode | None) -> int:
       # i am finding middle of the list so i can break it into half as we have even link list so my second half list will start from slow.
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next 
            fast = fast.next.next 


        secondh = prev.next 
        prev.next = None

# now i am reversing the second half of list so later on i can add two lists together 


        curr = secondh 
        prev = None
        while curr:
            temp= curr.next
            curr.next = prev

            prev = curr 
            curr = temp 

        
        
        head2 = prev

        t1 = head
        t2 = head2

        max = 0
        twinsum = 0
        while (t1 and t2):
            twinsum = t1.val + t2.val

            if (twinsum > max):
                max = twinsum

            t1 = t1.next
            t2 = t2.next
        
        return max

            



        










            









