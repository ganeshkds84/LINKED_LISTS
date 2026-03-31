class Node:
    def __init__(self,data):
        self.val=data
        self.next=None
class Solution:
    def isInterscetion(self,headA,headB):
        a=headA
        b=headB
        while a!=b:
            if a:
                a=a.next 
            else:
                a=headB
            if b:
                b=b.next 
            else:
                b=headA
        return None if a==None else a.val
if __name__=='__main__':
    n1=Node(1)
    n2=Node(2)
    n3=Node(3)
    n4=Node(4)
    n5=Node(5)
    n6=Node(7)
    n7=Node(8)
    
    n1.next=n2
    n2.next=n3
    n3.next=n4
    n4.next=n5
    n6.next=n7
    n7.next=n4
    headA=n1
    headB=n6
    obj=Solution()
    print(obj.isInterscetion(headA,headB))
    