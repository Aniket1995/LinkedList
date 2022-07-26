from re import L

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

    def ZigZag(self):
        if(self.head is None):
            return 
        
        c=self.head
        big=True

        while(c and c.next):
            if(big):
                if(c.data > c.next.data):
                    c.next.data,c.data = c.data,c.next.data
            else:
                if(c.data < c.next.data):
                    c.next.data,c.data = c.data,c.next.data
            c=c.next
            big=not big
                  

def main(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)
    ll.print()
    ll.ZigZag()
    ll.print()

main([1,2,3,4,5,6])
main([2,6,4])
main([1,3,5])
main([1,0,0,1])
main([0,1,1,0])
main([0,1,1,1])

main([10,22,30,43,56,70])