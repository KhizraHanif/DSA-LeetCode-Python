class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


# create new nodes

node1 = Node(10)
head = node1
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# now connect the nodes 

node1.prev = None 
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2
node3.next = node4
node4.prev = node3
node4.next = None

temp = head
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next

print(None)


#print backward

temp = node4
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.prev

print(None)


#insert new head 

newhead = Node(5)
newhead.prev = None
newhead.next = node1
node1.prev = newhead

temp = newhead
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next

print(None)
temp = node4
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.prev

print(None)

# insert nee node at the end

def insertend(newhead, data):
    temp = newhead
    newtail = Node(data)

    if newhead is None:
        return newtail 

    while temp.next:
        temp = temp.next
        
    temp.next = newtail
    newtail.next = None 
    newtail.prev = temp 

        
            
    return newhead

newhead = insertend(newhead, 50)
temp = newhead
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next

print(None)

# insert in a specific location lets add after 2nd index node  consider ll 0 index ll
def insertatps(newhead,data,ps):
    count = 0 

    temp = newhead
    node = Node(data)
    while temp:
        if count == ps:
            node.next = temp.next
            temp.next.prev = node
            temp.next = node   
            node.prev = temp
        temp = temp.next
        count = count + 1
    return newhead



insertatps(newhead,25,2)
temp = newhead
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next

print(None)

# also for loop can be use to reach that position 
def insertAtPos(head, p, x):
    newnode = Node(x)
    cur = head

    # traverse to the given position
    for _ in range(p):
        cur = cur.next

    if cur.next is None:
        cur.next = newnode
        newnode.prev = cur
    else:
        newnode.next = cur.next
        cur.next = newnode
        newnode.next.prev = newnode
        newnode.prev = cur
    return head

insertAtPos(newhead, 3, 28)

            
temp = newhead
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next
print(None)



# remove head 
def removehead(newhead):
    Newhead = newhead.next 

    Newhead.prev = None 

    return Newhead

Newhead = removehead(newhead)
temp =  Newhead
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next
print(None)


# Python Program to delete a node from the end of Doubly Linked List
def delfromend(head):

    curr = head
     # Corner cases
    if head is None:
        return None
    if head.next is None:
        return None

    while curr.next:

        curr = curr.next


    curr.prev.next = None 

    return head


Newhead = delfromend(Newhead)
temp =  Newhead
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next
print(None)



# reverse a dubly link list 

head = Newhead
while head:
    temp = head.next
    head.next = head.prev 
    head.prev = temp
    if temp is None:
        Newhead = head  # Original last node becomes the new head

    head = head.prev




temp =  Newhead
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next
print(None)
