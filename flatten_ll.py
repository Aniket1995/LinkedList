
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.bottom=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def pushNext(self,data):
        if(self.head is None):
            self.head=self.tail=Node(data)
        else:
            self.tail.next=Node(data)
            self.tail=self.tail.next
        return self.tail
    
    def pushDown(self,node,data):
        if(node is None):
            return
        node.bottom=Node(data)
        return node.bottom
    
    @staticmethod
    def build2DLL(data):
        ll=LinkedList()
        for i in range(0,len(data)):
            for j in range(0, len(data[i])):
                if(j==0):
                    node=ll.pushNext(data[i][j])
                else:
                    node=ll.pushDown(node,data[i][j])
        return ll

    def bottomList(self,node):
        if(node is None):
            return []
        c=node
        res=[]
        while(c):
            res.append(str(c.data))
            c=c.bottom
        return res
        
    def print(self):
        print("->:bottom, |:next")
        c=self.head
        while(c):
            res=self.bottomList(c)
            print("->".join(res))
            c=c.next
            if(c):
                print("|")

    @staticmethod
    def merge(a,b):
        if(a is None):
            return b
        
        if(b is None):
            return a
        
        res=None

        if(a.data < b.data):
            res=a
            res.bottom=LinkedList.merge(a.bottom,b)
        else:
            res=b
            res.bottom=LinkedList.merge(a,b.bottom)
        
        res.next=None

        return res

    @staticmethod
    def flattenList(root):
        if(root is None or root.next is None):
            return root
        
        root.next = LinkedList.flattenList(root.next)

        root = LinkedList.merge(root,root.next)

        return root
        

def flatten(data):
    ll=LinkedList.build2DLL(data)
    ll.print()
    ll.head=LinkedList.flattenList(ll.head)
    ll.print()


flatten([ [1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20]])
        
                


