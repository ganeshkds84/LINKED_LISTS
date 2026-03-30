class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
        
class Solution:
    def sortList(self,head):
        if head is None or head.next is None:
            return head
        mid=self.findMid(head)
        left=head
        right=mid.next 
        mid.next=None
        
        left_sorted=self.sortList(left)
        right_sorted=self.sortList(right)
        
        return self.merge(left_sorted,right_sorted)
        
    def findMid(self,head):
        slow=head
        fast=head.next 
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 
        return slow
    
    def merge(self,lefty,righty):
        dummy=Node(0)
        tail=dummy
        
        left=lefty
        right=righty
        while left and right:
            if left.val<=right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next
        if left:
            tail.next=left
        if right:
            tail.next=right
                        
        return dummy.next
    
if __name__=='__main__':
    node1=Node(5)
    node2=Node(6)
    node3=Node(1)
    node4=Node(4)
    node5=Node(1)
    
    #creating_links
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    
    head=node1
    obj=Solution()
    
    head=obj.sortList(head)
    
    current=head
    while current:
        print(current.val,end='->')
        current=current.next 
    print(None)