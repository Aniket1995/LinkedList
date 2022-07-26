class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.last = None

	def append(self,data):
		n=Node(data)
		if(self.head is None):
			self.head=n
			self.last=n
		else:
			self.last.next=n
			self.last=n

	def push(self,data):
		n=Node(data)
		n.next=self.head
		self.head=n

	def printList(self):
		t=self.head
		data=[]
		while(t):
			# print(t.data)
			data.append(str(t.data))
			t=t.next
		if(data):
			print("->".join(data))
		else:
			print("Linked list is empty")

	def swapAdjNodes(self):
		if(self.head is None):
			return;

		c = self.head
		
		px=None
		cx=None
		py=None
		cy=None
		pc=None


		while(c and c.next):
			if(c == self.head):
				px = None
			else:
				px=pc
			cx=c
			py=c
			cy=c.next
			self.swapNodes_(px, cx, py, cy)
			pc=c
			c=c.next



	def swapNodes_(self, px, cx, py, cy):
		if( cx == cy):
			return

		# print('x is {0}, y is {1}'.format(cx.data,cy.data))

		if(cx is None or cy is None):
			return

		if(px is None):
			self.head = cy
		else:
			px.next = cy

		if(py is None):
			self.head = cx
		else:
			py.next = cx

		c=cx.next
		cx.next=cy.next
		cy.next=c


	def swapNodes(self, x, y):
		if( x == y):
			return

		px=None
		cx=None

		py=None
		cy=None

		c=self.head
		pc=None

		while(c):
			if(c.data == x):
				px=pc
				cx=c

			if(c.data == y):
				py=pc
				cy=c

			pc=c
			c=c.next

		# print('x is {0}, y is {1}'.format(cx.data,cy.data))

		if(cx is None or cy is None):
			return

		if(px is None):
			self.head = cy
		else:
			px.next = cy

		if(py is None):
			self.head = cx
		else:
			py.next = cx

		c=cx.next
		cx.next=cy.next
		cy.next=c

	def makeLastElemFirst(self):
		c=self.head

		while(c.next.next):
			c = c.next

		c.next.next = self.head
		self.head = c.next
		c.next=None

	def segregateEvenOdd(self):
		
		


	@staticmethod
	def intersectionList(ll1, ll2):
		if(ll1.head is None or ll2.head is None):
			return None
		e1=ll1.head
		e2=ll2.head
		newLL=LinkedList()
		while(e1 and e2):
			while(e1 and e1.data < e2.data):
				e2=e2.next
			if(e1.data == e2.data):
				newLL.append(e1.data)
				e2=e2.next
			e1=e1.next
		return newLL

def segregate(data):
	ll = LinkedList()

	for i in data:
		ll.append(i)

	ll.segregateEvenOdd()
	print("list agter segragation")
	ll.printList()

def findIntersection2LinkedList(ll1, ll2):
	llist = LinkedList()
	llist2 = LinkedList()

	for i in ll1:
		llist.append(i)

	for i in ll2:
		llist2.append(i)
	
	# The constructed linked list is:
	# 1->2->3->4->5->6->7
	# llist.swapNodes(1, 7)
	# llist.swapAdjNodes()
	# llist.makeLastElemFirst()
	# llist.makeLastElemFirst()
	# llist.makeLastElemFirst()
	# llist.makeLastElemFirst()

	print("Linked list 1")
	llist.printList()

	print("\nLinked list 2 ")
	llist2.printList()

	newLL = LinkedList.intersectionList(llist,llist2)

	if(newLL is None):
		print("\nintersection is empty")
	else:
		print("\nintersection Linked List")
		newLL.printList()


# findIntersection2LinkedList -- start
# findIntersection2LinkedList([1,2,3,4,5,6,7],[1,2,3,4,5,6,7])
# findIntersection2LinkedList([1,2,3,4,5,6,7],[1])
# findIntersection2LinkedList([1],[1,2,3,4,5,6,7])
# findIntersection2LinkedList([1,2,3,4,5,6,7],[])
# findIntersection2LinkedList([],[1,2,3,4,5,6,7])
# findIntersection2LinkedList([1],[1])
# findIntersection2LinkedList([5,6,7],[1,2,3])
# findIntersection2LinkedList -- end


# segregate - start
segregate([1,5,3,2,4,5])
# segregate - end