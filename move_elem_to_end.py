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
			self.head=self.tail=Node(data)
		else:
			self.tail.next=Node(data)
			self.tail = self.tail.next
	
	def print(self):
		c=self.head
		res=[]
		while(c):
			res.append(str(c.data))
			c=c.next
		print("->".join(res))
		print()
	
	def pushData(self,data):
		for i in data:
			self.push(i)

	def moveToEnd(self,x):
		if(self.head == None):
			return
		cnt=0
		c=self.head
		prev=None
		while(c):
			if(c.data == x):
				cnt+=1
				next=c.next
				c.next=None
				if(prev == None):
					self.head=next
				else:
					prev.next=next
				c=next
			else:
				prev=c
				c=c.next

		c=self.head
		while(c.next):
			c=c.next
		tail=c

		while(cnt > 0):
			tail.next=Node(x)
			tail=tail.next
			cnt-=1
				
		



def main(data1,x):
	ll=LinkedList()

	ll.pushData(data1)

	ll.moveToEnd(x)

	ll.print()



main([1,4,2,3,1,2],2)
main([1,6,2,4,1,2],1)
main([1,1,1,1,1,1,1,1,1,6,2,4,1,2],1)
main([1,4,2,3,1,2,2,2,2,2,2],2)
main([1,2,1,2,1,2,1,2,1,2,1,2,1,1,1,6,2,4,1,2],1)