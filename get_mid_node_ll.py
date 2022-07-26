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
    
    def print(self):
        n=self.head
        res=[]
        while(n):
            res.append(str(n.data))
            n=n.next
        print("->".join(res))


def getMiddle1(head):

    if(head is None):
        return head
    p1=head
    p2=head
    while(p2 and p2.next):
        p1=p1.next
        p2=p2.next.next
    
    return p1


def getMiddle2(source):

    # Base case
    if (source == None):
        return source
        
    fastptr = source.next
    slowptr = source

    # Move fastptr by two and slow ptr by one
    # Finally slowptr will point to middle node
    while (fastptr != None):
        fastptr = fastptr.next
        if (fastptr != None):
            slowptr = slowptr.next
            fastptr = fastptr.next
        
    return slowptr

def main(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)

    ll.print()
    print("mid 1:{0}".format(getMiddle1(ll.head).data))
    print("mid 2:{0}".format(getMiddle2(ll.head).data))
    
    

main([1,2,3,4,5,6,7])
main([1,2])
main([1])
main([1,2,3,4,5,6,7,9])