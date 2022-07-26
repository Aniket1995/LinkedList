class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def push(self,data):
        if(self.head is None):
            self.head=Node(data)
            self.tail=self.head
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
    
    def insert(self,data):
        if(self.head is None):
            self.head=Node(data)
            self.tail=self.head
        else:
            node=Node(data)
            node.next=self.head
            self.head=node
    
    def print(self):
        c=self.head
        res=[]
        while(c):
            res.append(str(c.data))
            c=c.next
        print("->".join(res))
        print()
    
    def pushToTail(self,head,tail,node):
        if(node is None):
            return head,tail
        
        if(head is None):
            head=tail=node
        else:
            tail.next=node
            tail=node
        node.next=None
        return head,tail

    def pprint(head):
        if(head is None):
            return
        c=head
        res=[]
        while(c):
            res.append(str(c.data))
            c=c.next
        print("->".join(res))
    
    def reorder(self):
        if(self.head is None):
            return
        
        c=self.head
        e_h=None
        e_t=None
        o_h=None
        o_t=None

        while(c):
            next=c.next
            if(c.data % 2 == 0):
                e_h,e_t=self.pushToTail(e_h,e_t,c)
            else:
                o_h,o_t=self.pushToTail(o_h,o_t,c)
            c=next
        
        if(e_h and not o_h):
            self.head = e_h
        else:
            o_t.next=e_h
            self.head=o_h
        


def main(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)
    ll.print()
    ll.reorder()
    ll.print()

# main([1,2,3,4,5,6])
# main([2,6,4])
# main([1,3,5])
# main([1,0,0,1])
# main([0,1,1,0])
# main([0,1,1,1])

main([10,22,30,43,56,70])
