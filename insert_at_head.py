class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class Solution:
    def insert_at_head(self,head,new_node):
        new_node.next=head
        head=new_node
        current=head
    
    def print_ll(self,current):
        while current!=None:
            print(current.data,end='->')
            current=current.next
        print('None')
     
        #return
        #while current
    
if __name__=='__main__':
    #Creating nodes
    
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    
    #Giving addresses
    node1.next=node2
    node2.next=node3
    node3.data=7
    #node3
    
    head=node1
    newnode=Node(10)
    
    obj=Solution()
    obj.insert_at_head(head,newnode)
    obj.print_ll(head)
    

        