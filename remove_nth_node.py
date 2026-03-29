class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        pass
    
class Solution:
    def removeNthnode(self,head,n):
        if head is None:
            return None
        count=0
        current=head
        while current:
            count+=1
            current=current.next 
        current=head
        prev=None
        while current:
            if count-n==0:
                if prev is None:
                    return None
                prev.next=current.next 
                current.next=None
            count-=1
            prev=current
            current=current.next 
        return head
        pass
    
if __name__=='__main__':
    t=Node(1)
    u=Node(2)
    v=Node(3)
    w=Node(4)
    x=Node(5)
    
    #Link_nodes
    t.next=u
    u.next=v
    v.next=w
    w.next=x
    
    head=t
    n=int(input('Enter a number within size of ll:'))
    obj=Solution()
    head=obj.removeNthnode(head,n)
    current=head
    while current:
        print(current.data,end='->')
        current=current.next 
    print(None)
    