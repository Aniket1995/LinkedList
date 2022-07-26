from hashlib import new
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
    
    def print(self):
        n=self.head
        while(n):
            print(n.data,end=" ")
            n=n.next
        print()

    def segregate1(self):
        curr=self.head
        tail=self.tail
        prev=None
        new_tail=tail
        # move all odds to the end of the ll
        while(curr != tail and curr.data % 2 != 0):
            new_tail.next=curr
            curr=curr.next
            new_tail.next.next=None
            new_tail=new_tail.next
        
        # here curr is end or even
        if(curr.data %2 != 0):
            prev=curr
        else:
            self.head=curr
            #move all odds to end from even/odd nodes
            while(curr!=tail):
                if(curr.data %2 == 0):
                    prev=curr
                    curr=curr.next
                else:
                    prev.next=curr.next
                    new_tail.next=curr
                    curr=prev.next
                    new_tail.next.next=None
                    new_tail=new_tail.next
        
        if(tail != new_tail and tail.data %2 !=0):
            prev.next=tail.next
            new_tail.next=tail
            tail.next=None

    def insert(self,head,tail,data):
        if(head is None):
            head=Node(data)
            tail=head
        else:
            tail.next=Node(data)
            tail=tail.next
        return head,tail

    def segregate2(self):
        # make 2 lists. even,odd. append respt to list. join in the end.
        eh=None
        oh=None
        c=self.head
        et=None
        ot=None
        while(c):
            if(c.data % 2 == 0):
                eh,et=self.insert(eh,et,c.data) 
            else:
                oh,ot=self.insert(oh,ot,c.data)
            c=c.next
        
        if(eh and et and oh and ot):
            et.next=oh
            self.head=eh
        elif(eh and et):
            self.head=eh
        else:
            self.head=oh







    

def segregateEvenOdd(ll):
    l=LinkedList()

    for i in ll:
        l.push(i)
    
    l.print()
    l.segregate2()
    l.print()

segregateEvenOdd([1,2,3,4,5,6])
segregateEvenOdd([2,4,6])
segregateEvenOdd([1,3,5])
segregateEvenOdd([2,4,6,1,3,5])
segregateEvenOdd([1,3,5,2,4,6])