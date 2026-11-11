class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#create nodes

node1 = Node(1)
node2 = Node(2)
node3 = Node(3) 


Head = node1
#connect nodes
node1.next = node2
node2.next = node3


head = node1
# i want to add new node with data 4 at the end
newnode = Node(4)
current = head
while  current.next is not None:
    current = current.next
current.next = newnode


#print the nodess
current = head
while  current is not None:
    print(current.data, end="->")
    current = current.next
print(None)

