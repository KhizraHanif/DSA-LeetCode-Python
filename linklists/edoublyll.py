class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


# create nodes with data

node1 = Node(1)
node2 = Node(2)
node3 =  Node(3)

# connect nodes


node1.next = node2 
head = node1
node1.prev = None 

node2.next = node3
node2.prev = node1 

node3.next = None
node3.prev = node2



#print linklist 
temp = head

while temp:

    print(temp.data, end="->")

    temp = temp.next
print(None)


#print linklist backward 
temp = node3

while temp:

    print(temp.data, end="->")

    temp = temp.prev
print(None)








