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
        res=[]
        while(c):
            res.append(c.data)
            c=c.next
        print("->".join([str(i) for i in res]))

    @staticmethod
    def swap(root):
        if(root is None or root.next is None):
            return root
        
        rem=root.next.next
        nh=root.next
        root.next.next=root
        root.next=LinkedList.swap(rem)
        return nh


def pairwiseSwap(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)
    
    ll.print()

    ll.head = ll.swap(ll.head)

    ll.print()

pairwiseSwap([1,2,3,4,5,6,7])
pairwiseSwap([1,2,3,4,5,6])
pairwiseSwap([1,2])