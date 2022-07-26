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
            res.append(str(c.data))
            c=c.next
        print("->".join(res))

    @staticmethod
    def pprint(head,tail):
        c=head
        res=[]
        while(c != tail.next):
            res.append(str(c.data))
            c=c.next
        print("->".join(res))


    @staticmethod
    def insert(head,node):
        if(head == None or node == None or head == node):
            return head,False
        
        c=head
        prev=None
                
        while(c != node):
            if(c.data > node.data):
                if(prev is None):
                    node.next=head
                    head=node
                else:
                    prev.next=node
                    node.next=c
                return head,True
            prev=c
            c=c.next
            
        return head,False

    @staticmethod
    def insertionSort(head):
        if(head == None):
            return head
        
        c=head
        while(c and c.next):
            next_next=c.next.next
            head,is_inserted=LinkedList.insert(head,c.next)
            if(is_inserted):
                c.next=next_next
            else:
                c=c.next
        
        return head


def main(data):
    ll=LinkedList()

    for i in data:
        ll.push(i)


    ll.print()

    ll.head = LinkedList.insertionSort(ll.head)

    ll.print()


main([3,7,8,1,2,4,5,6])
main([1,2,3,4,5])
main([4,5,1,2,3])
main([1,2,3])
main([3,2,1])