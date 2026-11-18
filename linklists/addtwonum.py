# Add one column at a time, starting with the ones digit.
# Keep going while either list has a digit or a carry remains.
#
# 1. READ: Take one digit from each list. Use 0 if a list has ended.
# 2. ADD: Save both digits plus the incoming carry in total.
# 3. WRITE: Append total % 10. Save total // 10 as the next carry.
# 4. MOVE: Move curr to the new node. Advance each input pointer if it exists.
#
# Return dummy.next, the first digit of the result.





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy
        carry = 0 

        while l1 or l2 or carry :

            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            total = digit1 +digit2+ carry
            addval = total%10
            carry = total//10
            curr.next = ListNode(addval)
            curr = curr.next 

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
           

        return dummy.next




             
            
            










                














                