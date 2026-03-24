class Node:
    def __init__(self,data):
        self.next=None
        self.val=data
        
class Solution:
    def check_element(self,head,key):
        
        current=head
        while current:
            if current.val==key:
                return True
            current=current.next
        
        return False
    
if __name__=='__main__':
    values=list(map(int,input("Enter values:").split()))
    head=None
    prev=None
    
    for i in range(len(values)):
        node=Node(values[i])
        
        if head is None:
            head=node
        else:
            prev.next=node
        
        prev=node
        
    obj=Solution()
    #print(head)
    key=int(input("Enter key value to search:"))
    print(obj.check_element(head,key))
    