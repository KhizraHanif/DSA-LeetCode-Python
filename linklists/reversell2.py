# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:
        dummynode = ListNode(-1)
        dummynode.next = head

        curr = head 
        prevleft = dummynode
        for _ in range(left-1):
            prevleft = curr
            curr = curr.next
        
        prev = None 
        
        for _ in range(right-left+1):
            Next = curr.next 
            curr.next = prev 
            prev = curr 
            curr = Next
        
        temp = prevleft.next 
        prevleft.next = prev
        temp.next = curr 
        return dummynode.next

        





        


        





