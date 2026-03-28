from loop_length import Node
class Solution:
    def isPalindrome(self,head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next 
            fast=fast.next.next 
        
        prev=None
        while slow:
            nextnode=slow.next 
            slow.next=prev
            prev=slow
            slow=nextnode
        
        left=head
        right=prev
        while left:
            if left.data!=right.data:
                return False
            left=left.next
            right=right.next
        return True
    
if __name__=='__main__':
    
    node1=Node(10)
    node2=Node(15)
    node3=Node(20)
    node4=Node(25)
    node5=Node(20)
    node6=Node(15)
    node7=Node(10)
    
    #creating links
    
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    node5.next=node6
    node6.next=node7
    head =node1
    obj=Solution()
    print(obj.isPalindrome(head))