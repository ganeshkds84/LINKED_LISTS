class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class Solution:
    def findLoop(self,head):
        if head is None:
            return False
        
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 
            if slow==fast:
                return True
        return False    
    
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
    #node7.next=node3
    
    head=node1
    obj=Solution()
    print(obj.findLoop(head))
    
        