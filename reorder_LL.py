from tracemalloc import start
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

    # ================================================================
    #  time: O(n*n)
    #  space: O(1)

    # def find(self,start):
    #     if(start is None or start.next is None):
    #         return None
        
    #     c=start

    #     while(c.next.next):
    #         c=c.next
        
    #     node=c.next

    #     c.next=None

    #     return node


    
    # def reorder(self):
        
    #     if(self.head is None):
    #         return

    #     c=self.head

    #     while(c and c.next):
    #         next=c.next
    #         node=self.find(c.next)
    #         if(node == None or node == c.next):
    #             break
    #         c.next=node
    #         node.next=next
    #         c=next

    # ================================================================

    # ================================================================
    
    # time:O(n)
    # space:O(n) recursion
    
    # def len(self):
    #     if(self.head == None):
    #         return 0
    #     len=0
        
    #     c=self.head
        
    #     while(c):
    #         c=c.next
    #         len+=1
                
    #     return len


    # def reorderHelper(self,node,mid,even):
    #     if(node == None or mid == None):
    #         return

    #     if(even and node.next == mid):
    #         return
        
    #     if(not even and node == mid):
    #         return

    #     self.reorderHelper(node.next,mid,even)

    #     if(mid.next):
    #         mid_next = mid.next
    #         mid.next = mid.next.next
    #         node_next = node.next
    #         node.next = mid_next
    #         mid_next.next = node_next

    # def reorder(self):
    #     if(self.head is None):
    #         return 
        
    #     mid=self.getMid()

    #     if(mid == self.head):
    #         return
        
    #     self.reorderHelper(self.head,mid,self.len()%2 == 0)

    # ================================================================

    # time:o(n)
    # space:o(n)

    # def reorder(self):
    #     if(self.head is None):
    #         return 
    #     mid = self.getMid()

    #     stack=[]
    #     c=mid
        
    #     while(c and c.next):
    #         stack.append(c.next)
    #         c.next=c.next.next

    #     c=self.head

    #     while(len(stack) > 0):
    #         c_next = c.next
    #         node=stack.pop()
    #         c.next=node
    #         node.next=c_next
    #         c=c_next

    def getMid(self):
        if(self.head is None):
            return None

        p1=self.head
        p2=self.head

        while(p2 and p2.next):
            p1=p1.next
            p2=p2.next.next

        return p1

    def reverse(self,start):
        if(start is None or start.next is None):
            return start
        curr=start
        prev=None
        next=curr.next

        while(next):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev

    def merge(self,start1,start2):

        if(start1 == None or start2 == None):
            return
        
        start1_next=start1.next
        start1.next=start2
        start2_next=start2.next
        start2.next=start1_next

        self.merge(start1_next,start2_next)
        

    def reorder(self):
        if(self.head is None):
            return
        mid=self.getMid()
        node1=self.head
        node2=mid.next
        mid.next=None
        node2=self.reverse(node2)
        self.merge(node1,node2)
        self.head=node1


def main(data):
    ll=LinkedList()
    for i in data:
        ll.push(i)
    
    ll.print()

    ll.reorder()

    ll.print()


main([1,2,3,4,5,6])
main([1,2,3,4,5])
main([1,2,3,4])
main([1,2,3])
main([1,2])
main([1])
main([])