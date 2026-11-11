#create a node blueprint using class in python
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


#print the nodes by terversing it using while loop
head = node1
current =head 
while current is not None:
    print(current.data , end="->")
    current = current.next

print(None)

