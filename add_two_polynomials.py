class Node:
    def __init__(self,data,power):
        self.coef=data
        self.power=power
        self.next=None


class LinkedList:
	def __init__(self):
		self.head=None
		self.tail=None

	def push(self,data,power):
		if(self.head is None):
			self.head=self.tail=Node(data,power)
		else:
			self.tail.next=Node(data,power)
			self.tail = self.tail.next
	
	def print(self):
		c=self.head
		res=[]
		while(c):
			res.append(str(c.coef)+"x^"+str(c.power))
			c=c.next
		print("+".join(res))
		print()

	def mergeIterative(self,a,b):
		prev=None
		head=None
		c1=a
		c2=b
		while(c1 and c2):
			if(c1.power < c2.power):
				if(prev is None):
					head=c2
				else:
					prev.next=c2
				prev=c2
				c2=c2.next
			elif(c1.power > c2.power):
				if(prev is None):
					head=c1
				else:
					prev.next=c1
				prev=c1
				c1=c1.next
			else:
				if(prev is None):
					head=c1
				else:
					prev.next=c1
				prev=c1
				c1.coef+=c2.coef
				c1=c1.next
				c2=c2.next
		
		if(c1):
			prev.next=c1

		if(c2):
			prev.next=c2

		return head

	def merge(self,a,b):
		if(a is None):
			return b
			
		if(b is None):
			return a
		
		result=None
		
		if(a.power < b.power):
			result=b
			result.next=self.merge(a,b.next)
		elif(a.power > b.power):
			result=a
			result.next=self.merge(a.next,b)
		else:
			result=a
			result.coef+=b.coef
			result.next=self.merge(a.next,b.next)
			
		return result
	
	def pushData(self,data):
		for i in data:
			self.push(i[0],i[1])

def main(data1,data2):
	ll1=LinkedList()
	ll2=LinkedList()

	ll1.pushData(data1)
	ll2.pushData(data2)


	ll1.print()
	ll2.print()

	ll1.head=ll1.mergeIterative(ll1.head,ll2.head)

	ll1.print()

main([(1,4),(2,3),(1,2)],[(3,4),(2,3),(1,2)])
main([(1,6),(2,4),(1,2)],[(3,5),(2,3),(1,1)])
