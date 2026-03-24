from insert_at_head import Node,Solution

class Count:
    def count_of_elements(self,head):
        if not head:
            return 'No nodes'
        count=0
        while head!=None:
            count+=1
            head=head.next
            
        
        return count


if __name__=='__main__':
    
    #creating nodes
    
    x=Node(15)
    y=Node(20)
    z=Node(25)
    
    #Connecting nodes
    x.next=y
    y.next=z
    
    obj=Count()
    
    print(obj.count_of_elements(x))
    