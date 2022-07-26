from re import A, L

from requests import head


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def push(self,data):
        n=Node(data)
        
        if(self.head is None):
            self.head=n
            self.tail=n
        else:
            self.tail.next=n
            self.tail=n
    
    def insert(self,data):
        n=Node(data)
        
        if(self.head is None):
            self.head=n
            self.tail=n
        else:
            n.next=self.head
            self.head=n
    
    @staticmethod
    def pprint(head):
        c=head
        res=[]
        while(c):
            res.append(str(c.data))
            c=c.next
        
        print("->".join(res))

    def print(self):
        n=self.head
        res=[]
        while(n):
            res.append(str(n.data))
            n=n.next
        print("->".join(res))

    def merge(self,a,b):
        if(a is None):
            return b
        if(b is None):
            return a
        result=None
        if(a.data < b.data):
            result=a
            result.next=self.merge(a.next,b)
        else:
            result=b
            result.next=self.merge(a,b.next)
        return result
    
    def reorder(self):
        if(self.head is None):
            return
        
        c=self.head

        head2=None

        while(c and c.next):
            next_next = c.next.next
            node=c.next
            if(head2 is None):
                node.next=None
            else:
                node.next=head2
            head2=node
            c.next=next_next
            c=c.next

        self.head = self.merge(self.head,head2)



def main(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)
    
    ll.print()

    ll.reorder()

    ll.print()


main([1,15,2,14,3,13,4,12,5,11,6,10,7,9,8])
main([8,7,9,6,10,5,11,4,12,3,13,2,14,1,15])
main([1,2,3])
main([1,3,2])
main([1,2])
main([1])
main([])