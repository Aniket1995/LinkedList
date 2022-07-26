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
        # print("tail.next",tail.next.data if tail.next else None)

    # @staticmethod
    # def quickSort(head,tail,sp):

    #     if(head == None or tail == None or head == tail):
    #         return head
    #     print(sp+"head:{0} tail:{1}".format(head.data,tail.data))
    #     pivot=tail
    #     c=head
    #     tail_next=tail.next
    #     print(sp+"pivot:{0}".format(pivot.data))
    #     if(tail_next):
    #         print(sp+"storing tail {1}->{0}".format(tail_next.data,tail.data))
    #     else:
    #         print(sp+"storing tail {1}->{0}".format(None,tail.data))

    #     print(sp+"1 - start pivot:{0}".format(pivot.data))
    #     LinkedList.pprint(head,tail,sp)
    #     while(c != pivot and c.data > pivot.data):
    #         next=c.next
    #         head=head.next
    #         tail.next=c
    #         tail=c
    #         tail.next=None
    #         c=next
    #     print(sp+"1 - end pivot:{0}".format(pivot.data))
    #     LinkedList.pprint(head,tail,sp)


    #     if(c == pivot): # nothing in left go right
    #         c.next = LinkedList.quickSort(c.next,tail,sp+sp)
    #     else:
    #         prev=c
    #         c=c.next
            
    #         print(sp+"2 - start pivot:{0}".format(pivot.data))
    #         LinkedList.pprint(head,tail,sp)
            
    #         while(c != pivot):
    #             if(c.data > pivot.data):
    #                 next=c.next
    #                 prev.next=c.next
    #                 tail.next=c
    #                 tail=c
    #                 tail.next=None
    #                 c=next
    #                 continue
    #             prev=c
    #             c=c.next
            
    #         print(sp+"2 - end pivot:{0}".format(pivot.data))
    #         LinkedList.pprint(head,tail,sp)

    #         if(tail == pivot): # nothing in right go left
    #             head=LinkedList.quickSort(head,prev,sp+sp)
    #         else:# we have left and right go for both
    #             head=LinkedList.quickSort(head,prev,sp+sp)
    #             pivot.next=LinkedList.quickSort(pivot.next,tail,sp+sp)

    #     if(tail_next):
    #         print(sp+"restoring tail {1}->{0}".format(tail_next.data,tail.data))
    #     else:
    #         print(sp+"restoring tail {1}->{0}".format(None,tail.data))
    #     tail.next=tail_next
    #     return head

    @staticmethod
    def partition(head,tail):
        if(head is None or tail is None or head == tail):
            return head,None,None,tail
        pivot=tail
        prev=None
        c = head
        tail_next=tail.next

        while(c != pivot):
            if(c.data < pivot.data):
                if(prev is None):
                    next=c.next
                    tail.next=c
                    tail=c
                    head=head.next
                    c=next
                else:
                    prev.next=c.next
                    tail.next=c
                    tail=c
                    c=prev.next
                continue
            prev=c
            c=c.next
        
        tail.next=tail_next
        
        return head,prev,c,tail

    def getData(n):
        if(n):
            return n.data
        return None

    @staticmethod
    def quickSort(head,tail):
        if(head is None or tail is None or head == tail):
            return head,tail
        head,pivot_pre,pivot,tail = LinkedList.partition(head,tail)
        if(head == pivot_pre and tail == pivot):
            return head,tail
        if(pivot_pre == None and pivot == None):
            return head,tail
        if(pivot == head): # nothing  in left. go in right 
            head_right,tail_right=LinkedList.quickSort(pivot.next,tail)
            pivot.next=head_right
            head=pivot
            tail=tail_right
        elif(pivot == tail): # nothing  in right. go in left 
            head_left,tail_left=LinkedList.quickSort(head,pivot_pre)
            head=head_left
            tail_left.next=pivot
            tail=pivot
        else: # go left. go right 
            head_left,tail_left=LinkedList.quickSort(head,pivot_pre)
            head_right,tail_right=LinkedList.quickSort(pivot.next,tail)
            tail_left.next=pivot
            pivot.next=head_right
            head=head_left
            tail=tail_right 

        return head,tail

def main(data):
    ll=LinkedList()
    for i in data:
        ll.push(i)
    ll.print()

    ll.head,ll.tail=LinkedList.quickSort(ll.head,ll.tail)

    ll.print()

main([3,6,5,2,1])  
print("\n\n")
main([3,6,5])
print("\n\n")  
main([3,6])  
main([6,3])  
print("\n\n")
main([3])  
print("\n\n")
main([3,6,5,2,1,4,8,9,7])
print("\n\n")
main([5,2,7,4,5,2,3])
print("\n\n")  

main([1,2,3,4,5,6,7])
print("\n\n")
main([7,6,5,4,3,2,1])

main([1,2,3,4,4,3,2,1,5,6,7,8,8,7,6,5])