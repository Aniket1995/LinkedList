
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
        if(self.head is None and node is None):
            self.head = self.tail = Node(data)
            return self.head
        node.bottom=Node(data)
        return node.bottom
    
    # @staticmethod
    # def build2DLL(data):
    #     ll=LinkedList()
    #     for i in range(0,len(data)):
    #         for j in range(0, len(data[i])):
    #             if(j==0):
    #                 node=ll.pushNext(data[i][j])
    #             else:
    #                 node=ll.pushDown(node,data[i][j])
    #     return ll

    def bottomList(self,node):
        if(node is None):
            return []
        c=node
        res=[]
        while(c):
            res.append(str(c.data))
            c=c.bottom
        return res
        
    def printNext(self):
        # print("->:next, |:bottom")
        c=self.head
        
        res=[]

        while(c):
            res.append(str(c.data))
            c=c.next
        
        print("->".join(res))

    
        
    def printBottom(self):
        # print("->:next, |:bottom")
        c=self.head
        
        res=[]

        while(c):
            res.append(str(c.data))
            c=c.bottom
        
        print("\n|\n".join(res))


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
        
        root.bottom = LinkedList.flattenList(root.bottom)

        root.next = LinkedList.flattenList(root.next)

        root = LinkedList.merge(root,root.next)

        return root


    @staticmethod
    def mergeNext(a,b):
        if(a is None):
            return b
        
        if(b is None):
            return a
        
        res=None

        if(a.data < b.data):
            res=a
            res.next=LinkedList.merge(a.next,b)
        else:
            res=b
            res.next=LinkedList.merge(a,b.next)
        
        res.bottom=None

        return res


    @staticmethod
    def flattenListBottomToNext(root):
        if(root is None or root.next is None):
            return root
        
        root.bottom = LinkedList.flattenListBottomToNext(root.bottom)

        root.next = LinkedList.flattenListBottomToNext(root.next)

        root = LinkedList.mergeNext(root,root.bottom)

        return root
    
    @staticmethod
    def buildMiltiLL(data,is_next):
        ll=LinkedList()
        node=None
        for i in range(0,len(data)):
            d_=data[i]
            if(type(d_) is int):
                # print("{0} is {1} == int ".format(d_,type(d_)))
                # if(is_next):
                node=ll.pushNext(d_)
                # print("pushing {0} {1} to {2}".format(d_,"next" if is_next else "down",node.data))
                # else:
                    # if(node):
                    #     print("pushing {0} {1} to {2}".format(d_,"next" if is_next else "down",node.data))
                    # else:
                    #     print("pushing {0} {1} to {2}".format(d_,"next" if is_next else "down","head"))
                    # node=ll.pushDown(node,d_)
                # print("pushing {0} {1}".format(d_,"next" if is_next else "down"))
            elif(type(d_) is list):
                # print("{0} is {1} == list ".format(d_,type(d_)))
                llb=LinkedList.buildMiltiLL(d_,not is_next)
                # print("\nprinting LL down to {0}\n".format(node.data))
                # llb.print()
                if(llb.head):
                    node.bottom=llb.head
        return ll

def flatten(data,is_next):
    ll=LinkedList.buildMiltiLL(data,is_next)
    ll.printNext()
    ll.head=LinkedList.flattenList(ll.head)
    ll.printBottom()

    # ll.head=LinkedList.flattenListBottomToNext(ll.head)
    # ll.printBottom()


flatten([1,[2,3,4],5,[6,[7],8,9,10],11,12,[13,14,15,[16,17],18],19,20],True)
        
                


