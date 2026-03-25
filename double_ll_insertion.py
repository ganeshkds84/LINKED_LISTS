class Node:
    def __init__(self,val):
        
        self.prev=None
        self.val=val
        self.next=None
        
class Solution:
    
    def insertion(self,head,new_node):
        temp=head
        head.prev=new_node
        head=new_node
        head.next=temp
        
        current=head
        while current:
            print(current.val,end='->')
            current=current.next
        print(None)
        
if __name__=='__main__':
    
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    
    #Creating linked_lists
    node1.next=node2
    node2.next=node3
    
    node2.prev=node1
    node3.prev=node2
    
    head=node1
    
    newnode=Node(4)
    
    obj=Solution()
    obj.insertion(head,newnode)
    
    