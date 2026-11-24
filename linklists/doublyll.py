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



 
new = insertend(newhead, 50)
temp = new
print(None,end="<->")
while temp:
    print(temp.data, end="<->")
    temp = temp.next

print(None)


    
    
    
    

        

