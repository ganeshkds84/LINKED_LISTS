class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Solution:
    def removeMiddle(self,head):
        if head is None:
            return None
        slow=head
        fast=head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next 
            fast=fast.next.next
        if prev is None:
            return head.next 
        prev.next=slow.next
        slow.next=None
        
        return head
    
if __name__=='__main__':
    x=Node(1)
    y=Node(2)
    z=Node(3)
    u=Node(4)
    w=Node(5)
    
    #creating_links
    x.next=y
    y.next=z
    z.next=u
    u.next=w
    head=x
    obj=Solution()
    head=obj.removeMiddle(head)
    current=head
    while current:
        print(current.data,end='->')
        current=current.next
    print(None)
    