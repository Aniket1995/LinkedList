class Node:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.next=None

    def print(self):
        print("({0},{1})->".format(self.x,self.y))

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def push(self,x,y):
        if(self.head is None):
            self.head=Node(x,y)
            self.tail=self.head
        else:
            n=Node(x,y)
            n.next=self.head
            self.head=n
    
    def print(self):
        c=self.head
        res=[]
        while(c):
            res.append("({0},{1})".format(c.x,c.y))
            c=c.next
        print("->".join(res))

def removeMidElem(head):
    if(head is None or head.next is None):
        return head
    
    a=head
    b=head.next
    c=head.next.next

    while(a and b and c):
        if((a.x == b.x and b.x == c.x) or (a.y == b.y and b.y == c.y)):
            a.next=c
            b=a.next
            c=b.next
            continue
        a=a.next
        b=b.next
        c=c.next
    
    return head

def Solution(data):
    ll=LinkedList()

    for i in data:
        ll.push(i[0],i[1])
    
    ll.print()
    ll.head = removeMidElem(ll.head)
    ll.print()

# Solution([(40,5),(20,5),(10,5),(10,8),(10,10),(3,10),(1,10),(0,10)])


Solution([(0,10),(1,10),(5,10),(7,10),(7,5),(20,5),(40,5)])