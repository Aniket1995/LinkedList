from re import L


class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def print_right(root):
    c=root
    res=[]

    while(c):
        res.append(str(c.data))
        c=c.right
    print("\nright")
    print("->".join(res))

def printCDLLL(root):
    if(root is None):
        return
    res=[str(root.data)]
    c=root.right

    while(c and c != root):
        res.append(str(c.data))
        c=c.right
    print("right")
    print("->".join(res))

    res=[str(root.data)]

    c=root.left

    while(c and c != root):
        res.append(str(c.data))
        c=c.left
    
    print("left")
    print("->".join(res))



def print_left(root):
    c=root
    res=[]

    while(c):
        res.append(str(c.data))
        c=c.left
    print("\nleft")
    print("->".join(res))
    
def inorder_print(root):
    if(root == None):
        return
    
    inorder_print(root.left)
    print(root.data,end=" ")
    inorder_print(root.right)

def merge_right(root,left):
    if(root == None):
        return left
    if(left == None):
        return root
    c=left
    while(c.right):
        c=c.right
    c.right=root
    return left

def merge_left(root,right):
    if(root == None):
        return right
    if(right == None):
        return root
    c=right
    while(c.left):
        c=c.left
    c.left=root
    return right

def flatten_right(root):
    if(root is None):
        return root
    root.left=flatten_right(root.left)
    root.right=flatten_right(root.right)
    root=merge_right(root,root.left)
    return root

def flatten_left(root):
    if(root is None):
        return root
    root.right=flatten_left(root.right)
    root.left=flatten_left(root.left)
    root=merge_left(root,root.right)
    return root

def flat_right():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

def flat_left():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    inorder_print(root)
    root=flatten_left(root)
    print_left(root)

def BinaryTreeToCDLL():
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    # root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    # root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    # root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    # root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    # root.left=Node(2)
    root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    # root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    # root.left=Node(2)
    # root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    # root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    # root.left.right=Node(5)
    root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    # root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    # root.right.left=Node(6)
    # root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    # root.left.left=Node(4)
    # root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)
    inorder_print(root)
    root=flatten_right(root)
    print_right(root)

    if(root and root.right):
        c=root.right
        p=root
        while(c):
            c.left=p
            p=c
            c=c.right
        p.right=root
        root.left=p
    
    printCDLLL(root)


BinaryTreeToCDLL()
# flat_right()
# flat_left()