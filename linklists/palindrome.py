# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:

        if head is None or head.next is None:
            return True
       
       #function to reverse the link list with we will call after finding the middle using slow and fast pointer 

        def reverse(head):
            
            prev = None 
            curr = head 
            while curr:
                temp = curr.next 
                curr.next = prev 
                prev = curr
                curr = temp 
            return prev

        def isidentical (h1,h2):

            while h1 and h2:
                if h1.val != h2.val:
                    return False
                
                h1 = h1.next
                h2 = h2.next
            
            return True
        
        
        slow = head 
        fast = head

        while fast.next and fast.next.next:

            slow = slow.next 
            fast = fast.next.next 
            
        
        
       
        head2 = reverse(slow.next)
        
        slow.next = None 

        
        return isidentical(head,head2)




        


        


            

        