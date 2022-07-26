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
	
	def sortAround(self,x):
		if(self.head is None or self.tail is None):
			return 
		
		arr=[]
		c=self.head
		while(c):
			arr.append(c.data)
			c=c.next
		
		min=-1
		curr=0
		l=len(arr)
		while(curr < l):
			if(arr[curr] <= x):
				min+=1
				arr[min],arr[curr] = arr[curr],arr[min]
			curr+=1

		# arr[min+1],arr[curr] = arr[curr],arr[min+1]

		c=self.head
		curr=0

		while(curr < l):
			c.data=arr[curr]
			c=c.next
			curr+=1

def main(data):
	ll=LinkedList()

	for i in data:
		ll.push(i)
	
	ll.print()
	ll.sortAround(3)
	ll.print()

main([1,4,3,2,5,2,3])
	