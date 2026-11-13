class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#create nodes

node1 = Node(1)
node2 = Node(2)
node3 = Node(3) 
node4 = Node(4) 

head = node1
#connect nodes
node1.next = node2
node2.next = node3
node3.next = node4

current = head
while  current is not None:
    print(current.data, end="->")
    current = current.next
print(None)

# reverse the ll with brute force method using stack which takes extra memory of O(n)
def reverse_linked_list(head):
    temp = head
    stack = [
    ]


    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next


    current = head
    
    while  current is not None:
        print(current.data, end="->")
        current = current.next
    print(None)

reverse_linked_list(head)


# but above is not optimal solution as it uses extra space of stack, so we can do it in o(1) space complexity

#iterative method 
# we will use two pointer technique to reverse the link list inplace with O(n)


def reverse_linked_list_iterative(head):
    prev = None 
    current = head
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

reversed_head = reverse_linked_list_iterative(head)
current = reversed_head
while current:
    print(current.data, end="->")
    current = current.next
print(None)




#revursive method   # there can be two  cases ethier ll is empty means head is null or just  one elment    
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if (head is None or head.next is None):
            return head
        
        newhead = self.reverseList(head.next)
        head.next.next = head 
        head.next = None
        return newhead











       



