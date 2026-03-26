class Node:
    def __init__(self,data):
        
        self.val=data
        self.next=None

class Solution:
    def middle_elem(self,head):
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        
        current=head
        n=(count//2)+1
        while n>1:
            current=current.next 
            n-=1
        return current
        
    
if __name__=='__main__':
    node1=Node(10)
    node2=Node(15)
    node3=Node(20)
    node4=Node(25)
    node5=Node(30)
    node6=Node(35)
    node7=Node(40)
    
    #creating links
    
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=node6
    node6.next=node7
    
    head=node1
    
    obj=Solution()
    head=obj.middle_elem(head)
    
    current=head
    
    while current:
        print(current.val,end='->')
        current=current.next
    print(None)
    
    