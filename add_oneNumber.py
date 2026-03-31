from intersection import Node

class Solution:
    def addOne(self,head):
        head=self.reverseList(head)
        current=head
        carry=1
        while current and carry:
            total=current.val+carry
            current.val=total%10
            carry=total//10
            if current.next is None and carry:
                current.next=Node(0)
            current=current.next 
        head=self.reverseList(head)
        
        return head
    
    def reverseList(self,head):
        current=head
        prev=None
        while current:
            nextnode=current.next 
            current.next=prev
            prev=current
            current=nextnode
        return prev
    
if __name__=='__main__':
    n1=Node(9)
    n2=Node(9)
    n3=Node(9)
    n1.next=n2
    n2.next=n3
    obj=Solution()
    head=obj.addOne(n1)
    current=head
    while current:
        print(current.val,end='->')
        current=current.next 
    print(None)