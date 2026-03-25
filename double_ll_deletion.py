from double_ll_insertion import Node

class Deletion:
    def delete_head(self,head):
        
        if head is None:
            return None
        temp=head.next
        head.next=None
        if temp is None:
            return None
        head=temp
        head.prev=None
        
        return head

if __name__=='__main__':
    node1=Node(11)
    node2=Node(22)
    node3=Node(33)
    
    #creating links
    
    node1.next=node2
    node2.next=node3
    
    node2.prev=node1
    node3.prev=node2
    head=node1
    
    obj=Deletion()
    head=obj.delete_head(head)
    
    current=head
    while current:
        print(current.val,end='->')
        current=current.next
    print(None)
    
        
    
    
    
    