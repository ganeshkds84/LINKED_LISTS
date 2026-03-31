from intersection import Node
class Solution:
    def addLl(self,l1,l2):
        a=self.reverseList(l1)
        b=self.reverseList(l2)
        dummy=Node(0)
        tail=dummy
        carry=0
        while a or b or carry:
            val1=val2=0
            if a:
                val1=a.val
            if b:
                val2=b.val
            total=val2+val1+carry
            digit=total%10
            carry=total//10
            new=Node(digit)
            tail.next=new
            tail=tail.next
            if a:
                a=a.next
            if b:
                b=b.next 
        return dummy.next
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
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    
    n1.next=n2
    n2.next=n3
    n4.next=n5
    
    obj=Solution()
    head=obj.addLl(n1,n4)
    current=head
    while current:
        print(current.val,end='->')
        current=current.next 
    print(None)
    