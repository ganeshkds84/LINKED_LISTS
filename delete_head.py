import insert_at_head

class Deletion:
    def delete_head(self,head):
        if not head:
            return
        head=head.next
        return head
    def updated_ll(self,node):
        current=node
        while current!=None:
            print(current.data, end='->')
            current=current.next
        




if __name__=='__main__':
    node1=insert_at_head.Node(11)
    node2=insert_at_head.Node(22)
    node3=insert_at_head.Node(33)
    
    newnode=insert_at_head.Node(55)
    
    #Linking_nodes
    
    node1.next=node2
    node2.next=node3
    
    head=node1
    #new_node=newnode
    
    
    obj=insert_at_head.Solution()
    print(newnode.next)
    print(obj.print_ll(newnode))
    obj.insert_at_head(head,newnode)
    print(obj.print_ll(newnode))
    obj2=Deletion()
    updated_head=obj2.delete_head(newnode)
    print(obj2.updated_ll(updated_head))
    