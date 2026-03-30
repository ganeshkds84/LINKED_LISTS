class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class Solution:
    def sort_ll(self,head):
        zero=Node(0)
        one=Node(1)
        two=Node(2)
        
        temp0=zero
        temp1=one
        temp2=two
        
        current=head
        while current:
            if current.val==0:
                temp0.next=current
                temp0=temp0.next
            elif current.val==1:
                temp1.next=current
                temp1=temp1.next
            else:
                temp2.next=current
                temp2=temp2.next
            current=current.next 
            
        temp0.next=None
        temp1.next=None
        temp2.next=None
        temp0.next=one.next if one.next else two.next
        temp1.next=two.next
        return zero.next
        
    
if __name__=='__main__':
    node1=Node(1)
    node2=Node(2)
    node3=Node(0)
    node4=Node(1)
    node5=Node(0)
    
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    head=node1
    obj=Solution()
    head=obj.sort_ll(head)
    
    current=head
    while current:
        print(current.val,end='->')
        current=current.next 
    print(None)
    
    