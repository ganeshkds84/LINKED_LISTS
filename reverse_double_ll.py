class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
        
class Solution:
    
    def reverse_ll(self,head):
        if head is None:
            return None
        if head.next is None :
            return head
        current=head
        new_head=None
        while current:
            current.prev,current.next=current.next,current.prev
            new_head=current
            current=current.prev
            
        return new_head
            
        

if __name__=='__main__':
    node1=Node(10)
    node2=Node(20)
    node3=Node(30)
    
    #Creating links
    node1.next=node2
    node2.next=node3
    
    node2.prev=node1
    node3.prev=node2
    head=node1
    
    obj=Solution()
    head=obj.reverse_ll(head)
    
    current=head
    
    while current:
        print(current.data,end='<->')
        current=current.next
        
    print(None)
    