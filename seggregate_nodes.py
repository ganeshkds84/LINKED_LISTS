class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Solution:
    def seggregateNodes(self,head):
        if head is None :
            return None
        odd=head
        even=head.next 
        temp=head.next 
        while even and even.next:
            odd.next=even.next 
            odd=even.next 
            even.next=odd.next 
            even=odd.next 
        odd.next=temp        
        return head

if __name__=='__main__':
    node1=Node(1)
    node2=Node(2)
    x=Node(3)
    y=Node(4)
    z=Node(5)
    
    #Link_nodes
    node1.next=node2
    node2.next=x
    x.next=y
    y.next=z
    
    head=node1
    
    obj=Solution()
    head=obj.seggregateNodes(head)
    
    current=head
    while current:
        print(current.data,end='->')
        current=current.next 
        
    print(None)
    
    
    
        