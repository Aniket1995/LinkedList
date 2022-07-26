from re import I
from tkinter import N
from tkinter.messagebox import NO


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
        while(n):
            print(n.data,end=" ")
            n=n.next
        print()

def merge(ll1,ll2):
    if(ll1.head is None and ll2.head is None):
        return None
    if(ll1.head is None):
        return ll2

    if(ll2.head is None):
        return ll1

    res=LinkedList()

    c1=ll1.head
    c2=ll2.head

    while(c1 and c2):
        if(c1.data < c2.data):
            res.insert(c1.data)
            c1=c1.next
        else:
            res.insert(c2.data)
            c2=c2.next
    
    while(c1):
        res.insert(c1.data)
        c1=c1.next
    
    while(c2):
        res.insert(c2.data)
        c2=c2.next
    
    return res
        

def merge2LL(l1,l2):
    ll1 = LinkedList()
    ll2 = LinkedList()

    for i in l1:
        ll1.push(i)

    for i in l2:
        ll2.push(i)
    
    if(ll1):
        ll1.print()
    if(ll2):
        ll2.print()
    
    res_ll = merge(ll1,ll2)

    res_ll.print()


merge2LL([5,10,15,40],[])