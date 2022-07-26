from operator import le


class Node:
    def __init__(self,data):
        self.data=data
        self.arb=None
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.arb=None
    
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
        arb=[]
        while(c):
            res.append("->".join([str(c.data),str(c.arb.data) if c.arb else "None"]))
            c=c.next
        print("\n|\n".join(res))

    # def getMiddle(head):

    #     if(head is None):
    #         return head
        
    #     p1=head
    #     p2=head
    #     print("head:{0}".format(head.data))
    #     while(p2 and p2.arb):
    #         p1=p1.arb
    #         p2=p2.arb.arb
        
    #     if(p2 and p2.next):
    #         return p1.next
    #     return p1

    def getMiddle(source):
 
        # Base case
        if (source == None):
            return source
            
        fastptr = source.arb
        slowptr = source
    
        # Move fastptr by two and slow ptr by one
        # Finally slowptr will point to middle node
        while (fastptr != None):
            fastptr = fastptr.arb
            if (fastptr != None):
                slowptr = slowptr.arb
                fastptr = fastptr.arb
            
        return slowptr
    
    @staticmethod
    def pprint(head):
        res=[]
        c=head
        while(c):
            res.append(str(c.data))
            c=c.arb
        print("->".join(res))

    @staticmethod
    def merge(a,b):
        if(a is None):
            return b
        
        if(b is None):
            return a
        
        result=None

        if(a.data < b.data):
            result=a
            result.arb=LinkedList.merge(a.arb,b)
        else:
            result=b
            result.arb=LinkedList.merge(a,b.arb)

        return result
    
    @staticmethod
    def mergeSortArb(head):
        if(head is None or head.arb is None):
            return head
        
        mid=LinkedList.getMiddle(head)
        arb_mid=mid.arb
        mid.arb=None
        
        left = LinkedList.mergeSortArb(head)
        
        right = LinkedList.mergeSortArb(arb_mid)

        sortedList = LinkedList.merge(left,right)

        return sortedList


    def updateArbPOinters(self):
        c=self.head
        while(c):
            c.arb=c.next
            c=c.next
        
        self.arb=LinkedList.mergeSortArb(self.head)


def main(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)
    
    ll.print()

    ll.updateArbPOinters()

    ll.print()

main([1,5,2,3,46])