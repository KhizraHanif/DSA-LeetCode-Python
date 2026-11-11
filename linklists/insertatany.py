# lets ainsert new node at middle of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
#ceate new nodes using class
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)


#now link the nodes 

node1.next = node2
node2.next = node3
node3.next = node4


head = node1

# now i want to insert new node with data 25 after node2


newnode =Node(25)


current = head
while current is not None and current.data != 20:
    current = current.next

newnode.next = current.next
current.next = newnode


newnode =Node(35)


current = head
while current is not None and current.data != 30:
    current = current.next

newnode.next = current.next
current.next = newnode
#print the ll 

current= head 
while current is not None:
    print(current.data, end="->")
    current = current.next

print(None)


#Write count_nodes(head) that returns the number of nodes. An empty list should return 0.

def count_nodes(head):

    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count


countnodes = count_nodes(head)
print("length of linked list is ", countnodes)


def contains(head, target):
    # Return True if target exists.
    current = head 
    while current is not None:
        if current.data ==  target:
            return True
        current = current.next
    # Return False if you reach the end without finding it
    return False

contains_20 = contains(head, 20)
print("Does linked list contain 20? ", contains_20)
contains_50 = contains(head, 50)
print("Does linked list contain 50? ", contains_50)

#Start with head = None and insert 10 at the end. Make your code work for both empty and nonempty lists.

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

head = insert_at_end(head, 10)
print("After inserting 10 at the end:")
current = head
while current is not None:
    print(current.data, end="->")
    current = current.next

print(None)

def reverseList(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next      # save the rest of the list
        curr.next = prev     # flip the link
        prev = curr          # advance prev
        curr = nxt           # advance curr
    return prev
reversed_head = reverseList(head)
print("Reversed linked list:")
current = reversed_head
while current is not None:
    print(current.data, end="->")
    current = current.next
print(None)


