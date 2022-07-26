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
        while(c):
            print(c.data,end=" ")
            c=c.next
        print()
    
    def reverseBlockwise(self,head,k):
        if(head is None):
            return None
        
        curr=head
        next=None
        prev=None
        c=0

        while(curr and c<k):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
            c+=1
        
        if(next):
            head.next = self.reverseBlockwise(next,k)
        
        return prev

    def reverseAltBlockwise(self,head,k,alt):
        if(head is None):
            return None
        
        curr=head
        next=None
        prev=None

        if(alt):
            c=0
        else:
            c=1
        
        while(curr and c<k):
            if(alt):
                next=curr.next
                curr.next=prev
                prev=curr
                curr=next
            else:
                curr=curr.next  
            c+=1

        if(alt):
            if(next):
                head.next = self.reverseAltBlockwise(next,k,not alt)
        else:
            if(curr and curr.next):
                curr.next = self.reverseAltBlockwise(curr.next,k, not alt)
                
        if(alt):
            return prev
        else:
            return head

def main(list,k):
    ll = LinkedList()

    for i in list:
        ll.push(i)
    
    ll.print()

    # ll.head = ll.reverseBlockwise(ll.head, k)
    ll.head = ll.reverseAltBlockwise(ll.head, k, True)

    ll.print()

main([1,2,3,4,5,6,7,8,9],3)
main([1,2,3,4,5,6,7,8,9],5)
main([1,2,3,4,5,6,7,8,9],2)
main([1,2,3,4,5,6,7,8,9],6)