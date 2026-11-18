"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        
        hashmap = {}
        temp = head
        
        hashmap[None] = (None)
        #first pass creating deep copy of node and storing them in hash map 
        while temp:
  
            #create copy nodes and store them as value correspond to key which is node of orignal list
            copynode = Node(temp.val)
            hashmap[temp] = (copynode)
            

            temp = temp.next 

        #now link the copied nodes together

        temp = head
        while temp:
            copynode = hashmap[temp]
            copynode.next = hashmap[temp.next]
            
                
            copynode.random = hashmap[temp.random]

            temp = temp.next

        
        return hashmap[head]



#optimize solution:

#insert copy node after orignial within same l list . 
#then connect random pointers 
# extract copied nodes into new linklist using dummy node (restore orignal link list connections)
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None 
        
        temp = head 
        while temp:
            
                
            copynode = Node(temp.val)
            copynode.next = temp.next 
            temp.next = copynode
            

            temp = temp.next.next 

        temp = head
        while temp:
            if temp.random is None:
                temp.next.random = None
            else:
                temp.next.random = temp.random.next
            


            temp = temp.next.next 

        dummynode = Node(-1)
        res = dummynode
        temp = head
        while temp:
            res.next = temp.next 
            temp.next = temp.next.next
            res = res.next
            temp = temp.next

        
        return dummynode.next





        







        





        
        
        




        





        
        