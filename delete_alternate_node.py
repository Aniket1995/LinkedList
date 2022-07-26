from select import select


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
    
    def delAlternetNode(self):
        c=self.head
        while(c and c.next):
            c.next=c.next.next
            if(c):
                c=c.next
    def splitAlt(self):
        c=self.head
        ah=None
        at=None
        bh=None
        bt=None
        cnt=0
        global a,b
        while(c):
            if(cnt%2==0):
                if(ah is None):
                    ah=Node(c.data)
                    at=ah
                else:
                    at.next=Node(c.data)
                    at=at.next
            else:
                if(bh is None):
                    bh=Node(c.data)
                    bt=bh
                else:
                    bt.next=Node(c.data)
                    bt=bt.next
            cnt+=1
            c=c.next
        a=ah
        b=bh

def delAlternetNode(l):
    ll=LinkedList()

    for i in l:
        ll.push(i)
    
    ll.print()
    global a
    global b

    # res=ll.alternetEvenOdd()
    # ll.delAlternetNode()
    # ll.print()

    ll.splitAlt()

    c=a
    while(c):
        print(c.data, end=" ")
        c=c.next
    print()
    c=b
    while(c):
        print(c.data, end=" ")
        c=c.next
    print()

delAlternetNode([7, 41, 25, 8, 52, 0, 20, 5, 45])
# delAlternetNode([1,3])
# delAlternetNode([1,3,5])
# delAlternetNode([1])
# delAlternetNode([1,1,2])
# delAlternetNode([2,1,2])