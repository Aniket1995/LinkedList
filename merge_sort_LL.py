#User function Template for python3
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

def getMid(head):
    if(head is None):
        return head
    
    p1=head
    p2=head.next
    
    while(p2):
        p2=p2.next
        if(p2):
            p1=p1.next
            p2=p2.next
    
    return p1
    
def merge(a,b):
    
    if(a is None):
        return b
        
    if(b is None):
        return a
        
    r=None
    
    if(a.data < b.data):
        r=a
        r.next=merge(a.next,b)
    else:
        r=b
        r.next=merge(a,b.next)
    
    return r
    
def mergeSort(head):
    
    if(head is None or head.next is None):
        return head
        
    mid=getMid(head)
    print("mid: "+str(mid.data))
    mid_next=mid.next
    mid.next=None
    
    left=mergeSort(head)
    
    right=mergeSort(mid_next)
    
    return merge(left,right)
    
    
def sortList(head):
    if(head is None):
        return head
    head=mergeSort(head)

def main(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)
    
    ll.print()

    ll.head=mergeSort(ll.head)

    ll.print()

main([1, -2, -3, 4, -5])

