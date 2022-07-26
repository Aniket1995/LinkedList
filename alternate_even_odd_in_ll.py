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
    
    def print(self):
        c=self.head
        while(c):
            print(c.data,end=" ")
            c=c.next
        print()
    
    # time:o(n)
    # space:o(n)
    def alternetEvenOdd(self):
        el=LinkedList()
        ol=LinkedList()
        res=LinkedList()

        c=self.head

        while(c):
            if(c.data % 2 == 0):
                el.push(c.data)
            else:
                ol.push(c.data)
            c=c.next
        
        ce=el.head
        co=ol.head
        c=1
        while(ce and co):
            if(c%2==0):
                res.push(ce.data)
                ce=ce.next
            else:
                res.push(co.data) 
                co=co.next
            c+=1
        
        while(ce):
            res.push(ce.data)
            ce=ce.next

        while(co):
            res.push(co.data) 
            co=co.next
        
        return res

    def findNode(self, node, prev, even):
        c=node
        while(c):
            if((even and c.data % 2 == 0) or ( not even and c.data % 2 != 0)):
                return prev,c
            prev=c
            c=c.next
        return None,None


    def alternetEvenOdd2(self):
        curr=self.head
        even=curr.data %2 == 0
        prev=curr
        curr=curr.next
        while(curr != None):
            even = not even
            if((even and curr.data % 2 == 0) or ( not even and curr.data % 2 != 0)):
                prev=curr
                curr=curr.next
                continue
            else:
                p,n=self.findNode(curr.next,curr,even)
                if(n):
                    prev.next=n
                    p.next=curr
                    n.next,curr.next = curr.next,n.next
                    curr=n.next
                    prev=n
                else:
                    break

def separate(l):
    ll=LinkedList()

    for i in l:
        ll.push(i)
    
    ll.print()

    # res=ll.alternetEvenOdd()
    ll.alternetEvenOdd2()
    ll.print()

separate([1,3,5,7,2,4,6,8])
separate([1,3])
separate([1,3,5])
separate([1])
separate([1,1,2])
separate([2,1,2])